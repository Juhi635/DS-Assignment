from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'Juhi'

mysql = MySQL(app)


@app.route('/')
def registration_form():
    return render_template('registration_form.html')


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':

        student_name = request.form['student_name']
        father_name = request.form['father_name']
        mother_name = request.form['mother_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        dob = request.form['dob']
        address = request.form['address']
        blood_group = request.form['blood_group']
        department = request.form['department']
        course = request.form['course']
        password = request.form['password']


        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (student_name, father_name, mother_name, phone_number, email, dob, address, blood_group, department, course, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (student_name, father_name, mother_name, phone_number, email, dob, address, blood_group, department, course, password))
        mysql.connection.commit()
        cur.close()
        
        return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)