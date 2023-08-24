import scrapper as sc
import article as art
from constants import DATA_PATH, TAGS
import pandas as pd
import os
from datetime import datetime

def open_and_scrap_articles():
    f = pd.read_csv('../word_list.csv')
    words = f['word'].tolist()

    _Scrapper = sc.Scrapper()
    for word in words:
        _Scrapper.get_data(word, datetime.today().strftime("%Y-%m-%d"), 28)

def get_csvs_list():
    file_list = os.listdir(DATA_PATH)
    file_list_csv = [file for file in file_list if file.endswith('.csv')]
    return file_list_csv

def get_links_from_csv(csv_name: str):
    fcsv = pd.read_csv(DATA_PATH + csv_name)
    links = fcsv['links'].tolist()

    try:
        if len(links) == 0:
            raise ValueError('Not enough sources from ' + csv_name)
    except ValueError as ve:
        print('Value Error : ', ve)
    return links

def parsing_contents_from_article_url():
    csv_list = get_csvs_list()
    for csv_name in csv_list:
        links = get_links_from_csv(csv_name)
        if len(links) == 0:
            continue
        _Article = art.Article()
        for link in links:
            _Article.get_text_url(link, TAGS)

open_and_scrap_articles()

parsing_contents_from_article_url()