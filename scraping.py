from bs4 import BeautifulSoup, Tag
from helpers import Repo, Browser
from os import makedirs, path, environ

def parse_repo(repo: Tag):
    # First div in li element that wraps a github repo.
    div_wrap = repo.find("div") 
    # Next up are three div elements that seperate rows on information,
    # first of which has a link to the repo as well as its name
    div_title = div_wrap.find("div")
    title_link = div_title.select_one("h3 > a")
    repo_name = title_link.getText(strip=True)
    repo_link = f'https://github.com{title_link["href"]}'
    # Second div contains a nested p tag that contains repo description
    try:
        repo_description = div_wrap.find("p").getText(strip=True)
    except AttributeError:
        repo_description = "No description"
    # Third div conatains other information such as number of stars, forks,
    # etc and a special "relative-time" tag that contains the date of
    # the latests repo update
    repo_updated_at = div_wrap.find("relative-time")["title"]
    repo_tech = div_wrap.find("span",attrs={"itemprop":"programmingLanguage"}).getText(strip=True)
    return Repo(repo_name, repo_link, repo_description, repo_tech,repo_updated_at)

def scrape(github_username: str, log: bool=True):
    lang = environ["LANG"]
    with Browser() as browser:
        print(f"Scraping {github_username}'s github...")
        url = f"https://github.com/{github_username}?tab=repositories&type=source&langauge={lang}"
        browser.get(url)
        soup = BeautifulSoup(browser.page_source,"html.parser")
        reposRAW = soup.find("div",attrs={"id":"user-repositories-list"})
        data = [parse_repo(repo) for repo in reposRAW.find_all("li")]
    if log:
        scrapeDIR = environ.get("SCRAPED_DIR","scraped")
        if not path.isdir(scrapeDIR):
            makedirs(scrapeDIR)
        with open(f"{scrapeDIR}/{github_username}.txt", "w", encoding="utf-8") as file:
            for repo in data:
                file.write(f'{repo}\n')
    return data

def multiScrape(usernames: list, log: bool=True):
    lang = environ["LANG"]
    dataList = []
    with Browser() as browser:
        for github_username in usernames:
            print(f"Scraping {github_username}'s github...")
            url = f"https://github.com/{github_username}?tab=repositories&type=source&language={lang}"
            browser.get(url)
            soup = BeautifulSoup(browser.page_source,"html.parser")
            reposRAW = soup.find("div",attrs={"id":"user-repositories-list"})
            data = [parse_repo(repo) for repo in reposRAW.find_all("li")]
            dataList.append(data)
    if log:
        scrapeDIR = environ.get("SCRAPED_DIR","scraped")
        if not path.isdir(scrapeDIR):
            makedirs(scrapeDIR)
        for data, github_username in zip(dataList, usernames):
            with open(f"{scrapeDIR}/{github_username}.txt", "w", encoding="utf-8") as file:
               for repo in data:
                    file.write(f'{repo}\n')   
    return dataList
      