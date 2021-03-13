import pandas as pd
import yfinance as yf
from datetime import date
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

def update_table():
    get_data()


def get_table_data(table, last_n_records):


def predict(df, target_column):
    return y

def check_last_record(table):
    last_date = False
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT DATE FROM "+table+"ORDER BY id DESC LIMIT 1")
        last_date = mycursor.fetchone()
    except:
        last_date = False

    return last_date

def get_covid():
    df = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/casedistribution/csv')
    df['Date'] = df['dateRep']
    df['Date'] = pd.to_datetime(df.dateRep, format='%d/%m/%Y')
    df = df[['Date', 'deaths', 'cases']].groupby('Date').sum()
    dst['C_7'] = dst['cases'].rolling(window=7).mean()
    dst['D_7'] = dst['deaths'].rolling(window=7).mean()
    return df


def get_gold(from_date, to_date):
    dst = yf.download('GLD', from_date, to_date)
    dst = dst[['Close', 'High', 'Low', 'Volume']]
    dst = dst.dropna()
    dst['S_3'] = dst['Close'].rolling(window=3).mean()
    dst['S_9'] = dst['Close'].rolling(window=9).mean()
    i = 0
    while i <= 15:
        i += 1
        dst['future_' + str(i)] = dst['Close'].shift(-i)
    return dst

def get_data(from_date, to_date):
    gold = get_gold(from_date, to_date)
    covid = get_covid()
    df = pd.merge(gold, covid, how='left', on='Date').drop_duplicates()
    df['Date'] = df.index
    if from_date:
        df = df[df['Date'] > from_date]
    if to_date:
        df = df[df['Date'] < to_date]

    df = df.reset_index(drop=True, inplace=False)
    return df

def write_into_table(df, table):
    mycursor = mydb.cursor()
    for index, row in df.iterrows():
        has_date = mycursor.execute("SELECT Date_entry FROM " + table + "WHERE Date_entry = " + row['Date']).fetchone()
        if not has_date:
            sql = "INSERT INTO "+TABLE+ '(Date_entry, Close, High, Low, Volume, S_3, S_9, deaths, cases, D_7, C_7) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            val = (row['Date'], row['Close'], row['High'], row['Low'], row['Volume'], row['S_3'], row['S_9'], row['deaths'], row['cases'], row['D_7'], row['C_7'])
            mycursor.execute(sql, val)
            mydb.commit()

        daybefore = row['Date'] - timedelta(days = 1)
        is_updated = mycursor.execute("SELECT creal1 FROM " + table + "WHERE Date_entry = " + daybefore).fetchone()
        if not is_updated:
            i=0
            while i<=15:
                i += 1
                daybefore = row['Date'] - timedelta(days=i)
                mycursor.execute("Update "+table+ " SET creal"+str(i)+"="+str(row['Close'])+ " WHERE Date_entry = "+daybefore)
            mydb.commit()

def make_predictions():
    commodities = ['GLD']
    today = date.today()
    for commodity in commodities:
        fromdate = check_last_record(commodity)
        if fromdate == False | fromdate < today:
            df = get_data(fromdate, today)
            write_into_table(df, commodity)
        # get data
        data = get_table_data(commodity, 10)

        i = 0
        date_of_prediction = today + timedelta(days=1)
        while i <= 15:
            i += 1
            prediction = predict(data, target_column, window)
            data = update_with_prediction(data, prediction, date_of_prediction)
            date_of_prediction = date_of_prediction + timedelta(days=1)

        update_row(commodity, i, data, today)