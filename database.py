import sqlite3

DB_NAME = "phonebook.db"

def get_connection():
      return sqlite3.connect(DB_NAME)

def create_table():
      conn = get_connection()
      cursor = conn.cursor()
      cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts 
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  phone INTEGER NOT NULL)
      """)
      conn.commit()
      conn.close()

def add_contact(name, phone):
      conn = get_connection()
      cursor = conn.cursor()
      cursor.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)",(name, phone))
      conn.commit()
      conn.close()

def list_contacts():
      conn = get_connection()
      cursor = conn.cursor()
      cursor.execute("SELECT id, name, phone FROM contacts")
      contacts = cursor.fetchall()
      conn.close()
      return contacts

def update_contact(name, new_name, new_phone):
      conn = get_connection()
      cursor = conn.cursor()
      cursor.execute("UPDATE contacts SET name = ?, phone = ? WHERE name = ?",(new_name, new_phone, name))
      conn.commit()
      conn.close()

def delete_contact(name):
      conn = get_connection()
      cursor = conn.cursor()
      cursor.execute("DELETE FROM contacts WHERE name = ?",(name,))
      conn.commit()
      conn.close()

def search_contact(search):
      conn = get_connection()
      cursor = conn.cursor()
      cursor.execute("SELECT id, name, phone FROM contacts WHERE name LIKE ?",(f"%{search}%",))
      contacts = cursor.fetchall()
      conn.close()
      return contacts