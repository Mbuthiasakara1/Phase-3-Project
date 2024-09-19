import click
from models import Member, Gym_Class, Instructor, Session

@click.group()
def cli():
    pass

# Member functions
@cli.command()
def create_member():
    session = Session()
    name = input('Enter Member name: ')
    age = int(input('Enter Member Age: '))
    email = input('Enter Member email: ')
    class_id = int(input('Enter the class id: '))

    # Check if the class_id exists in the gym_classes table
    gym_class = session.query(Gym_Class).get(class_id)

    # Check if email is already taken
    existing_member = session.query(Member).filter_by(email=email).first()

    if gym_class:
        if existing_member:
            click.echo('Error: A member with this email already exists.')
        else:
            member = Member(name=name, age=age, email=email, class_id=class_id)
            session.add(member)
            session.commit()
            click.echo('Member created successfully!')
    else:
        click.echo(f'Error: Gym class with id {class_id} does not exist.')

    session.close()

@cli.command()
def display_members():
    session = Session()
    members = session.query(Member).all()
    for member in members:
        click.echo(member)
    session.close()

@cli.command()
def delete_members():
    member_id = int(input('Enter member id: '))
    session = Session()
    member = session.query(Member).get(member_id)
    if member:
        session.delete(member)
        session.commit()
        click.echo("Member deleted successfully")
    else:
        click.echo("Member not found")
    session.close()

@cli.command()
def update_member():
    session = Session()
    member_id = int(input('Enter Member id: '))
    member = session.query(Member).get(member_id)

    if member:
        name = input(f'Enter new name (current: {member.name}): ') or member.name
        age = input(f'Enter new age (current: {member.age}): ')
        email = input(f'Enter new email (current: {member.email}): ') or member.email

        if age:
            age = int(age)

        member.name = name
        member.age = age
        member.email = email

        session.commit()
        click.echo('Member details updated successfully!')
    else:
        click.echo('Member not found')

    session.close()

@cli.command()
def find_member_by_id():
    session = Session()
    member_id = int(input('Enter Member id: '))
    member = session.query(Member).get(member_id)

    if member:
        click.echo(member)
    else:
        click.echo("Member not found by id.")
    
    session.close()

@cli.command()
def find_member_by_name():
    session = Session()
    name = input('Enter Member name: ')
    members = session.query(Member).filter(Member.name == name).all()

    if members:
        for member in members:
            click.echo(member)
    else:
        click.echo("No members found with the given name.")
    
    session.close()

@cli.command()
def find_member_by_class_id():
    session = Session()
    class_id = int(input('Enter class id: '))
    members = session.query(Member).filter(Member.class_id == class_id).all()

    if members:
        for member in members:
            click.echo(member)
    else:
        click.echo("No members found in the specified class.")
    
    session.close()

# Gym_Class functions
@cli.command()
def create_gym_class():
    name = input('Enter Gym class name: ')
    description = input('Enter the description: ')
    instructor_id = int(input('Enter Instructor id: '))

    # Check if the instructor_id exists in the instructors table
    instructor = Session().query(Instructor).get(instructor_id)

    if instructor:
        gym_class = Gym_Class(name=name, description=description, instructor_id=instructor_id)
        session = Session()
        session.add(gym_class)
        session.commit()
        click.echo("Gym class created successfully")
    else:
        click.echo(f'Error: Instructor with id {instructor_id} does not exist.')

    session.close()

@cli.command()
def display_gym_classes():
    session = Session()
    gym_classes = session.query(Gym_Class).all()
    for gym_class in gym_classes:
        click.echo(gym_class)
    session.close()

@cli.command()
def delete_gym_class():
    class_id = int(input('Enter class id: '))
    session = Session()
    gym_class = session.query(Gym_Class).get(class_id)
    if gym_class:
        session.delete(gym_class)
        session.commit()
        click.echo("Class deleted successfully")
    else:
        click.echo("Class not found")
    session.close()

@cli.command()
def update_gym_class():
    session = Session()
    class_id = int(input('Enter Gym class id: '))
    gym_class = session.query(Gym_Class).get(class_id)

    if gym_class:
        name = input(f'Enter new class name (current: {gym_class.name}): ') or gym_class.name
        description = input(f'Enter new description (current: {gym_class.description}): ') or gym_class.description
        instructor_id = input(f'Enter new instructor id (current: {gym_class.instructor_id}): ')

        if instructor_id:
            instructor_id = int(instructor_id)
            instructor = session.query(Instructor).get(instructor_id)
            if instructor:
                gym_class.instructor_id = instructor_id
            else:
                click.echo(f'Error: Instructor with id {instructor_id} does not exist.')

        gym_class.name = name
        gym_class.description = description

        session.commit()
        click.echo('Gym class details updated successfully!')
    else:
        click.echo('Gym class not found')

    session.close()

@cli.command()
def find_gym_class_by_id():
    session = Session()
    class_id = int(input('Enter class id: '))
    gym_class = session.query(Gym_Class).get(class_id)

    if gym_class:
        click.echo(gym_class)
    else:
        click.echo("Gym class not found by id.")
    
    session.close()

@cli.command()
def find_gym_class_by_name():
    session = Session()
    name = input('Enter gym class name: ')
    gym_classes = session.query(Gym_Class).filter(Gym_Class.name == name).all()

    if gym_classes:
        for gym_class in gym_classes:
            click.echo(gym_class)
    else:
        click.echo("No gym classes found with the given name.")
    
    session.close()

# Instructor functions
@cli.command()
def create_instructor():
    name = input('Enter Instructor name: ')
    specialty = input('Enter Instructor specialty: ')
    instructor = Instructor(name=name, specialty=specialty)
    session = Session()
    session.add(instructor)
    session.commit()
    click.echo("Instructor created successfully")
    session.close()

@cli.command()
def display_instructors():
    session = Session()
    instructors = session.query(Instructor).all()
    for instructor in instructors:
        click.echo(instructor)
    session.close()

@cli.command()
def delete_instructor():
    instructor_id = int(input('Enter Instructor id: '))
    session = Session()
    instructor = session.query(Instructor).get(instructor_id)
    if instructor:
        session.delete(instructor)
        session.commit()
        click.echo("Instructor deleted successfully")
    else:
        click.echo("Instructor not found")
    session.close()

@cli.command()
def update_instructor():
    session = Session()
    instructor_id = int(input('Enter Instructor id: '))
    instructor = session.query(Instructor).get(instructor_id)

    if instructor:
        name = input(f'Enter new name (current: {instructor.name}): ') or instructor.name
        specialty = input(f'Enter new specialty (current: {instructor.specialty}): ') or instructor.specialty

        instructor.name = name
        instructor.specialty = specialty

        session.commit()
        click.echo('Instructor details updated successfully!')
    else:
        click.echo('Instructor not found')

    session.close()

@cli.command()
def find_instructor_by_id():
    session = Session()
    instructor_id = int(input('Enter Instructor id: '))
    instructor = session.query(Instructor).get(instructor_id)

    if instructor:
        click.echo(instructor)
    else:
        click.echo("Instructor not found by id.")
    
    session.close()

@cli.command()
def find_instructor_by_name():
    session = Session()
    name = input('Enter Instructor name: ')
    instructors = session.query(Instructor).filter(Instructor.name == name).all()

    if instructors:
        for instructor in instructors:
            click.echo(instructor)
    else:
        click.echo("No instructors found with the given name.")
    
    session.close()

if __name__ == '__main__':
    cli()
