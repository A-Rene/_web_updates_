# web scrape from my fanfiction bookmarks page and get the information of specific fics
from bs4 import BeautifulSoup
import requests

#requesting my updated fanfiction.net page
source = requests.get('fanfiction.net url ').text

soup = BeautifulSoup(source,'lxml')

# open document that contains the names of fanfiction stories
filename =  "file path name /Desktop/python/projects/web_scrape/fics.txt"
with open(filename) as names:
    fic_names = names.read()
# Turn fic_names into a list for conditional test
fanfiction = fic_names.split('\n')

def get_information(list_name):
    """Print out information about the stories names in the opened document"""
    num = 0
    # search the first 120 bookmarks 
    for story in soup.find_all('div', class_='z-list favstories'):
        if (num <= 120):
            # if there is a KeyError to code keeps executing
            try:
                # Story name
                name = story.find('a', class_='stitle').text
                # chapter link for the latest story
                link = story.span.parent['href']
                # link = story.span.parent['href']
                # story summary
                summary = story.find('div', class_='z-indent z-padtop').text

                num += 1

            # conditional test to get specific stories
                if(name in fanfiction):
            # add the new update information into a seperate file
                    filename = 'file path name /Desktop/new_updates.txt'
                    with open(filename, 'a') as new:
                        new.write(f"{'-' * 50}\n{name}\n\n{summary}\n\nhttps://www.fanfiction.net{link}\n\n")
            except KeyError:
                pass
