#!/usr/bin/env python

from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

id = sys.argv[1]


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
    data={}
# date diffusion , id , status et #platform

    content1=card.find_elements(By.CSS_SELECTOR,"div.x3nfvp2.x1e56ztr")
    for index, value in enumerate(content1):       
        if (index ==0):
            ajout=value.find_element(By.CSS_SELECTOR,"span.x8t9es0.xw23nyj.xo1l8bm.x63nzvj.x108nfp6.xq9mrsl.x1h4wwuj.xeuugli")
            data['Status'] = ajout.text
                
        if (index == 1):
            ajout=value.find_element(By.CSS_SELECTOR,"span.x8t9es0.xw23nyj.xo1l8bm.x63nzvj.x108nfp6.xq9mrsl.x1h4wwuj.xeuugli")
            data['Date De Diffusion'] = ajout.text
        if( index == 3):
            ajout=value.find_element(By.CSS_SELECTOR,"span.x8t9es0.xw23nyj.xo1l8bm.x63nzvj.x108nfp6.xq9mrsl.x1h4wwuj.xeuugli")
            data['ID']=ajout.text
#image et video publier
    img_element = card.find_elements(By.TAG_NAME, 'img')
    vid_element = card.find_elements(By.TAG_NAME,'video')
    
    if(len(img_element)>len(vid_element)):
        data['Nom_page']=img_element[0].get_attribute('alt')
        data['Image_Publier']=img_element[0].get_attribute('src')
    if(len(img_element)==len(vid_element)):
        data['Nom_Page']=vid_element[0].get_attribute('alt')   
        data['Video_Publier']=vid_element[0].get_attribute('src')
#type
    sponsored=card.find_elements(By.CSS_SELECTOR,"div._4ik4._4ik5")
    data['type']=sponsored[0].text
#description
    description=card.find_elements(By.CSS_SELECTOR,("div._7jyr._a25- > span.x8t9es0.xw23nyj.xo1l8bm.x63nzvj.x108nfp6.xq9mrsl.x1h4wwuj.xeuugli > div > div > div"))
    if(len(description)>0):
        data['Description']=description[0].text

    return(data)

def getData(url):
    data=[]
    cards=loadCards(url)
    
    for card in cards:
          data.append(getCardInfo(card))
          

    return data  
                
data = getData(id)
print(data)

