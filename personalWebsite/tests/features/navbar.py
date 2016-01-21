import requests
from lettuce import *
from bs4 import BeautifulSoup


def setup(self, url='http://127.0.0.1:5000/'):
    self.sourceCode = requests.get(url, verify=False)
    self.plainText = self.sourceCode.text
    self.soup = BeautifulSoup(self.plainText)

@step('the navbar links')
def the_navbar_link(self):
    for link in self.soup.findAll('a', {'class':'post-content'}):
        self.linksAttributes[link.string] = {
            'alt':link.get('alt'),
            'href':link.get('href')
        }

@step('the alt text matches the link')
def the_alt_text_matches_the_link(self):
    for link in self.linksAttributes:
        assert link['href'] == link['alt']



