from bs4 import BeautifulSoup
import requests
import json
from extractor import Extractor


class Linked_in_scraper:

    def scrape_profile_div(self, user_profile_url):

# Start session
        client = requests.Session()
        HOMEPAGE_URL = 'https://www.linkedin.com/uas/login'
        LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

# go to login page and get tokens
        home = client.get(HOMEPAGE_URL).content
        soup_login = BeautifulSoup(home, 'html.parser')
        csrf = soup_login.find(id="loginCsrfParam-login")['value']

# prepare header for POST request
        login_information = {
            'session_key': 'redleafpro@gmail.com',
            'session_password': 'asasas12',
            'loginCsrfParam': csrf,
        }

# login to linkedIn
        client.post(LOGIN_URL, data=login_information)

# get profile page
        profile_page = client.get(user_profile_url)

        soup_profile = BeautifulSoup(profile_page.content, 'html.parser')

        with open("linkedin.html", "wb") as file:
            file.write(profile_page.content)


#  extract info from profile

        div = soup_profile.find_all('code')
        data=div[26].text
        jsonData=json.loads(str(data))

        extract = Extractor()
        extract.extract_info(jsonData)



    def scrape_one_profile(self, profile_url):
        return self.scrape_profile_div(profile_url)

    def __init__(self, profile_name):
        self.profile_name = profile_name
