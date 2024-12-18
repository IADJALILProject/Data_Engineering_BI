import pandas as pd
from sqlalchemy import create_engine

def save_to_postgres(input_file, table_name, db_url):
    """
    Fonction pour sauvegarder un fichier CSV dans une table PostgreSQL.
    """
    try:
        engine = create_engine(db_url)
        df = pd.read_csv(input_file)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"✅ Table '{table_name}' sauvegardée avec succès dans PostgreSQL.")
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde de '{table_name}' : {e}")

if __name__ == "__main__":
    # Configuration de la connexion PostgreSQL
    db_url = "postgresql://postgres:anis1999@localhost:5432/banq_db"

    # Chemins des fichiers et noms des tables à sauvegarder
    tables_to_store = {
        # Tables de Faits
        "data/processed/fact_transactions.csv": "fact_transactions",
        "data/processed/fact_loans.csv": "fact_loans",
        "data/processed/fact_payments.csv": "fact_payments",
        "data/processed/fact_revenue.csv": "fact_revenue",
        "data/processed/fact_fraudes.csv": "fact_fraudes",

        # Tables de Dimensions
        "data/processed/dim_clients.csv": "dim_clients",
        "data/processed/dim_products.csv": "dim_products",
        "data/processed/dim_dates.csv": "dim_dates",
        "data/processed/dim_accounts.csv": "dim_accounts",
        "data/processed/dim_satisfaction.csv": "dim_satisfaction",
    }

    # Boucle pour sauvegarder chaque table dans PostgreSQL
    for input_file, table_name in tables_to_store.items():
        print(f"📤 Sauvegarde en cours : {table_name}")
        save_to_postgres(input_file, table_name, db_url)
