import boto3

LOCAL_PATH = '/Users/jjespin/Downloads/'
FILE_NAME = 'redfin_2021-02-01-11-52-17.csv'

s3 = boto3.resource('s3')
s3.meta.client.upload_file('{}/{}'.format(LOCAL_PATH, FILE_NAME), \
    'propertybot', \
    'redfin_2021-02-01-11-52-17.csv')


