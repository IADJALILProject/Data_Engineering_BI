import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="banq_db",  # Remplace par 'postgres' si bank_db n'existe pas encore
        user="postgres",
        password="anis1999"
    )
    print("✅ Connexion réussie à PostgreSQL !")
    connection.close()
except Exception as e:
    print(f"❌ Erreur de connexion : {e}")
