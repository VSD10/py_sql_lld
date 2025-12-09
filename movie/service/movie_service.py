from models.movie import movie
from db.db import get_connection
from tabulate import tabulate

class movie_service:
    def __init__(self):
        self.con = get_connection()

    def add_movie(self):
        if not self.con:
            return
        try:
            cursor = self.con.cursor()
            id = int(input("enter director id"))
            print("checking the director id and status")
            sql = "select status from directors where director_id=%s and status='Active'"
            cursor.execute(sql, (id,))
            data = cursor.fetchone()
            if not data:
                print("id not exists")
                return
            print("id exists")
            title = input("enter movie title")
            genre = input("enter movie genre")
            release_year = int(input("enter movie release year"))
            budget = int(input("enter movie budget"))
            data = movie(None, title, genre, release_year, budget, id)
            sql = "insert into movies(title,genre,release_year,budget,director_id) values(%s,%s,%s,%s,%s)"
            cursor.execute(sql, data.to_tuple())
            self.con.commit()
            print("movie added successfully")
        except Exception as e:
            print(e)
        finally:
            if cursor:
                cursor.close()

    def view_movies(self):
        if not self.con:
            return
        try:
            cursor = self.con.cursor()
            sql = "select m.movie_id, m.title, m.genre, m.release_year,m.budget, d.name as director from movies m join directors d on m.director_id=d.director_id"
            cursor.execute(sql)
            data = cursor.fetchall()
            print(tabulate(data))
        except Exception as e:
            print(e)
        finally:
            if cursor:
                cursor.close()

    def update_movie_director(self):
        if not self.con:
            return
        try:
            cursor = self.con.cursor()
            id = int(input("enter director id "))
            print("checking the id is presne and active")
            cursor.execute(
                "Select * from directors where director_id=%s and status='Active'",
                (id,),
            )
            r = cursor.fetchone()
            if r:
                print("id present")
            else:
                print("id not present")
                return
            movie_id = int(input("enter movie id"))
            cursor.execute(
                "Select * from movies where movie_id=%s and status='Active'", (movie_id,)
            )
            r = cursor.fetchone()
            if r:
                print("movie id present")
            else:
                print("movie id not present")
                return
            cursor.execute(
                "update movies set director_id=%s where movie_id=%s", (id, movie_id)
            )
            self.con.commit()
            print("director updated successfully ")
        except Exception as e:
            print(e)
        finally:
            if cursor:
                cursor.close()