import requests
from bs4 import BeautifulSoup

book = "John"
chapter = "05"
booknum = ""
as_array = True
string_array = []
full_string = ""
# Making a GET request
r = requests.get('https://www.biblegateway.com/passage/?search='+booknum+'%20'+book+'%2'+chapter+'&version=KJV')


# check status code for response received
# success code - 200
print(r)

def remove_tags(html):
    soup = BeautifulSoup(html, 'html.parser')
    s = soup.find('div', class_='passage-text')
    #content = s.find_all('p')
    #for data in s(['span', 'sup']):
        
        
    # Remove tags
        #print(data)

    # return data by retrieving the tag content
    for string in  s.stripped_strings:
        string_array.append(string)
    return ' '.join(s.stripped_strings)

# print content of request
full_string = remove_tags(r.content)
remove_tags(r.content)
print(string_array)
f = open((booknum+book+chapter+".txt"), "a")
if as_array == True:
    f.write(str(string_array))
else:
    f.write(full_string)
f.close()
