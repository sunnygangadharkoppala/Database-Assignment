import sqlite3


def createAuthorsTable():
    connection_obj = sqlite3.connect('quotes.db')
    cursor_obj = connection_obj.cursor()
    cursor_obj.execute("DROP TABLE IF EXISTS AUTHORS")
    authors_table = """ CREATE TABLE Authors (
                id INT NOT NULL PRIMARY KEY,
                name VARCHAR(500),
                author_url VARCHAR(250)
            ); """
    cursor_obj.execute(authors_table)
    print("Author Table is Ready")
    connection_obj.close()


def createQuotesTable():
    connection_obj = sqlite3.connect('quotes.db')
    cursor_obj = connection_obj.cursor()
    cursor_obj.execute("DROP TABLE IF EXISTS QUOTES")
    quotes_table = """ CREATE TABLE Quotes (
                id INT NOT NULL PRIMARY KEY,
                quote TEXT,
                author_id INT,
                CONSTRAINT fk_author FOREIGN KEY (author_id) REFERENCES Authors(id) ON DELETE CASCADE
            ); """
    cursor_obj.execute(quotes_table)
    print("Quotes Table is Ready")
    connection_obj.close()


def createTagsTable():
    connection_obj = sqlite3.connect('quotes.db')
    cursor_obj = connection_obj.cursor()
    cursor_obj.execute("DROP TABLE IF EXISTS Tags")
    tags_table = """ CREATE TABLE Tags (
                id INT NOT NULL PRIMARY KEY,
                category INT
            ); """
    cursor_obj.execute(tags_table)
    print("Tags Table is Ready")
    connection_obj.close()


def createQuotesAndTagsTable():
    connection_obj = sqlite3.connect('quotes.db')
    cursor_obj = connection_obj.cursor()
    cursor_obj.execute("DROP TABLE IF EXISTS QUOTESANDTAGS")
    quotesandtags_table = """ CREATE TABLE QuotesAndTags (
                id INT NOT NULL PRIMARY KEY,
                quote_id INT,
                tag_id INT,
                CONSTRAINT fk_quotes FOREIGN KEY (quote_id) REFERENCES Tags(id) ON DELETE CASCADE
                CONSTRAINT fk_tags FOREIGN KEY (tag_id) REFERENCES Quotes(id) ON DELETE CASCADE
            ); """
    cursor_obj.execute(quotesandtags_table)
    print("QuotesAndTags Table is Ready")
    connection_obj.close()


createAuthorsTable()
createQuotesTable()
createTagsTable()
createQuotesAndTagsTable()
