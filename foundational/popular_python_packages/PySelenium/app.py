"""
before running this you need to make sure that the chrome selenium driver is installed
do this by going to the selenium package in pypi and downloading the latest driver
you will need to put it in the PATH
"""
from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()
options.add_argument("--start-maximized")
browser = Chrome(options=options)
browser.get("https://github.com")
signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()
username_box = browser.find_element_by_id("login_field")
username_box.send_keys(USER)
password_box = browser.find_element_by_id("password")
password_box.send_keys(PASSWORD)
password_box.submit()
user_profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = user_profile_link.get_attribute("innerHTML")
assert USER.lower() in link_label.lower()
browser.close()