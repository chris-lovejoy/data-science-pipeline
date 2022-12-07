# Data Science Pipeline

Generalisable code for common stages of a data science task pipeline.

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)



## Purpose

The purpose of this repository is to provide template code to support each stage of the 'standard' data science pipeline.

(NOTE: This repository is a work-in-progress. I will be adding more template code over time as a by-product of different projects I am working on.)


## Stages of the pipeline

### Step 1: Set up repository

Recommended structure: [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) as starting point, modified based on requirements.

Core suggested folders are the following:
- data
- models
- notebooks
- src


### Step 2: Understand the data

Questions to answer:
- What type of data do we have here?
- What is the quality of the data? (E.g. How many missing variables?)
- What kind of task is this? What kind of models might be appropriate?

Template code to help wth this analysis is available in [this notebook](1.%20Initial%20Exploratory%20Data%20Analysis.ipynb).


### Step 3: Engineer features (as appropriate)

The exact process for feature engineering depends a lot on the task and model that will be used.

A suggested general process is the following:

Use the template code in [this notebook](2.%20Feature%20Engineering.ipynb) to visualise each feature while creating a custom function to extract it. Then, move the functions into [this src module](/src/build_features.py).


### Step 4: Train the appropriate models

First, decide the appropriate models to consider for your task. See [this diagram](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html) for selecting in common scenarios.

- For template code for classification, see [this notebook](3a.%20Classification.ipynb).
- For template code for regression, see [this notebook](3b.%20Regression.ipynb).
- For template code for clustering, see [this notebook](3c.%20Clustering.ipynb).


---

### Contributing
*Issues, pull requests and other suggestions for improvements warmly invited.*
