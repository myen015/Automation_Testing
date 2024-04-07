import time
from selenium.webdriver.common.by import By


class MostLiked:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_buzz_page(self):
        time.sleep(3)
        menu_items = self.driver.find_elements(By.CSS_SELECTOR, 'ul.oxd-main-menu li')
        if len(menu_items) >= 13:
            buzz_item = menu_items[13]
            buzz_item.click()
            time.sleep(3)

    def sorting_functionality(self):
        most_liked_button = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div['
                                                               '1]/div/div[2]/button[2]')
        most_liked_button.click()
        time.sleep(5)

    def get_all_posts(self):
        posts = self.driver.find_elements(By.CLASS_NAME, 'oxd-grid-item')
        return posts

    def get_likes_for_posts(self):
        likes = self.driver.find_elements(By.CLASS_NAME, 'orangehrm-buzz-stats-row')
        return likes

    def compare_likes_count(self):
        posts = self.get_all_posts()
        likes = self.get_likes_for_posts()

        post_likes = {}
        for post, like in zip(posts, likes):
            post_id = post.get_attribute("data-post-id")
            likes_text = like.text.strip()
            if likes_text.lower() == '0 likes':
                likes_count = 0
            else:
                likes_count = int(likes_text.split()[0])

            post_likes[post_id] = likes_count

        sorted_likes = sorted(post_likes.values(), reverse=True)
        assert list(post_likes.values()) == sorted_likes, "Posts are not sorted correctly by likes count"

