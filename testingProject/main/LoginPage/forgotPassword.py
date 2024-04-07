import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class ForgotPassword:
    def __init__(self, driver):
        self.driver = driver

    def forgot_pass(self):

        invalid_credentials = self.driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div['
                                                              '2]/div/div[1]/div[1]')
        if invalid_credentials:
            forgot_password = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div['
                                                                 '2]/form/div[4]/p')
            forgot_password.click()
            time.sleep(5)
            return True
        else:
            return False

    def reset_password(self):
        reset_username = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Username"]')
        reset_username.send_keys('Admin')
        reset_username.send_keys(Keys.ENTER)
        time.sleep(3)



