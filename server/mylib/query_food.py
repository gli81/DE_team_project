"""Query the database"""
import os
from databricks import sql
from dotenv import load_dotenv

# Define a global variable for the log file
LOG_FILE = "../../query_log_food.md"  # Replace with the absolute path


def log_query(query, result="none"):
    """Adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")
        file.write(f"```response from databricks\n{result}\n```\n\n")


def query():
    # Load environment variables
    load_dotenv()

    # Check if required environment variables are set
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")

    if not all([server_h, access_token, http_path]):
        print("One or more required environment variables are missing.")
        return

    try:
        with sql.connect(
            server_hostname=server_h,
            http_path=http_path,
            access_token=access_token,
        ) as connection:
            c = connection.cursor()
            # Modified SQL command to get column names
            c.execute("DESCRIBE TABLE food")
            result_columns = c.fetchall()
            # Extract column names from the result and store them in a list
            column_names = [column.col_name for column in result_columns]

            # You can perform additional modifications to column names if needed
            modified_columns = [
                column.replace("Data_", "").replace("_", " ") for column in column_names
            ]

            # Drop the first item from the modified_columns list
            result = modified_columns[1:-1]
            c.close()
    except Exception as e:
        print(f"Error executing query: {e}")
        result = "error"

    log_query("DESCRIBE TABLE food", result)


query()
