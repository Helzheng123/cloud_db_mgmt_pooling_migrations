from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from faker import Faker
from azure import Patient, LaboratoryTest
import os
import random 
from dotenv import load_dotenv

load_dotenv()

## Database credentials 
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string and creating the engine 
connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
connection_string = (f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
                    f"?charset={DB_CHARSET}")

engine = create_engine(
        connection_string,
        connect_args=connect_args)

# Creating a session to populate the data
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

for _ in range(10):
    patient = Patient(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        date_of_birth=fake.date_of_birth(minimum_age=10, maximum_age=100),
        contact_number = fake.phone_number()
    )
    session.add(patient)

for _ in range(20):
    labtest = LaboratoryTest(
        test_name=fake.first_name(),
        test_date=fake.date_between(start_date="-5y", end_date="today"),
        test_result=fake.random_element(elements=('Abnormal', 'Normal')),
        labtest_id=session.query(Patient).order_by(func.rand()).first().id
    )
    session.add(labtest)

# Commit the changes to the database
session.commit()

# Close the session
session.close()