#!/usr/bin/env python

from nilearn import datasets
from nilearn.input_data import NiftiLabelsMasker
from nilearn.connectome import ConnectivityMeasure
import numpy as np
import os
import pandas as pd

def prepare_data(data_dir, output_dir, pipeline = "cpac", quality_checked = True):
    # get dataset
    print("Loading dataset...")
    abide = datasets.fetch_abide_pcp(data_dir = data_dir,
                                     pipeline = pipeline,
                                     quality_checked = qc)
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

    all_features = [] # here is where we will put the data (a container)

    print("Extracting features...")
    for i,sub in enumerate(fmri_filenames):
        # extract the timeseries from the ROIs in the atlas
        time_series = masker.fit_transform(sub)
        # create a region x region correlation matrix
        correlation_matrix = correlation_measure.fit_transform([time_series])[0]
        # add to our container
        all_features.append(correlation_matrix)
        # keep track of status
        print('finished extracting %s of %s'%(i+1,len(fmri_filenames)))

    # save features
    np.savez_compressed(os.path.join(output_dir, 'ABIDE_BASC064_features'),
                        a = all_features)
    # load features
    feat_file = os.path.join(output_dir, 'ABIDE_BASC064_features.npz')
    X_features = np.load(feat_file)['a']

    # get target variable from csv
    phenotypic = pd.read_csv(os.path.join(data_dir, "ABIDE_pcp",
                                          "Phenotypic_V1_0b_preprocessed1.csv"))

    file_ids = []
    # get the file IDs from the file names
    for f in fmri_filenames:
        file_ids.append(f[-27:-20])

    # extract info about ASD for each participant
    y_target = []
    for i in range(len(phenotypic)):
        for j in range(len(file_ids)):
            if file_ids[j] in phenotypic.FILE_ID[i]:
                y_target.append(phenotypic.DX_GROUP[i])

    return(X_features, y_target)

def run_analysis(X_features, y_target):
    print("analyzing...")
    # TODO: split the data into training and test set

    # TODO: specify model(s)

    # TODO: train model(s)

if __name__ = "__main__":
    X_features, y_target = prepare_data()
    run_analysis(X_features = X_features, y_target = y_target)
