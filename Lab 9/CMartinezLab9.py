###########################################################################
# Program Header
# Course: CIS 117 Python Programming
# Name: Cuauhtemoc Alex Martinez
# Description: Lab 9
# Application: Python WWW API
# Topics: Web and Search
# Development Environment: Windows 10
# Version: Python 3.8.2
# Solution File: CMartinezLab9
# Due date: 04/14/20
###########################################################################

# Program Source Statements


from urllib.request import urlopen
import re
import datetime # datetime

d = datetime.date.today()
print('Today\'s date is ' + str(d))


def word_string(url):
    '''counts in resource with URL url the frequency
       of each topic in list topics'''
    # download and decode resource to obtain all lowercase content
    response = urlopen(url)  # open url
    html = response.read()  # read response
    content = html.decode()  # decode content and make lowercase
    result = re.findall(r'<td class="l3HOY" aria-label="No data"><span class="EtcnFb">No data</span></td><td class="l3HOY">(.*?)</td>', str(content))  # return all matches
    find_death = str(result)
    print("Total Deaths in San Mateo is " + find_death[-5:-2])
    # for topic in topics:  # find frequency of topic in result
    #     n = find_death.count(topic)
    #     if n == 1:  # if topic equals one, make singular
    #         print('{} appears {} time.'.format(topic, n))
    #     else:  # if topic equals more than one, make plural
    #         print('{} appears {} times.'.format(topic, n))
    
word_string('https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen&mid=%2Fm%2F0l2vz')

##<td class="l3HOY">28</td>
# Program Output

""""
Today's date is 2020-04-14
research appears 4 times.
climate appears 1 time.
evolution appears 1 time.
cultural appears 3 times.
leadership appears 2 times.
gene appears 3 times.
"""
