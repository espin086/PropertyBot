"""
Analysis rental listings from a database and writes results to a database
"""


import pandas as pd
import numpy as np
import sqlite3


DB = sqlite3.connect('data/propertybot.db')

def get_listings():
    """
    gets listing data from database
    """


    df = pd.read_sql_query("""
    SELECT *
    FROM listings
    """, DB)
    return df


def calc_mortgage(df, downpayment=.25, amortization=30, int_rate=.05):
    """
    Calculates the mortgage payment and ads it to dataframe
    """
    df['down_payment'] = df['price'] * downpayment
    df['loan_amount'] = df['price'] - df['down_payment']
    def calc_mortgage_payment(loan_amount, amortization_period=amortization, yearly_rate=int_rate):
        monthly_interest_rate = ((1 + yearly_rate)**(1 / 12) - 1)
        payment = np.pmt(rate=monthly_interest_rate, nper=12*amortization_period, pv=loan_amount)
        return payment
    df['mortgage_payment'] = df['loan_amount'].apply(calc_mortgage_payment)
    return df

def calc_property_tax(df, rate=.02):
    """
    Calculates the monthly tax liability for a property
    """
    df['property_tax'] = (df['price'] * rate * -1) / 12
    return df

def calc_rent():
    """
    Estimates average rent for unit
    """
    return None

def calc_miscellaneous_expense():
    """
    Estimates average rent for unit
    - Insurance
    - Capital expenditures
    - Maintenance
    - Property Management
    - Water
    - Electricity
    - Garbage
    - Vacancy

    """
    return None


if __name__ == "__main__":
    df = get_listings()
    df = calc_mortgage(df=df)
    df = calc_property_tax(df=df)
    #saves analysis of listings to a table in the database

    df = df.drop(['saletype',
        'solddate',
        'propertytype',
        'stateorprovince',
        'location',
        'status',
        'nextopenhousestarttime',
        'nextopenhouseendtime',
        'urlseehttpwwwredfincombuyahomecomparativemarketanalysisforinfoonpricing',
        'source',
        'pricesquarefeet',
        'hoamonth',
        'mls',
        'interested',
        'favorite',
        'latitude',
        'longitude'

        ], axis=1)
    print(df.columns)
    df.to_sql('listing_analysis', DB, if_exists='replace')


    output = pd.read_sql_query("""
    SELECT *
    FROM listing_analysis
    WHERE squarefeet > 2000
    ORDER BY down_payment ASC
    """, DB)

    print(output)
