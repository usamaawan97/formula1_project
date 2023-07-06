# Databricks notebook source
# MAGIC %run "../includes/configuration"

# COMMAND ----------

races_df = spark.read.parquet(f"{processed_folder_path}/races").filter("race_year = 2019") \
.withColumnRenamed("name","race_name")

# COMMAND ----------

circuits_df = spark.read.parquet(f"{processed_folder_path}/circuits") \
.withColumnRenamed("name","circuit_name")

# COMMAND ----------

race_circuits_df = circuits_df.join(races_df, circuits_df.circuit_id == races_df.circuit_id, "inner")\
.select(circuits_df.circuit_name, circuits_df.location, circuits_df.country, races_df.race_name, races_df.round)

# COMMAND ----------

display(race_circuits_df)

# COMMAND ----------

