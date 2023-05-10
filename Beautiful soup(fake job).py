import requests
from bs4 import BeautifulSoup
import csv
# Make a request
page = requests.get(
    "https://realpython.github.io/fake-jobs/")
soup = BeautifulSoup(page.content, 'html.parser')

# Create top_items as empty list
show_jobs = []
jobs = soup.find_all("div", {"class": "card"})
for job in jobs:
    job_title = job.find('h2').text.strip()
    company_name = job.find('h3').text.strip()
    company_location = job.find('p').text.strip()
    posting_date = job.find('time').text.strip()
    
    show_jobs.append({
            "job_title":job_title,
            "company_name": company_name,
            "company_location": company_location,
            "posting_date": posting_date,
        })

for i in show_jobs:
    '''print(i)'''
    

keys = show_jobs[0].keys()

with open('job_list.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(show_jobs)