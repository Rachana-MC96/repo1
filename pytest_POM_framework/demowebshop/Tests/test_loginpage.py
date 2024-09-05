import allure
import pytest
from allure_commons.types import AttachmentType

# import openpyxl
from demowebshop.POM.homepage import HomePage
from demowebshop.POM.loginpage import LogIn
from utilities.excel_reader import get_list_from_excel
values=get_list_from_excel("creds.xlsx","login_creds")
# usernames=["reddyvinuth27@gmail.com","abc@gmail.com","xyz@gmail.com","mno@gmail.com"]
# usernames=[("reddyvinuth27@gmail.com","selenium"),("abc@gmail.com","1234"),("xyz@gmail.com","1123"),("mno@gmail.com","1234567")]

#
# credentials= openpyxl.load_workbook("creds.xlsx")
# login_creds=credentials["login_creds"]
# # login_creds.cell(1,2)
# credentials_list=[]
# for row in range(1,8):
#     nested_creds=[]
#     for column in range(1,3):
#         data=login_creds.cell(row,column)
#         nested_creds.append(data.value)
#     credentials_list.append(nested_creds)

@pytest.mark.parametrize("username,password",values)
def test_login_with_proper_credentials(driver,username,password):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application(username, password)

    condition = driver.find_element("xpath", f"//a[.='{username}']").is_displayed()
    if not condition:
        allure.attach(driver.get_screenshot_as_png(), name="test_login_with_proper_credentials.png",
                      attachment_type=AttachmentType.PNG)
    assert condition


@pytest.mark.skip
def test_login_with_no_password(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("reddyvinuth27@gmail.com", "")
    assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()

@pytest.mark.skip
def test_login_with_no_username(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("", "selenium")
    assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()

@pytest.mark.skip
def test_login_with_no_credential(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("", "")
    assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()

@pytest.mark.skip
def test_login_with_invalid_credential(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_the_application("abc@gmail.com", "wastejava")
    assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()

