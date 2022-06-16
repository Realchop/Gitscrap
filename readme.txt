How to setup:
First, create a virtual env and move main.py, scraping.py, req.txt 
and .env file in it. Next, download the latest version of geckodriver
from: https://github.com/mozilla/geckodriver/releases .
Now run pip install -r req.txt to install dependencies.

NOTE: You will need to have firefox installed. Alternatively, you can
edit scraping.py to use a different webdriver.


How to use:
To scrape a single account, run main.py script and input a github 
username(case sensitive). Can also run main.py -u username. In order 
to scrape multiple accounts, run script with -m and input account 
names seperated with a comma. If you would like account names to be 
read from a separate file, run script with argument -f path_to_file. 
One account name per row. If you would like to search repos only for 
certain technology, add a -t followed by the name of technology.
By default, all of scraped data will be placed in a directory
called "scraped". If you would like them to be created in another folder,
use the -d path_to_dir option. If you would like to change the default
directory, simply change the value of "SCRAPED_DIR" in the .env file.

NOTE: Scraping for multiple programming languages would require one
full cycle of the process per language per github profile. So instead,
you should import data you scraped into a database and then query it.