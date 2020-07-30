import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
print(soup.body.contents) # gives the entire html content of the page
print(soup.find_all('div'))  # gives a list of all the div's on the page
print(soup.title)  # <title>Hacker News</title>
print(soup.a)  # gives first <a> tag on the page
print(soup.find(id='score_23995750'))  # <span class="score" id="score_23995750">1364 points</span>
print(soup.select('.score'))  # grabs all the span tags with class '.score'
print(soup.select('#score_23995750'))  # grabs all the span tags with id 'score_23995750'

links = soup.select('.storylink')
votes = soup.select('.score')
print(votes[0])  # <span class="score" id="score_23999542">181 points</span>
votes.get('id')  # score_23999542
