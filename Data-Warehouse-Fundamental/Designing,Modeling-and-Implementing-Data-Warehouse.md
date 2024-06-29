# Overview of Data Warehouse Architecture

## Data warehouse Architecture
- depend on  use cases

**General EDW(Enterprise Data Warehouse) Architecture**
![6](https://github.com/TanaphatSaeung/Data-Engineer-Journey/assets/174108415/587ffd2a-91b8-4822-81e3-086fb80f6892)
- Data sources: flat file, Database, and Operation System
- Staging Area/ Sandbox: for holding data and developing workplows
- Between the Enterprise Data Warehouse Repository, security data is incoming and passing
- Data Marts: Known as and spoke

**EDW reference architectures**
- Adaption of general model
- Interoperability: A data ware house platform is complex, thus, Interoperability is vital
- Tool integrations tested

**IBM Reference Architecture**

![7](https://github.com/TanaphatSaeung/Data-Engineer-Journey/assets/174108415/aaa54eff-5c82-453f-bb80-29515e8ecb2e)

- Left side (data aquisition): Consists of components to acquire raw data from the source system
- IBM InfoSphere Metadata Workbench: Provide End-to-End data flow reporting
- IBM InfoSphere DataStage: To support data quality and information governance
- IBM InfoSphere DataStage
  - Scalable ETL plaform , and
  - Data Integration: For ETL the data into repository
- IBM Db2 Warehouse: Manage all types structured data
- IBM Cognos Analytics: General report, Scoreboard and dashborad

## Cubes, Rollups, and Meteriallized Views and Tables
Data Cube: 
