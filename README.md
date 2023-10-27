# cloud_db_mgmt_pooling_migrations
Gain practical experience in managing a cloud-based MySQL database with a focus on implementing connection pooling and performing database migrations. You will work with both Azure and Google Cloud Platform (GCP) for this assignment.

## 1. Connection Pooling Setup:
 - Azure:
    - Go to Azure Database for MySQL servers --> Click Create --> Choose Flexible Server --> Choose a Resource Group/Create new one --> Enter a server name and change compute + storage to Standard_B1s --> Enter server admin login name, password, confirm password --> Click Next: Networking --> Click + Add 0.0.0.0 - 255.255.255.255 and + Add current client IP address --> Hit create
    - Once created, go to Server Parameters and change the max_connections to 20 and connect_timeout to 3, change require_secure_transport to OFF
 - GCP:
    - Go to SQL--> Create Instance --> Choose MySQL --> Enter an Instance ID and a Password --> Choose Enterprise and change the preset to Sandbox --> Click Show Configuration Options --> Go to Machine Configuration and choose Shared Core and 1vCPU, 0.614 GB --> Go to Connections and Add a Network --> Name it Allow-All and set it as 0.0.0.0/0

## 2a. Database Schema and Data:
 - [Azure](https://github.com/Helzheng123/cloud_db_mgmt_pooling_migrations/blob/main/AZURE/azure.py) and [GCP](https://github.com/Helzheng123/cloud_db_mgmt_pooling_migrations/blob/main/GCP/gcp.py): I created two tables (Patients and Laboratory Test) and populated them.
 - I have used these tables in a [previous assignment](https://github.com/Helzheng123/flask_4_databases_mysql_vm).
 - There is a [one to many](https://github.com/Helzheng123/cloud_db_mgmt_pooling_migrations/blob/main/Screenshots/ERD%20AZURE%20diagram.png) relationship between patients and laboratory tests
 - You can check if your table was made by entering the terminal ```mysql -u <user> -h <server name/IP address> -p```
 - I then [populated](https://github.com/Helzheng123/cloud_db_mgmt_pooling_migrations/blob/main/AZURE/populate_azure.py) the tables with random generated data.
 - Once I was done with the file, I went into the terminal and typed in ```python populate_gcp.py``` or ```python populate_azure.py``` (whichever one you start with).
 - Then check in mysql terminal with ```SELECT * FROM patients;``` and ```SELECT * FROM laboratory_test```

## 2b. Using MySQL Workbench to Generate ERD:
 - After connecting to MySQL workbench for both Azure and GCP, I used the reverse engineer function to generate the [ERD](https://github.com/Helzheng123/cloud_db_mgmt_pooling_migrations/blob/main/Screenshots/ERD%20GCP%20diagram.png) for my database.

## 3. SQLAlchemy and Flask Integration:
 - I used the [templates](https://github.com/Helzheng123/flask_4_databases_mysql_vm/tree/main/templates) I have used in a previous assignment.
 - I made a ```.env``` file and a ```.gitignore``` file with my credentials in it. I also used ```app.py``` for Flask.
 - Please check out the [Screenshots](https://github.com/Helzheng123/cloud_db_mgmt_pooling_migrations/tree/main/Screenshots) folder to see the Flask App.

## 4. Database Migrations with Alembic:
 - To set up Alembic, I first typed in the terminal ```alembic init migrations```
 - Then I went to ```alembic.ini``` to edit ```sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name``` with my own credentials. Make sure to add ```alembic.ini``` in your ```.gitignore``` file.
 - I went to ```env.py``` to change models to ```from <your .py file that was used to generate the tables> import Base``` and ```target_metadata = Base.metadata```. Make sure to comment the ```target_metadata = None``` line.
 - Then go back to the terminal and create a migration with ```alembic revision --autogenerate -m "create tables"```
 - Then run the migration with ```alembic upgrade head```
 - Then save it as ```alembic upgrade head --sql > migration.sql``` which will create a file ```migration.sql```
 - Go to [gcp.py](https://github.com/Helzheng123/cloud_db_mgmt_pooling_migrations/blob/main/GCP/gcp.py) and [azure.py](https://github.com/Helzheng123/cloud_db_mgmt_pooling_migrations/blob/main/AZURE/azure.py) and add a new column in one of the tables.
   - For example: In [azure.py](https://github.com/Helzheng123/cloud_db_mgmt_pooling_migrations/blob/main/AZURE/azure.py) I added a column ```tetris_score = Column (Integer)```. Though it does not relate to the database, I added it to note that this column was generated through Alembic.
   - In [gcp.py](https://github.com/Helzheng123/cloud_db_mgmt_pooling_migrations/blob/main/GCP/gcp.py) I added a column ```suika_score = Column(Integer)``` which also does not relate to the database but I added it since I was playing the game at the moment 😄 (also to note that this column was generated through Alembic).
  
## 5. Error Handling:
I ran into many errors in this assignment, mainly in integrating with Flask and populating the data. The populating portion ran into errors because the range was small and I had to check out what the Faker package had. Flask integration was problematic because I was able to deploy it but I wasn't able to deploy it with the randomly generated data I populated. Migration with Alembic was tedious for me since I kept deleting and restarting the process for my data since I didn't realize I already had an Alembic_version column in my table. Once I dropped the column with ```DROP TABLE alembic_version```, I was able to go through the steps for migration with Alembic. 
