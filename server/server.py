# -*- coding: utf-8 -*-

## do CRUD now, include flask later


# from databricks import sql
# import pandas as pd
# from dotenv import load_dotenv
# import os
from flask import Flask

app = Flask(__name__)

# routing 
@app.route("/query_neutrient")
def query_nutrient():
    pass


@app.route("/query_some")
def query_one():
    pass


if __name__ == "__main__":
    app.run(debug=True)