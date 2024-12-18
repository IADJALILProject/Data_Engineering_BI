import pandas as pd

def aggregate_transactions(input_file, output_file):
    df = pd.read_csv(input_file)
    agg = df.groupby('client_id')['amount'].agg(['count', 'sum', 'mean']).reset_index()
    agg.columns = ['client_id', 'transaction_count', 'total_amount', 'average_amount']
    agg.to_csv(output_file, index=False)
    print("Aggregated transactions saved.")

def aggregate_loans(input_file, output_file):
    df = pd.read_csv(input_file)
    agg = df.groupby('client_id')['loan_amount'].agg(['sum', 'mean']).reset_index()
    agg.columns = ['client_id', 'total_loan_amount', 'average_loan_amount']
    agg.to_csv(output_file, index=False)
    print("Aggregated loans saved.")

if __name__ == "__main__":
    aggregate_transactions("data/processed/fact_transactions.csv", "data/processed/aggregated_transactions.csv")
    aggregate_loans("data/processed/fact_loans.csv", "data/processed/aggregated_loans.csv")
