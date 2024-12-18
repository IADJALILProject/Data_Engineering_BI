import pandas as pd

def data_quality_checks(file, table_name):
    df = pd.read_csv(file)
    print(f"Data Quality Report for {table_name}")
    print(f"Total Rows: {len(df)}")
    print(f"Missing Values:\n{df.isnull().sum()}")
    print(f"Duplicate Rows: {df.duplicated().sum()}\n")

if __name__ == "__main__":
    data_quality_checks("data/processed/enriched_transactions.csv", "fact_transactions")
    data_quality_checks("data/processed/enriched_loans.csv", "fact_loans")
    data_quality_checks("data/processed/dim_clients.csv", "dim_clients")
