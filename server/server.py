# -*- coding: utf-8 -*-
## just a flask api

from flask import Flask, render_template, request, jsonify
from mylib.extract_databricks import extract
from mylib.transform_load_databricks import load
from mylib.query_food import query
from mylib.query_nutrition import query_food
import os

app = Flask(__name__)
DB_NAME = "FoodNutritionDB.db"
TABLE_NAME = "FoodNutritionDB"

## do check database here
if not os.path.exists(DB_NAME):
    extract()
    load()


# routing
@app.route("/")
def index():
    ## make a query to get all distinct nutrients in our database
    columns = query()
    # nuts = ["Alpha Carotene", "Beta Carotene", ""]
    return render_template("index.html", nuts=columns)

@app.route("/index_for_react")
def index_():
    ## make a query to get all distinct nutrients in our database
    # nuts = ["Alpha Carotene", "Beta Carotene", ""]
    # return render_template("index.html", nuts = nuts)
    columns = query()
    return {"nutrients": columns}


@app.route("/query_one")
def query_one():
    ## make a query to get {maybe 5} food with that nutrient
    selected = request.args.get("selectedOption")
    food = query_food(selected, TABLE_NAME)
    food = list(map(lambda x:x[0], food))
    return render_template(
        "result.html",
        selected=selected,
        table=food
    )
    return {"Result": "page", "display": "results for the selected nutrient"}
    abab = jsonify({"Result": "page", "display": "results for the selected nutrient"})
    print(abab)
    return abab


@app.route("/members")
def members():

    # data = {"members": ["m1", "m2"]}
    # response = jsonify(data)
    # response.headers["Content-Type"] = "application/json"
    # print(response.json)
    response = {"members": ["m1", "m2"]}
    return response
    


if __name__ == "__main__":
    app.run(debug=True)
