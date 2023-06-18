import os
import requests
import shutil
from selenium.webdriver.common.by import By


def getPostStatus(value):
    return value.find_element(By.CSS_SELECTOR,
                              "span.x8t9es0.xw23nyj.xo1l8bm.x63nzvj.x108nfp6.xq9mrsl.x1h4wwuj.xeuugli", ).text


def getPostDate(value):
    return value.find_element(By.CSS_SELECTOR,
                              "span.x8t9es0.xw23nyj.xo1l8bm.x63nzvj.x108nfp6.xq9mrsl.x1h4wwuj.xeuugli", ).text


def getPlatforms(value):
    platforms = value.find_elements(By.CSS_SELECTOR, "div.xtwfq29")
    platforms_ = []
    for elem in platforms:
        if "y1FuvrbyrJG.png" in elem.get_attribute("style"):
            platforms_.append("Instagram")
        if ("w7LzRvH0HL-.png") and "0px -539px" in elem.get_attribute("style"):
            platforms_.append("Facebook")
        if ("BIcOqnqNbE9.png") and ("-106px -186px") in elem.get_attribute(
                "style"
        ):
            platforms_.append("AudienceNetwork")
        if ("BIcOqnqNbE9.png") and ("-68px -289px") in elem.get_attribute(
                "style"
        ):
            platforms_.append("Messenger")
    return platforms_


def getPostId(value):
    return value.find_element(By.CSS_SELECTOR,
                              "span.x8t9es0.xw23nyj.xo1l8bm.x63nzvj.x108nfp6.xq9mrsl.x1h4wwuj.xeuugli", ).text[4:]


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
    else:
        print("Unable to download image.")

