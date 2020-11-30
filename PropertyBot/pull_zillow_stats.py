"""
Pulls data from zillow research on real estate markets
"""

import pandas as pd


def get_csv_from_web(url):
    """
    gets csv form a url
    """
    data_url = url
    df = pd.read_csv(data_url)
    return df


def save_raw_data(df, save_as):
    """
    saves raw data into local file
    """
    df.to_csv('../data/raw_{}'.format(save_as))
    return None 


if __name__ == "__main__":
    df = get_csv_from_web(
        url='http://files.zillowstatic.com/research/public_v2/zhvi/Metro_Zhvi_SingleFamilyResidence.csv')
    print(df.head)
