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

I am a Master's student in Psychology currently enrolled at the University of Montréal. My main focus is in genomic imagery which consists of investigating the effect of genetic mutations on functional and structural brain phenotypes. More specifically, I have been interested in resting-state functional connectivity measures in carrier populations.

#### Mikkel

[TO DO]

---

### Tools 

#### Emily

My project planned to incorporate the following tools and technologies: 

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

---

### Data 

The goal of this project is to compare different machine learning models and cross-validation methods and see how well each is able to predict autism from resting state fMRI data. For that we are using the preprocessed open source [ABIDE database](http://fcon_1000.projects.nitrc.org/indi/abide/) which contains structural, functional, and phenotypic data of 539 individuals with autism and 573 typical controls from 20 different research sites.

---

### Deliverables 

By the end of The BrainHack School, we hope to have the following: 
* `README.md` file
* `requirements.txt` file that outlines the packages needed to run the script
* Jupyter notebooks with code and explanations
* GitHub repository documenting project workflow
* Presentation showing project results

## Project Results

### Becoming a Team 
The three of us joined forces when we realized that we shared many similar learning goals and interests. With such similar project ideas, we figured we would accomplish more working together by each taking on a different cross-validation methods to train various machine learning models. 

---

### Team Project Management

We all shared a common interest in making our project as reproducible as possible. This goal meant creating a transparent, collaborative workflow that could be tracked at any time by anyone. To achieve this objective, we utilized the many features that GitHub has to offer, all of which you can see in action at our shared repository [here](https://github.com/brainhack-school2020/abide-fmri).
* **Branches:** used to simultaneously on our own parts and then push changes to the master branch
* **Pull requests:** created when making changes to the master branch
* **Issues:** used to communicate with each other and keep track of tasks
* **Tags:** used to keep issues organized
* **Milestones:** used to keep our main goals in mind (Week 4 presentation and final deliverable)
* **Projects:** used to track various aspects of our work 

---

### Standardized Data Preparation and Jupyter Notebooks

The data are processed in a standardized way using a Python script that prepares the data for the machine learning classifiers. Several Jupyter notebooks then implement different models and cross-validation techniques which are described in detail below.

---

### Tools, Technologies, and Libraries Learned

Many of these contribute to open science practices! 

* Git/GitHub
* Jupyter notebooks
* Python
* Visual Studio Code
* `nilearn`
* `scikit-learn`
* `plotly`
* `matplotlib`
* `numpy` 
* `pandas`
* `seaborn`
* `venv`

---

### Deliverables

#### Deliverable 1: Jupyter notebooks

* ##### Leave-site-out cross-validation

[*`leave-site-out-cv_classifier.ipynb`*](https://github.com/brainhack-school2020/abide-fmri/blob/master/code/leave-site-out-cv_classifier.ipynb)

This notebook contains code to run a linear support vector classification to predict autism from resting state data. It uses leave-group-out cross-validation using site as the group variable. The results give a good estimate of how stable the model is. While for most of the sites the prediction works above chance level, for some, autism is predicted only at or even below chance level.

* ##### K-fold and leave-one-out cross-validation

[*`kfold-leave-one-out-cv_classifier.ipynb`*](https://github.com/brainhack-school2020/abide-fmri/blob/master/code/kfold-leave-one-out-cv_classifier.ipynb)

This notebook contains the code to run support vector classification, k nearest neighbors, decision tree and random forest on the ABIDE dataset. The models are trained and evaluated using k-fold and leave-one out cross-validation methods. We obtain accuracy scores that represent how skilled the model is at predicting the labels of unseen data.  Leave-one out cross validation gives more accurate predictions than kfold cross validation. The accuracy values range from 55.8% to 69.2%.

* ##### Group k-folds cross-validation

[*`group-kfolds-cv_classifier.ipynb`*](https://github.com/brainhack-school2020/abide-fmri/blob/master/code/group-kfolds-cv_classifier.ipynb)

[DESCRIPTION TO DO]

#### Deliverable 2: [`prepare_data.py`](https://github.com/brainhack-school2020/abide-fmri/blob/master/code/prepare_data.py) script

This script

* downloads the data
* extracts the time series of 64 regions of interest defined by the BASC brain atlas
* computes the correlations between time series for each participant
* uses a principal component analysis for dimensionality reduction

To fetch and prepare the data set you can call the `prepare_data.py` script like this:

`./prepare_data.py data_dir output_dir`

or alternatively:

`python prepare_data.py data_dir output_dir`

where
* `data_dir` is the directory where you want to save the data or have it already saved and
* `output_dir` is the directory where you want to store the outputs the script generates.

The notebooks also call the `prepare_data` function from the preparation script.

#### Deliverable 3: [`requirements.txt`](https://github.com/brainhack-school2020/abide-fmri/blob/master/requirements.txt) file 

This file increases reproducibility by helping to ensure that the scripts run correctly on any machine. To make sure that all scripts work correctly, you can create a virtual environment using pythons built-in library `venv`. To do this, follow these steps:

1. Clone repo and navigate to folder in a shell
2. Create a virtual environment in a folder of your choice: `python -m venv /path/to/folder`
3. Activate it (bash command, see [here](https://docs.python.org/3/library/venv.html) how to activate in different shells): `source /path/to/folder/bin/activate`
4. Install all necessary requirements from requirements file: `pip install -r requirements.txt`
5. Create kernel for jupyter notebooks: `ipython kernel install --user --name=abide-ml`
6. Open a jupyter notebook: `jupyter-notebook`, then click the notebook you want to run
7. Select different kernel by clicking *Kernel -> Change Kernel -> abide-ml*
8. Run the code!

#### Deliverable 4: Data visualizations (Week 3)

* [Emily's GitHub Repository](https://github.com/emilyemchen/bhs2020-dataviz)
    * [Age at Scan Distribution by ABIDE Test Site](https://emilyemchen.github.io/bhs2020-dataviz/abide_age.html)

    <iframe src="https://emilyemchen.github.io/bhs2020-dataviz/abide_age.html" width="800px" height="600px"></iframe>

    * [FIQ Score Distribution by ABIDE Test Site](https://emilyemchen.github.io/bhs2020-dataviz/abide_fiq.html)

    <iframe src="https://emilyemchen.github.io/bhs2020-dataviz/abide_fiq.html" width="800px" height="600px"></iframe>

    * [VIQ Score Distribution by ABIDE Test Site](https://emilyemchen.github.io/bhs2020-dataviz/abide_viq.html)

    <iframe src="https://emilyemchen.github.io/bhs2020-dataviz/abide_viq.html" width="800px" height="600px"></iframe>

    * [PIQ Score Distribution by ABIDE Test Site](https://emilyemchen.github.io/bhs2020-dataviz/abide_piq.html)

    <iframe src="https://emilyemchen.github.io/bhs2020-dataviz/abide_piq.html" width="800px" height="600px"></iframe>

* [Andréanne's GitHub Repository](https://github.com/brainhack-school2020/anproulx-fMRI-autism)
    * [Various data visualizations](https://chart-studio.plotly.com/~anproulx/2/data-visualization/#/)
* [Mikkel's GitHub Repository](https://github.com/brainhack-school2020/mschoettner_fMRI-ML)
    * [Age Distributions at Different Research Sites](https://mschoettner.github.io/brainhack_visualization/)

    <iframe src="https://mschoettner.github.io/brainhack_visualization/" width="800px" height="600px"></iframe>

#### Deliverable 5: Presentation (Week 4)

The presentation slides can be viewed [here](https://www.canva.com/design/DAD-ByEQaXI/QLgHbYgnKd-xDWJXVnaGDA/view) on Canva, which is the platform we used to create the slides. A video of our presentation can be viewed on this project page. We presented our work to the BrainHack School on June 5, 2020 using the RISE integration in a Jupyter notebook, which can be found [here](https://github.com/brainhack-school2020/abide-fmri/tree/master/presentation). 

#### Deliverable 6: Overview of the project and results in the [`README.md`](https://github.com/brainhack-school2020/abide-fmri/blob/master/README.md) file

This `README.md` file contains the content that will be shown on the BrainHack School website [project page](https://school.brainhackmtl.org/project/). 

## Conclusion and Acknowledgement

First and foremost, we would like to thank our Weeks 3 and 4 peer clinic mentor and co-organizer of the Brainhack School, Pierre Bellec. A special thank you as well to our Week 2 mentors Désirée Lussier-Lévesque, Alexa Pichet-Binette, and Sebastian Urchs. 

Thank you also to The BrainHack School leaders and co-organizers Jean-Baptiste Poline, Tristan Glatard, and Benjamin de Leener, as well as the instructors and mentors Karim Jerbi, Elizabeth DuPre, Ross Markello, Peer Herholz, Samuel Guay, Valerie Hayot-Sasson, Greg Kiar, Jake Vogel, and Agâh Karakuzu. 

## References 

1. Choosing appropriate estimators with `scikit-learn` https://scikit-learn.org/stable/tutorial/machine_learning_map/

2. Benchmarking functional connectome-based predictive models for resting-state fMRI (for classification estimator inspiration) https://hal.inria.fr/hal-01824205

3. Getting the data using `nilearn.datasets.fetch` https://nilearn.github.io/modules/generated/nilearn.datasets.fetch_abide_pcp.html

4. Python Data Science Handbook GitHub and website https://github.com/jakevdp/PythonDataScienceHandbook

5. BrainHack School course materials and lectures https://github.com/neurodatascience/course-materials-2020