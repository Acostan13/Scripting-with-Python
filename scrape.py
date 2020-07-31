import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body.contents) # gives the entire html content of the page
# print(soup.find_all('div'))  # gives a list of all the div's on the page
# print(soup.title)  # <title>Hacker News</title>
# print(soup.a)  # gives first <a> tag on the page
# print(soup.find(id='score_23995750'))  # <span class="score" id="score_23995750">1364 points</span>
# print(soup.select('.score'))  # grabs all the span tags with class '.score'
# print(soup.select('#score_23995750'))  # grabs all the span tags with id 'score_23995750'

links = soup.select('.storylink')
subtext = soup.select('.subtext')
print(subtext[0])  # <span class="score" id="score_23999542">181 points</span>
subtext[0].get('id')  # score_23999542


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda key: key['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for ind, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[ind].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                # print(points)
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtext))  # displays all the links on the page

