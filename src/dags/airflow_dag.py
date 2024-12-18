import sys
import os
from prefect import flow, task
from src.ingestion.dta_ingestion import DataIngestion

# Ajouter le chemin absolu vers 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Configuration des chemins
RAW_DATA_DIR = "/opt/prefect/data/raw/"
PROCESSED_DATA_DIR = "/opt/prefect/data/processed/"

# Tâche d'ingestion pour Prefect
@task
def run_data_ingestion():
    ingestion = DataIngestion(RAW_DATA_DIR, PROCESSED_DATA_DIR)
    ingestion.ingest_all_csv()

# Définition du flow Prefect
@flow(name="data-ingestion-flow")
def data_ingestion_flow():
    run_data_ingestion()

# Exécution du flow
if __name__ == "__main__":
    data_ingestion_flow()

