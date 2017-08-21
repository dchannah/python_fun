# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

"""A collection of methods useful for scraping pages.

This is just a bunch of cleaned-up soup routines, more or less; I'm still
deciding on final formats for all that stuff.

"""

def make_soup(url):
    """
    Makes a BeautifulSoup object out of a page pulled from a URL.

    Args:
        url (str): URL we want a soup object for.

    Returns:
        A BeautifulSoup HTML-parsed object.

    """
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')


def get_all_article_links(soup):
    """
    Gets all the links on a souped page.

    Args:
        soup (BeautifulSoup):

    Returns:

    """

def get_author(soup):
    """
    Gets the author of a page that has been into a soup.

    Args:
        soup (BeautifulSoup): A Beautifully-souped HTML page

    Returns:
        A string which is the author's name.

    """
    all_titles = soup.find_all(class_="article-title")
