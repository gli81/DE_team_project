import os
from databricks import sql
from dotenv import load_dotenv

# Get the current directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# Define a global variable for the log file with the full path
LOG_FILE = os.path.join(current_dir, "query_log_food.md")


def log_query(query, result="none"):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")
        file.write(f"```response from databricks\n{result}\n```\n\n")


def query():
    # print("got here")
    try:
        # Ensure the directory for the log file exists
        log_dir = os.path.dirname(LOG_FILE)
        os.makedirs(log_dir, exist_ok=True)

        # Load environment variables
        load_dotenv()

        # Check if required environment variables are set
        server_h = os.getenv("SERVER_HOSTNAME")
        access_token = os.getenv("ACCESS_TOKEN")
        http_path = os.getenv("HTTP_PATH")
        # print(server_h, access_token, http_path)
        if not all([server_h, access_token, http_path]):
            # print("missing")
            raise ValueError("One or more required environment variables are missing.")
        # print("eeeeee")
        with sql.connect(
            server_hostname=server_h,
            http_path=http_path,
            access_token=access_token,
        ) as connection:
            # print("set up connection")
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
            log_query("DESCRIBE TABLE food", result)
            c.close()

    except Exception as e:
        # Log the error to a separate log file or console
        print("Error executing query:", e)
        # Optionally, log the error to a separate log file
        with open(os.path.join(current_dir, "error_log.txt"), "a") as error_file:
            error_file.write(f"Error executing query: {e}\n")
        result = ["error"]
    finally: return result


# query()
