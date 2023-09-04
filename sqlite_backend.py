"""SQLITE backend (db_sqlite3).
Each database operations (create, read, update, and delete) should 
be able to connect to the databse unless it is existed.
"""
import sqlite3

db_name = "db_test"

def db_connection(db):
    """This method establishes connection to local SQLITE3 DB."""
    if db is None:
        print("Did not connect to local SQLITE3 DB...")
    else:
        db_test = "{}.db".format(db)
        print("Connected to SQLITE3 '{}' successfully...".format(db_test))
    
    connection = sqlite3.connect(db_test)

    return connection

def db_connect(func):
    """Decorator to (re)connect sqlite3 database when needed. Argument
    func is an inner function performing db query."""

    def db_inner_connect(conn, *args, **kwargs):
        try:
            conn.execute("SELECT name FROM sqlite_temp_master WHERE type='table';")
        except(AttributeError, sqlite3.ProgrammingError):
            conn = db_connection(db_name)
        return func(conn, *args, **kwargs)

    return db_inner_connect

def db_disconnect(db=None, conn=None):
    """This method disconnects SQLITE3 DB."""
    if db is not db_name:
        print("It is trying to disconnect from wrong database.")
    else:
        conn.close()

@db_connect
def db_create_table(conn, table_name):
    """This method creates a table SQLITE3 DB."""
    query = (
        "CREATE TABLE {} (rowid INTEGER PRIMARY KEY AUTOINCREMENT,"
        "name TEXT, employee TEXT UNIQUE, salary INTEGER)".format(table_name)
        )
    try:
        conn.execute(query) 
    except sqlite3.Error as e:
        print("Warning: {} ".format(e))

@db_connect
def db_insert_one(conn, name, employee, salary, table_name):
    """This method inserts an entry into SQLITE3 DB."""
    query = (
        "INSERT INTO {} ('name', 'employee', 'salary') VALUES (?, ?, ?)".format(table_name)
    )
    try:
        conn.execute(query, (name, employee, salary))
        conn.commit()
    except sqlite3.Error as error_message:
        error_message = 1
        return error_message

@db_connect
def db_delete_one(conn, employee, table_name):
    """This method deletes an entry from SQLITE3 DB."""
    query_check = "SELECT EXISTS(SELECT 1 FROM {} WHERE employee=? LIMIT 1)".format(table_name)
    query_delete = "DELETE FROM {} WHERE employee=?".format(table_name)

    c = conn.execute(query_check, (employee,)) 
    result = c.fetchone()
    if result:
        c.execute(query_delete, (employee,)) 
        conn.commit()
        error_message = 0
    else:
        error_message = 1
    return error_message

@db_connect
def db_update_one(conn, employee, salary, table_name):
    """This method updates an entry in SQLITE3 DB."""
    query_check = "SELECT EXISTS(SELECT 1 FROM {} WHERE employee=? LIMIT 1)".format(table_name)
    query_update = "UPDATE {} SET salary=? WHERE employee=?".format(table_name)
    c = conn.execute(query_check, (employee,)) 
    result = c.fetchone()
    if result:
        c.execute(query_update, (salary, employee))
        conn.commit()
        error_message = 1
    else:
        error_message = 0
    return error_message

@db_connect
def db_select_one(conn, employee, table_name):
    """This method executes select single entry query in SQLITE3 DB."""
    conn.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])
    query = "SELECT * FROM {} WHERE employee='{}'".format(table_name, employee)
    c = conn.execute(query)
    result = c.fetchall()
    if result:
        return result
    else:
        pass 

@db_connect
def db_select_group(conn, name, table_name):
    """This method executes select group entries query in SQLITE3 DB."""
    conn.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])
    query = "SELECT * FROM {} WHERE name='{}'".format(table_name, name)
    c = conn.execute(query)
    result = c.fetchall()
    if result:
        return result
    else:
        pass 

@db_connect
def db_select_all(conn, table_name):
    """This method executes select all entries query in SQLITE3 DB."""
    conn.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])
    query = "SELECT * FROM {}".format(table_name)
    c = conn.execute(query)
    result = c.fetchall()
    if result is not None:
        return result
    else: 
        pass 