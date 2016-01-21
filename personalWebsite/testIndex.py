import os
import unittest
import tempfile
import personalWebsite
from bs4 import BeautifulSoup
import requests
import warnings

class testIndex(unittest.TestCase):

    def setUp(self):
        self.db_fd, personalWebsite.app.config['DATABASE'] = tempfile.mkstemp()
        personalWebsite.app.config['TESTING'] = True
        self.app = personalWebsite.app.test_client()

        #gets the webpage
        self.sourceCode = requests.get('http://127.0.0.1:5000/', verify=False)
        #removes the header from the webpage text
        self.plainText = self.sourceCode.text
        #turns the text into a beautiful soup object
        self.soup = BeautifulSoup(self.plainText)

        self.navbarChildren = {}
        self.verbose = True

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(personalWebsite.app.config['DATABASE'])

    def test_alt_text_matches_any_navbar_link(self):
        self.navbar = given_the_navbar(self.soup)
        if self.verbose:
            print('Given the navbar')
        self.navText = and_the_navbar_text(self.navbar)
        if self.verbose:
            print('And the navbar text')

        #assert False


#Given the navbar
def given_the_navbar(soup):
    navbar = soup.findAll( attrs={'class':'nav navbar-nav'})
    print(navbar)
    if len(navbar) != 1:
        Warning('''
            TestSuite will only test one <ul> with class \'nav navbar-nav\''''
        )
    return navbar

#And the navbar text
def and_the_navbar_text(navbar):
    navbarChildren = navbar[0].findAll('li')
    navbarText = []
    for navbarChild in navbarChildren:
        print(navbarChild.string)
        navbarText.append(navbarChild.string)
    return navbarText



#And the navbar link
def test_the_navbar_link():
    pass

def test_the_navbar_alt_text():
    pass

def test_the_alt_text_matches_the_link():
    pass

if __name__ == '__main__':
    unittest.main()
