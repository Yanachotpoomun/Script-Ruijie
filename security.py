from clear_screen import clear_screen
from send_request import send_request


def security(cookie_name, cookie_value, url):
    clear_screen()
    print("(1) DHCP Snooping")
    print("(2) IP-MAC Binding")
    print("(3) ACL")
    print("(4) Port Protection")
    print("(5) IP Source Guard")
    print("(6) Anti-ARP Spoofing")
    print("(7) Storm Control")

    choice = input("Select function: ")

    clear_screen()
    if choice == "1":
        print("DHCP Snooping")
        print("save")
    elif choice == "2":
        print("IP-MAC Binding")
        print("(1) add")
        print("(2) delete")
        print("(3) search")
        ip_mac_binding_sub_choice = input("Select function: ")
        if ip_mac_binding_sub_choice == "1":
            print("(1) add")
            sip = input("Enter IP: ")
            smac = input("Enter MAC: ")
            ports_input = input("Enter port IDs (comma-separated): ")
            port_ids = [int(port.strip()) - 1 for port in ports_input.split(",")]

            url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"
            payload = {
                "method": "devConfig.add",
                "params": {
                    "module": "ipmac_bind",
                    "noParse": True,
                    "async": None,
                    "remoteIp": False,
                    "data": {
                        "sip": sip,
                        "smac": smac,
                        "portid": port_ids,
                        "name_uuid": "",
                    },
                    "device": "pc",
                },
            }
            response = send_request(url, payload, cookie_name, cookie_value)
            print(response.text)
            print(port_ids)
            input("Press Enter to continue...")

        elif ip_mac_binding_sub_choice == "2":
            print("(1) delete")
        elif ip_mac_binding_sub_choice == "3":
            print("(1) search")
    elif choice == "3":
        print("ACL")
        print("(1) ACL list")
        print("(2) ACL Binding")
    elif choice == "4":
        print("Port Protection")
        print("edit")
    elif choice == "5":
        print("IP Source Guard")
        print("(1) basic setting")
        print("(2) Excluded VLAN")
        print("(3) Binding List")
    elif choice == "6":
        print("Anti-ARP Spoofing")
        print("(1) add")
        print("(2) delete")
    elif choice == "7":
        print("Storm Control")
        print("(1) edit")
        print("(2) delete")
    else:
        print("Invalid function selected")
