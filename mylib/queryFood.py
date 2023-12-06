"""Query the database"""

import sqlite3

# Define a global variable for the log file
# LOG_FILE = "query_log.md"


# def log_query(query):
#     """adds to a query markdown file"""
#     with open(LOG_FILE, "a") as file:
#         file.write(f"```sql\n{query}\n```\n\n")


def query_food(nutrition, table_name):
    """runs a query a user inputs"""
    # Connect to the SQLite database
    conn = sqlite3.connect("FoodNutritionDB.db")

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute the query to get the top 10 food of the nutrient
    nutrition_column = "Data_" + nutrition.replace(" ", "_")
    cursor.execute(
        f"SELECT Category FROM {table_name} ORDER BY {nutrition_column} DESC LIMIT 10"
    )
    result = cursor.fetchall()

    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # log_query(f"{query}")

    # return a list of foods
    print(result)
    return result


if __name__ == "__main__":
    # Test the function
    nutrition = "Protein"
    table_name = "FoodNutritionDB"
    query_food(nutrition, table_name)
    # print("Query Executed")
    # print("Query Logged")
