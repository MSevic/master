import pandas as pd
import yfinance as yf
from datetime import date, timedelta
import requests
import vars
import io


def predict(df, target_column, window):
    # url = "http://broker:8000/md3rw/rw/d3"
    url = "http://modelator_d3_rw:6001/rw/d3"
    params = {'frame_size': window,
              'target_column': target_column}
    files = {'train.csv': io.StringIO(df.to_csv())}
    response = requests.post(url, data=params, files=files)
    return response.content.decode('utf-8')


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
    dst['c_to_guess'] = dst['Close'].shift(-1)
    return dst


def get_data(commodity, from_date, to_date):
    gold = get_gold(commodity, from_date, to_date)
    covid = get_covid()
    df = pd.merge(gold, covid, how='left', on='Date').drop_duplicates()
    df.loc[[df.tail(1).index.item()], 'c_to_guess'] = 0
    df = df.dropna()
    df['Date'] = df.index
    df = df.reset_index(drop=True, inplace=False)
    return df


def make_predictions(commodity='GLD'):
    to_date = date.today().strftime("%Y-%m-%d")
    from_date = '2010-01-01'
    df = get_data(commodity, from_date, to_date)
    window = 10
    target_column = "c_to_guess"
    predicted_df = predict(df, target_column, window)
    predicted_df = io.StringIO(predicted_df)
    result = pd.read_csv(predicted_df, index_col=0)
    return result


def get_prediction_for(commodity, rows):
    rsp = getattr(vars, "df" + commodity)
    rows = int(rows)
    if rows != 0:
        rsp = rsp.tail(rows)
    return rsp.to_csv()

def update_predictions():
    vars.update()
