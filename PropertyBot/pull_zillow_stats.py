"""
Pulls data from zillow research on real estate markets
"""

import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


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
    df.to_csv('data/raw_{}'.format(save_as))
    return None 


if __name__ == "__main__":

    files = {
        'zhvi/Metro_zhvi_bdrmcnt_3_uc_sfrcondo_tier_0.33_0.67_sm_sa_mon': "home_values_metro_3_bedroom",
        'zhvi/Zip_zhvi_bdrmcnt_3_uc_sfrcondo_tier_0.33_0.67_sm_sa_mon': "home_values_zip_3_bedroom",
        'zori/Metro_ZORI_AllHomesPlusMultifamily_Smoothed': 'home_rents_metro',
        'zori/Zip_ZORI_AllHomesPlusMultifamily_Smoothed': 'home_rents_zip'

    }

    for key, value in files.items():
        df = get_csv_from_web(
            url='https://files.zillowstatic.com/research/public_v2/{0}.csv'.format(key))
        save_raw_data(df=df, save_as='{0}.csv'.format(value))
        print(df.head)
