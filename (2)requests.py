#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 22:59:45 2025

@author: rrcolivarez
"""

from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text # print the text of the specific page
#print(html_text)

soup = BeautifulSoup(html_text, 'lxml')

#jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
#print(job)
company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
print(company_name)
skills = job.find('div', class_='more-skills-sections').text.replace(' ', '')
print(skills)

print(f'''
      Company Name: {company_name}
      Required Skills: {skills}
      ''')
      
     

#li - list tags. inside ul
# ul - unordered list - contains a lot of list tags

#%%
published_date = job.find('span', class_='sim-posted').span.text
print(published_date)

#%%

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    
    if 'few' in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
        skills = job.find('div', class_='srp-skills').text.replace(' ', '')
    
        print(f'''
              Company Name: {company_name}
              Required Skills: {skills}
              ''')
          