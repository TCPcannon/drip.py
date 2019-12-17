"""
@name	Drip.py
@author	Jordan Cannon
@date	12/16/2019
@time	10:25 PM
Simple python script to retrieve my grades from iNow
"""
from requests import Session
from bs4 import BeautifulSoup as bs
import urllib

inject = {

	"txtUsername": "chrjcann0302",
	"txtPassword": "762160",
	"__EVENTVALIDATION": "/wEdAAYwFgklbmiMRbjkTsgQqmcxVK7BrRAtEiqu9nGFEI+jB3Y2+Mc6SrnAqio3oCKbxYainihG6d/Xh3PZm3b5AoMQaWblGWlWhpKppq/72/feNIVi3B09F0PtmOzzeTYZxWOrK56ULJ8+Tmpxk75pYyFMvLAgQg=="
	

}

with Session() as s:
	site = s.get("https://inowhome.attalla.k12.al.us/InformationNow/Login.aspx")
	s.post("https://inowhome.attalla.k12.al.us/InformationNow/Login.aspx", inject)
	
	grades = 'https://inowhome.attalla.k12.al.us/InformationNow/ParentPortal/Sti.Home.UI.Web/Student/Grades.aspx'
	page = urllib.request(grades)
	soup = bs(page, "html.parser")

	# couldnt get the grades page to work 10:58 PM