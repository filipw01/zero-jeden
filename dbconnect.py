import pymysql

def connection():
    conn = pymysql.connect(host='localhost',
                            user='flask',
                            password='b@z@d@nych',
                            db='flask',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()
    return c, conn
