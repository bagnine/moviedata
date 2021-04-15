from bs4 import BeautifulSoup
import requests
import time
import numpy as np

class Scraper:
    
    def __init__(self, titles, title= None):
        self.titles = titles
        self.title = title
    
    def find_freshness(title):
        '''Given a title (formatted as a movie title 
           with underscores between words), find_freshness 
           inserts the title into the url and returns a
           percentage freshness score'''
        page = requests.get(f'http://rottentomatoes.com/m/{title}')
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup.find(class_= 'mop-ratings-wrap__percentage').text.strip()
        
    def fresh_list(self):
        '''Given a list of titles, fresh_list iterates
        through using find_freshness and returns a dictionary
        of title and rating percentage key:value pairs'''
        f = {}
        for i in self.titles:
            try:
                f.update({i : find_freshness(i)})
                time.sleep(np.random.randint(.01,1))
            except:
                AttributeError
                time.sleep(np.random.randint(.01, 1))
                continue
        return f