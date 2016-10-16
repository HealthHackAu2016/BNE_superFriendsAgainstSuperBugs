# parser for data to be passed to graphing functions
import pandas as pd
import numpy as np

pc_filename = "/home/jake/workspace/healthhack/data/Outbreak.csv"

def read_postcode_csv(pc_filename):
    
    df = pd.read_csv(pc_filename)
    df = df[np.isfinite(df['postcode'])] # make sure the postcodes exist...
    df['postcode'] = df['postcode'].apply(lambda x: int(x)) # and are integers

    return df


def parse_outbreak(outbreak_filename):
    # now, let's import the data
    df = pd.read_csv(outbreak_filename)
    df = df[np.isfinite(df['Postcode'])] # make sure the postcodes exist...
    df['Postcode'] = df['Postcode'].apply(lambda x: int(x)) # and are integers

    return df
