from datetime import datetime
from sqlalchemy import (
    create_engine,
    PrimaryKeyConstraint, UniqueConstraint, ForeignKey,
    Index, Column, DateTime, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///gym.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Member(Base):
    __tablename__ = 'members'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='id_pk'),
        UniqueConstraint('email', name='unique_email')
    )

    Index('index_name', 'name')  # Creates an index on the name column to improve querying

    id = Column(Integer(), primary_key=True)#like giving each member a membership number
    name = Column(String())
    age = Column(Integer())
    email = Column(String())
    enrolled_date = Column(DateTime(), default=datetime.now())
    class_id = Column(Integer(), ForeignKey('gym_classes.id'))  # Refers to the id column in the gym_classes table uses the gyms class id to link say member 1 might be linked to class 2(hii line says the class_id column in the Members table refers to the id in the Gym_class table)
    gym_class = relationship('Gym_Class', back_populates='members')

    def __repr__(self):
        return f"<Member id={self.id}, name={self.name}, email={self.email}, class_id={self.class_id}>"

class Gym_Class(Base):
    __tablename__ = 'gym_classes'

    id = Column(Integer(), primary_key=True)#giving each class a unique code
    name = Column(String())
    description = Column(String())
    members = relationship('Member', back_populates='gym_class')
    instructor_id = Column(Integer(), ForeignKey('instructors.id'))  # Links to Instructor
    instructor = relationship('Instructor', back_populates='classes')

    def __repr__(self):
        return f"<GymClass id={self.id}, name={self.name}, description={self.description}>"

class Instructor(Base):
    __tablename__ = 'instructors'

    id = Column(Integer(), primary_key=True)# like tagging each instructor(a badge)
    name = Column(String())
    specialty = Column(String())
    classes = relationship('Gym_Class', back_populates='instructor')

    def __repr__(self):
        return f"<Instructor id={self.id}, name={self.name}, specialty={self.specialty}>"
