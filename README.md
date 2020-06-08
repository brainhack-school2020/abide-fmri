# abide-fmri
Repository for the Brainhack School 2020 team working with fMRI and ABIDE data to train machine learning models. 

## The goal

The goal of this project is to compare different machine learning models and cross-validation methods and see how well each is able to predict autism from resting state fMRI data. For that we are using the [ABIDE data set](http://fcon_1000.projects.nitrc.org/indi/abide/) which combines data from 20 different research sites.

## Project structure

The data are processed in a standardized way using a Python script that prepares the data for the machine learning classifier. Several Jupyter notebooks then implement different models and cross-validation techniques which are described in detail below.

### The preparation script

*prepare_data.py*

This script

- downloads the data
- extracts the time series of 64 regions of interest defined by the BASC brain atlas
- computes the correlations between time series for each participant
- uses a principal component analysis for dimensionality reduction

### Leave-site-out cross-validation

*leave-site-out-cv_classifier.ipynb*

This notebook contains code to run a linear support vector classification to predict autism from resting state data. It uses leave-group-out cross-validation using site as the group variable. The results give a good estimate of how stable the model is. While for most of the sites the prediction works above chance, for some autism is predicted only at chance or even below chance.

### K-fold and leave-one-out cross-validation
*kfold_LeaveOneOut_cv_classifier.ipynb*

This notebook contains the code to run support vector classification, k neirest neighbors, decision tree and random forest on the Abide dataset. The models are trained and evaluated using k-fold and leave-one out cross-validation methods. We obtain accuracy scores that represent how skilled the model is at predicting the labels of unseen data.  Leave-ont out cross validation gives more accurate predictions than kfold cross validation. The accuracy values range from 55.8% to 69.2%.

## How to run

This repository contains several python scripts that train different classifiers with different cross-validation techniques on the ABIDE data set to predict autism from resting state fMRI data.

To fetch and prepare the data set you can call the script like this:

`./prepare_data.py data_dir output_dir`

or alternatively:

`python prepare_data.py data_dir output_dir`

where
- `data_dir` is the directory where you want to save the data or have it already saved and
- `output_dir` is the directory where you want to store the outputs the script generates.

The notebooks also call the `prepare_data` function from the preparation script.

### Using venv

To make sure that all scripts work correctly, you can create a virtual environment using pythons built-in library `venv`. To do this, follow these steps:

1. Clone repo and navigate to folder in a shell
1. Create a virtual environment in a folder of your choice: `python -m venv /path/to/folder`
2. Activate it (bash command, see [here](https://docs.python.org/3/library/venv.html) how to activate in different shells): `source /path/to/folder/bin/activate`
3. Install all necessary requirements from requirements file: `pip install -r requirements.txt`
4. Create kernel for jupyter notebooks: `ipython kernel install --user --name=abide-ml`
5. Open a jupyter notebook: `jupyter-notebook`, then click the notebook you want to run
6. Select different kernel by clicking *Kernel -> Change Kernel -> abide-ml*
7. Run the code!

## Week 3 Deliverable: Data Visualization
* [Emily's GitHub Repository](https://github.com/emilyemchen/bhs2020-dataviz)
* [Andréanne's GitHub Repository](https://github.com/brainhack-school2020/anproulx-fMRI-autism)
* [Mikkel's GitHub Repository]()
