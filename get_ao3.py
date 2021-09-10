# web scrape from my ao3 bookmarks page and get the information of specific fics 
# import requests and BeautifulSoup
from bs4 import BeautifulSoup
import requests

# my ao3 bookmarks update page 
source = requests.get("ao3 url").text

soup = BeautifulSoup(source, 'lxml')
ol = soup.find('ol', class_='bookmark index group')

# open document that contains the names of fanfiction stories 
filename = "file pathname"
with open(filename) as names: 
    fic_names = names.read()
# Turn fic_names into a list for conditional test
fanfiction = fic_names.split('\n')

def get_stories(list_name):
    """Print out information about the stories names in the opened document"""
    for x in ol.find_all('li', class_='bookmark blurb group'):
        # if there is an TypeError the code keeps executing 
        try: 
            # story names 
            name = x.div.h4.a.text
            # story summaries 
            summary = x.find('blockquote', class_='userstuff summary').text
            # chapter number 
            chapter_link = x.find('dd', class_='chapters')
            # latest chapter link 
            # latest_chapter = x.div.h4.a['href']
            latest_chapter = chapter_link.a['href']

            if (name in fanfiction): 
                # story main relationship 
                people = x.find('li', class_='relationships').text
            # add the new update information into a seperate file 
                filename = 'file path name '
                with open(filename, 'a') as new_file: 
                    new_file.write(f"{'-' * 50}\n{name}\n{people}\n{summary}\n{chapter_link.text}\nhttps://archiveofourown.org{latest_chapter}\n") 
        except TypeError:
            pass





            

