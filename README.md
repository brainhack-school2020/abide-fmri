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

### Using venv

To make sure that all scripts work correctly, you can create a virtual environment using pythons built-in library venv. To do this, follow these steps:

1. Clone repo and navigate to folder in a shell
1. Create a virtual environment in a folder of your choice: `python -m venv /path/to/folder`
2. Activate it (bash command, see [here](https://docs.python.org/3/library/venv.html) how to activate in different shells): `source /path/to/folder/bin/activate`
3. Install all necessary requirements from requirements file: `pip install -r requirements.txt`
4. Create kernel for jupyter notebooks: `ipython kernel install --user --name=abide-ml`
5. Open a jupyter notebook: `jupyter-notebook`, then click the notebook you want to run
6. Select different kernel by clicking *Kernel -> Change Kernel -> abide-ml*
7. Run the code!
