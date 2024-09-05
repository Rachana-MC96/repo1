# from demowebshop.POM.homepage import HomePage
# from demowebshop.POM.registerpage import Register
#
# def test_register_with_all_valid_input(driver):
#     home=HomePage(driver)
#     home.click_on_register()
#     register=Register(driver)
#     register.register_an_account("rachana","MC","rachu123456@gmail.com","heyram","heyram")
#     assert driver.find_element("xpath","//input[@value='Continue']").is_displayed()
#
#
# def test_register_without_first_name(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account(" ", "MC", "rachu123456@gmail.com", "heyram", "heyram")
#     assert driver.find_element("xpath", "//span[@for='FirstName']").is_displayed()
#
# def test_register_without_last_name(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account("rachana", " ", "rachu123456@gmail", "heyram", "heyram")
#     assert driver.find_element("xpath", "//span[@for='LastName']").is_displayed()
#
#
# def test_register_without_email(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account("rachana", "MC", " ", "heyram", "heyram")
#     assert driver.find_element("xpath", "//span[@for='Email']").is_displayed()
#
# def test_register_with_improper_email(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account("rachana", "MC", "rachana@", "heyram", "heyram")
#     assert driver.find_element("xpath", "//span[.='Wrong email']//span").is_displayed()
#
# def test_register_without_password(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account("rachana", "MC", "rachu123456@gmail", " ", "heyram")
#     assert driver.find_element("xpath", "//span[@for='Password']").is_displayed()
#
# def test_register_without_Con_password(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account("rachana", "MC", "rachu123456@gmail.com", "heyram", " ")
#     assert driver.find_element("xpath", "//span[@for='ConfirmPassword']").is_displayed()
#
# def test_register_without_input(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account(" ", " ", " ", " ", " ")
#     assert driver.find_element("xpath", "//span[@for='ConfirmPassword']").is_displayed()
#
#
#
#
#
#
#
#
#
#
#
#
#
