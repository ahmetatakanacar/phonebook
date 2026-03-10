import time
from database import create_table, add_contact, list_contacts, update_contact, delete_contact, search_contact

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
                  while True:
                        try:
                              phone = int(input("Phone: "))
                              break
                        except ValueError:
                              print("Please enter a valid phone number.")
                  add_contact(name, phone)
                  print("Contact added.")

            elif choice == 2:
                  contacts = list_contacts()
                  if not contacts:
                        print("Phonebook is empty.")
                  for contact in contacts:
                        print(f"ID: {contact[0]}. Name: {contact[1]} - Phone: {contact[2]}")
                  
            elif choice == 3:
                  name = input("Name of contact to update: ")
                  new_name = input("New name: ")
                  while True:
                        try:
                              new_phone = int(input("New phone: "))
                              break
                        except ValueError:
                              print("Please enter a valid phone number.")
                  update_contact(name, new_name, new_phone)
                  print("Contact updated.")

            elif choice == 4:
                  name = input("Name of contact to delete: ")
                  delete_contact(name)
                  print("Contact deleted.")

            elif choice == 5:
                  search = input("Search name: ")
                  result = search_contact(search)
                  if not result:
                        print("No result found.")
                  for contact in result:
                        print(f"ID: {contact[0]} - Name: {contact[1]} - Phone: {contact[2]}")
            elif choice == 6:
                  print("Exit..")
                  time.sleep(1.5)
                  break
            else:
                  print("Invalid choice.")

if __name__ == "__main__":
      create_table()
      menu()








