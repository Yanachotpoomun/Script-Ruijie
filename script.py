from enter_cookie import enter_cookie
from main_menu import main_menu

if __name__ == "__main__":
    cookie_name, cookie_value, url = enter_cookie()
    main_menu(cookie_name, cookie_value, url)
