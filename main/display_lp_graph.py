import matplotlib.pyplot as plt
import MySQLdb
import matplotlib.dates as mdate


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

cursor.execute("""
    select access_date, league_point
    from online_match
    where fighters_id = 'test'
    order by access_date
;""")

#タプルを転置してリストにする
data = [list(tup) for tup in zip(*cursor.fetchall())]

fig, ax = plt.subplots()
fig.autofmt_xdate()
ax.plot(data[0], data[1])

formatter = mdate.DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_formatter(formatter)

fig.savefig('lpgraph/out.png')

connection.close()
