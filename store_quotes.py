import sqlite3

connection_obj = sqlite3.connect('quotes.db')


cursor_obj = connection_obj.cursor()


authors_table = """ CREATE TABLE Authors (
			id INT NOT NULL PRIMARY KEY,
			name VARCHAR(500),
            author_url VARCHAR(250),
		) """
# quotes_table = """ CREATE TABLE Quotes (
# 			id INT NOT NULL PRIMARY KEY,
# 			quote TEXT,
#             author_id INT,
#             FOREGIN KEY (author_id) REFERENCES Authors(id) ON DELETE CASCADE
# 		); """
cursor_obj.execute(authors_table)

print("Table is Ready")

connection_obj.close()
