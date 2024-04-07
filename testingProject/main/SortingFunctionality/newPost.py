import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class NewPost:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_buzz_page(self):
        menu_items = self.driver.find_elements(By.CSS_SELECTOR, 'ul.oxd-main-menu li')
        if len(menu_items) >= 13:
            buzz_item = menu_items[13]
            buzz_item.click()
            time.sleep(3)

    def get_post_count(self):
        try:
            posts = self.driver.find_elements(By.CLASS_NAME, 'oxd-grid-item')
            print("Found posts:", len(posts))
            return len(posts)
        except NoSuchElementException:
            print("Posts not found")
            return 0

    def create_post(self, post_text):
        self.navigate_to_buzz_page()
        new_post_button = self.driver.find_element(By.CLASS_NAME, 'oxd-buzz-post-input')
        new_post_button.click()
        time.sleep(4)

        post_textarea = self.driver.find_element(By.CLASS_NAME, 'oxd-buzz-post-input')
        post_textarea.send_keys(post_text)
        time.sleep(4)

        submit_button = self.driver.find_element(By.CLASS_NAME, 'oxd-buzz-post-slot')
        submit_button.click()
        time.sleep(3)

        initial_post_count = self.get_post_count()

        # timeout = 10  # seconds
        # start_time = time.time()
        # while time.time() - start_time < timeout:
        #     if self.get_post_count() > initial_post_count:
        #         print("Post added successfully!")
        #         return
        #     time.sleep(1)
        #
        # print("Failed to add post.")

