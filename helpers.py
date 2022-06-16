from selenium import webdriver
from selenium.webdriver.firefox.service import Service

class Repo:
    def __init__(self, name: str, link: str, description: str, tech: str, updated: str):
        self.name = name
        self.link = link
        self.description = description
        self.tech = tech
        self.updated = updated

    def __str__(self):
        return f'Repo "{self.name}" @ {self.link}. Made with {self.tech}. Last updated on {self.updated}'

class Browser:
    def __init__(self):
        self.browser = webdriver.Firefox(service=Service(executable_path="./geckodriver.exe"))
    def __enter__(self):
        return self.browser
    def __exit__(self, type, value, traceback):
        self.browser.quit()
