import sys
import os

# Ajouter le chemin du projet à sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import pandas as pd
from src.transformation import cleaning

class TestTransformation(unittest.TestCase):
    def setUp(self):
        self.input_file = "data/raw/transactions.csv"
        self.output_file = "data/processed/test_cleaned_transactions.csv"

    def test_cleaning(self):
        # Appel de la fonction de nettoyage
        cleaning.clean_data(self.input_file, self.output_file)

        # Vérifie si le fichier nettoyé est créé
        self.assertTrue(os.path.exists(self.output_file), "Le fichier nettoyé n'a pas été créé.")

        # Vérifie si les doublons et les valeurs manquantes sont supprimés
        df = pd.read_csv(self.output_file)
        self.assertFalse(df.duplicated().any(), "Le fichier contient des doublons.")
        self.assertEqual(df.isnull().sum().sum(), 0, "Le fichier contient des valeurs manquantes.")

    def tearDown(self):
        # Nettoyage après le test
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

if __name__ == "__main__":
    unittest.main()
