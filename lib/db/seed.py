from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Member, Gym_Class, Instructor
from datetime import datetime

# Database connection and session setup
my_engine= 'sqlite:///gym.db'
engine = create_engine(my_engine)
Session = sessionmaker(bind=engine)
session = Session()

def seed_database():
    # Create all tables
    Base.metadata.create_all(engine)

    # Create instructors
    instructors = [
        Instructor(name='Christine Gakii', specialty='Yoga'),
        Instructor(name='Maureen Mbuthia', specialty='Pilates'),
        Instructor(name='Mike Mahugu', specialty='Strength Training')
    ]
    
    session.add_all(instructors)
    session.commit()
    
    # Create gym classes with assigned instructors
    gym_classes = [
        Gym_Class(name='Upper Body', description='Join our intense upper body class', instructor_id=1),
        Gym_Class(name='Yoga', description='Connect with your inner self', instructor_id=1),
        Gym_Class(name='Pilates', description='Be lean and clean', instructor_id=2)
    ]

    session.add_all(gym_classes)
    session.commit()

    # Create members
    members = [
        Member(name='Dinx John', age=30, email='dinx@gmail.com', class_id=1, enrolled_date=datetime.now()),
        Member(name='Fiona Charagu', age=25, email='fiona@gmail.com', class_id=2, enrolled_date=datetime.now()),
        Member(name='Henry Odhiambo', age=28, email='henry@gmail.com', class_id=3, enrolled_date=datetime.now())
    ]

    session.add_all(members)
    session.commit()

    print("Database  with initial data!")

if __name__ == "__main__":
    seed_database()
