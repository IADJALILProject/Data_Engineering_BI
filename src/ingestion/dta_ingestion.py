import os
import pandas as pd

class DataIngestion:
    def __init__(self, raw_data_dir, processed_data_dir):
        self.raw_data_dir = raw_data_dir
        self.processed_data_dir = processed_data_dir
        os.makedirs(self.processed_data_dir, exist_ok=True)

    def ingest_all_csv(self):
        """Ingestion des 10 fichiers CSV."""
        csv_files = [
            "transactions.csv",
            "clients.csv",
            "loans.csv",
            "card_payments.csv",
            "revenue_costs.csv",
            "accounts.csv",
            "fraudes.csv",
            "products.csv",
            "interest_rates.csv",
            "satisfaction_clients.csv"
        ]

        for file in csv_files:
            input_path = os.path.join(self.raw_data_dir, file)
            output_path = os.path.join(self.processed_data_dir, f"cleaned_{file}")

            if os.path.exists(input_path):
                print(f"Ingesting and cleaning file: {file}")
                df = pd.read_csv(input_path)

                # Nettoyage de base : suppression des doublons et valeurs manquantes
                df = df.drop_duplicates().dropna()

                # Enregistrement du fichier nettoyé
                df.to_csv(output_path, index=False)
                print(f"File {file} cleaned and saved to {output_path}")
            else:
                print(f"WARNING: {file} not found in {self.raw_data_dir}")

if __name__ == "__main__":
    raw_data_dir = "data/raw/"
    processed_data_dir = "data/processed/"

    ingestion = DataIngestion(raw_data_dir, processed_data_dir)

    # Ingestion et nettoyage des 10 fichiers CSV
    ingestion.ingest_all_csv()