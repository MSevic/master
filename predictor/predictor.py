import pandas as pd
import yfinance as yf
from datetime import date, timedelta
import requests
import vars


def predict(df, target_column, window):
    url = "http://broker:8000/md3rw/rw/d3"
    params = {'train.csv': df.to_csv(),
              'frame_size': window,
              'target_column': target_column}
    response = requests.post(url, data=params)
    return response


def get_covid():
    df = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/casedistribution/csv')
    df['Date'] = df['dateRep']
    df['Date'] = pd.to_datetime(df.dateRep, format='%d/%m/%Y')
    df = df[['Date', 'deaths', 'cases']].groupby('Date').sum()
    df['C_7'] = df['cases'].rolling(window=7).mean()
    df['D_7'] = df['deaths'].rolling(window=7).mean()
    return df


def get_gold(commodity, from_date, to_date):
    dst = yf.download(commodity, from_date, to_date)
    dst = dst[['Close', 'High', 'Low', 'Volume']]
    dst = dst.dropna()
    dst['S_3'] = dst['Close'].rolling(window=3).mean()
    dst['S_9'] = dst['Close'].rolling(window=9).mean()
    dst['cpred_1'] = dst['Close'].shift(-1)
    return dst


def get_data(commodity, from_date, to_date):
    gold = get_gold(commodity, from_date, to_date)
    covid = get_covid()
    df = pd.merge(gold, covid, how='left', on='Date').drop_duplicates()
    df['Date'] = df.index
    df = df.reset_index(drop=True, inplace=False)
    return df


def make_predictions(commodity='GLD'):
    to_date = date.today().strftime("%Y-%m-%d")
    from_date = '2010-01-01'
    df = get_data(commodity, from_date, to_date)
    window = 10
    target_column = "cpred_1"
    predicted_df = predict(df, target_column, window)
    result = pd.read_csv(predicted_df)
    return result.to_json()


def get_prediction_for(commodity):
    rsp = getattr(vars, "df" + commodity)
    resp

def update_predictions():
    vars.update()
