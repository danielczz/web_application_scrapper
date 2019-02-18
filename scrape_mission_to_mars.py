# import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import time  

# define init_browser function
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"} # Mac
    return Browser("chrome", **executable_path, headless=False)

# Step 1 - Scraping
def scrape():
    # call function init_browser
    browser = init_browser()

    # start empty dictionary to store data
    listings = {}

    # NASA Mars News
    # define url to visit
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    # create html variable with html info from browser
    html = browser.html
    # parse data to a variable called soup 
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
    url_tweet_mars = "https://twitter.com/MarsWxReport/media?lang=en"
    browser.visit(url_tweet_mars)

    # Scrape page into Soup
    html_tweet = browser.html
    soup = BeautifulSoup(html_tweet, "html.parser")

    # listings["tweet"] = soup.find(class_="content").get_text()    
    tweet_result = soup.find(class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text()    
    # result_soup = tweet_result.text.split("pic.")
    # listings["tweets"] = result_soup[0]

    listings["tweets"] = tweet_result
    # listings["tweets_02"] = soup.find(class_= "content", class_=" TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text()    


#     time.sleep(1)

# # JPL Mars Space Images - Featured Image

    # Visit image for listings["website"]
    url_mars_2 = "http://www.planetary.org/blogs/guest-blogs/bill-dunford/20140203-the-faces-of-mars.html"
    browser.visit(url_mars_2)

    # http://www.planetary.org/blogs/guest-blogs/bill-dunford/20140203-the-faces-of-mars.html

    time.sleep(1)

    # Scrape page into Soup
    html_mars_2 = browser.html
    soup = BeautifulSoup(html_mars_2, "html.parser")

    # listings["image"] query
    # listings["headline_img_2"] = soup.find('h5').get_text()    

    relative_image_path_2 = soup.find_all('img')[2]["src"]
    # Build final url to store
    # url_intro = "https://www.jpl.nasa.gov"
    mars_img_2 = relative_image_path_2
    # listings["image"] file
    listings["image_2"] = mars_img_2


    # listings["image"] query
    relative_image_path_3 = soup.find_all('img')[3]["src"]
    # Build final url to store
    # url_intro = "https://www.jpl.nasa.gov"
    mars_img_3 = relative_image_path_3
    # listings["image"] file
    listings["image_3"] = mars_img_3


    # listings["image"] query
    relative_image_path_4 = soup.find_all('img')[4]["src"]
    # Build final url to store
    # url_intro = "https://www.jpl.nasa.gov"
    mars_img_4 = relative_image_path_4
    # listings["image"] file
    listings["image_4"] = mars_img_4


    # listings["image"] query
    relative_image_path_5 = soup.find_all('img')[5]["src"]
    # Build final url to store
    # url_intro = "https://www.jpl.nasa.gov"
    mars_img_5 = relative_image_path_5
    # listings["image"] file
    listings["image_5"] = mars_img_5



    relative_image_path_4 = soup.find_all('h5')[1].get_text()
    listings["first_image_header_2"] = relative_image_path_4   

    relative_image_path_5 = soup.find_all('h5')[2].get_text()
    listings["first_image_header_3"] = relative_image_path_5   

    relative_image_path_6 = soup.find_all('h5')[3].get_text()
    listings["first_image_header_4"] = relative_image_path_6

    relative_image_path_7 = soup.find_all('h5')[4].get_text()
    listings["first_image_header_5"] = relative_image_path_7     

    # Close the browser after scraping
    browser.quit()

    return listings