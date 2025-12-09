import mysql.connector


def createdb():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="#Harinisri2012"
    )
    cursor=con.cursor()
    cursor.execute("create database if not exists movie_db")
    con.commit()
    print("Database created successfully")


def createtable():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="#Harinisri2012",
        database="movie_db"
    )
    cursor=con.cursor()
    s1='''create table  if not exists directors (
    director_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    email VARCHAR(50),
    experience INT ,
    status VARCHAR(20) )
'''
    cursor.execute(s1)
    cursor=con.cursor()
    s2='''create table  if not exists movies ( movie_id        INT PRIMARY KEY AUTO_INCREMENT,
title           VARCHAR(100),
genre           VARCHAR(50),
release_year    INT,
budget          INT,
director_id     INT
)
'''
    cursor.execute(s2)
    s3='''create table  if not exists castings (cast_id         INT PRIMARY KEY AUTO_INCREMENT,
movie_id        INT,
actor_name      VARCHAR(50),
role_name       VARCHAR(50),
salary          INT,
status          VARCHAR(20) 
)

'''
    cursor.execute(s3)


    con.commit()
    print("table created successfully")
     
# createdb()
# createtable()

def get_connection():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="#Harinisri2012",
        database="movie_db"
    )
    if con:
        return con
    else:
        print("error while connecting")
        return None
