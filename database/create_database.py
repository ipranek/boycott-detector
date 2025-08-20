import pandas as pd 
import sqlite3
import numpy as np 
import os

boycott_info = pd.read_csv("/Users/ipekoner/Documents/GitHub/boycott-detector/data/boycott_reasons.csv")

conn = sqlite3.connect("boycott_info.pd")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS boycott_info( 
            Brand TEXT PRIMARY KEY,
            Boycott_Status TEXT,
            Reason TEXT,
            Citation NOT NULL
            );
""")


conn.commit()

boycott_info.to_sql("boycott_info", conn, if_exists="append", index=False)

conn.commit()
conn.close()