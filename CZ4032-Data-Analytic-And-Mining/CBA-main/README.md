# CBA Classificationn Based Association Rules

This is a CZ4032 Project 2 implementing Classification Based Association Rules onto datasets for data analysis.

# Members

Tan Jiawei, Eric <br/>
Zon Liew Hur Zhen <br/>
Chan Jun Jie <br/>
Seph Chen Kian Leong <br/>
Samuel Png Yao Wei <br/>

# Datasets
1. Iris
2. Breast Cancer
3. Wine
4. Heart Failure Clinical Records
5. Zoo
6. Adults
7. Car Evaluation
8. Bank Marketing

# Requirements

1. Working Editor / Anaconda with Python installed
2. Run `pip install requirements.txt`
# Control Variables

`SELECT_DATASET_INDEX` - Represents the dataset that will be loaded to build the classifier <br/>
`min_support` - determines how interesting the generated association rules will be <br/>
`min_threshold` - confidence cutoff to shave off less confident rules<br/>
`NELEMENT` - used for the bagging algorithm <br/>

# How to run

## M1 Classifier
1. Run `Build Classifier.ipynb` <br/>
2. Select a dataset using `SELECT_DATASET_INDEX` <br/>
3. Tweak `min_support` & `min_threshold` to optimize the accuracy <br/>

## Enhanced Classifier
1. Run `EnhancedClassifier.ipynb` <br/>
2. Select a dataset using `SELECT_DATASET_INDEX` <br/>
3. Tweak `min_support`, `min_threshold` and `NELEMENT` to optimize the accuracy <br/>

## Data Cleaning
1. Run `{DATASET_NAME}_Data_Cleaning.ipynb`. (Replace DATASET_NAME with name of the dataset)