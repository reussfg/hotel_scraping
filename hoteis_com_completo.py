import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import html5lib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys

# Input of the city I want do dig in
url = input('Insert the URL of what you want to dig in: ')

# Setting Chrome Window Sizes
options = Options()
options.add_argument('window-size= 400,800')

# Opening Chrome
browser = webdriver.Chrome()
url_open = browser.get(url)  # Website I want to open with its search

# Waiting for response time
sleep(5)

# Get the Loop to Start Dig in
a = 1
while a < 30:
    # Start the Soup Process
    link = requests.get('https://bit.ly/3hSIkW9')
    resultado = link.content
    soup = BeautifulSoup(resultado, 'html.parser')
    urls = []

    # Start Looping for All Links
    for div in soup.find_all('div', attrs={'class', '-RcIiD'}):
        a_tag = div.find('a')
        urls.append(a_tag.attrs['href'])

    # Adding the prefix to the link
    for i in range(len(urls)):
        urls[i] = str(urls[i])
        urls[i] = 'hoteis.com' + urls[i]
        print(urls[i])

    # Scroll down on the page
    down = browser.find_element_by_class_name('_12VuEX')
    down.send_keys(Keys.END)
    sleep(7)
    browser.execute_script("window.scrollTo(document.body.scrollHeight, 700);")
    a += 1
    sleep(10)

