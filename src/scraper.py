import requests
from bs4 import BeautifulSoup

link = "https://oscar.gatech.edu/bprod/bwckschd.p_disp_detail_sched?term_in=202402&crn_in="
crn = "20002"

link += crn
link = BeautifulSoup(requests.get(link).content, "html.parser")
seats = link.find_all("table", class_="datadisplaytable")[1].find_all("td", class_="dddefault")
print("Class: " + link.find("th", class_="ddlabel").text)
print("Seats: " + seats[0].text + " - Taken: " + seats[1].text + " - Remaining: " + seats[2].text)
print("Waitlist Space: " + seats[3].text + " - Taken: " + seats[4].text + " - Remaining: " + seats[5].text)