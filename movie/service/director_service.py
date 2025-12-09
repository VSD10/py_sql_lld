from models.director import director
from db.db import get_connection


class director_service:
    def __init__(self):
        self.con=get_connection()
    def add_director(self):
        
        if not self.con:
            return 
        try:
            cursor=self.con.cursor()
            name=input("enter director name")
            email=input("enter director email")
            experience=int(input("enter director experience"))
            status=input("enter director status")
            data=director(name,email,experience,status)
            sql="insert into directors(name,email,experience,status) values(%s,%s,%s,%s)"
            cursor.execute(sql,data.to_tuple())
            self.con.commit()
            print("director added successfully")
        except Exception as e:
            print(e)
        finally:
            try:
                self.con.close()
                cursor.close()
            except:
                pass

