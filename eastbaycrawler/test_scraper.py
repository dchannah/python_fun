# -*- coding: utf-8 -*-
from author_scraper import AuthorScraper
from scraper_tools import make_soup, get_authors


def main():
    """
    The main method.

    Returns: What I want it to.

    """
    author_name = "Aaron Davis"
    ad_scraper = AuthorScraper(author_name)
    print(len(ad_scraper.get_articles_by_author()))


if __name__ == "__main__":
    main()