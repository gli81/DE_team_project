"""
transform and load function
"""
# import pandas as pd

# from pyspark.sql import SparkSession
# from pyspark.sql.functions import monotonically_increasing_id

def load(dataset="dbfs:/FileStore/data/food_new.csv"):
    # spark = SparkSession.builder.appName("Read CSV").getOrCreate()
    # # load csv and transform it by inferring schema 
    # food = spark.read.csv(dataset, header=True, inferSchema=True)

    # # add unique IDs to the DataFrames
    # food = food.withColumn("id", monotonically_increasing_id())

    # # transform into a delta lakes table and store it 
    # food.write.format("delta").mode("overwrite").saveAsTable("Food")
    # # food = pd.read_csv(dataset)
    # # print(food.head())

    # # num_rows = food.count()
    # # print(num_rows)
    
    return "finished transform and load"

if __name__ == "__main__":
    load()