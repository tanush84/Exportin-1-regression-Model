import pandas as pd
import numpy as np
import csv 
import operator
from rdkit.Chem import PandasTools
import os, sys
import argparse
import configparser
import re
import joblib
from assets.asset import calculate_morgan_fingerprint, read_smi_file, smi_to_dataframe

df = []
    
def main():
    parser = argparse.ArgumentParser(description="Convert a .smi file to a pandas DataFrame.")
    parser.add_argument('input_file', type=str, help='Path to the .smi file')

    args = parser.parse_args()
    input_file = args.input_file

    df = smi_to_dataframe(input_file)

    if df is not None:
        print("DataFrame created successfully:")
        print(df.head())
        PandasTools.AddMoleculeColumnToFrame(df, 'SMILES')
        df['MorganFingerprint'] = df['SMILES'].apply(calculate_morgan_fingerprint)
        # Split Morgan fingerprints into separate columns
        df_fingerprints = df['MorganFingerprint'].apply(pd.Series)
        # Concatenate the new columns with the original DataFrame
        df = pd.concat([df, df_fingerprints], axis=1)
        # Drop the original "MorganFingerprint" column
        df = df.drop(columns=['MorganFingerprint'])

        X = df.drop(df.columns[[0,1]],axis = 1)
        
        filename = './assets/model-xpo1.joblib'
        # load the model from disk
        loaded_model = joblib.load(filename)

        y_predicted = loaded_model.predict(X)
        
        print("pIC50 value for the molecule is ", y_predicted[0])
        # Convert pIC50 back to IC50
        val_ic50 = 10**(-y_predicted) * 1e9

        print("IC50 value for the molecule is ", val_ic50[0], "nM")
        

    else:
        print("DataFrame creation failed.")
        
        
        
if __name__ == "__main__":
    main()
