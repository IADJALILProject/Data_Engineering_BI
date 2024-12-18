import pandas as pd
import os   
# Tables de Faits
def create_fact_transactions(file, output):
    df = pd.read_csv(file)
    fact = df[['transaction_id', 'client_id', 'date', 'amount', 'fraud_flag']]
    fact.to_csv(output, index=False)

def create_fact_loans(file, output):
    df = pd.read_csv(file)
    fact = df[['loan_id', 'client_id', 'loan_amount', 'interest_rate', 'term_months', 'start_date']]
    fact.to_csv(output, index=False)

def create_fact_payments(file, output):
    df = pd.read_csv(file)
    fact = df[['payment_id', 'client_id', 'date', 'amount', 'merchant']]
    fact.to_csv(output, index=False)

def create_fact_revenue(file, output):
    df = pd.read_csv(file)
    fact = df[['branch_id', 'date', 'revenue', 'operational_cost', 'profit']]
    fact.to_csv(output, index=False)

def create_fact_fraudes(file, output):
    df = pd.read_csv(file)
    fact = df[['fraud_id', 'client_id', 'transaction_date', 'amount', 'flag']]
    fact.to_csv(output, index=False)

# Tables de Dimensions
def create_dim_clients(file, output):
    df = pd.read_csv(file)
    dim = df[['client_id', 'name', 'age', 'gender', 'income', 'credit_score']]
    dim.to_csv(output, index=False)

def create_dim_products(file, output):
    df = pd.read_csv(file)
    dim = df[['product_id', 'name', 'type', 'interest_rate']]
    dim.to_csv(output, index=False)

def create_dim_dates(file, output):
    df = pd.read_csv(file)
    dates = pd.to_datetime(df['date'], errors='coerce').dropna().drop_duplicates()
    dim = pd.DataFrame({
        'date': dates,
        'year': dates.dt.year,
        'month': dates.dt.month,
        'day': dates.dt.day,
        'quarter': dates.dt.quarter
    })
    dim.to_csv(output, index=False)

def create_dim_accounts(file, output):
    df = pd.read_csv(file)
    dim = df[['account_id', 'client_id', 'account_type', 'balance']]
    dim.to_csv(output, index=False)



def create_dim_satisfaction(input_file, output_file):
    df = pd.read_csv(input_file)
    # Sélectionne uniquement les colonnes existantes
    columns_to_keep = [col for col in ['client_id', 'service', 'rating', 'comments'] if col in df.columns]
    dim = df[columns_to_keep]
    dim.to_csv(output_file, index=False)
# === Fonction Principale ===
def create_star_schema():
    print("📊 Début de la création du schéma en étoile...")

    # Dossiers
    processed_dir = "data/processed/"
    output_dir = "data/processed/"
    os.makedirs(output_dir, exist_ok=True)

    # Faits
    create_fact_transactions(f"{processed_dir}cleaned_transactions.csv", f"{output_dir}fact_transactions.csv")
    create_fact_loans(f"{processed_dir}cleaned_loans.csv", f"{output_dir}fact_loans.csv")
    create_fact_payments(f"{processed_dir}cleaned_card_payments.csv", f"{output_dir}fact_payments.csv")
    create_fact_revenue(f"{processed_dir}cleaned_revenue_costs.csv", f"{output_dir}fact_revenue.csv")
    create_fact_fraudes(f"{processed_dir}cleaned_fraudes.csv", f"{output_dir}fact_fraudes.csv")

    # Dimensions
    create_dim_clients(f"{processed_dir}cleaned_clients.csv", f"{output_dir}dim_clients.csv")
    create_dim_products(f"{processed_dir}cleaned_products.csv", f"{output_dir}dim_products.csv")
    create_dim_dates(f"{processed_dir}cleaned_transactions.csv", f"{output_dir}dim_dates.csv")
    create_dim_accounts(f"{processed_dir}cleaned_accounts.csv", f"{output_dir}dim_accounts.csv")
    create_dim_satisfaction(f"{processed_dir}cleaned_satisfaction_clients.csv", f"{output_dir}dim_satisfaction.csv")

    print("✅ Schéma en étoile créé avec succès !")

if __name__ == "__main__":
    create_star_schema()
    
