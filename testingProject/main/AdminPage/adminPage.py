import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class AdminPage(object):
    def __init__(self, driver):
        self.driver = driver

    def navigate_To_AdminPage(self):
        menu_items = self.driver.find_elements(By.CSS_SELECTOR, 'ul.oxd-main-menu li')
        if len(menu_items) >= 3:
            admin_item = menu_items[0]
            admin_item.click()
            time.sleep(5)
        else:
            print("Not enough menu items to navigate to the profile page")

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 200);")

    def click_delete_record(self):
        self.scroll_down()
        time.sleep(3)
        delete_button = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div['
                                                           '3]/div/div[2]/div[2]/div/div[6]/div/button[1]/i')
        delete_button.click()
        time.sleep(3)
        submit_delete = self.driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div/div/div[3]/button[2]')
        submit_delete.click()
        time.sleep(5)

    def get_record_count(self):
        records = self.driver.find_elements(By.CSS_SELECTOR, '.oxd-table-card')  # Adjust the XPath accordingly
        return len(records)

