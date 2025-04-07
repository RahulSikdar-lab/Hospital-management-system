from hms import add_patient, add_doctor, add_appointment, add_bill, view_patients, view_appointments, view_bill

add_patient("Karan", 30, "Male", "123 Main St", "123-456-7890")
add_patient("Rohit", 28, "Female", "456 Oak St", "987-654-3210")

add_doctor("Dr. Vivek", "Cardiology", "555-1234")
add_doctor("Dr. Mohit", "Neurology", "555-5678")

add_appointment(1, 1, "2025-04-10", "10:00 AM")

add_bill(1, 200.50)

view_patients()

view_appointments(1)

view_bill(1)
