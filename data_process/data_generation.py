# Importing required libraries
import numpy as np
import pandas as pd
import logging
import os
import sys
import json

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

def load_and_split_iris_data(output_dir="data"):
    """
    Load the Iris dataset using sklearn and split into training and inference sets.
    """
    # Load the Iris dataset
    iris = load_iris()
    data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    data['species'] = iris.target

    # Split into training and inference sets
    train_data, inference_data = train_test_split(data, test_size=0.2, random_state=42, stratify=data['species'])

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Save dataset locally
    train_data.to_csv(os.path.join(output_dir, "train.csv"), index=False)
    inference_data.to_csv(os.path.join(output_dir, "inference.csv"), index=False)
    print(f"Data saved in {output_dir}")

if __name__ == "__main__":
    load_and_split_iris_data()