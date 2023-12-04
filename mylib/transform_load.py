"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv


def load(dataset="data/food_new.csv"):
    """Transforms and Loads data into the local SQLite3 database"""
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    # skips the header of csv
    next(payload)
    conn = sqlite3.connect("FoodNutritionDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS FoodNutritionDB")
    c.execute(
        """
        CREATE TABLE FoodNutritionDB (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Category TEXT,
            Data_Alpha_Carotene REAL,
            Data_Beta_Carotene REAL,
            Data_Beta_Cryptoxanthin REAL,
            Data_Carbohydrate REAL,
            Data_Cholesterol REAL,
            Data_Choline REAL,
            Data_Fiber REAL,
            Data_Lutein_and_Zeaxanthin REAL,
            Data_Lycopene REAL,
            Data_Niacin REAL,
            Data_Protein REAL,
            Data_Retinol REAL,
            Data_Riboflavin REAL,
            Data_Selenium REAL,
            Data_Sugar_Total REAL,
            Data_Thiamin REAL,
            Data_Water REAL,
            Data_Fat_Monosaturated_Fat REAL,
            Data_Fat_Polysaturated_Fat REAL,
            Data_Fat_Saturated_Fat REAL,
            Data_Fat_Total_Lipid REAL,
            Data_Major_Minerals_Calcium REAL,
            Data_Major_Minerals_Copper REAL,
            Data_Major_Minerals_Iron REAL,
            Data_Major_Minerals_Magnesium REAL,
            Data_Major_Minerals_Phosphorus REAL,
            Data_Major_Minerals_Potassium REAL,
            Data_Major_Minerals_Sodium REAL,
            Data_Major_Minerals_Zinc REAL,
            Data_Vitamins_Vitamin_A_RAE REAL,
            Data_Vitamins_Vitamin_B12 REAL,
            Data_Vitamins_Vitamin_B6 REAL,
            Data_Vitamins_Vitamin_C REAL,
            Data_Vitamins_Vitamin_E REAL,
            Data_Vitamins_Vitamin_K REAL
        )
        """
    )
    # insert
    c.executemany(
        """
        INSERT INTO FoodNutritionDB(
            Category,
            Data_Alpha_Carotene,
            Data_Beta_Carotene,
            Data_Beta_Cryptoxanthin,
            Data_Carbohydrate,
            Data_Cholesterol,
            Data_Choline,
            Data_Fiber,
            Data_Lutein_and_Zeaxanthin,
            Data_Lycopene,
            Data_Niacin,
            Data_Protein,
            Data_Retinol,
            Data_Riboflavin,
            Data_Selenium,
            Data_Sugar_Total,
            Data_Thiamin,
            Data_Water,
            Data_Fat_Monosaturated_Fat,
            Data_Fat_Polysaturated_Fat,
            Data_Fat_Saturated_Fat,
            Data_Fat_Total_Lipid,
            Data_Major_Minerals_Calcium,
            Data_Major_Minerals_Copper,
            Data_Major_Minerals_Iron,
            Data_Major_Minerals_Magnesium,
            Data_Major_Minerals_Phosphorus,
            Data_Major_Minerals_Potassium,
            Data_Major_Minerals_Sodium,
            Data_Major_Minerals_Zinc,
            Data_Vitamins_Vitamin_A_RAE,
            Data_Vitamins_Vitamin_B12,
            Data_Vitamins_Vitamin_B6,
            Data_Vitamins_Vitamin_C,
            Data_Vitamins_Vitamin_E,
            Data_Vitamins_Vitamin_K
            ) 
            VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        payload,
    )
    conn.commit()
    conn.close()
    return "FoodNutritionDB.db"


# Call the function to load the data
load()
