import pymysql

# Connect to database
cnx = pymysql.connect(user='dev',
                      password='ax2',
                      host='127.0.0.1',
                      port=3307,
                      db='People')

# Create a cursor object
cursor = cnx.cursor()

#---------------------------------------------#
# If the table doesnt exist do this only once!
## SQL query string
newTable = "CREATE TABLE People(id int auto_increment primary key, Name varchar(32))"
try:
## Execute the sqlQuery
    cursor.execute(newTable)

## Throw exeception if failed
except Exception as e:
    print("Exeception occured:{}".format(e))

finally:
## Close connection    
    cursor.close()
#--------------------------------------------#


