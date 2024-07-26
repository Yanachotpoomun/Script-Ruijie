from clear_screen import clear_screen


def advanced(cookie_name, cookie_value, url):
    clear_screen()
    print("(1) STP")
    print("(2) LLDP")
    print("(3) RLDP")
    print("(4) LOCAL DNS")

    choice = input("Select function: ")

    clear_screen()
    if choice == "1":
        print("STP")
        print("save")
    elif choice == "2":
        print("LLDP")
        print("(1) LLDP Settings")
        print("(2) LLDP Management")
    elif choice == "3":
        print("RLDP")
        print("save")
    elif choice == "4":
        print("LOCAL DNS")
        print("save")
    else:
        print("Invalid function selected")
