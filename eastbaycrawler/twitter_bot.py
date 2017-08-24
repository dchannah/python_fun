import tweepy
import yaml
import sys
from scrapers import AuthorScraper, ArticleScraper

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


def compose_tweet(article_scraper):
    """
    Composes a tweet about an article.

    Args:
        article_scraper (ArticleScraper): An ArticleScraper object.

    Returns:
        A string to be passed to the status update of the API.

    """
    tweet_text = article_scraper.title + " " + article_scraper.url
    tweet_text += " via @eastbaytimes"
    return tweet_text


def post_tweet(status_text, twitter_api):
    """
    Posts a tweet with the specified text.

    Args:
        status_text (str): The status text of a tweet.
        twitter_api (API): A tweepy API object.

    Returns:
        None

    """
    twitter_api.update_status(status_text)
    return


def create_api(cred_yaml_file):
    """
    Creates a tweepy API object using credentials in the supplied YAML file.
    Args:
        cred_yaml_file (str): Path to the YAML file.

    Returns:
        The author's name, a tweepy API object.

    """
    with open(cred_yaml_file, 'r') as f:
        cred_yaml = yaml.load(f)
    auth = tweepy.OAuthHandler(cred_yaml['consumer_key'],
                               cred_yaml['consumer_secret'])
    auth.set_access_token(cred_yaml['access_key'] ,cred_yaml['access_secret'])
    return cred_yaml['author_name'], tweepy.API(auth)


def main():
    """
    The main method.

    Returns:
        None

    """
    config_file = "./credentials.yaml"
    author_name, api_for_author = create_api(config_file)
    author_scraper = AuthorScraper(author_name)
    known_articles = read_article_list(author_scraper.name)
    if known_articles is None:
        print("This appears to be the bot's first run; writing and exiting.")
        write_article_list(author_scraper.article_links, author_scraper.name)
        sys.exit(0)

    new_articles = list(set(author_scraper.article_links) - set(known_articles))

    for article_link in new_articles:
        scraper = ArticleScraper(article_link)
        tweet_body = compose_tweet(scraper)
        post_tweet(tweet_body, api_for_author)

    write_article_list(author_scraper.article_links, author_scraper.name)

if __name__ == "__main__":
    main()
