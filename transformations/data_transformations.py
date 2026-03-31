from pyspark.sql.functions import col, when

def flag_high_value_transactions(df):

    df = df.withColumn(
        "high_value_flag",
        when(col("amount") > 200, 1).otherwise(0)
    )

    return df
