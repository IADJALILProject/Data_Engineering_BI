import pandas as pd

def validate_transactions(input_file):
    df = pd.read_csv(input_file)
    print("Validation - Transactions:")
    print(f"Total Rows: {len(df)}")
    print(f"Missing Values:\n{df.isnull().sum()}")
    print(f"Invalid Amounts: {len(df[df['amount'] <= 0])}")

def validate_loans(input_file):
    df = pd.read_csv(input_file)
    print("Validation - Loans:")
    print(f"Total Rows: {len(df)}")
    print(f"Missing Values:\n{df.isnull().sum()}")
    print(f"Invalid Interest Rates: {len(df[df['interest_rate'] <= 0])}")

def validate_clients(input_file):
    df = pd.read_csv(input_file)
    print("Validation - Clients:")
    print(f"Total Rows: {len(df)}")
    print(f"Missing Values:\n{df.isnull().sum()}")
    print(f"Invalid Income: {len(df[df['income'] <= 0])}")

def validate_payments(input_file):
    df = pd.read_csv(input_file)
    print("Validation - Payments:")
    print(f"Total Rows: {len(df)}")
    print(f"Missing Values:\n{df.isnull().sum()}")
    print(f"Invalid Amounts: {len(df[df['amount'] <= 0])}")

if __name__ == "__main__":
    validate_transactions("data/processed/enriched_transactions.csv")
    validate_loans("data/processed/enriched_loans.csv")
    validate_clients("data/processed/enriched_clients.csv")
    validate_payments("data/processed/enriched_payments.csv")
