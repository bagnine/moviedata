import pandas as pd 
import re
import requests
import time
import numpy as np
from bs4 import BeautifulSoup

def money_to_int(column):
    a = column.astype(str)
    b = a.str.replace('$', '')
    c = b.str.replace(',', '')
    return c.astype(float)

def col_datetime(column):
    a = pd.to_datetime(column)
    return a

def calculate_net(gross, budget):
    a = gross - budget
    return a

def calculate_roi(net, budget):
    a = (net / budget) * 100
    return a

def release_window(df, column_name):
    a = df[~df[column_name].isin(pd.date_range(start='1915-01-01', end= '1999-12-31'))]
    return a 

def genre_convert(column):
    a = column.apply(lambda x: re.split(",",x) if isinstance(x,str) else x)
    for i in list(range(len(a))):
        try:
            if  type(a[i][0]) == str:
                a[i][0].split(',')
        except KeyError:
            i +=1
            continue
    return a

def scrape(titles):
    
    def find_freshness(title):
        page = requests.get(f'http://rottentomatoes.com/m/{title}')
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup.find(class_= 'mop-ratings-wrap__percentage').text.strip()
    
    def fresh_list(titles):
        f = {}
        for i in titles:
            try:
                f.update({i : find_freshness(i)})
                time.sleep(np.random.randint(.01,1))
            except:
                AttributeError
                time.sleep(np.random.randint(.01, 1))
                continue
        return f 
    fresh_scores = fresh_list(titles)
    return fresh_scores

def create_genre_column(column, genre):
    a = column.apply(lambda x: genre in x).astype(int)
    return a

def create_genre_columns(df, column, list_of_genres):
    for i in list_of_genres:
         df[i] = create_genre_column(column, i)
    return df

def find_genre_profit(df, genre):
    df1 = df[df[genre]!=0]
    return df1['profit_percentage'].mean()

def find_genre_profits(df, list_of_genres):
    gendict = {}
    for i in list_of_genres:
        gendict.update({i : find_genre_profit(df, i)})
    return gendict 

def find_genre_rating(df, genre):
    df1 = df[df[genre]!=0]
    return df1['rating'].mean()

def find_genre_ratings(df, list_of_genres):
    gendict = {}
    for i in list_of_genres:
        gendict.update({i : find_genre_rating(df, i)})
    return gendict 