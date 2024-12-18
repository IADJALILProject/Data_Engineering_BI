from prefect import flow, task
from prefect.server.schemas.schedules import IntervalSchedule
from datetime import timedelta
from src.ingestion.dta_ingestion import DataIngestion
from src.transformation.star_schema import create_star_schema
from src.storage.database_storage import save_to_postgres
from src.monitoring.data_quality import data_quality_checks

@task
def ingestion_step(raw_data_path, processed_data_path):
    print("📥 Étape d'ingestion des données...")
    ingestion = DataIngestion(raw_data_path, processed_data_path)
    ingestion.ingest_all_csv()
    return processed_data_path

@task
def transformation_step(processed_data_path, transformed_data_path):
    print("🔄 Étape de transformation des données...")
    create_star_schema(processed_data_path, transformed_data_path)
    return transformed_data_path

@task
def storage_step(transformed_data_path, db_url, table_names):
    print("📦 Étape de stockage des données dans PostgreSQL...")
    for file, table in table_names.items():
        file_path = f"{transformed_data_path}/{file}"
        save_to_postgres(file_path, table, db_url)

@task
def monitoring_step(transformed_data_path, table_names):
    print("📊 Étape de monitoring des données...")
    for file, table_name in table_names.items():
        file_path = f"{transformed_data_path}/{file}"
        data_quality_checks(file_path, table_name)

@flow(name="Full Data Pipeline Orchestration")
def full_data_pipeline():
    raw_data_path = "data/raw/"
    processed_data_path = "data/processed/"
    transformed_data_path = "data/transformed/"
    db_url = "postgresql://postgres:anis1999@localhost:5432/banq_db"

    table_names = {
        "fact_transactions.csv": "fact_transactions",
        "fact_loans.csv": "fact_loans",
        "fact_payments.csv": "fact_payments",
        "fact_revenue.csv": "fact_revenue",
        "fact_fraudes.csv": "fact_fraudes",
        "dim_clients.csv": "dim_clients",
        "dim_products.csv": "dim_products",
        "dim_dates.csv": "dim_dates",
        "dim_accounts.csv": "dim_accounts",
        "dim_satisfaction.csv": "dim_satisfaction"
    }

    processed_path = ingestion_step(raw_data_path, processed_data_path)
    transformed_path = transformation_step(processed_path, transformed_data_path)
    storage_step(transformed_path, db_url, table_names)
    monitoring_step(transformed_path, table_names)
    print("🚀 Pipeline complet exécuté avec succès !")

if __name__ == "__main__":
    full_data_pipeline()
