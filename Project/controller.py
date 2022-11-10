import mysql.connector


class MySql:
    host = "localhost"
    user = "root"
    password = "sanjeev266"
    database = "ansrone"
    student_table = "students"

    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host=self.host, user=self.user, password=self.password
            )
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute(
                f"CREATE DATABASE IF NOT EXISTS {self.database}"
            )
            self.mycursor.execute(f"USE {self.database}")
        except Exception as e:
            return {"success": False, "error": e}

    def student_register(self, fname, lname, class_, username, sec_ques, answer, password):
        try:
            self.mycursor.execute(
                f"CREATE TABLE IF NOT EXISTS {self.student_table} (username VARCHAR(100) PRIMARY KEY, fname VARCHAR(100) NOT NULL, lname VARCHAR(100), class INT NOT NULL, sec_ques VARCHAR(200) NOT NULL, answer VARCHAR(100) NOT NULL, password VARCHAR(100) NOT NULL, grade CHAR(1))"
            )

            self.mycursor.execute(
                f"INSERT INTO {self.student_table} (username, fname, lname, class, sec_ques, answer, password) VALUES ('{username}', '{fname}', '{lname}', '{class_}', '{sec_ques}', '{answer}', '{password}')"
            )

            self.mydb.commit()

            return {"success": True}
        except Exception as e:
            return {"success": False, "error": e}

    def student_login(self, username, password):
        try:
            self.mycursor.execute(
                f"SELECT * FROM {self.student_table} WHERE username='{username}' AND password='{password}'"
            )

            myresult = self.mycursor.fetchone()

            return {"success": myresult != None,"error": "wrong username or password" if myresult == None else ""}
        except Exception as e:
            return {"success": False, "error": e}

    def get_students(self):
        try:
            self.mycursor.execute(
                f"SELECT * FROM {self.student_table}"
            )

            myresult = self.mycursor.fetchall()

            return {"success": True, "result": myresult}

        except Exception as e:
            return {"success": False, "error": e}

    def update_student(self, fname, lname, class_, username):
        try:
            self.mycursor.execute(
                f"UPDATE {self.student_table} SET username='{username}', fname='{fname}', lname='{lname}', class='{class_}' WHERE username='{username}'"
            )

            self.mydb.commit()

            return {"success": True}
        except Exception as e:
            return {"success": False, "error": e}

    def delete_student(self, username):
        try:
            self.mycursor.execute(
                f"DELETE FROM {self.student_table} WHERE username='{username}'"
            )

            self.mydb.commit()

            return {"success": True}
        except Exception as e:
            return {"success": False, "error": e}

    def set_grade(self, username, grade):
        try:
            self.mycursor.execute(
                f"UPDATE {self.student_table} SET grade='{grade}' WHERE username='{username}'"
            )
            self.mydb.commit()
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": e}

    def get_grades(self, class_):
        try:
            self.mycursor.execute(
                f"SELECT * FROM {self.student_table} WHERE class={class_} AND grade IS NOT NULL"
            )

            myresult = self.mycursor.fetchall()

            return {"success": True, "result": myresult}
        except Exception as e:
            return {"success": False, "error": e}