
# MVC Controller for Data Analysis

The MVC (Model-View-Controller) Controller class in this project serves as the central component that connects user input to both the Model and View components. It manages user interactions, invokes Model methods to manipulate data, and calls specific View methods to present data to the user. Both the Model and View are initialized within the Controller.

## Table of Contents

- [Overview](#overview)
- [Python Files Hierarchy](#python-files-hierarchy)
- [Usage](#usage)
- [Methods](#methods)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Controller class is a critical part of the MVC architectural pattern, facilitating the flow of data between the Model (responsible for data manipulation and retrieval) and the View (responsible for presenting data to the user). It handles various user actions, such as querying data, inserting records, updating entries, and displaying statistics.

## Python Files Hierarchy

The project consists of the following Python files and their respective purposes:

- `controller.py`: The Controller class, which connects user input to the Model and View components.

- `model.py`: The Model class, responsible for data manipulation, retrieval, and interactions with the database.

- `view.py`: The View class, responsible for displaying data to the user through various methods.

- `sqlite_backend.py`: Backend functions for interacting with an SQLite database.

## Usage

The Controller class provides a user-friendly interface for interacting with the underlying data and generating meaningful insights. Users can perform various actions using this Controller class, including querying individual entries, calculating averages and medians, generating charts, and more.

To use the Controller class, you need to initialize it with instances of the Model and View classes. Once initialized, you can call the Controller's methods to interact with the data and view the results.

## Methods

- `display_entry_in_db(employee)`: Displays information about a specific employee's entry in the database.

- `display_all_averages()`: Displays average salary information for all employees in the database.

- `display_all_medians()`: Displays median salary information for all employees in the database.

- `display_group_average(name)`: Displays the average salary for employees belonging to a specific group or company.

- `display_group_median(name)`: Displays the median salary for employees belonging to a specific group or company.

- `display_all_entries_in_db()`: Displays all entries in the database.

- `display_one_chart()`: Displays a chart representing data from the database.

- `display_stat_chart()`: Displays statistical charts based on data from the database.

- `display_group_histogram(name)`: Displays a histogram for employees belonging to a specific group or company.

- `insert_entry_in_db(name, employee, salary)`: Inserts a new entry into the database, ensuring that the provided information is valid.

- `update_entry_in_db(employee, salary)`: Updates the salary information for a specific employee in the database.

- `delete_entry_in_db(employee)`: Deletes an employee's entry from the database.

## Contributing

Contributions to this project are welcome! If you have any suggestions, bug fixes, or improvements, please feel free to open an issue or create a pull request on the project's GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to customize this README with additional information or sections as needed for your project.
