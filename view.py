import pandas as pd
import matplotlib.pyplot as plt

"""The view class handles how datasets are presented to the user. 
It can not call its own methods, only Controller does so."""

class View:
    @staticmethod
    def show_entry_in_db(entry):
        """This method prints single entry on console/terminal."""
        if entry:
            print(50*"/")
            df = pd.DataFrame(entry)
            df.columns = ["ID", "Company name", "Employee", "Salary"]
            df.set_index("ID", inplace=True)
            print(df)
            print(50*"/")
        else:
            pass

    @staticmethod
    def show_all_entries_in_db(entry):
        """This method prints all entries on console/terminal."""
        print(50*"/")
        df = pd.DataFrame(entry)
        df.columns = ["ID", "Company name", "Employee name", "Salary"]
        df.set_index("ID", inplace=True)
        print(df)
        print(50*"/")

    @staticmethod
    def show_all_averages(entry):
        """This method prints employee salary averages per company on console/terminal."""
        df = pd.DataFrame(entry)
        df.columns = ["id", "Company", "Employee", "Salary"]
        df.set_index("id", inplace=True)
        averages = df.groupby("Company").agg(["mean", "std"]).round(2)
        print(50*"=")
        print("Average employee salary per company and standard deviation")
        print(averages)
        print(50*"=")

    @staticmethod
    def show_all_medians(entry):
        """This method prints employee salary medians per company on console/terminal."""
        df = pd.DataFrame(entry)
        df.columns = ["id", "Company", "Employee", "Salary"]
        df.set_index("id", inplace=True)
        medians = df.groupby("Company").agg(["median", "std"]).round(2)
        print(50*"=")
        print("Median employee salary per company and standard deviation")
        print(medians)
        print(50*"=")

    @staticmethod
    def show_group_average(entry, name):
        """This method prints employee salary average for one company on console/terminal."""
        df = pd.DataFrame(entry)
        df.columns = ["id", "Company", "Employee", "Salary"]
        df.set_index("id", inplace=True)
        averages = df[df["Company"] == name].agg(["mean", "std"]).round(2)
        print(50*"=")
        print("Average employee salary and standard deviation \n for {}".format(name))
        print(averages)
        print(50*"=")

    @staticmethod
    def show_group_median(entry, name):
        """This method prints employee salary median for one company on console/terminal."""
        df = pd.DataFrame(entry)
        df.columns = ["id", "Company", "Employee", "Salary"]
        df.set_index("id", inplace=True)
        averages = df[df["Company"] == name].agg(["median", "std"]).round(2)
        print(50*"=")
        print("Median employee salary and standard deviation for {}".format(name))
        print(averages)
        print(50*"=")

    @staticmethod
    def show_stat_chart(entry):
        df = pd.DataFrame(entry)
        df.columns = ["id", "Company", "Employee", "Salary"]
        df.set_index("id", inplace=True)
        print(50*"=")
        print("Bar chart showing all company employee \n salary averages and standard deviations")
        print(50*"=")
        dfg = df.groupby("Company").agg(["mean", "std"]).round(2)
        dfg.plot(kind='bar', figsize=(8, 6))
        plt.title("Mean company employee salaries")
        plt.xlabel("Company")
        plt.ylabel("Mean employee salary [\$]")
        plt.legend(["Mean", "Standard deviation"])
        plt.show()

    @staticmethod
    def show_one_chart(entry):
        df = pd.DataFrame(entry)
        df.columns = ["id", "Company", "Employee", "Salary"]
        df.set_index("id", inplace=True)
        print(50*"=")
        print("Histogram showing company employee salary statistics")
        print(50*"=")
        df.plot.barh(x="Employee", y="Salary", grid=False, fontsize=9, 
                    figsize=(11,5), legend=False, stacked=True)
        plt.title("Mean company employee salaries")
        plt.ylabel("Employee name")
        plt.xlabel("Employee salary [\$]")
        plt.show()

    @staticmethod
    def show_group_histogram(entry, name):
        df = pd.DataFrame(entry)
        df.columns = ["id", "Company", "Employee", "Salary"]
        df.set_index("id", inplace=True)
        print(50*"=")
        print("Employee salaries on bar chart for {}".format(name))
        print(50*"=")
        df.plot.barh(x="Employee", y="Salary", grid=False, fontsize=9, 
                    figsize=(10,5), width=0.3, legend=False, 
                    color="red", stacked=True)
        plt.title("{} employee salaries".format(name))
        plt.xlabel("Employee salaries [\$]")
        plt.ylabel("Employee name")
        plt.show()

    @staticmethod
    def show_no_entry_in_db(employee):
        print(50*"x")
        print("Sorry, no {} found in database!".format(employee.upper()))
        print(50*"x")

    @staticmethod
    def show_entry_already_in_db(employee):
        print(50*"!")
        print("Entry {} already in database!".format(employee.upper()))
        print(50*"!")

    @staticmethod
    def show_entry_inserted_in_db(name, employee, salary, table_type):
        print(50*">")
        print("{} - {} - {}$ \n added to {} table in database!".
             format(name.upper(), employee.upper(), salary, table_type))
        print(50*">")

    @staticmethod
    def show_entry_updated_in_db(employee, salary, table_type):
        print(50*"@")
        print("Employee {} salary updated to {} \n in {} table in database!".format(employee, salary, table_type))
        print(50*"@")

    @staticmethod
    def show_entry_deleted_from_db(employee, table_type):
        print(50*"-")
        print("Employee {}  deleted \n from table {} in database!".format(employee.upper(), table_type))
        print(50*"-")