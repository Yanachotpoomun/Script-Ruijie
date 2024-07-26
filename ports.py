from clear_screen import clear_screen
from send_request import send_request


def ports(cookie_name, cookie_value, url):
    clear_screen()
    print("(1) Aggregate")
    print("(2) Basic setting")
    print("(3) Port Mirroring")
    print("(4) MGMT IP")
    print("(5) Rate Limiting")

    choice = input("Select function: ")
    clear_screen()

    if choice == "1":
        print("Aggregate")
        print("(1) Src MAC")
        print("(2) Src IP")
        print("(3) Src L4 Port")
        print("(4) Src Port")
        print("(5) Dest MAC")
        print("(6) Dest IP Address")
        print("(7) Dest L4 Port")
        print("(8) Src & Dest MAC")
        print("(9) Src & Dest IP Address")
        print("(10) Src & Dest L4 Port")

        sub_choice = input("Select sub-function: ")
        if sub_choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            print(f"Option {sub_choice} selected")

            url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"
            payload = {
                "method": "devConfig.set",
                "params": {
                    "module": "load_balance",
                    "noParse": True,
                    "async": None,
                    "remoteIp": False,
                    "data": {"load_balance": int(sub_choice)},
                    "device": "pc",
                },
            }

            response = send_request(url, payload, cookie_name, cookie_value)
            print(response.text)
        else:
            print("Invalid sub-function selected")

    elif choice == "2":
        print("Basic setting")
        print("(1) Basic Settings")
        print("(2) Physical Settings")

        sub_choice = input("Select sub-function: ")
        clear_screen()

        if sub_choice == "1":
            print("Basic Settings")
            print("Batch edit")

            port_index = int(input("1. Enter port (1-24): "))
            lpid_value = port_index

            status_choice = input(
                "2. Status\n   (1) Enable\n   (2) Disable\nSelect status: "
            )
            enable_value = 1 if status_choice == "1" else 0

            rate_choice = input(
                "3. Rate\n   (1) Auto\n   (2) 10M\n   (3) 100M\n   (4) 1000M\nSelect Rate: "
            )
            if rate_choice == "1":
                c_speed_value = 4
            elif rate_choice == "2":
                c_speed_value = 0
            elif rate_choice == "3":
                c_speed_value = 1
            elif rate_choice == "4":
                c_speed_value = 2
            else:
                print("Invalid rate choice")
                exit()

            work_mode_choice = input(
                "4. Work Mode\n   (1) Auto\n   (2) Half-Duplex\n   (3) Full-Duplex\nSelect Work Mode: "
            )
            if work_mode_choice == "1":
                c_duplex_value = 0
            elif work_mode_choice == "2":
                c_duplex_value = 1
            elif work_mode_choice == "3":
                c_duplex_value = 2
            else:
                print("Invalid work mode choice")
                exit()

            flow_control_choice = input(
                "5. Flow Control\n   (1) Disable\n   (2) Enable\nSelect Flow Control: "
            )
            c_flowcontrol_value = 0 if flow_control_choice == "1" else 1

            url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"
            payload = {
                "method": "devConfig.update",
                "params": {
                    "module": "port_base",
                    "noParse": True,
                    "async": None,
                    "remoteIp": False,
                    "data": {
                        "data": [
                            {
                                "c_flowcontrol": c_flowcontrol_value,
                                "c_speed": c_speed_value,
                                "lpid": lpid_value,
                                "c_duplex": c_duplex_value,
                                "enable": enable_value,
                            }
                        ],
                        "device": "pc",
                    },
                },
            }

            response = send_request(url, payload, cookie_name, cookie_value)
            print(response.text)
        elif sub_choice == "2":
            print("Physical Settings")
            print("Batch edit")

            lpid = int(input("Please enter lpid (1-24): ")) - 1
            description = input("Please enter description: ")
            eee_input = int(input("Please select EEE:\n(1) Enable\n(2) Disable:\n"))
            eee = 1 if eee_input == 1 else 0
            mtu = int(input("Please enter MTU (Range: 64-9216): "))

            url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"
            payload = {
                "method": "devConfig.update",
                "params": {
                    "module": "port_phy",
                    "noParse": True,
                    "async": None,
                    "remoteIp": False,
                    "data": {
                        "data": [
                            {
                                "lpid": lpid,
                                "description": description,
                                "eee": eee,
                                "media_type": 1,
                                "mtu": mtu,
                            }
                        ]
                    },
                    "device": "pc",
                },
            }

            response = send_request(url, payload, cookie_name, cookie_value)
            print(response.text)
        else:
            print("Invalid sub-function selected")

    elif choice == "3":
        print("Port Mirroring")

        while True:
            try:
                user_input_src = input(
                    "Enter source port numbers 1-28 separated by commas: "
                )
                src_ports = [int(port) - 1 for port in user_input_src.split(",")]

                if any(port < 0 or port > 27 for port in src_ports):
                    print(
                        "All source port numbers must be between 1 and 28. Please try again."
                    )
                elif 23 in src_ports:
                    print(
                        "Port number 24 is not allowed. Please enter a different port."
                    )
                else:
                    src_ports = list(set(src_ports))
                    break
            except ValueError:
                print("Invalid input. Please enter valid integers separated by commas.")

        while True:
            try:
                user_input_dst = int(input("Enter a destination port number 1-28: "))

                if user_input_dst < 1 or user_input_dst > 28:
                    print(
                        "The destination port number must be between 1 and 28. Please try again."
                    )
                elif user_input_dst - 1 in src_ports:
                    print(
                        f"The port number {user_input_dst - 1} is already in the source ports list. Please enter a different port."
                    )
                elif user_input_dst - 1 == 23:
                    print(
                        "Port number 23 is not allowed. Please enter a different port."
                    )
                else:
                    dst = user_input_dst - 1
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        print(f"Source Ports: {src_ports}")
        print(f"Destination Port: {dst}")

        while True:
            try:
                mirror_input = int(
                    input("Enter mirror direction (1)Both (2)Incoming (3)Outgoing: ")
                )
                if mirror_input < 1 or mirror_input > 3:
                    print("The mirror direction must be 1, 2, or 3. Please try again.")
                else:
                    mirror = mirror_input - 1
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        while True:
            try:
                pkt_input = int(input("Enter pkt option (1)Enable (2)Disable: "))
                if pkt_input == 1:
                    pkt = 1
                    break
                elif pkt_input == 2:
                    pkt = 0
                    break
                else:
                    print("The pkt option must be 1 or 2. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        while True:
            try:
                port = int(input("Enter port number 1-4: "))
                if port < 1 or port > 4:
                    print("The port number must be between 1 and 4. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"
        payload = {
            "method": "devConfig.update",
            "params": {
                "module": "mirror",
                "noParse": True,
                "async": None,
                "remoteIp": False,
                "data": {
                    "src_port": src_ports,
                    "dst_port": dst,
                    "mirror_direction": mirror,
                    "switch": pkt,
                    "session": port,
                },
                "device": "pc",
            },
        }

        response = send_request(url, payload, cookie_name, cookie_value)
        print(response.text)

    elif choice == "4":
        print("MGMT IP")
        proto_choice = int(input("Internet:\n(1) Static IP\n(2) DHCP\n"))

        if proto_choice == 1:
            proto = "static"
            vlanid = input("VLAN ID:\n")
            ipaddr = input("IP Address:\n")
            netmask = input("Netmask:\n")
            gateway = input("Gateway:\n")
            dns = input("DNS:\n")
            wan_data = {
                "proto": proto,
                "vlanid": vlanid,
                "ipaddr": ipaddr,
                "netmask": netmask,
                "ignore": "1",
                "dns": dns,
                "gateway": gateway,
            }
        elif proto_choice == 2:
            proto = "dhcp"
            vlanid = input("VLAN ID:\n")
            wan_data = {"proto": proto, "vlanid": vlanid}
        else:
            print("Invalid choice")
            return

        url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"
        payload = {
            "method": "devConfig.set",
            "params": {
                "module": "network",
                "noParse": True,
                "async": None,
                "remoteIp": False,
                "data": {
                    "version": "1.0.0",
                    "lanNum": "0",
                    "wan": [wan_data],
                    "wanNum": "1",
                },
                "device": "pc",
            },
        }

        response = send_request(url, payload, cookie_name, cookie_value)
        print(response.text)

    elif choice == "5":
        print("Rate Limiting")
        print("(1) Batch Edit")
        print("(2) Delete")
        rate_limiting_choice = input("Select Rate Limiting function: ")
        clear_screen()

        if rate_limiting_choice == "1":
            # Batch Edit functionality here
            print("Batch Edit functionality selected")

            while True:
                try:
                    lpid = int(input("Please enter Port index (1-28): ")) - 1
                    if lpid == 23:
                        print("Value 23 is not allowed. Please enter a new value.")
                    else:
                        break
                except ValueError:
                    print("Please enter a numeric value.")

            while True:
                try:
                    irate = int(
                        input("Please enter RX rate (Range: 16-10000000kbps): ")
                    )
                    break
                except ValueError:
                    print("Please enter a numeric value.")

            while True:
                try:
                    orate = int(
                        input("Please enter TX rate (Range: 16-10000000kbps): ")
                    )
                    break
                except ValueError:
                    print("Please enter a numeric value.")

            url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"
            payload = {
                "method": "devConfig.update",
                "params": {
                    "module": "rate_limit",
                    "noParse": True,
                    "async": None,
                    "remoteIp": False,
                    "data": {
                        "data": [
                            {
                                "lpid": lpid,
                                "irate": irate,
                                "orate": orate,
                            }
                        ],
                        "device": "pc",
                    },
                },
            }

            response = send_request(url, payload, cookie_name, cookie_value)
            print(response.text)

        elif rate_limiting_choice == "2":
            # Delete functionality here
            print("Delete functionality selected")
            lpid_list = int(input("Enter port index to delete(1-28):\n")) - 1

            url = f"{url}/cgi-bin/luci/api/cmd?auth={cookie_value}"
            payload = {
                "method": "devConfig.del",
                "params": {
                    "module": "rate_limit",
                    "noParse": True,
                    "async": None,
                    "remoteIp": False,
                    "data": {"lpid_list": lpid_list},
                    "device": "pc",
                },
            }

            response = send_request(url, payload, cookie_name, cookie_value)
            print(response.text)

        else:
            print("Invalid Rate Limiting sub-function selected")
    else:
        print("Invalid choice")

    input("Press Enter to continue...")
