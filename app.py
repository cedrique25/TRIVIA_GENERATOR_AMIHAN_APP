from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure db
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)


@app.route('/my-link/')
def my_link():
  print ('I got clicked!')

  return 'Click.'

@app.route('/trivia1.html')
def trivia1():
  return render_template('trivia1.html')

@app.route('/trivia2.html')
def trivia2():
  return render_template('trivia2.html')

@app.route('/trivia3.html')
def trivia3():
  return render_template('trivia3.html')

@app.route('/trivia4.html')
def trivia4():
  return render_template('trivia4.html')

@app.route('/trivia5.html')
def trivia5():
  return render_template('trivia5.html')

@app.route('/trivia6.html')
def trivia6():
  return render_template('trivia6.html')

if __name__ == '__main__':
    app.run(debug=True)
