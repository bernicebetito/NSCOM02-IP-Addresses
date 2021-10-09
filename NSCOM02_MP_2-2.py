# BETITO, Bernice Marie M. NSCOM02 - S12


def check(num, addresses):
    ctr = 0
    limit = 255

    while ctr < num:
        if num == 2 and ctr == 1:
            limit = 32
        if '/' in addresses[ctr]:
            addresses[ctr] = addresses[ctr].split('/', 1)[0]
        try:
            if 0 <= int(addresses[ctr]) <= limit:
                ctr += 1
            else:
                ctr = 0
                break
        except ValueError:
            ctr = 0
            break

    return ctr == num


def arrange(number, names, total):
    result = {}
    for x in range(total):
        result.update({names[x]: number[x]})

    sorted_result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

    return sorted_result


def subnet_calc():
    print("\n1. Subnet Calculator")
    print("For this option, the following is needed in the indicated example:")
    print("\nEXAMPLE:")
    print("IP Address:                    123.456.7.8/24")
    print("Number of Networks:            2")
    print("Name of Network 1:             Network 1")
    print("Number of IP Addresses Needed: 70")
    print("Name of Network 2:             Network 2")
    print("Number of IP Addresses Needed: 20\n")

    address = "0"
    countA = 0
    countB = 0
    while True:
        print("Please provide the needed information:")
        if address == "0" and countA == 0 and countB == 0:
            address = input("IP Address:\t")
            countA = address.count(".")
            countB = address.count("/")
        if countA != 3:
            print("Invalid IP Address Format. Please try again.\n")
            address = "0"
            countA = 0
            countB = 0
        elif countB == 1:
            point = address.rfind('.')
            slash = address.rfind('/')
            if point < slash:
                ip_add = list(address.split("."))
                cidr = list(ip_add[len(ip_add) - 1].split("/"))
                if check(len(ip_add), ip_add) == 1 and check(len(cidr), cidr) == 1:
                    while True:
                        try:
                            names_ntwk = []
                            numbers_ntwk = []
                            num_ntwk = int(input("Number of Networks:\t"))
                            break
                        except ValueError:
                            print("Invalid Number of Networks. Please try again.\n")
                            print("IP Address:\t", address)
                    for x in range(num_ntwk):
                        name = "0"
                        while name == "0":
                            print("Name of Network", x + 1, end="")
                            name = input(":\t")
                            for ctr in names_ntwk:
                                if name.upper() == ctr.upper():
                                    print(name, "is already taken, please enter a new one.\n")
                                    name = "0"
                                    break
                        number = -1
                        while 0 > number or number > 4294967294:
                            try:
                                number = int(input("Number of IP Addresses Needed:\t"))
                                if 0 > number or number > 4294967294:
                                    print("Number of IP Addresses is out of bounds. Please try again.\n")
                            except ValueError:
                                print("Invalid Number of IP Addresses. Please try again.\n")
                                print("Name of Network", x + 1, ":\t", name)
                                number = -1
                        names_ntwk.append(name)
                        numbers_ntwk.append(number)
                    break
                else:
                    print("Invalid IP Address Format. Please try again.\n")
                    address = "0"
                    countA = 0
                    countB = 0
            else:
                print("Invalid IP Address Format. Please try again.\n")
                address = "0"
                countA = 0
                countB = 0
        else:
            print("Invalid IP Address Format. Please try again.\n")
            address = "0"
            countA = 0
            countB = 0

    sorted_ntwk = arrange(numbers_ntwk, names_ntwk, num_ntwk)
    counter = 0

    for key, value in sorted_ntwk.items():
        names_ntwk[counter] = key
        numbers_ntwk[counter] = value
        counter += 1

    ntwk_id = [0] * num_ntwk
    ip_add[3] = 0
    net_addresses = ["0"] * num_ntwk
    masks = ["0"] * num_ntwk
    pref_length = [0] * num_ntwk
    prefix = ["0"] * num_ntwk
    num_address = [4294967296] * num_ntwk
    first_hosts = ["0"] * num_ntwk
    last_hosts = ["0"] * num_ntwk
    broadcast_add = ["0"] * num_ntwk
    unused_add = [0] * num_ntwk

    for x in range(num_ntwk):
        for number in range(32):
            num_address[x] /= 2
            pref_length[x] += 1
            if num_address[x] < (numbers_ntwk[x] + 2):
                num_address[x] *= 2
                pref_length[x] -= 1

        i = 32
        pow_two = 0
        curr = 3
        subnet_mask = [255] * 4
        while i >= pref_length[x]:
            i -= 1
            subnet_mask[curr] = 256
            hold = pow(2, pow_two)
            if hold >= 256:
                subnet_mask[curr] = 0
                curr -= 1
                pow_two = 0
            else:
                subnet_mask[curr] -= hold
            pow_two += 1

        ntwk_address = [0] * 4
        one_host = [0] * 4
        last_host = [0] * 4
        brd_add = [0] * 4

        for i in range(3):
            ntwk_address[i] = int(ip_add[i])
            one_host[i] = int(ip_add[i])
            last_host[i] = int(ip_add[i])
            brd_add[i] = int(ip_add[i])

        if x > 0:
            for ctr in range(x):
                ntwk_address[3] += int(num_address[ctr])
        one_host[3] = ntwk_address[3] + 1
        last_host[3] = one_host[3] + (num_address[x] - 3)
        brd_add[3] = last_host[3] + 1

        for ctr in range(3, -1, -1):
            if ntwk_address[ctr] > 255:
                while ntwk_address[ctr] > 255:
                    ntwk_address[ctr] -= 256
                    ntwk_address[ctr - 1] += 1
            if one_host[ctr] > 255:
                while one_host[ctr] > 255:
                    one_host[ctr] -= 256
                    one_host[ctr - 1] += 1
            if last_host[ctr] > 255:
                while last_host[ctr] > 255:
                    last_host[ctr] -= 256
                    last_host[ctr - 1] += 1
            if brd_add[ctr] > 255:
                while brd_add[ctr] > 255:
                    brd_add[ctr] -= 256
                    brd_add[ctr - 1] += 1

        a = ""
        b = ""
        c = ""
        d = ""
        e = ""
        for i in range(4):
            a += str(int(subnet_mask[i]))
            b += str(int(ntwk_address[i]))
            c += str(int(one_host[i]))
            d += str(int(last_host[i]))
            e += str(int(brd_add[i]))
            if i < 3:
                a += "."
                b += "."
                c += "."
                d += "."
                e += "."
        ntwk_id[x] = x + 1
        masks[x] = a
        prefix[x] = "/" + str(int(pref_length[x]))
        net_addresses[x] = b
        first_hosts[x] = c
        last_hosts[x] = d
        broadcast_add[x] = e
        unused_add[x] = int(num_address[x] - numbers_ntwk[x] - 2)

    for i in range(num_ntwk):
        num_address[i] = int(num_address[i]) - 2

    print("\n{:<10} {:<10} {:<18} {:<18} {:<10} {:<11} {:<18} {:<18} {:<18} {:<11}".format(
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Number of'))

    print("{:<10} {:<10} {:<18} {:<18} {:<10} {:<11} {:<18} {:<18} {:<18} {:<11}".format(
        'Network', 'Network', ' ', ' ', 'Prefix ', 'Number of', 'First Usable',
        'Last Usable', ' ', 'Unused'))

    print("{:<10} {:<10} {:<18} {:<18} {:<10} {:<11} {:<18} {:<18} {:<18} {:<11}".format(
        'ID', 'Name', 'Network Address', 'Subnet Mask', 'Length',
        'Usable IPs', 'Host Address', 'Host Address', 'Broadcast Address', 'Address'))

    print("{:<10} {:<10} {:<18} {:<18} {:<10} {:<11} {:<18} {:<18} {:<18} {:<11}".format(
        '---------', '---------', '-----------------', '-----------------', '---------',
        '----------', '-----------------', '-----------------', '-----------------', '----------'))

    temp = 0
    for i in range(num_ntwk):
        arr = []
        if len(names_ntwk[i]) > 7:
            temp = 1
            ctr = int((len(names_ntwk[i]) / 7) + 2)
            index = 0
            for x in range(ctr):
                start = index
                index = x * 7
                if index > len(names_ntwk[i]):
                    index = len(names_ntwk[i])
                arr.append(names_ntwk[i][start:index])
        if temp == 0:
            print("{:<10} {:<10} {:<18} {:<18} {:<10} {:<11} {:<18} {:<18} {:<18} {:<11}".format(
                ntwk_id[i], names_ntwk[i], net_addresses[i], masks[i], prefix[i], num_address[i],
                first_hosts[i], last_hosts[i], broadcast_add[i], unused_add[i]))
        elif temp == 1:
            temp = 0
            print("{:<10} {:<10} {:<18} {:<18} {:<10} {:<11} {:<18} {:<18} {:<18} {:<11}".format(
                ntwk_id[i], arr[1], net_addresses[i], masks[i], prefix[i], num_address[i],
                first_hosts[i], last_hosts[i], broadcast_add[i], unused_add[i]))
            for x in range(2, len(arr)):
                print("{:<10} {:<10} {:<18} {:<18} {:<10} {:<11} {:<18} {:<18} {:<18} {:<11}".format(
                      ' ', arr[x], ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '))
        print()

    choose(1)


def add_class():
    print("2. Check Address Class")
    print("For this option, an IP Address is needed.")

    while True:
        print("Needed format of IP Address: 123.456.789.012")
        address = input("Please enter the IP Address:\t")
        count = address.count(".")
        if count != 3:
            print("Invalid Format. Please try again.\n")
        else:
            ip_add = list(address.split("."))
            if check(len(ip_add), ip_add) == 1:
                break
            else:
                print("Invalid Format. Please try again.\n")

    ntwk_add = ""
    for i in range(3):
        ntwk_add += str(ip_add[i])
        ntwk_add += "."

    ntwk_add += "0"

    if 0 <= int(ip_add[0]) < 127:
        ntwk_add += "/8"
        if int(ip_add[3]) == 0:
            address = address + "/8"
            print("\nThe address", address, "is a Class A Network Address")
        else:
            print("\nThe address", address, "is a Class A Address, whose Network Address is", ntwk_add)
    elif int(ip_add[0]) == 127:
        ntwk_add += "/8"
        print("\nThe address", address, "is a Loopback Address, whose Network Address is", ntwk_add)
    elif 128 <= int(ip_add[0]) < 192:
        ntwk_add += "/16"
        if int(ip_add[3]) == 0:
            address = address + "/16"
            print("\nThe address", address, "is a Class B Network Address")
        else:
            print("\nThe address", address, "is a Class B Address, whose Network Address is", ntwk_add)
    elif 192 <= int(ip_add[0]) < 224:
        ntwk_add += "/24"
        if int(ip_add[3]) == 0:
            address = address + "/24"
            print("\nThe address", address, "is a Class C Network Address")
        else:
            print("\nThe address", address, "is a Class C Address, whose Network Address is", ntwk_add)
    elif 224 <= int(ip_add[0]) < 240:
        ntwk_add += "/32"
        if int(ip_add[3]) == 0:
            address = address + "/32"
            print("\nThe address", address, "is a Class D Network Address")
        else:
            print("\nThe address", address, "is a Class D Address, whose Network Address is", ntwk_add)
    elif 240 <= int(ip_add[0]) < 256:
        ntwk_add += "/32"
        if int(ip_add[3]) == 0:
            address = address + "/32"
            print("\nThe address", address, "is a Class E Network Address")
        else:
            print("\nThe address", address, "is a Class E Address, whose Network Address is", ntwk_add)
    else:
        print("\nThe address", address, "class could not be identified.")
    choose(2)


def add_type():
    print("3. Check Address Type")
    print("For this option, an IP Address, inlcuding CIDR value, is needed.")

    while True:
        print("Needed format of IP Address: 123.456.789.012/24")
        address = input("Please enter the IP Address:\t")
        countA = address.count(".")
        countB = address.count("/")
        if countA != 3:
            print("Invalid Format. Please try again.\n")
        elif countB == 1:
            point = address.rfind('.')
            slash = address.rfind('/')
            if point < slash:
                ip_add = list(address.split("."))
                cidr = list(ip_add[len(ip_add) - 1].split("/"))
                if check(len(ip_add), ip_add) == 1 and check(len(cidr), cidr) == 1:
                    break
                else:
                    print("Invalid Format. Please try again.\n")

        else:
            print("Invalid Format. Please try again.\n")

    value = int(cidr[1])
    maximum = 4294967296
    ctr = 0

    while ctr != value and ctr <= 32:
        maximum /= 2
        ctr += 1

    last = int(cidr[0])
    ntwk = 0
    brdcst = (ntwk + maximum) % 256 - 1
    if brdcst < 0:
        brdcst += 256

    while brdcst < last:
        ntwk += maximum
        while ntwk >= 256:
            ntwk -= 256
        brdcst = (ntwk + maximum) % 256 - 1
        if brdcst < 0:
            brdcst += 256

    hostA = ntwk + 1
    hostB = brdcst - 1

    if last == ntwk:
        ip_type = "Network Address"
    elif hostA <= last <= hostB:
        ip_type = "Host Address"
    elif last == brdcst:
        ip_type = "Broadcast Address"
    else:
        ip_type = "Undefined"

    if address.find('/') == len(address) - 2:
        ip_print = address[:-2]
    elif address.find('/') == len(address) - 3:
        ip_print = address[:-3]
    else:
        ip_print = address

    print("\nThe IP Address", ip_print, "is a", ip_type)
    choose(3)


def choose(num):
    choice = ""
    if num == 1:
        choice = "Subnet Calculator"
    elif num == 2:
        choice = "Check Address Class"
    elif num == 3:
        choice = "Check Address Type"

    letter = 0
    while letter == 0:
        print("\n\nChoose an action:")
        print("[R]edo", choice, "\n[B]ack to Home Page\n[E]xit")
        chosen = input("Enter the letter of your choice:\t")
        if chosen.upper() == "R":
            letter = 1
            print("\n\n")
            options(num)
        elif chosen.upper() == "B":
            letter = 1
            print()
            homepage()
        elif chosen.upper() == "E":
            letter = 1
            print("\n\n")
            exit_prog()
        else:
            print("Invalid input, please try again.")


def exit_prog():
    print("4. Exit")
    ext = 0
    while ext == 0:
        print("Are you sure you want to exit the program?")
        print("\t[Yes] to Exit\n\t[No] to Go Back to Home Page")
        choice = input("Input:\t")
        if choice.upper() == "YES":
            print("Thank you for using this program!")
            ext = 1
        elif choice.upper() == "NO":
            print("Alright, Back to homepage!\n")
            ext = 1
            homepage()
        else:
            print("Invalid input, please try again.\n")


def options(num):
    if num == 1:
        subnet_calc()
    elif num == 2:
        add_class()
    elif num == 3:
        add_type()
    elif num == 4:
        exit_prog()


def homepage():
    print("\nHello there Network Engineer!")
    print("In order to help you, please select any of the following options:\n")
    print("\t1. Subnet Calculator\n\t2. Check Address Class\n\t3. Check Address Type\n\t4. Exit\n")

    while True:
        try:
            choice = int(input("Input:\t"))
            if 0 < choice < 5:
                break
            else:
                print("Invalid input, please try again.\n")
        except ValueError:
            print("Invalid input, please try again.\n")

    print("\n")
    options(choice)


homepage()
