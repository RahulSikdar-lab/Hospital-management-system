import sqlite3
from datetime import datetime

conn = sqlite3.connect('hospital_management.db')
cursor = conn.cursor()

def add_patient(name, age, gender, address, phone):
    try:
        cursor.execute('''INSERT INTO patients (name, age, gender, address, phone)
                          VALUES (?, ?, ?, ?, ?)''', (name, age, gender, address, phone))
        conn.commit()
        print(f"Patient {name} added successfully.")
    except sqlite3.Error as e:
        print(f"Error occurred while adding patient: {e}")

def add_doctor(name, specialty, phone):
    try:
        cursor.execute('''INSERT INTO doctors (name, specialty, phone)
                          VALUES (?, ?, ?)''', (name, specialty, phone))
        conn.commit()
        print(f"Doctor {name} added successfully.")
    except sqlite3.Error as e:
        print(f"Error occurred while adding doctor: {e}")

def add_appointment(patient_id, doctor_id, appointment_date, appointment_time):
    try:
        cursor.execute('''INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time)
                          VALUES (?, ?, ?, ?)''', (patient_id, doctor_id, appointment_date, appointment_time))
        conn.commit()
        print(f"Appointment added successfully for patient ID {patient_id}.")
    except sqlite3.Error as e:
        print(f"Error occurred while adding appointment: {e}")

def add_bill(patient_id, amount):
    try:
        bill_date = datetime.now().strftime('%Y-%m-%d')
        cursor.execute('''INSERT INTO bills (patient_id, amount, bill_date)
                          VALUES (?, ?, ?)''', (patient_id, amount, bill_date))
        conn.commit()
        print(f"Bill of amount {amount} added for patient ID {patient_id}.")
    except sqlite3.Error as e:
        print(f"Error occurred while adding bill: {e}")

def view_patients():
    cursor.execute('SELECT * FROM patients')
    patients = cursor.fetchall()
    print("Patients in the database:")
    for patient in patients:
        print(patient)

def view_appointments(patient_id):
    try:
        cursor.execute('''SELECT a.appointment_date, a.appointment_time, d.name 
                         FROM appointments a
                         JOIN doctors d ON a.doctor_id = d.doctor_id
                         WHERE a.patient_id = ?''', (patient_id,))
        appointments = cursor.fetchall()
        if appointments:
            print(f"Appointments for patient ID {patient_id}:")
            for appointment in appointments:
                print(f"Date: {appointment[0]}, Time: {appointment[1]}, Doctor: {appointment[2]}")
        else:
            print(f"No appointments found for patient ID {patient_id}.")
    except sqlite3.Error as e:
        print(f"Error occurred while fetching appointments: {e}")

def view_bill(patient_id):
    try:
        cursor.execute('''SELECT b.bill_date, b.amount
                          FROM bills b
                          WHERE b.patient_id = ?''', (patient_id,))
        bills = cursor.fetchall()
        if bills:
            print(f"Bills for patient ID {patient_id}:")
            for bill in bills:
                print(f"Bill Date: {bill[0]}, Amount: {bill[1]}")
        else:
            print(f"No bills found for patient ID {patient_id}.")
    except sqlite3.Error as e:
        print(f"Error occurred while fetching bills: {e}")

