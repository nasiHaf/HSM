from classes import *

def View_Appointments(connection):
    """Creates a list of all the appointments in the database"""
    cursor = connection.cursor()
    cursor.execute("SELECT appointment.patient_id, " 
                    "patient.patient_name, "
                    "appointment.doctor_id, "
                    "doctor.doctor_name, "
                    "appointment.appointment_time "
                    "FROM appointment "
                    "JOIN patient "
                    "ON appointment.patient_id = patient.patient_id "
                    "JOIN doctor "
                    "ON appointment.doctor_id = doctor.doctor_id "
                    "ORDER BY appointment.appointment_time DESC;"
                    )
    appointments = cursor.fetchall()

    list_appointments = []

    for info in appointments:
        patient = Patient(info[0], info[1])
        doctor = Doctor(info[2], info[3])
        appointment = Appointment(info[0], info[2], info[4])
        list_appointments.append((appointment, patient, doctor))

    cursor.close()
    return list_appointments

def Search_Appointment_Date(connection, appointment_date):
    """Searches for all appointments on a specific date."""
    cursor = connection.cursor()
    cursor.execute("SELECT appointment.patient_id, "
                    "patient.patient_name, "
                    "appointment.doctor_id, "
                    "doctor.doctor_name, "
                    "appointment.appointment_time "
                    "FROM appointment "
                    "JOIN patient "
                    "ON appointment.patient_id = patient.patient_id "
                    "JOIN doctor "
                    "ON appointment.doctor_id = doctor.doctor_id "
                    "WHERE DATE(appointment.appointment_time) = %s",
                    (appointment_date,)
    )
    appointments = cursor.fetchall()
    list_appointments = []

    for info in appointments:
        patient = Patient(info[0], info[1])
        doctor = Doctor(info[2], info[3])
        appointment_time = Appointment(info[0], info[2], info[4])
        list_appointments.append((appointment_time, patient, doctor))

    cursor.close()
    return list_appointments

def Search_Appointment_Patient(connection, patient_id):
    """Search a patient on patient id and get the appointments"""

    cursor = connection.cursor()
    cursor.execute("SELECT appointment.patient_id, "
                    "patient.patient_name, "
                    "appointment.doctor_id, "
                    "doctor.doctor_name, "
                    "appointment.appointment_time "
                    "FROM appointment "
                    "JOIN patient "
                    "ON appointment.patient_id = patient.patient_id "
                    "JOIN doctor "
                    "ON appointment.doctor_id = doctor.doctor_id "
                    "WHERE appointment.patient_id = %s",
                    (patient_id,)
    )
    appointments = cursor.fetchall()
    list_appointments = []
    
    for info in appointments:
        #Create patient,doctor and appointment option
        patient = Patient(info[0], info[1])
        doctor = Doctor(info[2], info[3])
        appointment_time = Appointment(info[0], info[2], info[4])
        list_appointments.append((appointment_time, patient, doctor))
    
    cursor.close()  
    return list_appointments

def Search_Appointment_Doctor(connection, doctor_id):
    """Search a patient on patient id and get the appointments"""

    cursor = connection.cursor()
    cursor.execute("SELECT appointment.patient_id, "
                    "patient.patient_name, "
                    "appointment.doctor_id, "
                    "doctor.doctor_name, "
                    "appointment.appointment_time "
                    "FROM appointment "
                    "JOIN patient "
                    "ON appointment.patient_id = patient.patient_id "
                    "JOIN doctor "
                    "ON appointment.doctor_id = doctor.doctor_id "
                    "WHERE appointment.doctor_id = %s",
                    (doctor_id,)
    )
    appointments = cursor.fetchall()
    list_appointments = []
    
    for info in appointments:
        #Create patient,doctor and appointment option
        patient = Patient(info[0], info[1])
        doctor = Doctor(info[2], info[3])
        appointment_time = Appointment(info[0], info[2], info[4])
        list_appointments.append((appointment_time, patient, doctor))
    
    cursor.close()  
    return list_appointments