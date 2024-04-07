import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class AddComment:
    def __init__(self, driver):
        self.driver = driver

    def click_most_recent_post(self):
        most_recent_post = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div['
                                                              '2]/button[1]')
        most_recent_post.click()
        time.sleep(2)

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(2)

    def addComment(self, comment):
        self.scroll_down()
        comment_icon = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div['
                                                          '3]/div[1]/div/div[3]/div[1]/button[1]')
        comment_icon.click()
        time.sleep(2)

        write_comment = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Write your comment..."]')
        write_comment.send_keys(comment)
        time.sleep(3)
        write_comment.send_keys(Keys.ENTER)
        time.sleep(5)
