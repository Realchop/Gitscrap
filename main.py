from scraping import scrape, multiScrape
import argparse
from os import environ


parser = argparse.ArgumentParser()
parser.add_argument("-u","--user", type=str)
parser.add_argument("-m","--multi_search", type=str)
parser.add_argument("-f","--file", type=str)
parser.add_argument("-d","--directory", type=str)
parser.add_argument("-t","--tech", type=str)

args = parser.parse_args()
github_username = args.user

if args.directory:
    environ["SCRAPED_DIR"] = args.directory

if args.tech:
    environ["LANG"] = args.tech

if github_username:
    data = scrape(github_username)
elif args.multi_search:
    usernames = [_.strip() for _ in args.multi_search.split(",")]
    dataList = multiScrape(usernames)
elif args.file:
    try:
        with open(args.file) as file:
            usernames = [username.strip("\n\t ") for username in file]
    except FileNotFoundError:
        print("Invalid path to file.")
    else:
        dataList = multiScrape(usernames) 
else:
    github_username = input("Please input a github username(case sensitive): ")
    data = scrape(github_username)