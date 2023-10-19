# Supply Chain Analysis! ![page](https://img.shields.io/badge/Data%20Analytics-8A2BE2) ![page](https://img.shields.io/badge/Data%20Cleaning-DBC4F0) ![page](https://img.shields.io/badge/Feature%20Engineering-916DB3) ![page](https://img.shields.io/badge/Vizualization-8A2BE2) ![page](https://img.shields.io/badge/Statistics-9BE8D8)

Please visit my Tableau Public profile [here](https://public.tableau.com/app/profile/truposzeq/vizzes) to check out the dashboards created for this analysis!

## Contents
- [About the project](#about_the_project)
- [Requirements](#requirements)
- [Instalation](#instalation)
- [Usage](#usage)
- [Repositoty structure](#repository_structure)



## About the project
Supply chain analytics are one of the essential elements when making decisions in many fields, such as retail, procurment, logistics and farming. In this process I will be analyzing and interpreting the movement of products and it's customers preferences in order to give a good, data-driven insight at the stong points and weaker spots of supply chain and demand. 

This repository contains my analysis of Supply Chain data.  
Data provided in this analysis has been borrowed from this dataset on [Kaggle](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis).

In this analysis, I will be looking at the Supply Chain data of the DataCo Global company, but I will analyse it in two was:
- Firstly, let's go back in time to 2018, close to the end of the dataset to analyse what works good and what doesn't;
- Secondly, **SPOILER ALERT**, I will draw some conlusion on why this company failed and didn't generate more sales, based on the data presented.

For this project, since the dataset is rather big, I will be using not `.csv` files, but `.parquet` files instead - I transformed the original dataset on my local device and ran it through `data_cleaning.py`, which is my program, written to clean up this dataset for further smooth analysis. I excluded some order and customer data, that I wouldn't need, deleted duplicated columns (which there were a few, but with different names) and cleaned up the column names. I also translated two of the columns, Customer Country (the way United States were named was odd, hence I did it by simple dictionary), and Order Country (here I used `mtranslate` library, as there were many countries).

In the notebook you can read through my exploration and my conclusions.

Another thing I will present here, is **ABC analysis**. ABC analysis in supply chain management is a way to sort and prioritize things based on their importance. "A" is for the most important, "B" is for middle importance, and "C" is for the least important. It helps companies focus on what matters most for efficiency and cost. ABC analysis is useful because it helps businesses allocate resources wisely. It ensures that efforts are concentrated on crucial aspects of the supply chain, leading to better decision-making and optimized operations.

Lastly, I created 3 dashboards for this dataset, representing the [general overview on the data](https://public.tableau.com/app/profile/truposzeq/viz/Supply_Chain_Analysis_Dashboard_1/Gen), [in-depth department understanting](https://public.tableau.com/app/profile/truposzeq/viz/Supply_Chain_Analysis_Dashboard_2/DPC) and [delay analysis](https://public.tableau.com/app/profile/truposzeq/viz/Supply_Chain_Analysis_Dashboard_3/Delays). 


## Requirements

All the requirements can be found in the `requirements.txt` in the repository.


## Instalation
To run this project on you local machine, please follow the below steps:
1. **Creation of virtual environment** (recommended):
    Creation and activation of virtual environment:

    ```bash
    python -m venv supply_chain_analysis_venv
    source supply_chain_analysis_venv/bin/activate   # for  Unix/Linux
    .\supply_chain_analysis_venv\Scripts\activate    # for Windows
    ```
2. **Instalation of requirements:**

    Install the needed versionf of the packages from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```
    Make sure you are using the latest version of pip:

    ```bash
    pip install --upgrade pip
    ```
    The `requirements.txt` contains the list of dependencies and it's versions.

3. **Running the project**:
    After the instalation of dependencies, you should be able to run the project.


## Usage
This project is created for education purposes, as a portfolio analysis. Majoryti of the techniques can be apllied to other similar analysis of Supply Chains - if you were to use any of the code provided in here, please make sure your data is structured the same way it is in this dataset, otherwise you might get some errors.

## Repositoty structure
- 📁 **data** - directory containing all dataframes and dictionaries;
- 📁 **graphs** - directory containing few of the graphs created in the notebook;
- **data_cleaning.py** - data cleaning program for preprocessing;
- **sca_functions.py** - few useful functions for the analysis;
- **SupplyChain_EDA.ipynb** - the main analysis of Supply Chain;
- **requirements.txt** - containing all the dependencies for this project.

I also used Tableau Public for this project, dashboards are mentioned above.
