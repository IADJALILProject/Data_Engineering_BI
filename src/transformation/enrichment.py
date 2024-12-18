import pandas as pd

def enrich_transactions(input_file, output_file):
    df = pd.read_csv(input_file)
    df['transaction_category'] = df['amount'].apply(lambda x: 'High' if x > 1000 else 'Low')
    df['transaction_year'] = pd.to_datetime(df['date']).dt.year
    df.to_csv(output_file, index=False)
    print("Enriched transactions saved.")

def enrich_loans(input_file, output_file):
    df = pd.read_csv(input_file)
    df['loan_status'] = df['loan_amount'].apply(lambda x: 'Large' if x > 20000 else 'Small')
    df['loan_interest_category'] = df['interest_rate'].apply(lambda x: 'High' if x > 5 else 'Low')
    df.to_csv(output_file, index=False)
    print("Enriched loans saved.")

def enrich_clients(input_file, output_file):
    df = pd.read_csv(input_file)
    df['income_category'] = df['income'].apply(lambda x: 'High' if x > 80000 else 'Medium' if x > 40000 else 'Low')
    df['age_group'] = pd.cut(df['age'], bins=[0, 25, 50, 100], labels=['Young', 'Adult', 'Senior'])
    df.to_csv(output_file, index=False)
    print("Enriched clients saved.")

def enrich_payments(input_file, output_file):
    df = pd.read_csv(input_file)
    df['large_payment'] = df['amount'].apply(lambda x: True if x > 500 else False)
    df.to_csv(output_file, index=False)
    print("Enriched payments saved.")

if __name__ == "__main__":
    enrich_transactions("data/processed/fact_transactions.csv", "data/processed/enriched_transactions.csv")
    enrich_loans("data/processed/fact_loans.csv", "data/processed/enriched_loans.csv")
    enrich_clients("data/processed/dim_clients.csv", "data/processed/enriched_clients.csv")
    enrich_payments("data/processed/fact_payments.csv", "data/processed/enriched_payments.csv")
