# enter fanfiction link and scrape the story from the page 
# import the needed functions 
from fanfiction_read import read as fanfiction_read 
from ao3_read import read as ao3_read
import os 


# use a conditional statement to ask the user what site the link came from
site = input("What site is the link from 'ao3' or 'fanfiction.net': " ).strip()

# remove fic file 
path = 'file path name/Desktop/fics/new_story.txt'
if os.path.exists(path):
    os.remove(path)

if(site == "ao3"):
    fic = ao3_read()

if(site == "fanfiction"):
   fic = fanfiction_read() 


