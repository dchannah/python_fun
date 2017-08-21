# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

"""Author scraper for East Bay News.

This class implements functionality to pull information about a particular
author's page on the Easy Bay News website. Right now, we are focused on 
providing a list of all articles created by that particular author, but other 
functionality will be added in the future.

"""

__author__ = "Daniel Hannah"
__email__ = "dansseriousbusiness@gmail.com"

class AuthorScraper():
    """
    This is a class, to be declared for a particular author, which will get
    information about that author's page on the East Bay News website.

    Attributes:
        name (str): "<Author's first name> <Author's last name>"
        url (str): Author's homepage on the East Bay News website.
        main_soup(BeautifulSoup): A BeautifulSoup object of the author's page.

    """

    def __init__(self, authorname):
        """
        Initializes the AuthorScraper.

        Args:
            authorname (str):  "<Author's first name> <Author's last name>"

        """
        self.name = authorname
        author_first_name, author_last_name = authorname.split(sep=" ")
        base_url = "http://www.eastbaytimes.com/author/"
        base_url += author_first_name + "-" + author_last_name + "/"
        self.url = base_url
        self.main_soup = self.make_soup(self.url)

    def make_soup(self, url):
        """
        Creates a BeautifulSoup object from the given URL.

        Args:
            url (str): URL we want a Soup object for.

        Returns:
            A BeautifulSoup HTML-parsed object.

        """
        page = requests.get(url)
        return BeautifulSoup(page.content, 'html.parser')

    def get_all_article_links(self):
        """
        Gets all of the article links on a given page, author or not.

        Args:
            None

        Returns:
            A list of all article links on the Beautiful soup page.

        """
        links = [h.get('href') for h in
                 self.main_soup.find_all('a', class_="article-title")]
        return links

    def get_author(self):
        """
        Finds the author of an East Bay News article page.

        Args:
            None

        Returns:
            A string which is the author's name.

        """
        all_titles = self.main_soup.find_all(class_="article-title")
        for title in all_titles:
            print(title)