from WebDriver import WebDriver
from Post import Post
import sys

id = sys.argv[1]
url = ("https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id="+ id+ "&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=page&media_type=all")


def run_script():
    webdriver = WebDriver(url)
    webdriver.maximise_window()
    webdriver.scrolling()
    cards = webdriver.getCards()
    for card in cards:
        post = Post(card)
        post.getTopCardInfo()
        post.getPostImageVideo()
        post.getSponsored()
        post.getDescription()
        post.print()


run_script()

