"""
Extract a dataset from a URL. 
JSON or CSV formats tend to work well
"""
import os
import requests
import pandas as pd


def extract(
    url="https://raw.githubusercontent.com/gli81/DE_team_project/master/food_new.csv?raw=true",
    file_path="data/food_new.csv",
    directory="data",
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)

    # Load the CSV into a Pandas DataFrame
    df = pd.read_csv(file_path)

    # Save the two DataFrames into CSV file.
    df.to_csv(os.path.join(directory, "food_new.csv"), index=False)

    return file_path


# Call the function to extract the dataset
# extract()
