# NSCOM02-IP-Addresses
_An IP Address tool that includes Subnet Calculator, Checking of Address Class, and Checking of Address Type._\
Date Accomplished: September 25, 2020

## Use
This project allows users to learn more about IP Addresses through different tools.

## Pre-requisites
1. Python / Python3
  * Programming language used.
  * To download in **Linux**: `sudo apt-get install python3`
  * To download in **Windows**: [Python for Windows](https://www.python.org/downloads/windows/)
2. Curl
  * Command that allows the transfer (upload / download) of data using command line interface.
  * To download in **Linux**: `sudo apt-get install curl`
  * To download in **Windows**: [Curl for Windows](https://curl.se/windows/)

## Download
Download the project through the following commands:
* Linux:
``` sudo curl -O https://raw.githubusercontent.com/bernicebetito/NSCOM02-IP-Addresses/main/NSCOM02_MP_2-2.py ```
* Windows:
``` curl -O https://raw.githubusercontent.com/bernicebetito/NSCOM02-IP-Addresses/main/NSCOM02_MP_2-2.py ```

Once downloaded, the project can be used through the following commands:
* Linux: ` sudo python3 NSCOM02_MP_2-2.py `
* Windows: ` python NSCOM02_MP_2-2.py `

## Options
1. Subnet Calculator
  * Needed information:
    * IP Address
    * Number of Networks
    * Name of Networks
    * Number of IP Addresses needed in each network
  * The given IP Address would be divided between the networks.
2. Check Address Class
  * Needed information:
    * IP Address
  * The class of the given IP Address would be determined along with it's Network Address. Possible address class includes:
    * Class A Network Address
    * Class A Address
    * Class B Network Address
    * Class B Address
    * Class C Network Address
    * Class C Address
    * Class D Network Address
    * Class D Address
    * Class E Network Address
    * Class E Address
    * Loopback Adress
3. Check Address Type
  * Needed information:
    * IP Address
  * The address type of the given IP Address would be determined. Possible adress type includes:
    * Network Address
    * Host Address
    * Broadcast Adress
4. Exit
  * Exit the program
