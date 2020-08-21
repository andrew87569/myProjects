from bs4 import BeautifulSoup
import requests

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

full_text = []

for paragraph in soup.find_all('p'):
    paragraph = paragraph.string
    if paragraph == None:
        continue
    else:
        full_text.append(paragraph)

full_text = " ".join(full_text)

# Take the code from the How To Decode A Website exercise, and instead of printing the results to a screen,
# write the results to a txt file. In your code, just make up a name for the file you are saving to.

# Extras:
# - Ask the user to specify the name of the output file that will be saved.

with open(input("Name of output file: ")+'.txt','w',encoding="UTF-8") as f:
    f.write(full_text)
    f.close()
