# -*- coding: utf-8 -*-

## do CRUD now, include flask later


from databricks import sql
import pandas as pd
from dotenv import load_dotenv
import os

def load():
    directory = "./extracted/"
    df1 = pd.read_csv(directory + "USCrime.csv")
    df1 = df1[["year", "State", "Total"]]
    # print(df1)
    df2 = pd.read_csv(directory + "state-abbrevs.csv")
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
        c.execute("SHOW TABLES FROM default LIKE 'us_*'")
        rslt = c.fetchall()
        print(rslt)
        if not rslt:
            ## create table
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS us_crime (
                    year int,
                    state string,
                    total int
                )
                """
            )
            ## insert crime data into table
            for _, row in df1.iterrows():
                convert = tuple(row)
                c.execute(f"INSERT INTO us_crime VALUES {convert}")
        # print(df2)
        # c.execute("DROP TABLE IF EXISTS state_abbrevs")
        c.execute("SHOW TABLES FROM default LIKE 'state_*'")
        rslt = c.fetchall()
        print(rslt)
        if not rslt:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS state_abbrevs (
                    state string,
                    abbrev string
                )
                """
            )
            for _, row in df2.iterrows():
                convert = tuple(row)
                c.execute(f"INSERT INTO state_abbrevs VALUES {convert}")
        c.close()
    return 0
    


if __name__ == "__main__":
    load()