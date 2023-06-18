from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class WebDriver:
    def __init__(self, url):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("useAutomationExtension", False)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(url)

    def maximise_window(self):
        self.driver.maximize_window()

    def scrolling(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(10)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def getCards(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "div.xrvj5dj.xdq2opy.xexx8yu.xbxaen2.x18d9i69.xbbxn1n.xdoe023.xbumo9q.x143o31f.x7sq92a.x1crum5w > div.xh8yej3")

    def getPostsLength(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, "div.xrvj5dj.xdq2opy.xexx8yu.xbxaen2.x18d9i69.xbbxn1n.xdoe023.xbumo9q.x143o31f.x7sq92a.x1crum5w > div.xh8yej3"))