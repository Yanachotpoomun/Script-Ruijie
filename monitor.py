import re
from clear_screen import clear_screen
from send_request import send_request


def monitor(cookie_name, cookie_value, url):
    while True:
        clear_screen()
        print("(1) portflow")
        print("(2) endpoint")
        print("(0) Exit")

        choice = input("Select function: ")
        clear_screen()

        if choice == "1":
            print("portflow")
            print("(1) Select clear batch")
            print("(2) clear batch")
            sub_choice = input("Select sub-function: ")
            clear_screen()

            if sub_choice == "1":
                print("(1) Select clear batch")
                user_input_lpid = input(
                    "Enter source port numbers 1-28 separated by commas: "
                )

                try:
                    lpid = [int(port) - 1 for port in user_input_lpid.split(",")]
                except ValueError:
                    print(
                        "Invalid input. Please enter valid integers separated by commas."
                    )
                    input("Press Enter to continue...")
                    continue

                url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"
                payload = {
                    "method": "devSta.set",
                    "params": {
                        "module": "flow_status",
                        "noParse": True,
                        "async": None,
                        "remoteIp": False,
                        "data": {"lpid": lpid},
                        "device": "pc",
                    },
                }
                response = send_request(url, payload, cookie_name, cookie_value)
                print(response.text)
                input("Press Enter to continue...")

            elif sub_choice == "2":
                print("(2) clear batch")
                url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"
                payload = {
                    "method": "devSta.set",
                    "params": {
                        "module": "flow_status",
                        "noParse": True,
                        "async": None,
                        "remoteIp": False,
                        "data": {"lpid": []},
                        "device": "pc",
                    },
                }
                response = send_request(url, payload, cookie_name, cookie_value)
                print(response.text)
                input("Press Enter to continue...")

        elif choice == "2":
            print("endpoint")
            print("(1) arp list")
            print("(2) Mac list")
            print("(3) Static mac")
            print("(4) Aging time")
            print("(5) Filter mac")
            print("(0) Back to main menu")

            sub_choice = input("Select sub-function: ")
            clear_screen()

            if sub_choice == "1":
                print("(1) arp list")
                print("(2) show list")
                sub_sub_choice = input("Select Sub choice:\n")
                if sub_sub_choice == "1":
                    print("arp list")
                elif sub_sub_choice == "2":
                    print("show list")

            elif sub_choice == "2":
                print("Mac list")
                print("show list")

            elif sub_choice == "3":
                while True:
                    print("Static mac")
                    print("(1) add")
                    print("(2) remove")
                    static_sub_choice = input("Select Sub choice:\n")
                    clear_screen()
                    if static_sub_choice == "1":
                        print("(1) add")

                        # รับค่า macaddr และตรวจสอบความถูกต้อง
                        while True:
                            macaddr = input(
                                "Enter MAC Address (e.g., 00:22:11:44:33:55): "
                            )
                            mac_regex = re.compile(
                                r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
                            )
                            if mac_regex.match(macaddr):
                                break
                            print("Invalid MAC address format. Please enter again.")

                        # รับค่า vlanid และตรวจสอบความถูกต้อง
                        while True:
                            try:
                                vlanid = int(input("Enter VLAN ID: "))
                                if vlanid < 0 or vlanid > 4095:
                                    print(
                                        "VLAN ID must be between 0 and 4095. Please enter again."
                                    )
                                    continue
                                if (vlanid - 1) == 23:
                                    print("VLAN ID - 1 is 23. Please enter again.")
                                    continue
                                # แปลง vlanid เป็น string ก่อนส่ง
                                vlanid_str = str(vlanid)
                                break
                            except ValueError:
                                print("Invalid input. Please enter a valid VLAN ID.")

                        # รับค่า lpid
                        while True:
                            try:
                                lpid = int(input("Enter lpid (1-28): ")) - 1
                                if lpid < 0 or lpid > 27:
                                    print(
                                        "lpid must be between 1 and 28. Please enter again."
                                    )
                                    continue
                                break
                            except ValueError:
                                print("Invalid input. Please enter a valid lpid.")

                        url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"
                        payload = {
                            "method": "devConfig.add",
                            "params": {
                                "module": "static_mac",
                                "noParse": True,
                                "async": None,
                                "remoteIp": False,
                                "data": {
                                    "macaddr": macaddr,
                                    "vlanid": vlanid_str,  # ใช้ vlanid_str ที่แปลงเป็น string
                                    "lpid": lpid,
                                },
                                "device": "pc",
                            },
                        }
                        response = send_request(url, payload, cookie_name, cookie_value)
                        print(response.text)
                        input("Press Enter to continue...")

                    elif static_sub_choice == "2":
                        print("(2) remove")
                        while True:
                            macaddr = input(
                                "Enter MAC Address (e.g., 00:22:11:44:33:55): "
                            )
                            mac_regex = re.compile(
                                r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
                            )
                            if mac_regex.match(macaddr):
                                break
                            print("Invalid MAC address format. Please enter again.")

                        # รับค่า vlanid และตรวจสอบความถูกต้อง
                        while True:
                            try:
                                vlanid = int(input("Enter VLAN ID: "))
                                if vlanid < 0 or vlanid > 4095:
                                    print(
                                        "VLAN ID must be between 0 and 4095. Please enter again."
                                    )
                                    continue
                                if (vlanid - 1) == 23:
                                    print("VLAN ID - 1 is 23. Please enter again.")
                                    continue
                                # แปลง vlanid เป็น string ก่อนส่ง
                                vlanid_str = str(vlanid)
                                break
                            except ValueError:
                                print("Invalid input. Please enter a valid VLAN ID.")
                        url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"
                        payload = {
                            "method": "devConfig.del",
                            "params": {
                                "module": "static_mac",
                                "noParse": True,
                                "async": None,
                                "remoteIp": False,
                                "data": {
                                    "list": [
                                        {
                                            "vlanid": vlanid_str,
                                            "macaddr": macaddr,
                                        }
                                    ]
                                },
                                "device": "pc",
                            },
                        }
                        response = send_request(url, payload, cookie_name, cookie_value)
                        print(response.text)
                        input("Press Enter to continue...")

            elif sub_choice == "4":
                print("Aging time")
                try:
                    agetime = int(input("Aging Time (Range: 10-630. 0 indicates): "))
                    if agetime < 0 or agetime > 630:
                        print("Aging time must be between 10 and 630 or 0.")
                        input("Press Enter to continue...")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a valid aging time.")
                    input("Press Enter to continue...")
                    continue

                url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"
                payload = {
                    "method": "devConfig.set",
                    "params": {
                        "module": "mac_agetime",
                        "noParse": True,
                        "async": None,
                        "remoteIp": False,
                        "data": {"mac_agetime": agetime},
                        "device": "pc",
                    },
                }
                response = send_request(url, payload, cookie_name, cookie_value)
                print(response.text)
                input("Press Enter to continue...")

            elif sub_choice == "5":
                print("Filter mac")
                print("(1) add")
                print("(2) remove")
                filter_sub_choice = input("Select sub-choice: ")
                clear_screen()
                if filter_sub_choice == "1":
                    print("(1) add")
                    while True:
                        macaddr = input("Enter MAC Address (e.g., 00:22:11:44:33:55): ")
                        mac_regex = re.compile(
                            r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
                        )
                        if mac_regex.match(macaddr):
                            break
                        print("Invalid MAC address format. Please enter again.")

                    # รับค่า vlanid และตรวจสอบความถูกต้อง
                    while True:
                        try:
                            vlanid = int(input("Enter VLAN ID: "))
                            if vlanid < 0 or vlanid > 4095:
                                print(
                                    "VLAN ID must be between 0 and 4095. Please enter again."
                                )
                                continue
                            if (vlanid - 1) == 23:
                                print("VLAN ID - 1 is 23. Please enter again.")
                                continue
                            # แปลง vlanid เป็น string ก่อนส่ง
                            vlanid_str = str(vlanid)
                            break
                        except ValueError:
                            print("Invalid input. Please enter a valid VLAN ID.")

                    url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"
                    payload = {
                        "method": "devConfig.add",
                        "params": {
                            "module": "filter_mac",
                            "noParse": True,
                            "async": None,
                            "remoteIp": False,
                            "data": {
                                "macaddr": macaddr,
                                "vlanid": vlanid_str,
                                "lpid": "",
                            },
                            "device": "pc",
                        },
                    }
                    response = send_request(url, payload, cookie_name, cookie_value)
                    print(response.text)
                    input("Press Enter to continue...")

                elif filter_sub_choice == "2":
                    print("(2) remove")
                    while True:
                        macaddr = input("Enter MAC Address (e.g., 00:22:11:44:33:55): ")
                        mac_regex = re.compile(
                            r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
                        )
                        if mac_regex.match(macaddr):
                            break
                        print("Invalid MAC address format. Please enter again.")

                    # รับค่า vlanid และตรวจสอบความถูกต้อง
                    while True:
                        try:
                            vlanid = int(input("Enter VLAN ID: "))
                            if vlanid < 0 or vlanid > 4095:
                                print(
                                    "VLAN ID must be between 0 and 4095. Please enter again."
                                )
                                continue
                            if (vlanid - 1) == 23:
                                print("VLAN ID - 1 is 23. Please enter again.")
                                continue
                            # แปลง vlanid เป็น string ก่อนส่ง
                            vlanid_str = str(vlanid)
                            break
                        except ValueError:
                            print("Invalid input. Please enter a valid VLAN ID.")

                    url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"
                    payload = {
                        "method": "devConfig.del",
                        "params": {
                            "module": "filter_mac",
                            "noParse": True,
                            "async": None,
                            "remoteIp": False,
                            "data": {
                                "list": [
                                    {
                                        "macaddr": macaddr,
                                        "vlanid": vlanid_str,
                                    }
                                ]
                            },
                            "device": "pc",
                        },
                    }
                    response = send_request(url, payload, cookie_name, cookie_value)
                    print(response.text)
                    input("Press Enter to continue...")

            elif sub_choice == "0":
                continue  # กลับไปที่หน้าหลัก

            else:
                print("Invalid sub-function selected")
                input("Press Enter to continue...")

        elif choice == "0":
            break  # ออกจากโปรแกรม

        else:
            print("Invalid function selected")
            input("Press Enter to continue...")
