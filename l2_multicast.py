from clear_screen import clear_screen

def l2_multicast(cookie_name, cookie_value, url):
    clear_screen()
    print("(1) Global Settings")
    print("(2) MVR")
    print("(3) IGMP Snooping")
    print("(4) Multicast Group")
    print("(5) IGMP Filter")
    print("(6) Querier")

    choice = input("Select function: ")

    clear_screen()
    if choice == "1":
        print("Global Settings")
        print("save")
    elif choice == "2":
        print("MVR")
        print("(1) save")
        print("(2) edit")
    elif choice == "3":
        print("IGMP Snooping")
        print("(1) save")
        print("(2) edit")
    elif choice == "4":
        print("Multicast Group")
        print("(1) add")
        print("(2) delete")
    elif choice == "5":
        print("IGMP Filter")
        print("(1) add")
        print("(2) delete")
        print("(3) edit")
    elif choice == "6":
        print("Querier")
        print("edit")
    else:
        print("Invalid function selected")
