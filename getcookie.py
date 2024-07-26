get_cookie_name = "G1RP7AW002233"
get_cookie_value = "32a9940b107e4ce1a5432872cffa5a30"
get_url = "http://10.53.9.71"



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.service import Service
# import time

# # Function to open the browser
# def open_browser(headless=True):
#     options = webdriver.FirefoxOptions()
#     if headless:
#         options.add_argument('--headless')  # Use headless mode to not open browser window

#     # Specify the path to geckodriver
#     service = Service('C:/Program Files/geckodriver.exe')  # Adjust geckodriver path as installed

#     # Create instance of Firefox WebDriver
#     driver = webdriver.Firefox(service=service, options=options)
#     return driver

# # Function to login and retrieve cookies
# def login_and_get_cookies(driver, choice):
#     try:
#         # Determine URL based on choice
#         if choice == 1:
#             url = 'http://10.53.9.111'
#         elif choice == 2:
#             url = 'http://10.53.9.71'
#         else:
#             raise ValueError("Invalid choice. Must be 1 or 2.")

#         # Open the web page
#         driver.get(url)

#         # Find and enter the password
#         password_input = driver.find_element(By.ID, 'password')  # Adjust to actual password input element on the webpage
#         password_input.send_keys('cs-901_ruijie_@floor9')
#         password_input.send_keys(Keys.RETURN)

#         # Wait for login to complete (replace with explicit wait as needed)
#         time.sleep(5)

#         # Retrieve all cookies
#         cookies = driver.get_cookies()

#         # Convert cookies into a format usable with requests
#         cookie_dict = {cookie['name']: cookie['value'] for cookie in cookies}

#     finally:
#         driver.quit()
#         time.sleep(1)

#     return cookie_dict

# # Function to get cookie name based on switch choice
# def get_cookie_name(choice):
#     if choice == 1:
#         return 'G1RP7AW001511'
#     elif choice == 2:
#         return 'G1RP7AW002233'
#     else:
#         raise ValueError("Invalid choice. Must be 1 or 2.")

# # Function to get cookie value based on switch choice
# def get_cookie_value(choice):
#     driver = open_browser(headless=False)
#     cookies = login_and_get_cookies(driver, choice)
#     cookie_name = get_cookie_name(choice)
#     return cookies.get(cookie_name, '')

# # Function to get URL based on switch choice
# def get_url(choice):
#     if choice == 1:
#         return 'http://10.53.9.111'
#     elif choice == 2:
#         return 'http://10.53.9.71'
#     else:
#         raise ValueError("Invalid choice. Must be 1 or 2.")

# # Main script (for standalone testing)
# if __name__ == '__main__':
#     choice = int(input("1.G1RP7AW001511\n2.G1RP7AW002233\nEnter choice (1 or 2): "))
#     cookie_name = get_cookie_name(choice)
#     cookie_value = get_cookie_value(choice)
#     url = get_url(choice)
#     print(f"Cookie Name: {cookie_name}")
#     print(f"Cookie Value: {cookie_value}")
#     print(f"URL: {url}")


