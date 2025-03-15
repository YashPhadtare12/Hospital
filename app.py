from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# Load data from JSON file
def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            return json.load(file)
    return {"doctors": [], "appointments": [], "patients": [], "users": []}

# Save data to JSON file
def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Add Doctor Page
@app.route("/add-doctor", methods=["GET", "POST"])
def add_doctor():
    if request.method == "POST":
        data = load_data()
        new_doctor = {
            "name": request.form["doctor-name"],
            "mobile": request.form["mobile"],
            "email": request.form["email"],
            "gender": request.form["gender"],
            "dob": request.form["dob"],
            "address": request.form["address"],
            "specialization": request.form["specialization"],
            "experience": request.form["experience"],
            "qualification": request.form["qualification"],
            "consultation_fee": request.form["consultation-fee"],
        }
        data["doctors"].append(new_doctor)
        save_data(data)
        return redirect(url_for("home"))
    return render_template("add-doctor.html")

# Add Patient Page
@app.route("/add-patient", methods=["GET", "POST"])
def add_patient():
    if request.method == "POST":
        data = load_data()
        new_patient = {
            "name": request.form["patient-name"],
            "mobile": request.form["mobile"],
            "email": request.form["email"],
            "gender": request.form["gender"],
            "address": request.form["address"],
            "dob": request.form["dob"],
        }
        data["patients"].append(new_patient)
        save_data(data)
        return redirect(url_for("home"))
    return render_template("add-patient.html")

# Schedule Appointment Page
@app.route("/schedule-appointment", methods=["GET", "POST"])
def schedule_appointment():
    data = load_data()
    if request.method == "POST":
        new_appointment = {
            "patient_name": request.form["patient-name"],
            "doctor": request.form["doctor"],
            "date": request.form["date"],
            "time": request.form["time"],
            "status": "Scheduled",
        }
        data["appointments"].append(new_appointment)
        save_data(data)
        return redirect(url_for("view_appointments"))
    return render_template("schedule-appointments.html", doctors=data["doctors"])

# View Appointments Page
@app.route("/view-appointments")
def view_appointments():
    data = load_data()
    return render_template("view-appointments.html", appointments=data["appointments"])

# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = load_data()
        username = request.json.get("username")
        password = request.json.get("password")

        # Check if user exists
        user = next((user for user in data["users"] if user["username"] == username and user["password"] == password), None)
        if user:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": "Invalid username or password."})
    return render_template("login.html")

# Signup Page
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        data = load_data()
        name = request.json.get("name")
        email = request.json.get("email")
        username = request.json.get("username")
        password = request.json.get("password")

        # Check if username already exists
        if any(user["username"] == username for user in data["users"]):
            return jsonify({"success": False, "message": "Username already exists."})

        # Add new user
        new_user = {
            "name": name,
            "email": email,
            "username": username,
            "password": password,
        }
        data["users"].append(new_user)
        save_data(data)
        return jsonify({"success": True})
    return render_template("signup.html")

# Run the application
if __name__ == "__main__":
    app.run(debug=True)