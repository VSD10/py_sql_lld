import mysql.connector

def safe_input(p,c):
	try:
		while True:
			val=c(input(p))
			return val
	except:
		print("Enter a right data type ")

def getcon():
	con=mysql.connector.connect(
		host="localhost",
		user="root",
		password="#Harinisri2012",
		database="university_db"

	)
	if con:
		return con
	else:
		print("Not connected")
		return



def main():
	while True:
		data='''
Main menu:

1. Add student
2. Add course
3. Enroll Student in course
4. Add Assignment Marks
5. Calculate Gpa for a student
6. View student enrollment (join)
7. View course roster
8. Drop a course
9. Exit
'''
		print(data)
		choice=safe_input("Enter a choice : ",int)
		if choice==1:
			addstudent()
		elif choice == 2:
			addcourse()
		elif choice ==3:
			enroll()
		elif choice ==4:
			addmark()
		elif choice==5:
			cal()
		elif choice==6:
			view()
		elif choice==7:
			viewcourse()
		elif choice==8:
			drop()
		elif choice==9:
			print("bye")
			return
		else:
			print("Choose between 1 to 9")

def addstudent():
	con=getcon()
	if not con:
		return
	try:
		cursor=con.cursor()
		name=safe_input("Enter a name : ",str)
		email=safe_input("Enter a email : ",str)
		year=safe_input("Enter a year : ",int)
		major =safe_input("Enter amajor : ",str)
		data=(name,email,year,major)
		sql="insert into students(name,email,year,major) values(%s,%s,%s,%s)"
		cursor.execute(sql,data)
		con.commit()
		print("inserted")
	except:
		print("Not inserted")
	finally:
		try:
			cursor.close()
			con.close()
		except:
			pass		
		
def addcourse():
	con=getcon()
	if not con:
		return
	try:
		cursor=con.cursor()
		course_name=safe_input("Enter a course_name : ",str)
		department=safe_input("Enter a department : ",str)
		credit=safe_input("Enter a credit : ",int)
		capacity =safe_input("Enter a capacity : ",int)
		data=(course_name,department,credit,capacity)
		sql="insert into courses(course_name,department,credits,capacity) values(%s,%s,%s,%s)"
		cursor.execute(sql,data)
		con.commit()
		print("inserted")
	except:
		print("Not inserted")
	finally:
		try:
			cursor.close()
			con.close()
		except:
			pass		
		
def enroll():
	con=getcon()
	if not con:
		return
	try:
		cursor=con.cursor()
		student_id=safe_input("Enter a Id: ",int)
		print("Checking the student Id..")
		cursor.execute("select * from students where student_id=%s",(student_id,))
		s1=cursor.fetchone()
		if s1:
			print("ID found")
		else:
			print("Id not found")
			return
		course_id=safe_input("Enter a course Id: ",int)
		print("checking the course id....")
		cursor.execute("Select * from courses where course_id=%s",(course_id,))
		s2=cursor.fetchone()
		if s2:
			print("course found")
		else:
			print("course not found")
			return
		print("Checking the vacancy..")
		cursor.execute("Select count(*) from enrollments where status=%s and  course_id=%s",("Active",course_id))
		s3=cursor.fetchone()
		print(s2[3],s3[0])
		if s2[4]>s3[0]:
			print("The Seats are available")
		else:
			print("The Seats are filled ")
			return
		print("Checking the studne already enrolled or not...")
		cursor.execute("Select * from enrollments where student_id=%s and status=%s",(student_id,"Inactive"))
		s4=cursor.fetchone()
		if not s4 :
			print("Your not enrolled any courses...")
		else:
			print("you already enrolled in course  ",s4)
			return
		print("your course are enrolling on process.....")
		cursor.execute("insert into enrollments(student_id,course_id,enroll_date,status) values(%s,%s,%s,%s)",(student_id,course_id,"2025-12-12","Active"))
		con.commit()
		print("Course enrolled successfully......")
	except Exception as e:
		print(e)
	finally:
		try:
			cursor.close()
			con.close()
		except:
			pass

def addmark():
	con=getcon()
	if not con:
		return
	try:
		cursor=con.cursor()
		enroll_id=safe_input("Enter a Id",int)
		print("Checking the  id....")
		cursor.execute("Select * from enrollments where enroll_id=%s and status=%s",(enroll_id,'Active'))
		r=cursor.fetchone()
		if r:
			print("Student exists")
		else:
			print("Student not exists")
			return
		assignment_name=safe_input("Enter a assignment name : ",str)
		mark=safe_input("Enter a mark : ",int)
		grade_map = {
			(90, 100): "A",
			(80, 89):  "B",
			(70, 79):  "C",
			(60, 69):  "D",
			(0, 59):   "F"
		}
		grade=0
		for (s,e),g in grade_map.items():
			if s<=mark<=e:
				grade=g
				break
			else:
				print("Enter a valid mark")
		cursor.execute("insert into grades(enroll_id,assignment_name,marks,grade)values(%s,%s,%s,%s)",(enroll_id,assignment_name,mark,grade))
		con.commit()
		print("grade inserted sucessfully")
	except Exception as e:
		print(e)
	finally:
		try:
			cursor.close()
			con.close()
		except:
			pass

def view():
	con=getcon()
	if not con:
		return
	try:
		cursor=con.cursor()
		sql='''
		select     from students s 
		join enrollments e on s.student_id=e.student_id  
		join courses c on c.course_id,e.course_id
		'''
		cursor.execute(sql)
		con.commit()
		print("inserted")
	except:
		print("Not inserted")
	finally:
		try:
			cursor.close()
			con.close()
		except:
			pass	

if __name__=="__main__":
	main()
















# def createdb():
# 	con=mysql.connector.connect(
# 	host="localhost",
# 	user="root",
# 	password="#Harinisri2012"
# 			)	
# 	if not con:
# 		print("db not connected")
# 		return
# 	cursor=con.cursor()
# 	cursor.execute("create database if not exists university_db")
# 	con.commit()
# 	print("db created")



# def createtable():
# 	con=mysql.connector.connect(
# 	host="localhost",
# 	user="root",
# 	password="#Harinisri2012",
# 	database="university_db"
# 					)
# 	if not con:
# 		print("db not connected")
# 		return
# 	cursor=con.cursor()
# 	sql1='''create table if not exists students(
# 	student_id int primary key auto_increment,
# 	 name varchar(50) , 	
# 	email varchar(50),
# 	year int,
# 	major varchar(50))'''

# 	cursor.execute(sql1)

# 	sql2='''create table if not exists courses (
# 	course_id int primary key auto_increment, 
# 	course_name varchar(100),
# 	department varchar(50), 
# 	credits int,
# 	 capacity int)'''

# 	cursor.execute(sql2)
	
# 	sql3='''create table if not exists enrollments(enroll_id int primary key auto_increment,student_id int, course_id int,enroll_date date, status varchar(20))'''
# 	cursor.execute(sql3)

# 	print("table created")




# createdb()
# createtable()