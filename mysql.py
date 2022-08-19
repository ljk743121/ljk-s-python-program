import pymysql
import pprint

HOST= "6noc3qgxo6l1.ap-northeast-2.psdb.cloud"
USERNAME="bjjb8e27lpot"
PASSWORD="pscale_pw_J6irUp9i0vxMGrFMPEso3d8XUDTctQap_hq41zIL81k"
DATABASE="github-page"
SSL_MODE = "VERIFY_IDENTITY"
SSL = {"ca": "/etc/ssl/cert.pem"}

connection = pymysql.connect(HOST,USERNAME,PASSWORD,DATABASE,ssl=SSL)
cursor = connection.cursor()
cursor.execute("SELECT VERSION()")
result = cursor.fetchone()

pprint.pprint(connection)
pprint.pprint(cursor)
pprint.pprint(result)

cursor.close()
connection.close()