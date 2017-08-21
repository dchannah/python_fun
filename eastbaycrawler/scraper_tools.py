# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

"""A collection of methods useful for scraping pages on the East Bay News site.

This is just a bunch of cleaned-up soup routines, more or less; I'm still
deciding on final formats for all that stuff.

"""

__author__ = "Daniel Hannah"
__email__ = "dansseriousbusiness@gmail.com"

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
        A list of all article links on the BeautifulSoup page.

    """
    return [h.get('href') for h in soup.find_all('a', class_="article-title")]

def get_authors(soup):
    """
    Gets the author(s) of a page that has been into a soup.

    Args:
        soup (BeautifulSoup): A Beautifully-souped HTML page

    Returns:
        A list of authors as ["Jim Doe", "Jane Doe", etc.]

    """
    author_name_class = soup.find_all(class_=" author-name")
    author_titles = [h.get('title') for h in author_name_class]
    list_of_authors = []
    for title in author_titles:
        firstname = title.split(" ")[2]
        lastname = title.split(" ")[3]
        authorname = firstname + " " + lastname
        list_of_authors.append(authorname)
    return list_of_authors

