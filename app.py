#from crypt import methods
from multiprocessing import connection
from pickle import GET
from uu import Error
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

from flask import Flask, request, jsonify, render_template
from google.cloud import aiplatform

from flask import Flask, request, jsonify
import openai
import os

openai.api_key = os.getenv("IzaSyDrxh7Jyk8faCRoBlTthy5nDCPGuGlFVRg")



app = Flask(__name__)
app.secret_key = "your_secret_key"

# MySQL database configuration
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'user_db'
}

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
    except Error as e:
        print(f"the error '{e}' occured!!")
    return connection



@app.route('/')
def home():
    return render_template('home.html')

# Rider login page
@app.route('/riderlogin', methods=['GET', 'POST'])
def rider():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and check_password_hash(user[5], password):
            session['user_id'] = user[0]
            flash("Login successful!", "success")
            return redirect(url_for('ridebooking'))
        else:
            flash("Invalid username or password", "error")
            return redirect(url_for('riderhomepage'))
    
    return render_template('riderlogin.html')

# Ride booking
@app.route('/ridebooking', methods=['POST','GET'])
def ridebook():

    return render_template('ridebooking.html')

# Rider Account registration
@app.route('/riderregister', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        phone = request.form['phone']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        if password != confirm_password:
            flash("Passwords do not match!", "error")
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (first_name, last_name, phone, username, password) VALUES (%s, %s, %s, %s, %s)",
                (first_name, last_name, phone, username, hashed_password)
            )
            conn.commit()
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for('/riderlogin'))
        except mysql.connector.Error as err:
            flash("Username already exists!", "error")
            return redirect(url_for('register'))
        finally:
            cursor.close()
            conn.close()

    return render_template('riderregister.html')

# Driver login page
@app.route('/driverlogin')
def driver():
    return render_template('driver.html')

# Admin login page
@app.route('/adminlogin')
def admin():
    return render_template('admin.html')

# Sample dashboard route
@app.route('/dashboard1', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        # Retrieve form data
        pickup_location = request.form['pickup_location']
        drop_location = request.form['drop_location']
        timing = request.form['timing']

        # For now, we'll just print them, but here is where you would save to a database.
        print("Pickup Location:", pickup_location)
        print("Drop Location:", drop_location)
        print("Timing:", timing)

        flash("Ride details saved successfully!", "success")
        return redirect(url_for('dashboard1'))

    return render_template('dashboard1.html')

# rider home page

@app.route('/riderprofile')
def riderhome():

    return render_template('riderhomepage.html')
# rider profile
@app.route('/rprofile')
def profile():

    return render_template('riderprofile.html')

# ride booked
@app.route('/bride', methods=['POST', 'GET'])
def bride():

    return render_template('bride.html')

# payment
@app.route('/payment')
def payment():

    return render_template("payment.html")

#--------------------------------------------------------------------------------------#

# admin dashboard
@app.route('/Adashboard')
def adashboard():


    return render_template("Adashboard.html")

# user management
@app.route('/usermanagement')
def usermanagemnt():

    return render_template("usermanagement.html")

# ride monitoring
@app.route("/ridemonitoring")
def ridemonitoring():
    return render_template('ridemonitoring.html')

# reports
@app.route('/reports')
def reports():
    return render_template('reports.html')

# issue management
@app.route('/issuemanagement')
def issuemanagement():
    return render_template('issuemanagement.html')


# policy management
@app.route('/policymanagement')
def policymanagement():
    return render_template('policymanagement.html')

#---------------------------------------------------------------------------------------------#

@app.route('/dlogin')
def dlogin():

    return render_template("driver.html")

@app.route('/ddashboard')
def ddashboard():

    return render_template("dhomepage.html")

@app.route('/postridepage')
def postridepage():

    return render_template('dpostpage.html')

@app.route('/driderrequest')
def driderrequest():
    return render_template('riderequest.html')

@app.route('/tripdetailpage')
def tripdetailpage():

    return render_template('tripdetailpage.html')

@app.route('/paymentsummary')
def paymentsummary():

    return render_template('paymentsummary.html')

@app.route('/feedback')
def feedback():
    return render_template('feedbackpage.html')

@app.route('/customercare')
def customercare():

    return render_template('customercare.html')


# Set your OpenAI API key
openai.api_key = 'IzaSyDrxh7Jyk8faCRoBlTthy5nDCPGuGlFVRg'


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "Message field is required"}), 400

    try:
        # Replace with your specific Vertex AI model call
        model = aiplatform.TextGenerationModel.from_pretrained("IzaSyDrxh7Jyk8faCRoBlTthy5nDCPGuGlFVRg")
        response = model.predict(user_message)
        return jsonify({"reply": response.text})

    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500








if __name__ == '__main__':
    app.run(debug=True)
