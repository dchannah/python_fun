# -*- coding: utf-8 -*-
from author_scraper import AuthorScraper


def main():
    """
    The main method.

    Returns: What I want it to.

    """
    author_name = "Aaron Davis"
    ad_scraper = AuthorScraper(author_name)

    links_on_page = ad_scraper.get_all_article_links()
    for link in links_on_page:
        page_soup =


if __name__ == "__main__":
    main()