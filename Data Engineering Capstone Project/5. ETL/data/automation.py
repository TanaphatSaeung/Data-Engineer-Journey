import mysql.connector
import ibm_db
#before use this auto
#use: call sysproc.admin_cmd('reorg table gpw87924.SALES_DATA');
#to avoid: Exception Error: Code "7" SQLSTATE=57007 SQLCODE=-668
#then you can you this python code

# Connect to MySQL
connection = mysql.connector.connect(user='root', password='xucKpPcB6tLLtkslPlf1thoj', host='172.21.72.177', database='sales')

# Create cursor
cursor = connection.cursor()

# Connect to DB2
dsn_hostname = "0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
dsn_uid = "gpw87924"
dsn_pwd = "Z1vOihd3nQK8EURl"
dsn_port = "31198"
dsn_database = "bludb"
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_protocol = "TCPIP"
dsn_security = "SSL"

# Create the dsn connection string
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd, dsn_security)

# Create connection
conn = ibm_db.connect(dsn, "", "")
print("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

def get_last_rowid():
    SQL = "SELECT MAX(ROWID) FROM sales_data"
    stmt = ibm_db.exec_immediate(conn, SQL)
    res = ibm_db.fetch_both(stmt)
    print(res)
    return int(res[0])

last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with 
# rowid greater than the one on the Data warehouse
# The function get_latest_records must return a 
# list of all records that have a rowid greater than 
# the last_row_id in the sales_data table in the 
# sales database on the MySQL staging data warehouse.

def get_latest_records(rowid):
    SQL = "SELECT * FROM sales_data WHERE rowid > %s"
    cursor.execute(SQL, [rowid])
    new_recs = cursor.fetchall()
    # for row in new_recs: print(row)
    return new_recs

new_records = get_latest_records(last_row_id)

print("New rows on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into DB2 data warehouse.
# The function insert_records must insert all the records passed
# to it into the sales_data table in IBM DB2 database.

def insert_records(records):
    SQL = "INSERT INTO sales_data(rowid,product_id,customer_id,quantity) VALUES(?,?,?,?);"
    stmt = ibm_db.prepare(conn, SQL)

    for record in records:
        print(record)
        ibm_db.execute(stmt, record)

insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse
connection.close()

# disconnect from DB2 data warehouse
ibm_db.close(conn)

# End of program
