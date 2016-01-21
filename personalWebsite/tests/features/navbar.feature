Feature: Personal Website Navbar
	In order to discover the Person's Website
	As a Potential Employer
	We'll click all the links in the navbar
	
Scenario: alt text matches any navbar link
	Given the navbar
	And the navbar text
	And the navbar link
	And the navbar alt text
	Then the alt text matches the link
	
Scenario: Clicks any navbar link
	Given a navbar link
	When the user clicks the link
	Then a new page should open

	