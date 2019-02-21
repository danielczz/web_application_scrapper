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
    # Visit image for listings["image"]
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
    url_tweet_mars = "https://twitter.com/MarsWxReport?lang=en"
    browser.visit(url_tweet_mars)

    # Scrape page into Soup
    html_tweet_scrape = browser.html
    soup = BeautifulSoup(html_tweet_scrape, "html.parser")

    # listings["tweet"] = soup.find(class_="content").get_text()    
    latest_tweet_result = soup.find(class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text()    
    result_soup = latest_tweet_result.split("https")
    listings["latest_tweet"] = result_soup[0]

###
    # Mars Facts
###

# Mars Hemispheres 
    time.sleep(1)

    x = 0
    y = 0

    # Loop to get different names 
    for x in range(4):
        # Visit image for listings["images_hemispheres"]
        url_mars_hemispheres = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(url_mars_hemispheres)

        # Scrape page into Soup
        html_mars_hemispheres = browser.html
        soup = BeautifulSoup(html_mars_hemispheres, "html.parser")
        
        image_path_title = soup.find_all('h3')[x].get_text()
        listings["img_title_" + str(x) ] = image_path_title

        image_path_url = soup.find_all('a', attrs={'class':'itemLink product-item'})[y]["href"]
        url_first_string = "https://astrogeology.usgs.gov"
        image_url = url_first_string + image_path_url
        listings["image_url_" + str(x) ] = image_url
        y += 2

        time.sleep(1)

        # Visit image for listings["image_file_link_"]
        browser.visit(image_url)

        # Scrape page into Soup
        html_scraper_hemispheres = browser.html
        soup = BeautifulSoup(html_scraper_hemispheres, "html.parser")
        image_final_query = soup.find(class_='downloads')
        listings["image_file_link_" + str(x) ] = image_final_query.a['href']

        time.sleep(1)

    # Close the browser after scraping
    browser.quit()

    return listings