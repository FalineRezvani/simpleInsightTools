## Web Scraping Company Culture

2025-03-20

Author: Faline Rezvani

This notebook navigates to user's webpage of choice, locates the search bar, searches "About", gathers results, and returns the most frequently used words, statistically the most significant words.

from selenium import webdriver # Web testing library
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep # To allow time for webpage to load
import nltk # Stripping suffixes and removing stopwords
from nltk.corpus import stopwords # Stopwords are commonly used in language, but not useful to meaning
import re, string # Regular expressions for text cleaning

# Instantiating the browser driver object
driver=webdriver.Chrome()

# Assigning URL
driver.get("https://www.cognizant.com/us/en")
sleep(20) # Allow 20 seconds for webpage to load

### Finding elements: Navigate to the desired element on the webpage. Right click > Inspect > Right click highlighted selection > Copy XPath > Paste between multiline string quotes.

# Navigating to search field on a webpage
# To be manually adjusted by user per website, is there an icon?

# Clicking search icon (dependent upon webpage)
link=driver.find_element(By.XPATH,"""//*[@id="mobile-nav-search"]""")
link.click()

# Locating search bar
search=driver.find_element(By.XPATH,"""//*[@id="search-input"]""")
# Assigning keyword to use in search
search.send_keys("About")
# Pressing enter
search.send_keys(Keys.ENTER)
sleep(5)

# Locating search results
articles=driver.find_elements(By.XPATH,"""//*[@id="container-7e192f6c4b"]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div""")
sleep(20)

# Placing results in list of strings
about = []

for i in articles:
    about.append(i.text)

driver.close()
print(about)

# Creating single string out of list of strings
about_singlestring = """""".join(about)

## Pre-processing using Regular Expressions: Use-case specific

# Removing HTML 
about_singlestring = re.sub(r'<.*?>','', about_singlestring)
# Removing digits
about_singlestring = re.sub(r'\d+', '', about_singlestring)
# Removing punctuation
about_singlestring = re.sub(r'[^\w\s]', '', about_singlestring)

# The most basic tokenization
about_tokens = about_singlestring.split()

# Setting stopwords to be used in loop
stopWords = set(stopwords.words("english"))

# Creating frequency table to keep score of each word
freqTable = dict()

# Counts only words not in stopword list
for word in about_tokens:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

## Displaying only the most frequently used words

# Calculating sum of word frequencies
sumValues = 0

for word in freqTable:
    sumValues += freqTable[word]

# Calculating average word frequency
average = int(sumValues / len(freqTable))

# Print only most important word calculated by frequency
companyCulture = []

for word in freqTable:
    if freqTable[word] > average:
        companyCulture.append(word)

print(companyCulture)

## We have returned the most significant words in the company culture.
