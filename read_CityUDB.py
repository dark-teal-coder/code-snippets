# This program requires CityUDB.db file. 
import sqlite3

dbconn = sqlite3.connect("CityUDB.db")
cityudb = dbconn.cursor()

createCourse = "CREATE TABLE Course(\
                CourseNo CHAR(15) NOT NULL PRIMARY KEY,\
                CourseName CHAR(100) NOT NULL,\
                Classroom CHAR(30) NOT NULL,\
                FacultyID INTEGER NOT NULL,\
                Credit INTEGER NOT NULL,\
                FOREIGN KEY(FacultyID) REFERENCES Faculty (FacultyID));"
dropCourse = "DROP TABLE IF EXISTS COURSE;"
cityudb.execute(dropCourse)
cityudb.execute(createCourse)
insertCourse = "INSERT INTO Course (CourseNo, CourseName, Classroom, FacultyID, Credit) VALUES (?, ?, ?, ?, ?);"
insertValue = ['CB2021', 'Big Data Management', 'AC3-146', 1, 2]
cityudb.execute(insertCourse, insertValue)
insertTable = "INSERT INTO Course (CourseNo, CourseName, Classroom, FacultyID, Credit) VALUES (?, ?, ?, ?, ?);"
insertMultiRows = [['IS2240', 'Python Programming', 'AC3-359', 7, 3],
                   ['CB2023', 'Mobile Application', 'AC3-125', 3, 1],
                   ['CB2500', 'Information MGMT', 'AC3-37', 5, 2]]
cityudb.executemany(insertTable, insertMultiRows)
insertTable = "INSERT INTO Course (CourseNo, CourseName, Classroom, FacultyID, Credit) VALUES (?, ?, ?, ?, ?);"
insertData = []
insertFile = open("Course.csv", "r")
for row in insertFile:
    insertData = row.split(',')
    cityudb.execute(insertTable, insertData)
updateTable = "UPDATE Course SET Classroom = ?, FacultyID =? WHERE CourseNo =?;"
updateData = ['AC3-6-209', 14, 'IS2240']
cityudb.execute(updateTable, updateData)
deleteCourse = "DELETE FROM Course WHERE CourseNo = ?;"
deleteData = ['CB2555']
cityudb.execute(deleteCourse, deleteData)
selectCourse = "SELECT CourseNo, CourseName, Classroom, Credit FROM Course WHERE Credit >= ? AND Classroom LIKE ?;"
conData = [2, "%AC%"]
rows = cityudb.execute(selectCourse, conData).fetchall()
for course in rows:
    print(course)
dbconn.commit()
dbconn.close()

# print("This program shows min., max. and average.")
# num = -2
# while num < 0:
#     num = eval(input("Enter a non-negative number: "))
# count = 0
# total = 0
# min = num
# max = num
# while num >= 0:
#     if num < min:
#         min = num
#     if num > max:
#         max = num
#     num = eval(input("Enter a non-negative number or -1 to terminate: "))
#     if num == -1:
#         break
#     total += num
#     count += 1
# print("Average:", total/count)
# print("Min.:", min)
# print("Max.:", max)

# count = 0
# total = 0
# print("Enter -1 to terminate entering numbers.")
# num = eval(input("Enter a non-negative number: "))
# min = num
# max = num
# while num != -1:
#     count += 1
#     total += num
#     if num < min:
#         min = num
#     elif num > max:
#         max = num
#     num = eval(input("Enter a non-negative number: "))
# if count > 0:
#     print("Average:", total/count)
#     print("Min.:", min)
#     print("Max.:", max)
# else:
#     print("No non-negative no. found.")

