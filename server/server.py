# -*- coding: utf-8 -*-

## just a flask api


# from databricks import sql
# import pandas as pd
# from dotenv import load_dotenv
# import os
from flask import Flask, render_template, request, jsonify
from mylib.extract import extract
from mylib.transform_load import load
from mylib.queryFood import query_food
from mylib.queryNutrition import get_column_names

app = Flask(__name__)

## do check database here
extract()


# routing 
@app.route("/")
def index():
    ## make a query to get all distinct nutrients in our database
    nuts = ["Alpha Carotene", "Beta Carotene", ""]
    return render_template("index.html", nuts = nuts)
    return {
        "nutrients": ['Alpha CaroteneBeta Carotene']
    }

@app.route("/index_for_react")
def index_():
    ## make a query to get all distinct nutrients in our database
    # nuts = ["Alpha Carotene", "Beta Carotene", ""]
    # return render_template("index.html", nuts = nuts)
    return {
        "nutrients": ["Alpha Carotene","Beta Carotene"]
    }

@app.route("/query_one")
def query_one():
    ## make a query to get {maybe 5} food with that nutrient
    selected = request.args.get("selectedOption")
    print(selected)
    table = ["aaa", "bbb", "ccc"]
    return render_template(
        "result.html",
        selected = selected,
        table = table
    )
    return {
        "Result": "page",
        "display": "results for the selected nutrient"
    }
    abab = jsonify({
        "Result": "page",
        "display": "results for the selected nutrient"
    })
    print(abab)
    return abab

@app.route("/members")
def members():
    # return "fuck you react"

    # data = {"members": ["m1", "m2"]}
    # response = jsonify(data)
    # response.headers["Content-Type"] = "application/json"
    # print(response.json)
    response = {"members": ["m1", "m2"]}
    return response


if __name__ == "__main__":
    app.run(debug=True)