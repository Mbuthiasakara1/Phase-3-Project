Gym Management CLI Application
This project is a command-line interface (CLI) application designed to manage gym members and gym classes. It uses SQLAlchemy for database interactions and Click for CLI commands.

Table of Contents
CLI Script
Models
Functions
Additional Information
CLI Script
cli.py
This is the main script for the CLI application. It provides commands to interact with the gym database, including managing members and gym classes.

Commands:

create_member: Prompts for member details (name, age, email, and class id) and adds a new member to the database if the email is not already taken and the class id exists.
display_members: Lists all members in the database.
delete_members: Deletes a member by their ID.
update_member: Updates a member's details (name, age, email) based on their ID.
find_member_by_id: Finds and displays a member by their ID.
find_member_by_name: Finds and displays members by their name.
find_member_by_class_id: Finds and displays members by their class ID.
create_gym_class: Prompts for gym class details (name and description) and adds a new class to the database.
display_gym_classes: Lists all gym classes in the database.
delete_gym_class: Deletes a gym class by its ID.
update_gym_class: Updates a gym class's details (name, description) based on its ID.
find_gym_class_by_id: Finds and displays a gym class by its ID.
find_gym_class_by_name: Finds and displays gym classes by their name.
Models
models.py
This file contains the SQLAlchemy models used in the application. It defines the structure of the database tables and the relationships between them.

Classes:

Member: Represents a gym member with attributes such as ID, name, age, email, and class ID. It includes constraints for unique email addresses and an index on the name column for optimized queries. It has a foreign key linking it to the Gym_Class model and a relationship to allow access to associated classes.

Attributes:

id: Integer, primary key
name: String
age: Integer
email: String, unique
enrolled_date: DateTime, default to the current date and time
class_id: Integer, foreign key linking to Gym_Class
Methods:

__repr__: Provides a string representation of the Member instance.
Gym_Class: Represents a gym class with attributes such as ID, name, and description. It includes a relationship to the Member model to access members associated with each class.

Attributes:

id: Integer, primary key
name: String
description: String
Methods:

__repr__: Provides a string representation of the Gym_Class instance.
Additional Information
Database Configuration: The SQLite database is used for storing data, configured in models.py with the URI 'sqlite:///gym.db'.
Session Management: SQLAlchemy's sessionmaker is used to create and manage database sessions.
For more detailed instructions on setting up and using this application, refer to the respective command functions in cli.py.