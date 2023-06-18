#!/usr/bin/env python

from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import requests
import shutil

id = sys.argv[1]
path = "/Images" + id

def loadCards(id):
    url = (
        "https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id="
        + id
        + "&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=page&media_type=all"
    )

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=options)
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )
    driver.get(url)
    driver.maximize_window()
    WebDriverWait(driver, 6).until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "#content > div > div > div > div.x8bgqxi.x1n2onr6 > div._8n_0 > div.x6s0dn4.x78zum5.xdt5ytf.xl56j7k.x1n2onr6.x1ja2u2z.x19gl646.xbumo9q > div.x1dr75xp.xh8yej3.x16md763 > div.xrvj5dj.xdq2opy.xexx8yu.xbxaen2.x18d9i69.xbbxn1n.xdoe023.xbumo9q.x143o31f.x7sq92a.x1crum5w > div:nth-child(1)",
            )
        )
    )
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(10)
        new_height = driver.execute_script("return document.body.scrollHeight")
        block_cards = driver.find_elements(
            By.CSS_SELECTOR,
            "div.xrvj5dj.xdq2opy.xexx8yu.xbxaen2.x18d9i69.xbbxn1n.xdoe023.xbumo9q.x143o31f.x7sq92a.x1crum5w > div.xh8yej3",
        )
        if new_height == last_height:
            break

        last_height = new_height

    return block_cards

    
def getCardInfo(card):
    data = {}
    # date diffusion , id , status et #platform

    content1 = card.find_elements(By.CSS_SELECTOR, "div.x3nfvp2.x1e56ztr")
    for index, value in enumerate(content1):
        if index == 0:
            ajout = value.find_element(
                By.CSS_SELECTOR,
                "span.x8t9es0.xw23nyj.xo1l8bm.x63nzvj.x108nfp6.xq9mrsl.x1h4wwuj.xeuugli",
            )
            data["Status"] = ajout.text

        if index == 1:
            ajout = value.find_element(
                By.CSS_SELECTOR,
                "span.x8t9es0.xw23nyj.xo1l8bm.x63nzvj.x108nfp6.xq9mrsl.x1h4wwuj.xeuugli",
            )
            data["Date De Diffusion"] = ajout.text
        if index == 2:
            platformes = value.find_elements(By.CSS_SELECTOR, "div.xtwfq29")
            platformes_ = []
            for elem in platformes:
                if "y1FuvrbyrJG.png" in elem.get_attribute("style"):
                    platformes_.append("Instagram")
                if ("w7LzRvH0HL-.png") and "0px -539px" in elem.get_attribute("style"):
                    platformes_.append("Facebook")
                if ("BIcOqnqNbE9.png") and ("-106px -186px") in elem.get_attribute(
                    "style"
                ):
                    platformes_.append("AudienceNetwork")
                if ("BIcOqnqNbE9.png") and ("-68px -289px") in elem.get_attribute(
                    "style"
                ):
                    platformes_.append("Messenger")
            data["Platformes"] = platformes_

        if index == 3:
            ajout = value.find_element(
                By.CSS_SELECTOR,
                "span.x8t9es0.xw23nyj.xo1l8bm.x63nzvj.x108nfp6.xq9mrsl.x1h4wwuj.xeuugli",
            )
            data["ID"] = ajout.text[4:]
        if index == 4:
            ajout = value.find_element(
                By.CSS_SELECTOR,
                "span.x8t9es0.xw23nyj.xo1l8bm.x63nzvj.x108nfp6.xq9mrsl.x1h4wwuj.xeuugli",
            )
            data["ID"] = ajout.text[4:]

    # image et video publier
    filename = data["ID"] + ".jpg"
    vidname = data["ID"] + ".mp4"
    img_element = card.find_elements(By.TAG_NAME, "img")
    vid_element = card.find_elements(By.TAG_NAME, "video")

    if len(img_element) > len(vid_element):
        data["Nom_page"] = img_element[0].get_attribute("alt")
        img_url = img_element[1].get_attribute("src")
        data["contenu"] = os.path.abspath(filename)
        download_image(img_url, path, filename)
    if len(img_element) == len(vid_element):
        data["Nom_Page"] = vid_element[0].get_attribute("alt")
        data["contenu"] = vid_element[0].get_attribute("src")
        vid_url = vid_element[0].get_attribute("src")
        data["contenu"] = os.path.abspath(filename)
        download_image(vid_url, path, vidname)
    # type
    sponsored = card.find_elements(By.CSS_SELECTOR, "div._4ik4._4ik5")
    data["type"] = sponsored[0].text
    # description
    description = card.find_element(
        By.CSS_SELECTOR,
        (
            "div.xh8yej3 > div > div > div.x6ikm8r.x10wlt62 > div > span > div > div > div"
        ),
    )
    data["Description"] = description.text

    return data

def download_image(url, path, filename):
    # Create the directory if it doesn't exist
    os.makedirs(path, exist_ok=True)

    # Concatenate the path and filename
    filepath = os.path.join(path, filename)

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filepath, "wb") as file:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, file)
        print("Image downloaded successfully.")
    else:
        print("Unable to download image.")
        

def getData(url):
    data=[]
    cards=loadCards(url)
    
    for card in cards:
          data.append(getCardInfo(card))
          

    return data  
                
data = getData(id)
print(data)

