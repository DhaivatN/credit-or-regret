import pandas as pd
from google.cloud import storage
from google.oauth2 import service_account

# Setup GCP credentials (placeholder)
# credentials = service_account.Credentials.from_service_account_file('your-key.json')

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df = df.dropna(subset=['loan_amnt', 'int_rate', 'term'])
    df['int_rate'] = df['int_rate'].str.rstrip('%').astype(float)
    return df
