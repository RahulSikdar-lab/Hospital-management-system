import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('hospital_management.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    address TEXT,
    phone TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS doctors (
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialty TEXT,
    phone TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    doctor_id INTEGER,
    appointment_date TEXT,
    appointment_time TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS bills (
    bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    amount REAL,
    bill_date TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
)
''')

conn.commit()
conn.close()

print("Database and tables created successfully!")
