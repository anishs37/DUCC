<p align="center">
    <img src="static/img/ducclogo1.png" alt="Model Architecture" width = 200; height = 200>
    <h1 align="center">
        Dermatological Underlying Cancer Classification
    </h1>
</p>

This repository contains the code to reproduce the results of D.U.C.C. (Dermatological Underlying Cancer Classifcation), our project at the 2023 TJ BioCode competition.

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [About the Project](#about-the-project)
- [Datasets](#datasets)
- [Contact](#issues-and-contact)
- [References](#references)

<!-- ABOUT THE PROJECT -->

## About The Project

Melanoma is the most deadly type of skin cancer. It occurs when the pigment-producing cells in the skin become cancerous. Additionally, a person has a 1 in 17 chance of being diagnosed with melanoma by the age of 85. Melanoma becomes more difficult to treat the deeper it spreads into the skin, so regular skin examinations are key to recognizing melanoma in its early stages.

D.U.C.C. (Dermatological Underlying Cancer Classification) is a tool for users to determine the likelihood of a skin lesion being malignant. The user uploads a picture of the lesion, and it is classified as malignant or benign using machine learning. Regular use of D.U.C.C. can increase the chance of melanoma being recognized early, thus decreasing the mortality rate of skin cancer.

<!-- Datasets -->

## Datasets

For this project, we utilized the _[HAM10000 Dataset](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T)_, a large collection of skin images, some being positive samples (where the patient has melanoma) and some being negative samples (where the patient does not have melanoma).

<!-- Model -->

## Model

[InceptionV3](https://doi.org/10.48550/arXiv.1512.00567)


<!-- Contact -->

## Issues and Contact

For any issues pertaining to the code, please use the Issues tab. For questions regarding the project itself, please reach out to the developers of D.U.C.C. (Anish Susarla, Cindy Yang, Athan Zhang, Elise Zhu).

<!-- References -->

## References

Parts of this repository are based on [existing Kaggle Code for the dataset](https://www.kaggle.com/datasets/drscarlat/melanoma/code). We extended upon this code by developing other models that were not publicly used on this dataset.
