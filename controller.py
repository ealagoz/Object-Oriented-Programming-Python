""" Controller class connect user input to Model and View. 
Controller takes care of the user input, invokes Model methods to manipulate 
the data, and invokes certain View methods to display the data back to the user. 
Both Model and View are initialized by Controller."""

from model import Model
from view import View
import sqlite_backend

class Controller:
    def __init__(self, model, view):
        "Initialze Model and View classes"
        self.model = model 
        self.view = view 

    def display_entry_in_db(self, employee):
        entry = self.model.read_entry(employee)
        if entry:
            self.view.show_entry_in_db(entry)
        else:
            self.view.show_no_entry_in_db(employee)

    def display_all_averages(self):
        entry = self.model.read_all_entries()
        if entry:
            self.view.show_all_averages(entry)
        else:
            self.view.show_no_entry_in_db(entry)

    def display_all_medians(self):
        entry = self.model.read_all_entries()
        if entry:
            self.view.show_all_medians(entry)
        else:
            self.view.show_no_entry_in_db(entry)
    
    def display_group_average(self, name):
        entry = self.model.read_group_entries(name)
        if entry:
            self.view.show_group_average(entry, name)
        else:
            self.view.show_no_entry_in_db(entry)

    def display_group_median(self, name):
        entry = self.model.read_group_entries(name)
        if entry:
            self.view.show_group_median(entry, name)
        else:
            self.view.show_no_entry_in_db(entry)

    def display_all_entries_in_db(self):
        entry = self.model.read_all_entries()
        if entry:
            self.view.show_all_entries_in_db(entry)
        else:
            self.view.show_no_entry_in_db(entry)

    def display_one_chart(self):
        entry = self.model.read_all_entries()
        if entry:
            self.view.show_one_chart(entry)
        else:
            self.view.show_no_entry_in_db(entry)

    def display_stat_chart(self):
        entry = self.model.read_all_entries()
        if entry:
            self.view.show_stat_chart(entry)
        else:
            self.view.show_no_entry_in_db(entry)

    def display_group_histogram(self, name):
        entry = self.model.read_group_entries(name)
        if entry:
            self.view.show_group_histogram(entry, name)
        else:
            self.view.show_no_entry_in_db(entry)

    def insert_entry_in_db(self, name, employee, salary):
        assert len(name) > 0, "Company name must not be NULL"
        assert len(employee) > 0, "Employee name must not be NULL"
        assert salary > 0, "Employee salary must be greater than 0"
        table_type = self.model.table_type

        err = self.model.insert_entry(name, employee, salary)
        if err:
            self.view.show_entry_already_in_db(employee)
        else:
            self.view.show_entry_inserted_in_db(name, employee, salary, table_type)

    def update_entry_in_db(self, employee, salary):
        assert salary > 0, "Employee salary must be greater than 0"
        table_type = self.model.table_type

        update_message = self.model.update_entry(employee, salary)
        if update_message == 0:
            self.view.show_no_entry_in_db(employee)
        else:
            self.view.show_entry_updated_in_db(employee, salary, table_type)

    def delete_entry_in_db(self, employee):
        table_type = self.model.table_type
        
        delete_message = self.model.delete_entry(employee)
        print(delete_message)
        if delete_message == 1:
            self.view.show_no_entry_in_db(employee)
        else: 
            self.view.show_entry_deleted_from_db(employee, table_type)

if __name__ == "__main__":
    mvc = Controller(Model(), View())

    #mvc.display_entry_in_db("Jon Doe")
    #mvc.display_all_entries_in_db()
    #mvc.display_all_averages()
    #mvc.display_all_medians()
    #mvc.display_group_average("GBI")
    #mvc.display_group_median("GBI")
    #mvc.display_one_chart()
    mvc.display_stat_chart()
    #mvc.display_group_histogram("SBI")
    #mvc.insert_entry_in_db("SBI", "Billy Boy", 58764)
    #mvc.display_entry_in_db("Billy Boy")
    #mvc.update_entry_in_db("Billy Boy", 72565)
    #mvc.display_entry_in_db("Billy Boy")
    #mvc.delete_entry_in_db("Billy Boy")
    #mvc.display_entry_in_db("Billy Boy")

    sqlite_backend.db_disconnect(sqlite_backend.db_name, mvc.model.connection)