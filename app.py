from flask import Flask, jsonify, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)
# Configure db
db = yaml.safe_load(open('db.yaml'))  
#db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] =  db['mysql_database']

mysql = MySQL(app)

@app.route('/trivia')
def trivia():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users ORDER BY rand() LIMIT 1")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)
      
if __name__ == '__main__':
     
    app.debug = True
    app.run(host='0.0.0.0',port=70)
