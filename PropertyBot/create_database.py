"""
Creates database from csv files
"""


import os
import pandas as pd
import sqlite3
from datetime import datetime



def csv_to_db(csv_file, db_name, table_name,  if_exists):
    """
    Takes a csv file and loads it into a sqlite database

    After the file is uploaded it deletes the csv that
    was used to load into the database to keep thing clean.

    filname = name of csv file to load
    db_name = name of database to add csv to
    table_name = name of table in database to add csv to
    if_exitst = what to do if table exists (e.g. replace or append)

    """
    #read csv from url
    df = pd.read_csv("data/{0}.csv".format(csv_file))
    df['ds'] = datetime.today().strftime('%Y-%m-%d')
    print(df)

    #creating the database
    db = sqlite3.connect('data/{0}.db'.format(db_name))
    db.text_factory = str

    #cleaning column names
    df.columns = df.columns.str.replace('$', 'price')
    df.columns = df.columns.str.replace('[^a-zA-Z]', '')
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = map(str.lower, df.columns)

    #saving to database
    df.to_sql('{0}'.format(table_name), db, if_exists=if_exists)

    #removing csv file after it has been imported
    os.remove("data/{0}.csv".format(csv_file))
    return None

if __name__ == "__main__":
    csv_to_db(csv_file='redfin_2020-05-24-14-22-24', db_name='propertybot', table_name='listings',  if_exists='replace')
