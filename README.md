# cloud_db_mgmt_pooling_migrations
Gain practical experience in managing a cloud-based MySQL database with a focus on implementing connection pooling and performing database migrations. You will work with both Azure and Google Cloud Platform (GCP) for this assignment.

## 1. Connection Pooling Setup:
 - Azure:
    - Go to Azure Database for MySQL servers --> Click Create --> Choose Flexible Server --> Choose a Resource Group/Create new one --> Enter a server name and change compute + storage to Standard_B1s --> Enter server admin login name, password, confirm password --> Click Next: Networking --> Click + Add 0.0.0.0 - 255.255.255.255 and + Add current client IP address --> Hit create
    - Once created, go to Server Parameters and change the max_connections to 20 and connect_timeout to 3, change require_secure_transport to OFF
 - GCP:
    - Go to SQL--> Create Instance --> Choose MySQL --> Enter an Instance ID and a Password --> Choose Enterprise and change the preset to Sandbox --> Click Show Configuration Options --> Go to Machine Configuration and choose Shared Core and 1vCPU, 0.614 GB --> Go to Connections and Add a Network --> Name it Allow-All and set it as 0.0.0.0/0

## 2a. Database Schema and Data:
 - Azure and GCP: I created two tables (Patients and Laboratory Test)
