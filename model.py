"""Model is the business logic of application. Model class methods are used
to access the application database and perfom database create, read, update, and delete
operations."""
import sqlite_backend

class Model:
    def __init__(self):
        """This method initializes sqlite3 table name, 
        executes sqlite3 connection and create_table methods in sqlite_backend."""
        self.table_type = "company"
        self._connection = sqlite_backend.db_connection(sqlite_backend.db_name)
        sqlite_backend.db_create_table(self.connection, self.table_type)

    @property
    def connection(self):
        """This method gets sqlite3 connection property."""
        return self._connection

    def insert_entry(self, name, employee, salary):
        """This method returns sqlite3 insert single entry."""
        return sqlite_backend.db_insert_one(self.connection, name, employee, salary, table_name = self.table_type)
    
    def delete_entry(self, employee):
        """This method returns sqlite3 delete single entry."""
        return sqlite_backend.db_delete_one(self.connection, employee, table_name = self.table_type)

    def update_entry(self, employee, salary):
        """This method returns sqlite3 update single entry."""
        return sqlite_backend.db_update_one(self.connection, employee, salary, table_name = self.table_type)

    def read_entry(self, employee):
        """This method returns sqlite3 select single entry."""
        return sqlite_backend.db_select_one(self.connection, employee, table_name = self.table_type)

    def read_all_entries(self):
        """This method returns sqlite3 select all entries."""
        return sqlite_backend.db_select_all(self.connection, table_name = self.table_type)

    def read_group_entries(self, name):
        """This method returns sqlite3 select group entries per company."""
        return sqlite_backend.db_select_group(self.connection, name, table_name = self.table_type)