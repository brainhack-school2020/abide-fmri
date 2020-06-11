# Predicting Autism with fMRI Data

Contributors: Emily Chen, Andréanne Proulx, and Mikkel Schöttner

[ADD PHOTO]

Repository for the Brainhack School 2020 team working with resting state fMRI data from the ABIDE dataset to train machine learning models. 

## Project Definition 

### Personal Backgrounds

#### Emily
Hello! I am an (incoming) fourth year undergraduate student at McGill University studying computer science and urban health geography with a minor in cognitive science. I am a research assistant with Isabelle Arseneau-Bruneau in the Zatorre Lab and have been learning a lot about neuroscience research while (hopefully) lending some of my technical skills to Isabelle's PhD work exploring the effect of musical training on FFR. 

When joining the BrainHack School, I was looking forward in particular to working on a project at the intersection of neuroscience and CS because my previous classes rarely focused on the application of the abstract concepts we learned. Upon completion of the BrainHack School, I had the opportunity to learn from and collaborate with talented neuroscience researchers and participants, write a machine learning script using python and neuroscience data, and gain hands-on practice in reproducibility efforts and good project management. 

You can find me on GitHub at [emilyemchen](https://github.com/emilyemchen) and on Twitter at [@emilyemchen](https://twitter.com/emilyemchen).

#### Andréanne

I am a Master's student in Psychology currently enrolled at the University of Montreal. My main focus is in genomic imagery which consists of investigating the effect of genetic mutations on fonctional and structural brain phenotypes. More specifically, I have been interested in resting-state functional connectivity measures in carrier populations.

#### Mikkel

[TO DO]

### Tools 

#### Emily

I planned to work with the following tools and technologies: 

* Python
* `nilearn`
* `scikit-learn`
* MNE
* Git/Github
* Visual Studio Code
* Terminal
* Jupyter notebooks
* Visualization packages (`matplotlib`, `seaborn`, `plotly`)
* Docker

#### Andréanne

My project planned to rely on the following tools and libraries:
* Jupyter notebooks
* GitHub
* `scikit-learn`, `nilearn`, `seaborn`, `matplotlib`, `pyplot`

#### Mikkel

My project planned to rely on the following technologies: 

* `nilearn`
* `scikit-learn`
* `plotly`
* HPC/Compute Canada

### Data 

The goal of this project is to compare different machine learning models and cross-validation methods and see how well each is able to predict autism from resting state fMRI data. For that we are using the [ABIDE data set](http://fcon_1000.projects.nitrc.org/indi/abide/) which combines data from 20 different research sites.

### Deliverables 




## Results

### Progress Overview

The data are processed in a standardized way using a Python script that prepares the data for the machine learning classifier. Several Jupyter notebooks then implement different models and cross-validation techniques which are described in detail below.

### Tools Learned



### Deliverables

#### Deliverable 1: Jupyter notebooks

##### Leave-site-out cross-validation

[*`leave-site-out-cv_classifier.ipynb`*](https://github.com/brainhack-school2020/abide-fmri/blob/master/code/leave-site-out-cv_classifier.ipynb)

This notebook contains code to run a linear support vector classification to predict autism from resting state data. It uses leave-group-out cross-validation using site as the group variable. The results give a good estimate of how stable the model is. While for most of the sites the prediction works above chance level, for some, autism is predicted only at or even below chance level.

### K-fold and leave-one-out cross-validation
*kfold_LeaveOneOut_cv_classifier.ipynb*

This notebook contains the code to run support vector classification, k neirest neighbors, decision tree and random forest on the Abide dataset. The models are trained and evaluated using k-fold and leave-one out cross-validation methods. We obtain accuracy scores that represent how skilled the model is at predicting the labels of unseen data.  Leave-ont out cross validation gives more accurate predictions than kfold cross validation. The accuracy values range from 55.8% to 69.2%.

##### 

[*`group-kfolds-cv_classifier.ipynb`*](https://github.com/brainhack-school2020/abide-fmri/blob/master/code/group-kfolds-cv_classifier.ipynb)

#### Deliverable 2: [*`prepare_data.py`*](https://github.com/brainhack-school2020/abide-fmri/blob/master/code/prepare_data.py) script

This script

* downloads the data
* extracts the time series of 64 regions of interest defined by the BASC brain atlas
* computes the correlations between time series for each participant
* uses a principal component analysis for dimensionality reduction

#### Deliverable 3: [*`requirements.txt`*](https://github.com/brainhack-school2020/abide-fmri/blob/master/requirements.txt) file 


#### Deliverable 4: Data visualizations (Week 3)

* [Emily's GitHub Repository](https://github.com/emilyemchen/bhs2020-dataviz)
* [Andréanne's GitHub Repository](https://github.com/brainhack-school2020/anproulx-fMRI-autism)
* [Mikkel's GitHub Repository](https://github.com/brainhack-school2020/mschoettner_fMRI-ML), [link to the plot](https://mschoettner.github.io/brainhack_visualization/)


#### Deliverable 5: Presentation (Week 4)

#### Deliverable 6: Overview of the project and results in the `README.md` file



## Conclusion and Acknowledgement



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

### Using `venv`

To make sure that all scripts work correctly, you can create a virtual environment using pythons built-in library `venv`. To do this, follow these steps:

1. Clone repo and navigate to folder in a shell
1. Create a virtual environment in a folder of your choice: `python -m venv /path/to/folder`
2. Activate it (bash command, see [here](https://docs.python.org/3/library/venv.html) how to activate in different shells): `source /path/to/folder/bin/activate`
3. Install all necessary requirements from requirements file: `pip install -r requirements.txt`
4. Create kernel for jupyter notebooks: `ipython kernel install --user --name=abide-ml`
5. Open a jupyter notebook: `jupyter-notebook`, then click the notebook you want to run
6. Select different kernel by clicking *Kernel -> Change Kernel -> abide-ml*
7. Run the code!


