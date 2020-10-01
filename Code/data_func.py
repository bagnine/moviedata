import pandas as pd 
import re
import requests
import time
import numpy as np

def money_to_int(column):
    ''' converts an object with $ and , to a float with no punctuation '''
    a = column.astype(str)
    b = a.str.replace('$', '')
    c = b.str.replace(',', '')
    return c.astype(float)

def col_datetime(column):
    ''' converts a columns or list to pandas datetime '''
    a = pd.to_datetime(column)
    return a

def calculate_net(gross, budget):
    ''' returns difference between gross and budget in two arrays '''
    a = gross - budget
    return a

def calculate_roi(net, budget):
    ''' takes in net and budget figures and calculates profit '''
    a = (net / budget) * 100
    return a

def release_window(df, column_name):
    ''' takes in a dataframe and column containing date and removes
        all rows containing values between 1915 and 2000 ''' 
    a = df[~df[column_name].isin(pd.date_range(start='1915-01-01', end= '1999-12-31'))]
    return a 

def genre_convert(column):
    ''' converts a column of genre names into a seperated list '''
    a = column.apply(lambda x: re.split(",",x) if isinstance(x,str) else x)
    for i in list(range(len(a))):
        try:
            if  type(a[i][0]) == str:
                a[i][0].split(',')
        except KeyError:
            i +=1
            continue
    return a

def create_genre_column(column, genre):
    ''' creates a column of 1 or 0 values depending on 
        the row containing the input genre'''
    a = column.apply(lambda x: genre in x).astype(int)
    return a

def create_genre_columns(df, column, list_of_genres):
    ''' using create_genre_column, this function creates 
        columns for every genre in a provided list'''
    for i in list_of_genres:
         df[i] = create_genre_column(column, i)
    return df

def find_genre_profit(df, genre):
    ''' returns the average profit of a given genre '''
    df1 = df[df[genre]!=0]
    return df1['profit_percentage'].mean()

def find_genre_profits(df, list_of_genres):
    ''' using find_genre_profit, returns a dictionary 
        of genre:average profit key/value pairs '''
    gendict = {}
    for i in list_of_genres:
        gendict.update({i : find_genre_profit(df, i)})
    return gendict 

def find_genre_rating(df, genre):
    ''' given a dataframe and genre, returns the average rating '''
    df1 = df[df[genre]!=0]
    return df1['rating'].mean()

def find_genre_ratings(df, list_of_genres):
    ''' given a dataframe and list of genres, returns a 
        dictionary of genre:rating key/value pairs '''
    gendict = {}
    for i in list_of_genres:
        gendict.update({i : find_genre_rating(df, i)})
    return gendict 