# get the story text and read the fics on my computer | import bs4, requests, and os
from bs4 import BeautifulSoup
import requests
import os

def read():
    """Save fanfiction stories from archiveofourown.org to my computer """
   # get user input for the url
    url = input("Url of the story that you want to read: \n")

    #requesting the page
    page = requests.get(url).text
    soup = BeautifulSoup(page,'lxml')

    # get the title of the selected story
    title = soup.find('h2', class_='title heading').text

    # get chapter
    chapter = soup.find('h3',class_="title" )
    chapter = chapter.a.text

    # open a text tile write the story name
    filename = f'path name /ao3/{title.strip()}_{chapter}.txt'
    with open(filename, 'w') as new:
        new.write(f"{title}\n{'-' * 250}")

    #pin pointing the location of the p tags that contain the actual story
    p_tags = soup.find('div', class_='userstuff module')
    # loops through all the p tags on the page
    for text in p_tags.find_all('p'):
    # prints out the response
        string = text.text
    # put the p tags in a list
        text_change = string.split('\n')

        with open(filename, 'a') as new:
    # append each p tage to the file
            for line in text_change:
                new.write(f"\n{line}")

    # if I want to format open atom and use regular expressions
    format = input("Do I want to format this story?   ")
    if(format.strip().lower() == 'yes'):
        os.system(f"open '{filename}' -a 'Sublime Text'")

# make a new text file and set up a naming convention
read()
