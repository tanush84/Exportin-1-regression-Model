from rdkit import Chem
from rdkit.Chem import AllChem
import pandas as pd
import numpy as np
import csv 
import operator
import os, sys
import argparse
import configparser
import re

def calculate_morgan_fingerprint(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        fingerprint = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=2048)
        return list(fingerprint)
    else:
        return [0] * 2048  # If a molecule cannot be parsed, return a zero vector
        
        
def read_smi_file(file_path):
    try:
        with open(file_path, 'r') as smi_file:
            lines = smi_file.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

def smi_to_dataframe(file_path):
    smi_data = read_smi_file(file_path)
    if not smi_data:
        return None
    
    data = {'SMILES': smi_data}
    df = pd.DataFrame(data)
    return df
