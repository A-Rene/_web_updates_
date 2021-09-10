# get the story text and read the fics on my computer | import bs4, requests, and os
from bs4 import BeautifulSoup
import requests 
import os 
# make a function that gets the story 
def read(): 
    """Save fanfiction stories from fanfiction.net to my computer  """
# get user input for the url
    url = input("Url of the story that you want to read: \n")
    #requesting the page 
    page = requests.get(url).text
    soup = BeautifulSoup(page,'lxml')

    # get the title of the selected story 
    title = soup.find('b', class_="xcontrast_txt").text

    # get the 
    fic = soup.find('div', class_='storytext xcontrast_txt nocopy')

    # get the chapter for the story using the URL
    get_chapter = url.split('/')
    get_chapter = url.split('/')
    chapter = get_chapter[5]

    # create and name the file, and write the title
    filename = f'file path name /fanfiction_net/{title}_{chapter.strip()}.txt'

    # open the file write the story title to it 
    with open(filename, 'w') as new:
        new.write(f"{title}\n{'-' * 250}")
# for loop to get all the p tags on the page 
    for p in fic.find_all('p'):
        string = p.text
        text_change = string.split('\n')
        # open the document that will contain the fics 
        with open(filename, 'a') as new_file:
            for line in text_change:     
                new_file.write(f"\n{line}")

    # if I want to format open atom and use regular expressions 
    format = input("Do I want to format this story?   ")
    if(format.strip().lower() == 'yes'):
        os.system(f"open '{filename}' -a 'Sublime Text'")
    





# make a new text file and set up a naming convention 
