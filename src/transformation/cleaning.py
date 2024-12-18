import pandas as pd
import os

def clean_data(input_file, output_file):
    df = pd.read_csv(input_file)
    df = df.drop_duplicates().dropna()
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    raw_files = [
        "transactions", "clients", "loans", "card_payments", "revenue_costs",
        "accounts", "fraudes", "products", "interest_rates", "satisfaction_clients"
    ]
    for file in raw_files:
        clean_data(f"data/raw/{file}.csv", f"data/processed/cleaned_{file}.csv")
