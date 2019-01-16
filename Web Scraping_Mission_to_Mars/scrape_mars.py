{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import BeautifulSoup for parsing and splinter for site navigation\n",
    "from splinter import Browser\n",
    "executable_path = {\"executable_path\": \"chromedriver.exe\"}\n",
    "browser = Browser(\"chrome\", **executable_path, headless=False)\n",
    "import pandas as pd\n",
    "import time\n",
    "import requests\n",
    "from splinter import Browser\n",
    "from selenium import webdriver\n",
    "import pandas as pd\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import pymongo\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initialize PyMongo\n",
    "conn = 'mongodb://localhost:27017'\n",
    "client = pymongo.MongoClient(conn)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the NASA news URL\n",
    "url = \"https://mars.nasa.gov/news/\"\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scrape page into soup\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# use beautiful soup to find the title\n",
    "\n",
    "soup.find(\"div\", class_=\"content_title\").text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# use beautiful soup to find the paragraph\n",
    "paragraph=soup.find(\"div\", class_=\"article_teaser_body\").text\n",
    "print(paragraph)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the JPL Mars URL\n",
    "\n",
    "url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#use the browser to click Full Image\n",
    "\n",
    "browser.click_link_by_partial_text(\"FULL IMAGE\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# use the browser to click more info\n",
    "browser.click_link_by_partial_text(\"more info\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#scrape page into soup\n",
    "html=browser.html\n",
    "soup=BeautifulSoup(html,\"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scrape the browser into soup and use soup to find the image of mars and save the image url to a variable called `img_url`\n",
    "\n",
    "img_url=\"https://www.jpl.nasa.gov\" + soup.find(\"img\", class_=\"main_image\")[\"src\"]\n",
    "\n",
    "featured_image_url = img_url\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the Mars Weather twitter account and scrap the lates Mars weather tweet.\n",
    "\n",
    "url = 'https://twitter.com/marswxreport?lang=en'\n",
    "browser.visit(url)\n",
    "soup = BeautifulSoup(browser.html, 'html.parser')\n",
    "mars_weather = soup.find('div', class_='js-tweet-text-container').text.split('\\n')[1]\n",
    "mars_results=results['mars_weather']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Visit the Mars Facts webpage here and use Pandas to scrape the table \n",
    "\n",
    "url = 'http://space-facts.com/mars/'\n",
    "facts_table = pd.read_html(url)\n",
    "mars_df = facts_table[0]\n",
    "mars_df.columns = ['Parameter','Value']\n",
    "facts_table = mars_df.to_html()\n",
    "Mars_facts_table=results['Mars_facts_table'] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#dictionary to be inserted as a MongoDB document\n",
    "post = {\n",
    "    'headline': headline, \n",
    "    'news': news, \n",
    "    'featured': featured_img_url,\n",
    "    'weather': mars_weather,\n",
    "    'facts': table_data\n",
    "}\n",
    "collection.insert_one(post)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import BeautifulSoup for parsing and splinter for site navigation\n",
    "from bs4 import BeautifulSoup\n",
    "from splinter import Browser\n",
    "executable_path = {\"executable_path\": \"chromedriver.exe\"}\n",
    "browser = Browser(\"chrome\", **executable_path, headless=False)\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Mars Hemispheres- visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres\n",
    "\n",
    "url = 'https://astrogeology.usgs.gov'\n",
    "imageurl = '/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url+imageurl)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use splinter to loop through the images and load them into a dictionary\n",
    "import time \n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "mars_hemis=[]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.\n",
    "#Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.\n",
    "for image in range (4):\n",
    "    time.sleep(5)\n",
    "    images = browser.find_by_tag('h3')\n",
    "    images[image].click()\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, 'html.parser')\n",
    "    partial = soup.find(\"img\", class_=\"wide-image\")[\"src\"]\n",
    "    img_title = soup.find(\"h2\",class_=\"title\").text\n",
    "    img_url = 'https://astrogeology.usgs.gov'+ partial\n",
    "    dictionary={\"title\":img_title,\"img_url\":img_url}\n",
    "    mars_hemis.append(dictionary)\n",
    "    browser.back()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(mars_hemis)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
