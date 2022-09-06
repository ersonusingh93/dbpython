from dbhelper import DBHelper

def main():
    db=DBHelper()
    while(True):
        print("****** WELCOME******")
        print()
        print("1 to insert new user")
        print("2 to display all user")
        print("3 to delete user")
        print("4 to update user")
        print("5 to exit program")
        print()
        try:
            choice=int(input())
            if (choice==1):
                #insert
                uid=int(input("Enter userid:"))
                username=input("Enter user name:")
                userphone=int(input("Enter user phone:"))
                db.insert_user(uid,username,userphone)
                pass
            elif choice==2:
                #display all user
                db.fetch_all()
                pass
            elif choice==3:
                #delete user
                userid=int(input("Enter the id you want to delete:"))
                db.delete_user(userid)
                pass
            elif choice==4:
                #update user
                uerid=int(input("Enter userId for update:"))
                Nusername=input("Enter New user name:")
                Nuserphone=int(input("Enter new user phone:"))
                db.update_user(uerid,Nusername,Nuserphone)
                pass
            elif choice==5:
                #exit program
                break
            else:
                print("Invalid Input, Try again!")
        except Exception as e:
            print(e)
            print("Invalid Details! Try Again!")

if __name__ == "__main__":
    main()