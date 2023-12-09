"""Query the database"""
import os
from databricks import sql
from dotenv import load_dotenv

# Define a global variable for the log file
LOG_FILE = "../../query_log_nutrition.md"  # Replace with the absolute path


def log_query(query, result="none"):
    """Adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")
        file.write(f"```response from databricks\n{result}\n```\n\n")


def query_food(nutrition):
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
            # Use parameterized query to avoid SQL injection
            nutrition_column = "Data_" + nutrition.replace(" ", "_")
            query = "SELECT Category FROM food ORDER BY {} DESC LIMIT 10".format(
                nutrition_column
            )
            c.execute(query)
            result = c.fetchall()
            result = [row[0] for row in result]
            log_query(query, result)
            c.close()
    except Exception as e:
        print(f"Error executing query: {e}")
        result = "error"


# query_food("Vitamins Vitamin B6")
