class Film:
    def __init__(self, film_name, release_year, rating, revenue, budget, duration, url, cur, conn):
        self.name = film_name
        self.release_year = release_year
        self.rating = rating
        self.revenue = revenue
        self.budget = budget
        self.duration = duration
        self.url = url
        self.cur = cur
        self.conn = conn

    def insert_data_if_not_exists(self):
        self.cur.execute('SELECT * FROM film WHERE film_name = %s', (self.name))
        if self.cur.rowcount == 0:
            self.cur.execute(
                'INSERT INTO film (film_name, rating, revenue, budget, duration, url, release_year) VALUES (%s,%s,%s,%s,%s,%s,%s)',
                (self.name, self.rating, self.revenue, self.budget, self.duration, self.url, self.release_year))
            self.conn.commit()


class Directors:
    def __init__(self, film_title, director_dict, cur, conn):
        self.dict = director_dict
        self.cur = cur
        self.conn = conn
        self.film_title = film_title

    def insert_data_if_not_exists(self):
        for name in self.dict:
            self.cur.execute('SELECT id FROM film WHERE film_name = %s ', (self.film_title))
            self.conn.commit()
            film_id = self.cur.fetchone()
            self.cur.execute('INSERT INTO directors (director_name,url) VALUES (%s,%s)', (name, self.dict[name]))
            self.conn.commit()
            self.cur.execute('SELECT * FROM direct WHERE film_id = %s', (film_id))
            self.conn.commit()
            if self.cur.rowcount == 0:
                self.cur.execute('SELECT id FROM directors WHERE director_name=%s', (name))
                self.conn.commit()
                director_id = self.cur.fetchone()
                self.cur.execute('INSERT INTO direct (director_id, film_id) VALUES (%s, %s)', (director_id, film_id))
                self.conn.commit()


class Writer:
    def __init__(self, film_title, writer_dict, cur, conn):
        self.writer_dict = writer_dict
        self.cur = cur
        self.conn = conn
        self.film_title = film_title

    def insert_data_if_not_exists(self):
        for name in self.writer_dict:
            self.cur.execute('SELECT id FROM film WHERE film_name = %s ', (self.film_title))
            self.conn.commit()
            film_id = self.cur.fetchone()
            self.cur.execute('INSERT INTO writer (writer_name,url) VALUES (%s,%s)', (name, self.writer_dict[name]))
            self.conn.commit()
            self.cur.execute('SELECT * FROM writing WHERE film_id = %s', (film_id))
            self.conn.commit()
            if self.cur.rowcount == 0:
                self.cur.execute('SELECT id FROM writer WHERE writer_name=%s', (name))
                self.conn.commit()
                writer_id = self.cur.fetchone()
                self.cur.execute('INSERT INTO writing (writer_id, film_id) VALUES (%s, %s)', (writer_id, film_id))
                self.conn.commit()

class Actor:
    def __init__(self, film_title, actor_dict, cur, conn):
        self.film_title = film_title
        self.actor_dict = actor_dict
        self.cur = cur
        self.conn = conn

    def insert_data_if_not_exists(self):
        for name in self.actor_dict:
            self.cur.execute('SELECT id FROM film WHERE film_name = %s ', (self.film_title))
            self.conn.commit()
            film_id = self.cur.fetchone()
            self.cur.execute('INSERT INTO actors (actor_name,url) VALUES (%s,%s)', (name, self.actor_dict[name]))
            self.conn.commit()
            self.cur.execute('SELECT id FROM actors WHERE actor_name=%s', (name))
            self.conn.commit()
            actor_id = self.cur.fetchone()
            self.cur.execute('SELECT * FROM act WHERE actor_id = %s', (actor_id))
            self.conn.commit()
            if self.cur.rowcount == 0:
                self.cur.execute('INSERT INTO act (actor_id, film_id) VALUES (%s, %s)', (actor_id, film_id))
                self.conn.commit()
