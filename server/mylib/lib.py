# -*- coding: utf-8 -*-

## do CRUD here

from databricks import sql
import pandas as pd
from dotenv import load_dotenv
import os

def load():
    directory = "./resources/"
    df1 = pd.read_csv(directory + "calendar_csv.csv")
    # print(df1)
    load_dotenv()
    hostname = os.getenv("SERVER_HOSTNAME")
    token = os.getenv("ACCESS_TOKEN")
    path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=hostname,
        http_path=path,
        access_token=token
    ) as connection:
        c = connection.cursor()
        # c.execute("DROP TABLE IF EXISTS us_crime") ## load once is enough torturing
        c.execute("SHOW TABLES FROM default LIKE 'calendar*'")
        rslt = c.fetchall()
        # print(rslt)
        if not rslt:
            ## create table
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS calendar (
                    date string
                    s_time string,
                    e_time string,
                    item string
                )
                """
            )
            ## insert data into table
            for _, row in df1.iterrows():
                convert = tuple(row)
                c.execute(f"INSERT INTO us_crime VALUES {convert}")
        c.close()
    return 0


if __name__ == "__main__":
    load()