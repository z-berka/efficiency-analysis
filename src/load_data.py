import pandas as pd

def load_dataset(path):
    df = pd.read_excel(path, sheet_name="Data PHEV")
    df = df.dropna(subset=["Distance [km]"])
    return df
