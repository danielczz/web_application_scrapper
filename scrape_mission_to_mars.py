from splinter import Browser
from bs4 import BeautifulSoup
import time  

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"} # Mac
    # executable_path = {"executable_path": "chromedriver.exe"} # Windows
    return Browser("chrome", **executable_path, headless=False)

# Step 1 - Scraping

def scrape():
    browser = init_browser()
    listings = {}

    # NASA Mars News

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # listings["headline"]
    listings["headline"] = soup.find(class_="content_title").get_text()    

    # listings["article_body"]
    listings["article_body"] = soup.find(class_="article_teaser_body").get_text()
    
    time.sleep(1)

# JPL Mars Space Images - Featured Image

    # Visit image for listings["website"]
    url_mars = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_mars)

    time.sleep(1)

    # Scrape page into Soup
    html_mars = browser.html
    soup = BeautifulSoup(html_mars, "html.parser")

    # listings["image"] query
    relative_image_path = soup.find_all('img')[3]["src"]

    # Build final url to store
    url_intro = "https://www.jpl.nasa.gov"
    mars_img = url_intro + relative_image_path

    # listings["image"] file
    listings["image"] = mars_img

# Mars Weather

    time.sleep(1)

    # Visit twitter for listings["tweet"]
    url_tweet_mars = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_tweet_mars)

    # Scrape page into Soup
    html_tweet = browser.html
    soup = BeautifulSoup(html_tweet, "html.parser")

    # listings["tweet"] = soup.find(class_="content").get_text()    
    listings["tweets"] = soup.find(class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text()    

    # Close the browser after scraping
    browser.quit()

# Mars Facts





    return listings