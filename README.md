# Gym Management CLI Application

This CLI application allows you to manage members, gym classes, and instructors in a gym database. It uses Python and SQLAlchemy to interact with a SQLite database (`gym.db`). With this application, you can create, update, delete, and search for members, classes, and instructors through the command line.

## Features
- **Manage Members**: Add, update, delete, and view gym members.
- **Manage Classes**: Create, update, delete, and view gym classes.
- **Manage Instructors**: Add, update, delete, and view instructors.
- **Relational Database**: Members are linked to gym classes, and gym classes are linked to instructors.
- **Validation**: Validates member email uniqueness and class and instructor existence before creating new records.

## Setup

### Prerequisites
- Python 3.7+
- Pipenv (or `pip` to install dependencies)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Mbuthiasakara1/Phase-3-Project.git
   ```

2. Navigate to the project directory:

   ```bash
   cd gym-cli
   ```

3. Install dependencies using Pipenv:

   ```bash
   pipenv install
   ```

   Or use `pip` if you're not using Pipenv:

   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:

   ```bash
   python -c "from models import Base, engine; Base.metadata.create_all(engine)"
   ```

### Running the CLI

Activate the Pipenv shell and run the CLI:

```bash
pipenv shell
python cli.py --help
```

This will display a list of available commands.

## Available Commands

### Member Management

- **Create a Member**:
  
  ```bash
  python cli.py create_member
  ```

  This will prompt you to enter the member's name, age, email, and class ID.

- **Display Members**:

  ```bash
  python cli.py display_members
  ```

  This will list all members in the gym.

- **Update Member**:

  ```bash
  python cli.py update_member
  ```

  You will be prompted to enter the member's ID and update their details.

- **Delete Member**:

  ```bash
  python cli.py delete_member
  ```

  This deletes a member by their ID.

- **Find Member by ID**:

  ```bash
  python cli.py find_member_by_id
  ```

  Finds a specific member by their unique ID.

- **Find Member by Name**:

  ```bash
  python cli.py find_member_by_name
  ```

  Finds members by name.

- **Find Members by Class ID**:

  ```bash
  python cli.py find_member_by_class_id
  ```

  Finds all members enrolled in a specific class.

### Gym Class Management

- **Create a Gym Class**:

  ```bash
  python cli.py create_gym_class
  ```

  This will prompt you to enter the class name, description, and the instructor ID for the class.

- **Display Gym Classes**:

  ```bash
  python cli.py display_gym_classes
  ```

  Lists all gym classes.

- **Update Gym Class**:

  ```bash
  python cli.py update_gym_class
  ```

  Prompts to update class details by class ID.

- **Delete Gym Class**:

  ```bash
  python cli.py delete_gym_class
  ```

  Deletes a class by its ID.

- **Find Gym Class by ID**:

  ```bash
  python cli.py find_gym_class_by_id
  ```

  Finds a class by its unique ID.

- **Find Gym Class by Name**:

  ```bash
  python cli.py find_gym_class_by_name
  ```

  Finds classes by their name.

### Instructor Management

- **Create an Instructor**:

  ```bash
  python cli.py create_instructor
  ```

  Prompts to create an instructor by entering their name and specialty.

- **Display Instructors**:

  ```bash
  python cli.py display_instructors
  ```

  Lists all instructors.

- **Update Instructor**:

  ```bash
  python cli.py update_instructor
  ```

  Updates an instructor’s details by their ID.

- **Delete Instructor**:

  ```bash
  python cli.py delete_instructor
  ```

  Deletes an instructor by their ID.

- **Find Instructor by ID**:

  ```bash
  python cli.py find_instructor_by_id
  ```

  Finds an instructor by their unique ID.

- **Find Instructor by Name**:

  ```bash
  python cli.py find_instructor_by_name
  ```

  Finds instructors by their name.

## Code Overview

### Models (`models.py`)

- **Member**: Represents a gym member. Each member has a unique email and is linked to a gym class.
  
- **Gym_Class**: Represents a gym class. Each class has a name, description, and is linked to an instructor.

- **Instructor**: Represents an instructor. Instructors have a name and a specialty (e.g., Yoga, Pilates).

### CLI Commands (`cli.py`)

Each function in `cli.py` corresponds to a command that you can execute from the command line. For example, `create_member` adds a new member, and `update_member` allows updating member information. The `click` module is used for handling command-line interactions.

## How to Contribute

1. Fork the project.
2. Create a new feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

