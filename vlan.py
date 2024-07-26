from clear_screen import clear_screen
from send_request import send_request


def vlan(cookie_name, cookie_value, url):
    clear_screen()
    print("(1) Add")
    print("(2) Remove")
    print("(3) Update")
    print("(4) Access VLAN")

    choice = input("Select function: ")

    clear_screen()
    if choice == "1":
        print("Add VLAN")

        v = input("VLAN ID: \n")
        n = input("Description: \n")

        url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"

        payload = {
            "method": "devConfig.add",
            "params": {
                "module": "vlan",
                "noParse": True,
                "async": None,
                "remoteIp": False,
                "data": {"v": v, "n": n},
                "device": "pc",
            },
        }
        response = send_request(url, payload, cookie_name, cookie_value)

        print(response.text)
        input("Press Enter to continue...")

    elif choice == "2":
        print("Remove VLAN")
        v = input("VLAN ID: \n")

        url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"

        payload = {
            "method": "devConfig.del",
            "params": {
                "module": "vlan",
                "noParse": True,
                "async": None,
                "remoteIp": False,
                "data": {"v": v},
                "device": "pc",
            },
        }
        response = send_request(url, payload, cookie_name, cookie_value)

        print(response.text)
        input("Press Enter to continue...")
    elif choice == "3":
        print("Update VLAN")
        v = input("VLAN ID: \n")
        n = input("Description: \n")

        url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"

        payload = {
            "method": "devConfig.update",
            "params": {
                "module": "vlan",
                "noParse": True,
                "async": None,
                "remoteIp": False,
                "data": {"v": v, "n": n},
                "device": "pc",
            },
        }
        response = send_request(url, payload, cookie_name, cookie_value)

        print(response.text)
        input("Press Enter to continue...")
    elif choice == "4":
        print("Access VLAN")

        lpid = int(input("Port index (1-24):\n")) - 1
        mode = int(input("Port Mode:\n(1) Access Port\n(2) Trunk Port\n"))
        pvid = input("Insert VLAN id :\n")
        if mode == 2:
            permitvlan = input("Permitted VLAN (1-4094) :\n")
        else:
            permitvlan = ""
        url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"

        payload = {
            "method": "devConfig.update",
            "params": {
                "module": "port_vlan",
                "noParse": True,
                "async": None,
                "remoteIp": False,
                "data": {
                    "list": [
                        {
                            "mode": mode,
                            "lpid": lpid,
                            "pvid": pvid,
                            "permitvlan": permitvlan,
                        }
                    ]
                },
                "device": "pc",
            },
        }
        response = send_request(url, payload, cookie_name, cookie_value)

        print(response.text)
        input("Press Enter to continue...")

    else:
        print("Invalid function selected")
