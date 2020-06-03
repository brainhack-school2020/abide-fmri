# abide-fmri
Repository for the Brainhack School 2020 team working with fMRI and ABIDE data to train machine learning models. 

## How to run

This repository contains several python scripts that train different classifiers with different cross-validation techniques on the ABIDE data set to predict autism from resting state fMRI data.

To fetch and prepare the data set you can call the script like this:

`./prepare_data.py data_dir output_dir`

or alternatively:

`python prepare_data.py data_dir output_dir`

where
- `data_dir` is the directory where you want to save the data or have it already saved and
- `output_dir` is the directory where you want to store the outputs the script generates.

The notebooks also call the function from the preparation script.
