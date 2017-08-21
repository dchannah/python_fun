# -*- coding: utf-8 -*-
from scraper_tools import make_soup, get_authors, get_all_article_links

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
        main_soup (BeautifulSoup): A BeautifulSoup object of the author's page.
        article_links (list): A list of URLs for all of this author's articles.

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
        self.main_soup = make_soup(self.url)
        self.article_links = self.get_articles_by_author()

    def get_articles_by_author(self):
        """
        Fetches a list of links to articles by this author.

        Returns:
            A list of URLs for articles by this author only.

        """
        all_articles_on_author_page = get_all_article_links(self.main_soup)
        links_to_author_articles = []
        for link in all_articles_on_author_page:
            link_soup = make_soup(link)
            author_list = get_authors(link_soup)
            if self.name in author_list:
                links_to_author_articles.append(link)
        return links_to_author_articles
