from selenium.webdriver.common.by import By
import Post_Functions as pf
import os


class Post:
    def __init__(self, card):
        self.status = ""
        self.date = ""
        self.id = ""
        self.image_path = ""
        self.sponsored = ""
        self.description = ""
        self.platforms = []
        self.filename = self.id + ".jpg"
        self.videoname = self.id + ".mp4"
        self.path = "/Images"
        self.card = card
        self.top_card_info = card.find_elements(By.CSS_SELECTOR, "div.x3nfvp2.x1e56ztr")
        self.img_element = card.find_elements(By.TAG_NAME, "img")
        self.vid_element = card.find_elements(By.TAG_NAME, "video")

    def getTopCardInfo(self):
        for index, value in enumerate(self.top_card_info):
            if index == 0:
                self.status = pf.getPostStatus(value)
            if index == 1:
                self.date = pf.getPostDate(value)
            if index == 2:
                self.platforms = pf.getPlatforms(value)
            if index == 3 or index == 4:
                self.id = pf.getPostId(value)

    def getPostImageVideo(self):
        if len(self.img_element) > len(self.vid_element):
            img_url = self.img_element[1].get_attribute("src")
            self.image_path = os.path.abspath(self.filename)
            pf.download_image(img_url, self.path, self.filename)
        if len(self.img_element) == len(self.vid_element):
            vid_url = self.vid_element[0].get_attribute("src")
            self.image_path = os.path.abspath(self.filename)
            pf.download_image(vid_url, self.path, self.videoname)

    def getSponsored(self):
        self.sponsored = self.card.find_elements(By.CSS_SELECTOR, "div._4ik4._4ik5")[0].text

    def getDescription(self):
        self.description = self.card.find_element(By.CSS_SELECTOR,"div.xh8yej3 > div > div > div.x6ikm8r.x10wlt62 > div > span > div > div > div",).text

    def print(self):
        print("Status:" + self.status + ", Date: " + self.date + ", ID: " + self.id + ", Platforms: " + str(self.platforms) + ", Desrciption:" + self.description + " , Image Path: " + self.image_path)
