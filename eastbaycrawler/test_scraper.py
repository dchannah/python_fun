# -*- coding: utf-8 -*-
from scrapers import AuthorScraper
from scraper_tools import make_soup, get_authors, get_article_title


def main():
    """
    The main method.

    Returns: What I want it to.

    """
    author_name = "Aaron Davis"
    ad_scraper = AuthorScraper(author_name)
    all_article_links = ad_scraper.get_articles_by_author()
    first_article = all_article_links[0]
    first_article_soup = make_soup(first_article)
    print(get_article_title(first_article_soup))


if __name__ == "__main__":
    main()