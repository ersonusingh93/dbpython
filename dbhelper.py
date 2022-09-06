import mysql.connector as connector
# con= connector.connect(host ='localhost', 
#                         port='3306', 
#                         user ='root', 
#                         password='123456', 
#                         database= 'pythontest')
# print(con)

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host ='localhost', 
                        port='3306', 
                        user ='root', 
                        password='123456', 
                        database= 'pythontest')
        query=' create table if not exists user( userId int primary key, userName varchar(200), phone varchar(20))'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")

#insert_user
    def insert_user(self,userid,username,phone):
        query="insert into user(userId,userName,phone)values({},'{}','{}')".format(userid,username,phone)
        # print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")

#fetch_all
    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id:", row[0])
            print("User Name:", row[1])
            print("User Phone:", row[2])
            print()
            print()

#delete_user
    def delete_user(self,userid):
        query = "delete from user where userId = {}".format(userid)
        # print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit() #for_permanent_change in the table
        print("Deleted")

#update_user
    def update_user(self,userId,newName,newPhone):
        query= "update user set userName='{}', phone='{}' where userId={}".format(newName,newPhone,userId)
        # print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated")
#main coding
# helper = DBHelper()
# helper.insert_user(22,"asd","123456")
# helper.insert_user(9,"bhdhf","12")
# helper.insert_user(10,"asdsd","1256")
# helper.insert_user(11,"asdddd","3456")
# helper.insert_user(12,"ghy","7548")
# helper.delete_user(12)
# helper.update_user(11,"Nine","4545")
# helper.fetch_all()


