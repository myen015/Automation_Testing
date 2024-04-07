import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from LoginPage.loginPage import LoginPage
from LoginPage.forgotPassword import ForgotPassword
from searchFunction import SearchFunction
from LoginPage.LogOut import LogOut
from AdminPage.adminPage import AdminPage
from SortingFunctionality.newPost import NewPost
from EditProfilePage.editProfile import EditProfile
from SortingFunctionality.mostLiked import MostLiked
from SortingFunctionality.addComment import AddComment
from SortingFunctionality.putLike import PutLike


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_verify_login_page(driver):
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz"
    assert expected_url == driver.current_url


def test_create_new_post(driver):
    new_post = NewPost(driver)
    initial_post_count = new_post.get_post_count()
    time.sleep(5)
    print("Initial post count:", initial_post_count)
    time.sleep(5)
    post_text = "This is a new post!!!"
    new_post.create_post(post_text)
    time.sleep(5)

    updated_post_count = new_post.get_post_count()
    print("Updated post count:", updated_post_count)
    time.sleep(5)

    assert updated_post_count == initial_post_count + 1, "New post was not created successfully"


def test_put_like(driver):
    like = PutLike(driver)
    before_text_count = like.likes_count_text()
    updated_text_count = like.find_like_icon()
    if before_text_count != updated_text_count:
        print("Like was putted successfully")
    else:
        print("Like was not putted successfully")


def test_most_liked_sorting(driver):
    most_liked = MostLiked(driver)
    most_liked.navigate_to_buzz_page()
    most_liked.sorting_functionality()
    post_likes = most_liked.compare_likes_count()
    print("Posts are sorted correctly by likes count:", post_likes)


def test_add_comment_sorting(driver):
    add_comment = AddComment(driver)
    add_comment.click_most_recent_post()

    add_comment.addComment("Automation Testing")
    comments = driver.find_elements(By.CLASS_NAME, 'oxd-comment-text')
    for comment in comments:
        if comment.text == add_comment:
            assert True
            print("Comment added successfully:", add_comment)
            return


def test_admin_page_functionality(driver):
    admin_page = AdminPage(driver)
    admin_page.navigate_To_AdminPage()
    count_before_deletion = admin_page.get_record_count()
    admin_page.click_delete_record()
    time.sleep(5)

    count_after_deletion = admin_page.get_record_count()

    assert count_after_deletion < count_before_deletion, "Record was not deleted"


def test_profile_edit(driver):
    edit_profile = EditProfile(driver)
    edit_profile.navigate_to_profile_page()
    initial_username = edit_profile.current_username()
    new_username = "Yernar"
    edit_profile.edit_name(new_username)
    edit_profile.save_edited_name()

    if initial_username != new_username:
        print("Username changed successfully!")
        time.sleep(5)
    else:
        print("Failed to change username.")


def test_verify_search_function(driver):
    search_function = SearchFunction(driver)
    search_function.search_functionality("d")


def test_logOutPage(driver):
    log_out_page = LogOut(driver)
    log_out_page.logout()
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    assert expected_url == driver.current_url


def test_forgot_password(driver):
    forgot_password_page = LoginPage(driver)
    forgot_password_page.login("Admin", "admin")
    forgot_password_page = ForgotPassword(driver)
    forgot_password_page.forgot_pass()
    forgot_password_page.reset_password()

    success_message = driver.find_element(By.XPATH,
                                          '/html/body/div/div[1]/div[1]/div/h6')
    assert "Reset Password link sent successfully" in success_message.text



