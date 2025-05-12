### MLE

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
