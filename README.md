# abide-fmri
Repository for the Brainhack School 2020 team working with fMRI and ABIDE data to train machine learning models. 

## How to run

This repository contains several python scripts that train different classifiers with different cross-validation techniques on the ABIDE data set to predict autism from resting state fMRI data.

The scripts follow the same structure and thus can be called the same way:

`./scriptname.py data_dir output_dir`

or alternatively:

`python scriptname.py data_dir output_dir`

where
- `scriptname` is the specific script you want to use,
- `data_dir` is the directory where you want to save the data or have it already saved and
- `output_dir` is the directory where you want to store the outputs the script generates.
