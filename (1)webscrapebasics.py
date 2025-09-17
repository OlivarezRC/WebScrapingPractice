#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 22:23:34 2025

@author: rrcolivarez
"""

from bs4 import BeautifulSoup
with open('home.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
   # print(soup.prettify())
   
    tags = soup.find('h5') #search for specific html tag. Searaches for the first element.
    print(tags)
    courses_html_tags = soup.find_all('h5') # list of h5 tags
    print (courses_html_tags)
    
    for course in courses_html_tags:
        print(course.text) # Output of the texts
    
#%%

## Using inspect of any browser

from bs4 import BeautifulSoup
with open('home.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card') #add underscore on class due to python class
    #print(course_cards)
    
    for course in course_cards:
     #   print(course.h5)
        course_name = course.h5.text
        course_price = course.a.text
        
        print(course_name)
        print(course_price)
        
        # #split method
        course_price = course.a.text.split()[-1] #last element
        print(f'{course_name} costs {course_price}')
    