from urllib.request import urlopen
import re
import datetime # datetime

d = datetime.date.today()
print('\n' + 'Today\'s date is ' + str(d) + '\n')

def riverside_california_us(url):
    # download and decode resource to obtain all lowercase content
    response = urlopen(url)  # open url
    html = response.read()  # read response
    content = html.decode()  # decode content
    result = re.findall(r'class="l3HOY">(.*?)</td>', str(content))  # return all matches
    find_death = str(result)
    # print(find_death)
    print(f"Deaths in Riverside County is {find_death[-5:-2]}")

riverside_california_us('https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0l2q3&gl=US&ceid=US%3Aen')

def san_mateo_california_us(url):
    # download and decode resource to obtain all lowercase content
    response = urlopen(url)  # open url
    html = response.read()  # read response
    content = html.decode()  # decode content
    result = re.findall(r'class="l3HOY">(.*?)</td>', str(content))  # return all matches
    find_death = str(result)
    # print(find_death)
    print(f"Deaths in San Mateo County is {find_death[-5:-2]}")
    print(f"Deaths in California is {find_death[-32:-27]}")
    print(f"Deaths in the U.S. are {find_death[-64:-57]}")
    print(f"Deaths in the World are {find_death[39:46]}" + "\n")

san_mateo_california_us('https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen&mid=%2Fm%2F0l2vz')