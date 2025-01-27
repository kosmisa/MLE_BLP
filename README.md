### Basic_MLE_HW

I am sorry due to very little time i had to spend on this HW i got confused and was unable to resolve the problems i had with homework in time. 

First problem i was unable to overcome in time is env setup. Somehow i keep getting errors on commands i want to call for pandas on VSC eventhought i am setting venv. separately from global.

Second problem is not spending enough time to work on problem, due to political nature in my country that is affecting both my work and university activities i found my self in situation that i have even less time to work on homework. I need to use iris data from sklearn but my template is focused on generating syntetic data and i failed to adapt that code to extract data


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
