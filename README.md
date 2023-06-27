# AdsScraping
Sponsored Ads Scraper with Python and Selenium

This project is a powerful and flexible tool designed to scrape sponsored ads from various websites using Python and the Selenium package. It provides an efficient way to gather information about sponsored ads for analytical purposes, competitive analysis, or any other use case that requires retrieving data from sponsored advertisements.

Key Features:

- Selenium Integration: The project leverages the Selenium package, a popular web automation tool, to interact with web browsers programmatically. Selenium allows the scraper to navigate through websites, perform actions, and extract sponsored ads data with ease.

- Scraping Sponsored Ads: With this tool, you can effortlessly scrape sponsored ads from multiple websites. It automates the process of navigating to ad listings, capturing relevant information such as ad titles, descriptions, images, URLs, and any other data associated with the sponsored ads.

- Web Server: We host this script into a FLASK Web Server in order to make your POST request with an id associated to a Facebook Company Ad and getting an array of company's ads.

## Steps to Deploy

1. Install Chrome

Open a terminal on your favorite linux distro and copy the following commands:

`cd /tmp`

`sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb`

`sudo dpkg -i google-chrome-stable_current_amd64.deb`

`sudo apt install --fix-broken -y`

`google-chrome`

2. Clone Repo and Install Packages

`git clone (https://github.com/Walids35/AdsScraping)`

`pip install -r requirements.txt`

3. Run Web Server

`./webserver`

4. Make a POST request with your favorite API Platform

`http://localhost:3000/scrape`
