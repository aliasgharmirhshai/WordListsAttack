import requests
import os
import sys
import datetime

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

def start():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(YELLOW + f"\n\nStarting At {datetime.datetime.now()}\n")

def help():
        print(WHITE + """
        WordPress Usage:
            -wordpress-plugin[Plugin], -wordpress-content[Content], -wordpress[Random]
        WordPress Examples:
            python3 WordListsAttack.py -wordpress-plugin [Host]
            python3 WordListsAttack.py -wordpress [Host]
        Enter Word List:
            python3 WordListsAttack.py -file [Your Word List] [Host]
        """)

def query_handler():
    global main_query
    global query_count
    global host
    
    try:
        if sys.argv[1] == '-wordpress-plugin':
            query_file = "Wordlists\wp-plugins.txt"
            host = sys.argv[2]

        elif sys.argv[1] == '-wordpress-content':
            query_file = "Wordlists\wp-plugins.txt"
            host = sys.argv[2]
            
        elif sys.argv[1] == "-wordpress":
            query_file = "Wordlists\wordpress-random.txt"
            host = sys.argv[2]

        elif sys.argv[1] == "-file":
            query_file = sys.argv[2]
            host = sys.argv[3]

        else:
            print(RED + "Command Not Found")
    
    except IndexError:
        print(RED + "Please Enter Host")

    with open(query_file, encoding="utf-8") as main_query:
        main_query = main_query.read().split("\n")
        query_count = len(main_query)


def send_query(main_query, host, query_count):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    
    if not "http://" in host or not "https://" in host:
        host = "http://" + host
    else:
        pass

    print(YELLOW + f"Use {query_count} WordList\n")

    for query in main_query:
        url = f'{host}/{query}'
        result = requests.get(url, headers=headers)

        if result.status_code == 200:
            print(f"{GREEN} [+] {host}/{query} Is Online")
        else:
            print(f"{RED} [-] {host}{query} Is Offline")



if __name__ == "__main__":
    try:
        if sys.argv[1] == "-h":
            help()
        else:
            start()
            query_handler()
            send_query(main_query, host, query_count)

    except KeyboardInterrupt:
        print('By......')
    except FileNotFoundError:
       print(RED + f"No such file or directory")
    except IndexError:
        help()
    except NameError:
        pass