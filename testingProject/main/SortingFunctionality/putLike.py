import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class PutLike:
    def __init__(self, driver):
        self.driver = driver

    def find_like_icon(self):
        like_icon = self.driver.find_element(By.CLASS_NAME, 'orangehrm-heart-icon')
        like_icon.click()
        time.sleep(3)
        return self.likes_count_text()

    def likes_count_text(self):
        likes_count = self.driver.find_element(By.XPATH,
                                               '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div['
                                               '1]/div/div[3]/div[2]/div[1]/p')
        likes_count_text = likes_count.text
        return likes_count_text
