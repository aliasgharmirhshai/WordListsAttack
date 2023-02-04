import requests
import os
import sys

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

def start():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(YELLOW + f"\nStart Scanning.......\n")


def query_handler():
    global main_query
    global query_count
    
    try:
        if sys.argv[2] == '-Pl':
            query_file = "wp-plugins.txt"
        elif sys.argv[2] == '-Co':
            query_file = "wp-plugins.txt"
        else:
            print(RED + "Command Not Found")
    except IndexError:
        query_file = "wordpress-random.txt"


    with open(query_file, encoding="utf-8") as main_query:
        main_query = main_query.read().split("\n")
        query_count = len(main_query)


def send_query(main_query, host, query_count):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    
    if not "http://" in host or not "https://" in host:
        host = "http://" + host
    else:
        pass

    print(YELLOW + f"Use {query_count} Best WordList\n")

    for query in main_query:
        url = f'{host}/{query}'
        result = requests.get(url, headers=headers)

        if result.status_code == 200:
            print(f"{GREEN} [+]{host}/{query} Is Online")
        else:
            print(f"{RED} [-]{host}{query} Is Offline")



if __name__ == "__main__":
    try:
        start()
        query_handler()
        host = sys.argv[1]
        send_query(main_query, host, query_count)
    except KeyboardInterrupt:
        print('By......')