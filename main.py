import requests
from bs4 import BeautifulSoup 
import html

# response = requests.get(url='https://news.ycombinator.com/')

# soup = BeautifulSoup(response.text, 'html.parser')

# article_titles = soup.find_all(name='span', class_='titleline')
# for article_title in article_titles:
# 	print(article_title.a.get('href'))
# 	print(article_title.a.getText())


response = requests.get(url='https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')

soup = BeautifulSoup(response.text, 'html.parser')

all_titles = soup.find_all(name='h3', class_='title')

movies_titles = [movies.getText() for movies in all_titles]

movies = movies_titles[::-1]
for movie in movies:
	with open('files.txt', 'a', encoding='utf-8') as file:
		file.write(f'{movie}\n')



