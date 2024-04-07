import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class EditProfile:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_profile_page(self):
        menu_items = self.driver.find_elements(By.CSS_SELECTOR, 'ul.oxd-main-menu li')
        if len(menu_items) >= 3:
            profile_item = menu_items[5]
            profile_item.click()
            time.sleep(5)
        else:
            print("Not enough menu items to navigate to the profile page")

    def current_username(self):
        username = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="First Name"]')
        curr_username = username.text
        return curr_username

    def edit_name(self, profile_name):
        name_input = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="First Name"]')
        actions = ActionChains(self.driver)
        actions.double_click(name_input).perform()
        time.sleep(5)
        # name_input.send_keys(Keys.CONTROL + 'a')
        # time.sleep(1)
        # name_input.send_keys(Keys.DELETE)
        # time.sleep(3)
        name_input.send_keys(profile_name)
        time.sleep(3)

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 200);")

    def save_edited_name(self):
        self.scroll_down()
        time.sleep(5)
        save_button = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div['
                                                         '2]/div/form/div[2]/button')
        save_button.click()
        time.sleep(5)

