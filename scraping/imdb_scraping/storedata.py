import pymysql
import requests
from bs4 import BeautifulSoup
from imdb_scraping.entities import *


def get_bs(url, header):
    html = requests.get(url, headers=header)
    bs = BeautifulSoup(html.content, 'html.parser')
    return bs


def get_film_detailes(url, headers):
    bs_film = get_bs(url, headers)
    film_details = []
    for item in ['Cumulative Worldwide Gross:', 'Budget:', 'Runtime:']:
        info = bs_film.find('h4', attrs={'class': 'inline'}, string=item).parent.get_text()
        info = info.replace(item, '').replace('$', '')
        info = info.replace(',', '').strip()
        if item == 'Budget:':
            info = info.replace('(estimated)', '').strip()
        if item == 'Runtime:':
            info = info[0:3].strip()
        film_details.append(info)
    return film_details, bs_film


def store_film_info(row, domain, headers, cur, conn):
    rank_and_title = row.find('td', {'class': 'titleColumn'})
    film_title = rank_and_title.find('a').text
    release_year = rank_and_title.find('span', {'class': 'secondaryInfo'}).text.replace('(', '').replace(')', '')
    film_rating = row.find('td', {'class': 'ratingColumn imdbRating'}).find('strong').text
    film_page_relative_url = row.find('td', {'class': 'titleColumn'}).find('a')['href']
    film_page_url = str(f'{domain}{film_page_relative_url}')
    [film_revenue, film_budget, film_duration], bs_film = get_film_detailes(film_page_url, headers)
    film = Film(film_title, release_year, film_rating, film_revenue, film_budget, film_duration, film_page_url, cur,
                conn)
    film.insert_data_if_not_exists()
    return bs_film, film_page_url, film_title


def get_directors_info(bs_cast_and_crew):
    directors = bs_cast_and_crew.find('table', {'class': 'simpleTable simpleCreditsTable'}).find('td', {
        'class': 'name'}).find_all('a')
    director_name = [name.text.strip() for name in directors]
    director_url = [domain + name['href'] for name in directors]
    director_dict = dict(zip(director_name, director_url))
    return director_dict


def store_directors_info(film_title, bs_cast_and_crew, cur, conn):
    director_dict = get_directors_info(bs_cast_and_crew)
    director = Directors(film_title, director_dict, cur, conn)
    director.insert_data_if_not_exists()


def get_cast_and_crew(bs_film, film_page_url):
    full_cast_and_crew_url = bs_film.find('a', string='See full cast & crew')['href']
    full_cast_and_crew_url = film_page_url[:36] + full_cast_and_crew_url
    bs_cast_and_crew = get_bs(full_cast_and_crew_url, headers)
    return bs_cast_and_crew


def get_writer_info(bs_cast_and_crew):
    writers = bs_cast_and_crew.find_all('table', {'class': 'simpleTable simpleCreditsTable'})[1].find_all('tr')
    writers_name = []
    writers_url = []
    for writer in writers:
        if writer.find('td', {'class': 'name'}):
            writers_name.append(writer.find('a').text.rstrip())
            writers_url.append(domain + writer.find('a')['href'])
    writer_dict = dict(zip(writers_name, writers_url))
    return writer_dict


def store_writer_info(bs_cast_and_crew, film_title, cur, conn):
    writer_dict = get_directors_info(bs_cast_and_crew)
    writer = Writer(film_title, writer_dict, cur, conn)
    writer.insert_data_if_not_exists()


def get_actors_info(bs_cast_and_crew):
    actors_name = []
    actors_url = []
    actors_table = bs_cast_and_crew.find('table', {'class': 'cast_list'})
    for actor in actors_table.find_all('tr')[1:]:
        for td in actor.find_all('td')[1:]:
            if td.find('a'):
                actors_name.append(td.find('a').text.rstrip())
                actors_url.append(domain + td.find('a')['href'])
    actor_dict = dict(zip(actors_name, actors_url))
    return actor_dict


def store_actors_if_not_exists(bs_cast_and_crew, film_title, cur, conn):
    actor_dict = get_actors_info(bs_cast_and_crew)
    actor = Actor(film_title, actor_dict, cur, conn)
    actor.insert_data_if_not_exists()


conn = pymysql.connect(host='localhost', user='root', database='imdb_scraping', passwd='XXXXXX')
cur = conn.cursor()
cur.execute("USE imdb_scraping;")
conn.commit()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
domain = 'http://www.imdb.com'
top_rated_movies = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
bs_top_rated_movies = get_bs(top_rated_movies, headers)

table = bs_top_rated_movies.find('tbody', {"class": "lister-list"})
rows = table.find_all('tr')

for row in rows[:5]:
    bs_film, film_page_url, film_title = store_film_info(row, domain, headers, cur, conn)
    bs_cast_and_crew = get_cast_and_crew(bs_film, film_page_url)
    store_directors_info(film_title, bs_cast_and_crew, cur, conn)
    store_writer_info(bs_cast_and_crew, film_title, cur, conn)
    store_actors_if_not_exists(bs_cast_and_crew, film_title, cur, conn)






