import MySQLdb


def read_mysql_enviroment():
    d = {}
    with open('./confidential/.env', 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            key, value = line.split('=')
            d[key] = value
    return d


mysql_environment = read_mysql_enviroment()
connection = MySQLdb.connect(
    host="127.0.0.1",
    user=mysql_environment["MYSQL_USER"],
    password=mysql_environment["MYSQL_PASSWORD"],
    db=mysql_environment["MYSQL_DATABASE"],
    port=13306
)

cursor = connection.cursor()

cursor.execute("select access_date, league_point from online_match where fighters_id = 'test' order by access_date;")

for (access_date, league_point) in cursor:
    print(access_date, league_point)

connection.close()
