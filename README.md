# Use these stacks
<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://opencv.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/opencv/opencv-icon.svg" alt="opencv" width="40" height="40"/> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> </a> <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a> <a href="https://seaborn.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="seaborn" width="40" height="40"/> </a> <a href="https://www.tensorflow.org" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" width="40" height="40"/> </a> </p>

  Get 30,000 Face-image-dataset from kaggle

  
![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) 	![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white) 	![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
  
# Mask_Ai_Project
This is about Mask Recognition AI. You can see how AI recognize whether people ware a mask or not.

## **💡Tip : a quick way to browse this document**


You can just watch ./original_app/**a_Module.py** and **D_mask_Tracking.py** in this Repository. Thank you.


## **💡Tip 2 : If you want to use this, you have to modify Pathvariable in the code**


1) At root path, you should make train-set and test-set pakage then change pathvariable like "your own".

    TRAINING_DIR = "C:/Users/I310/PycharmProjects/pythonProject/mask_dataset/train-set"
    VALIDATION_DIR = "C:/Users/I310/PycharmProjects/pythonProject/mask_dataset/test-set"

    should change Path "C:/Users/I310/PycharmProjects/pythonProject/mask_dataset/test-set" -> "your own"
  

2) get some pictures from google and make dataset file

   
    *there are no dataset file in this github because of the capacity of the picture they're over 1GB."
    So you have to do crolling some 'human Face image' from web and put them into folder which is called "train-set" and "test-set"

   
    while keep in mind that "train-set" has more picture then 'test-set'
    (I did this for train-set/on-mask 18 photos and for train-set/off-mask 19 photos. 
    I did this for test-set/on-mask 9 photos and for test-set/off-mask 9 photos.)
