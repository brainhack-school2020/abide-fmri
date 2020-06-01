#!/usr/bin/env python

from nilearn import datasets
from nilearn.input_data import NiftiLabelsMasker
from nilearn.connectome import ConnectivityMeasure
from argparse import ArgumentParser
import numpy as np
from sklearn.decomposition import PCA
import os
import pandas as pd

def prepare_data(data_dir, output_dir, pipeline = "cpac", quality_checked = True):
    # get dataset
    print("Loading dataset...")
    abide = datasets.fetch_abide_pcp(data_dir = data_dir,
                                     pipeline = pipeline,
                                     quality_checked = quality_checked)
    # make list of filenames
    fmri_filenames = abide.func_preproc

    # load atlas
    multiscale = datasets.fetch_atlas_basc_multiscale_2015()
    atlas_filename = multiscale.scale064

    # initialize masker object
    masker = NiftiLabelsMasker(labels_img=atlas_filename,
                               standardize=True,
                               memory='nilearn_cache',
                               verbose=0)

    # initialize correlation measure
    correlation_measure = ConnectivityMeasure(kind='correlation', vectorize=True,
                                             discard_diagonal=True)

    try: # check if feature file already exists
        # load features
        feat_file = os.path.join(output_dir, 'ABIDE_BASC064_features.npz')
        X_features = np.load(feat_file)['a']
        print("Feature file found.")

    except: # if not, extract features
        X_features_2d = [] # To contain data in the form of 2d matrix
        X_features = [] # To contain upper half of matrix as 1d array 
        print("No feature file found. Extracting features...")
        
        for i,sub in enumerate(fmri_filenames):
            # extract the timeseries from the ROIs in the atlas
            time_series = masker.fit_transform(sub)
            # create a region x region correlation matrix
            correlation_matrix = correlation_measure.fit_transform([time_series])[0]
            # Extract upper half of matrix
            correlation_matrix_1d=list(correlation_matrix[np.triu_indices(64)]) 
            # add to our containers
            X_features_2d.append(correlation_matrix) # add 2d matrix (64 , 64)
            X_features.append(correlation_matrix_1d) # add 1d array of half matrix (2080, )
            # keep track of status
            print('finished extracting %s of %s'%(i+1,len(fmri_filenames)))

    # Save features
    np.savez_compressed(os.path.join(output_dir, 'ABIDE_BASC064_features_2d'),
                            a = X_features_2d)
    np.savez_compressed(os.path.join(output_dir, 'ABIDE_BASC064_features'),
                            a = X_features)

    # Dimensionality reduction of features with PCA
    pca = PCA(0.99).fit(X_features) # keeping 99% of variance
    X_features_pca = pca.transform(X_features)

    #print("original shape: ", X_features.shape)
    #print("transformed shape:", X_features_pca.shape)

    # Transform phenotypic data into dataframe
    abide_pheno=pd.DataFrame(abide.phenotypic)

    # Get the target vector
    y_target= abide_pheno['DX_GROUP']


def run_analysis():
    description = "Train classifier on the ABIDE data to predict autism"
    parser = ArgumentParser(__file__, description)
    parser.add_argument("data_dir", action = "store",
                        help = """Path to the data directory that contains the
                        ABIDE data set. If you already have the data set, this
                        should be the folder that contains the subfolder
                        'ABIDE_pcp'. If this folder does not exists yet, it will
                        be created in the directory you provide.""")
    parser.add_argument("output_dir", action = "store",
                        help = """Path to the directory where you want to store
                        outputs.""")
    args = parser.parse_args()
    X_features_pca, y_target = prepare_data(args.data_dir, args.output_dir)
    print("analyzing...")
    # TODO: split the data into training and test set

    # TODO: specify model(s)

    # TODO: train model(s)

if __name__ == "__main__":
    run_analysis()
