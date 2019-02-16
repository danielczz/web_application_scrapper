from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"} # Mac
    # executable_path = {"executable_path": "chromedriver.exe"} # Windows
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    listings = {}

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # listings["headline"] = soup.find("a", class_="result-title").get_text()    
    listings["headline"] = soup.find(class_="content_title").get_text()    

    # listings["headline"] = /soup.find("a").get_text()
    listings["price"] = soup.find(class_="article_teaser_body").get_text()
    # listings["hood"] = soup.find("span", class_="result-hood").get_text()

    return listings
