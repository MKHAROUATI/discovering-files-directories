import sys
import requests

def file_reader(arg1, arg2):

    if not arg1.startswith("http://") and not arg1.startswith("https://"):
        arg1 = "http://" + arg1
    if not arg1.endswith("/"):
        arg1 += "/"
    try:
        with open(arg2, 'r') as file:
            for line in file:
                try:
                    response = requests.get(f"{arg1}{line.strip()}")
                    if response.status_code != 404:
                        print(f"[+] {arg1}{line.strip()} [{response.status_code}] [{response.reason}]")
                except requests.exceptions.RequestException as e:
                    print(f"An error occurred: {e}")

    except FileNotFoundError:
        print(f"File not found: {arg2}")
    except Exception as e:
        print(f"An error occurred: {e}")

if len(sys.argv) != 3:
    print("Usage: python3 script.py arg1 arg2")
    sys.exit(1)

argOne = sys.argv[1]
argTwo = sys.argv[2]

file_reader(argOne, argTwo)
