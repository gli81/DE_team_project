import sqlite3


def get_column_names(database_file, table_name):
    # Connect to the SQLite database
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    try:
        # Execute a query to retrieve column names
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 1")

        # Fetch the description of the query result, which contains column information
        result_columns = [description[0] for description in cursor.description]

        # Remove "Data_" prefix from each element
        modified_columns = [column.replace("Data_", "") for column in result_columns]

        # remove "_" from each element
        modified_columns = [column.replace("_", " ") for column in modified_columns]

        # Remove the first two items
        final_columns = modified_columns[2:]

        print(final_columns)

        return final_columns

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()


if __name__ == "__main__":
    # Test the function
    pass
    # database_file = "FoodNutritionDB.db"
    # table_name = "FoodNutritionDB"
    # columns = get_column_names(database_file, table_name)
    # print("Column Names:", columns)
