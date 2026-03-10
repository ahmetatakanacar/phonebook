import time

def menu():
      while True:
            print("1- Add Contact")
            print("2- List Contacts")
            print("3- Update Contact")
            print("4- Delete Contact")
            print("5- Search Contact")
            print("6- Exit")

            choice = int(input("\nChoice: "))

            if choice == 1:
                  name = input("Name: ")
                  phone = int(input("Phone: "))
            elif choice == 2:
                  pass
                  
            elif choice == 3:
                  name = input("Name of contact to update: ")
                  new_name = input("New name: ")
                  new_phone = int(input("New phone: "))
            elif choice == 4:
                  name = input("Name of contact to delete: ")
            elif choice == 5:
                  search = input("Search name: ")
            elif choice == 6:
                  print("Exit..")
                  time.sleep(1.5)
                  break
            else:
                  print("Invalid choice.")

if __name__ == "__main__":
      menu()








