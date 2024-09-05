# import allure
# from allure_commons.types import AttachmentType
#
# from demowebshop.POM.homepage import HomePage
#
# def test_check_for_login(driver):
#     home_page_obj=HomePage(driver)
#     home_page_obj.click_on_login()
#     condition=False
#     if condition==False:
#         allure.attach(driver.get_screenshot_as_png(), name="test_check_for_login.png",
#                       attachment_type=AttachmentType.PNG)
#     assert condition
#
#
# def test_check_for_register(driver):
#     home_page_obj = HomePage(driver)
#     home_page_obj.click_on_register()
#     condition = True
#     if condition == False:
#         allure.attach(driver.get_screenshot_as_png(), name="test_check_for_login.png",
#                       attachment_type=AttachmentType.PNG)
#     assert condition
#
#
#
