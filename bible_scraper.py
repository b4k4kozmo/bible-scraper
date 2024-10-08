import requests
from bs4 import BeautifulSoup

book = "John"
chapter = "203"
string_array = []
# Making a GET request
r = requests.get('https://www.biblegateway.com/passage/?search='+book+'%'+chapter+'&version=KJV')


# check status code for response received
# success code - 200
print(r)

def remove_tags(html):
    soup = BeautifulSoup(html, 'html.parser')
    s = soup.find('div', class_='passage-text')
    content = s.find_all('p')
    #for data in s(['span', 'sup']):
        
        
    # Remove tags
        #print(data)

    # return data by retrieving the tag content
    for string in  s.stripped_strings:
        string_array.append(string)

# print content of request
remove_tags(r.content)
print(string_array)
f = open((book+chapter+".txt"), "a")
f.write(str(string_array))
f.close()
