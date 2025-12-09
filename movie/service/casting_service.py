from db.db import get_connection
from models.casting import castings
from tabulate import tabulate

class casting_service():
    def __init__(self):
        self.con = get_connection()

    def add_cast(self):
        if not self.con:
            return
        try:
            cursor = self.con.cursor()
            movie_id = int(input("Enter a movie id: "))
            print("checking the moviee id")
            cursor.execute("select * from movies where movie_id=%s", (movie_id,))
            r = cursor.fetchone()
            if not r:
                print("movie not exists")
                return
            else:
                print("movie exists")
            actor_name = input("enter a actor name :")
            print("checking the actor status")
            cursor.execute("select status from castings where actor_name=%s", (actor_name,))
            r = cursor.fetchone()
            if r and r[0] == "Signed":
                print("actor cant be signed because of already commited")
                return
            else:
                print("actor can be signed")
            role_name = input("enter a role name :")
            salary = int(input("enter a salary :"))
            data = castings(movie_id, actor_name, role_name, salary, "Signed")
            cursor.execute("insert into castings(movie_id,actor_name,role_name,salary,status) values(%s,%s,%s,%s,%s)", data.to_tuple())
            self.con.commit()
            print("inserted successfully")
        except Exception as e:
            print(e)
        finally:
            if cursor:
                cursor.close()

    def view_cast(self):
        if not self.con:
            return
        try:
            cursor = self.con.cursor()
            sql = "select c.cast_id,c.actor_name,c.role_name,c.salary,c.status from castings c join movies m on c.movie_id=m.movie_id where m.movie_id=%s"
            movie_id = int(input("enter a movie id :"))
            cursor.execute(sql, (movie_id,))
            r = cursor.fetchall()
            print(tabulate(r))
        except Exception as e:
            print(e)
        finally:
            if cursor:
                cursor.close()

    def update_cast(self):
        if not self.con:
            return
        try:
            cursor = self.con.cursor()
            movie_id = int(input("enter a movie id :"))
            cursor.execute("select * from castings where movie_id=%s and status='Active'", (movie_id,))
            r = cursor.fetchone()
            if not r:
                print("not available")
            cursor.execute("update castings set status='Signed' where movie_id=%s", (movie_id,))
            self.con.commit()
            print("updated successfully")
        except Exception as e:
            print(e)
        finally:
            if cursor:
                cursor.close()
    