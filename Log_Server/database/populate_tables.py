from database.database_connection import connect

db = connect()
cursor = db.cursor()

#create table
cursor.execute("""CREATE TABLE IF NOT EXISTS Info(
id INT,
microservice VARCHAR(255),
begin_request_time TIMESTAMP(6),
end_request_time TIMESTAMP(6),
client_ip VARCHAR(255),
client_port INT,
function_called VARCHAR(255),
microservice_instance VARCHAR(255),
PRIMARY KEY(id))""")
db.commit()

cursor.execute(""" SET @@GLOBAL.local_infile = 1; """)

cursor.execute(""" LOAD DATA LOCAL INFILE '../Data.csv'
INTO TABLE Info
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
ignore 1 ROWS; """)
db.commit()
cursor.close()


