from clear_screen import clear_screen
from ports import ports
from monitor import monitor
from vlan import vlan
from security import security
from system import system
from l2_multicast import l2_multicast
from advanced import advanced

def main_menu(cookie_name, cookie_value, url):
    while True:
        clear_screen()
        print("Main Menu")
        print("(1) Ports")
        print("(2) Monitor")
        print("(3) VLAN")
        print("(4) Security")
        print("(5) System")
        print("(6) L2 Multicast")
        print("(7) Advanced")
        print("(8) Exit")

        choice = input("Select function: ")

        if choice == "1":
            ports(cookie_name, cookie_value, url)
        elif choice == "2":
            monitor(cookie_name, cookie_value, url)
        elif choice == "3":
            vlan(cookie_name, cookie_value, url)
        elif choice == "4":
            security(cookie_name, cookie_value, url)
        elif choice == "5":
            system(cookie_name, cookie_value, url)
        elif choice == "6":
            l2_multicast(cookie_name, cookie_value, url)
        elif choice == "7":
            advanced(cookie_name, cookie_value, url)
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please select again.")
            input("Press Enter to continue...")
