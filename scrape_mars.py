
import requests
from bs4 import BeautifulSoup
import pandas as pd


def news():
    url = "https://mars.nasa.gov/news/"
    data = requests.get(url)
    soup = BeautifulSoup(data.text, "html.parser")
    target = soup.find('div', {'class': 'content_title'})
    what_i_want = target.find('a')
    link = what_i_want.get("href")
    title = target.get_text()
    website = "https://mars.nasa.gov"
    article_url = website + link
    other_data = requests.get(article_url)
    soup = BeautifulSoup(other_data.text, "html.parser")
    target = soup.find('div', {'class': "wysiwyg_content"})
    paragraph_string = ''
    for each in target.findAll('p'):
        paragraph_string += each.get_text()
    return title, paragraph_string


def image():
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    data = requests.get(url)
    soup = BeautifulSoup(data.text, "html.parser")
    target = soup.find('a', {'class': 'fancybox'})
    image_url_end = target.get("data-fancybox-href")
    website = "https://www.jpl.nasa.gov"
    featured_image_url = website + image_url_end
    return featured_image_url


def twitter():
    url = "https://twitter.com/marswxreport?lang=en"
    data = requests.get(url)
    soup = BeautifulSoup(data.text, "html.parser")
    target = soup.find('p', {'class': 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'})
    mars_weather = target.get_text()
    return mars_weather

def table():
    url = "https://space-facts.com/mars/"
    mars_table = pd.read_html("http://space-facts.com/mars/")
    return mars_table



def scrape():
    paragraph_title, paragraph_string = news()
    my_dict = {}
    my_dict['paragraph_title'] = paragraph_title  
    my_dict['paragraph_string'] = paragraph_string
    my_dict['featured_image'] = image()
    my_dict['twitter'] = twitter()
    my_dict['table'] = table()

    return my_dict

