### Basic_MLE_HW

I am sorry due to very little time i had to spend on this HW i got confused and was unable to resolve the problems i had with homework in time. 

First problem i was unable to overcome is env setup. Somehow i kept getting errors for global and local env. . Even thought i think i made local env to avoid conflict i was unable to to resolve errors that kept poping up. I will redo my MLE part and try to find extra sources to deal with it.

Second problem is not spending enough time to work on problems, due to political nature in my country that is affecting both my work and university activities i found my self in situation that i have even less time to work on homework. I need to use iris data from sklearn but my template is focused on generating syntetic data and i failed to adapt that code to extract data.

I understood the concepts in this part but due to many factors was unable to implement it right. I started from given template and kept deleting many times due to losing track what i change and what i did not. 


Project structure:

project/  
├── data/  
│   └── data.py                # Script to handle data loading from the Iris dataset  
├── data_process/  
│   └── data_generation.py     # Data processing pipeline to prepare training and inference data  
├── inference/  
│   └── Dockerfile             # Dockerfile to build the inference container  
│   └── run.py                 # Script to perform batch inference  
├── models/                    # Directory where trained models are stored  
│   └── [model files]          # Trained model files  
├── training/  
│   └── Dockerfile             # Dockerfile to build the training container  
│   └── train.py               # Script to train the model using the Iris dataset  
├── settings.json              # Configuration file for paths and parameters  
├── utils.py                   # Utility functions for logging and project setup  
├── requirements.txt           # Dependencies needed for the project  
├── README.md                

### Instal and Setup
    Clone repo:
        1. git clone <repository-url>  
        2. cd {this project name}
    Install dependencies:
        1. pip install -r requirements.txt 
