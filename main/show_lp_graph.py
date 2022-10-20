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
connection = MySQLdb.connect()
