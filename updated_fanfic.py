# import functions from get_ao3.py and fanfiction.py 
from fanfiction import get_information 
from get_ao3 import get_stories
# module handles files 
import os 

# open ao3_stories.txt and make a list and use in imported functions 
filename = 'file path name /python/projects/web_scrape/fics.txt'

with open(filename) as new_file:
    lines = new_file.read()

fanfiction_names = lines.split('\n')

# delete old text file so it is not cluttered 
file_name = 'file path name /Desktop/new_updates.txt'
if os.path.exists(file_name):
    os.remove(file_name)

#check fanfiction.net
get_information(fanfiction_names)

# check archiveofourown.org
get_stories(fanfiction_names)

# open the file so I won't have to manually do it 
os.system("open file path name /new_updates.txt")



"""
path names for the imported functions if needed 
file path name/Desktop/python/projects/web_scrape/
file path name /Desktop/python/projects/web_scrape/
"""
