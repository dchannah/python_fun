import tweepy
import yaml
from author_scraper import AuthorScraper

"""A Twitter bot to automatically tweet about East Bay Times articles.

This script reads in a "known" list of articles from a YAML file and compares it
to a current list (pulled from the East Bay Times website) of articles
associated with a particular author. If there are differences, the bot
automatically posts a tweets about the new articles.

"""

__author__ = "Daniel Hannah"
__email__ = "dansseriousbusiness@gmail.com"

YAML_DIR = "./"  # A global variable to pre-pend to the YAML file names.


def generate_yaml_file(authorname):
    """
    Generates the standard YAML file name for an East Bay Times news author.

    Args:
        authorname (str): The name of author we are tweeting for.

    Returns:
        A string containing the appropriate YAML file name.

    """
    author_first_name = authorname.split(" ")[0]
    author_last_name = authorname.split(" ")[1]
    yaml_file = YAML_DIR + author_first_name + "_" + author_last_name + ".yaml"
    return yaml_file


def write_article_list(link_list, authorname):
    """
    Writes a list of article links to a YAML file.

    Args:
        link_list (list): A list of URLs to an author's articles.
        authorname (str): "Jim Doe"

    Returns:
        None

    """
    yaml_file = generate_yaml_file(authorname)
    with open(yaml_file, 'w') as f:
        yaml.dump(link_list, f, default_flow_style=False)
    return


def read_article_list(authorname):
    """
    Reads the "previous" or "known" articles from a known YAML file.

    Args:
        authorname (str): "Jim Doe"

    Returns:
        A list of article URL previously known to this bot.

    """
    yaml_file = generate_yaml_file(authorname)
    with open(yaml_file, 'r') as f:
        return yaml.load(f)


def main():
    """
    The main method.

    Returns:
        None

    """
    author_name = "Aaron Davis"
    author_scraper = AuthorScraper(author_name)
    known_articles = read_article_list(author_scraper.name)
    new_articles = list(set(author_scraper.article_links) - set(known_articles))

    """Eventually we want to have something like this:
    for article in new_articles:
        tweet_about_article(article)
    """

    write_article_list(author_scraper.article_links, author_scraper.name)

if __name__ == "__main__":
    main()
