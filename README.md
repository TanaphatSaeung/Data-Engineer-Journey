# Data Engineer Journey
**This is my journey from the IBM Data Engineering Professional Certificate, which includes lecture notes and projects.**

# Data Warehouse Introduction
**Data Warehouse Overview**

**Data Warehouse**
- a system that aggregates data from one or more sources in to a single consistent data store to support data analytics

<div style="text-align:center">
    <img src="https://github.com/TanaphatSaeung/Data-Engineer-Journey/assets/174108415/fa50653b-2ed1-47b8-b3a9-e807cfaaf273" alt="Data Warehouse">
</div>

**Data Analytics**
- Systems support
  - Data Mining
  - AI
  - Machine Learning
  - Front-End reporting
  - OLAP Online analytical processing

**Data Warehouses Hosted**
- On-premises
  - data warehouses hosted on-premises within Enterprise datacenters and then on Unix, Windows and Linux systems
- Appliances
  - DWAs(Data Warehouse Appliances), consisting of specialized hardware with pre-integrated software
- Cloud
  - Scalable service pay-as-you-go service

**Vendors - Appliance Offerings**
 <div style="text-align:center">
    <img src="https://github.com/TanaphatSaeung/Data-Engineer-Journey/assets/174108415/57b7ab08-7250-418a-98d4-38672c2ad6e8!" alt="IBM Netezza">
</div>
<div style="text-align:center">
    <img src="https://github.com/TanaphatSaeung/Data-Engineer-Journey/assets/174108415/f383a6e2-8e70-45b0-8597-1444e7543760" alt="Oracle Exadata">
</div>

**Vendors - Cloud Only**
<div style="text-align:center">
    <img src="https://github.com/TanaphatSaeung/Data-Engineer-Journey/assets/174108415/d4caa7ec-4bee-4a6e-86ef-50581ed18295" alt="Amazon RedShift">
</div>
<div style="text-align:center">
    <img src="https://github.com/TanaphatSaeung/Data-Engineer-Journey/assets/174108415/eed12ea2-44fc-45a7-9752-8f9cfa1ffe78" alt="Snowflake">
</div>
<div style="text-align:center">
    <img src="https://github.com/TanaphatSaeung/Data-Engineer-Journey/assets/174108415/55013ac6-f1a2-4a5f-8507-75126448db89" alt="Google BigQuery">
</div>

**Vendors - on Premises and Cloud**
<div style="text-align:center">
    <img src="https://github.com/TanaphatSaeung/Data-Engineer-Journey/assets/174108415/31033603-4acd-431b-82ca-d282eef8f4fb" alt="Microsoft Azure Synapse Analytics">
</div>
<div style="text-align:center">
    <img src="https://github.com/TanaphatSaeung/Data-Engineer-Journey/assets/174108415/c00e5ef1-0e05-476a-824e-75b9093589f9" alt="Teradata Vantage">
</div>
<div style="text-align:center">
    <img src="https://github.com/TanaphatSaeung/Data-Engineer-Journey/assets/174108415/33221182-6fe8-4f9b-a287-90d9b614fdfe" alt="IBM Db2 Warehouse">
</div>
<div style="text-align:center">
    <img src="https://github.com/TanaphatSaeung/Data-Engineer-Journey/assets/174108415/c2c763b3-d05d-46fe-9edc-5962f285fdc8" alt="Vertica">
</div>
<div style="text-align:center">
    <img src="https://github.com/TanaphatSaeung/Data-Engineer-Journey/assets/174108415/5cf8fab4-5234-41ea-8ddb-787926a00748" alt="Oracle Autonomous Data Warehouse">
</div>


# Selecting a Data Warehouse System
**Evaluating data warehouse systems**
1. Features and Capabilities
- Choose the location to store data from the previous section.
- to select location, organization must balance multiple demands
  - Security
  - Speed
  - Data privacy: requirements: such as CCPA or GDPR
- Architecture and Structure

2. Compatiblility and inplementation
- Governance
- Data migration
- Transformation capabilities
- Optimization
- User management
- Notification and reports

3. Ease of Use and skills
- Staff implementation skills
- Vendor or Implementation partner's data warehouse Implementation skills
- Technical and engineering staff front-end and administration skills for querying, reporting, and visualizaion tools

4. Support

5. Costs
- Total cost of ownership (TCO)

# Data Marts Overview
- It's an isolated part of the larger enterprise data warehouse
- Provide support for tactical decision-making
- Help end users focus only on relevant data
- Save time otherwise spent searching the data warehouse for answer

**Types of data marts**
- Dependent data marts
  
![2](https://github.com/TanaphatSaeung/Data-Engineer-Journey/assets/174108415/17d26110-9cd1-4df0-9fff-b19f69db2424)

- Independent data marts
  
![3](https://github.com/TanaphatSaeung/Data-Engineer-Journey/assets/174108415/066a268d-4bce-4d28-904f-6cb172cbfb3d)
- Hybrid data marts

![4](https://github.com/TanaphatSaeung/Data-Engineer-Journey/assets/174108415/90478149-5997-45c5-b886-da195fd71932)

## Data Lakes Overview

![5](https://github.com/TanaphatSaeung/Data-Engineer-Journey/assets/174108415/eae81d94-2804-42ed-aec3-769e7bd6e8c1)

- A storage repository that can store large amounts of all data types in their native format
- It is a pool of raw data
- Data can be loaded without defining the structure or schema of data
- Exists as a repository of raw data straight from the source, to be transformed based on the use case for which it needs to be analyzed
- Data lake is not the place where data can be dumped without governance

**Data Lake Benefits**
- Handles all types of data
- Scalable storage capacity
- Saves time that would have been used to define structures, create schemas, and transform data
- Can quickly repurpose data for a wide range of use cases

