"""All functions for the doctor page"""
from classes import *

def View_Doctors(connection):
    """Creates a list of all the doctors from the database"""
    cursor = connection.cursor()
    cursor.execute("SELECT doctor_id, "
                    "doctor_name "
                    "FROM doctor "
                    "ORDER BY doctor_name ASC"
                   )
    doctors = cursor.fetchall()
    list_doctors = []

    for info in doctors:
        #create a doctor object
        doctor = Doctor(info[0], info[1])
        list_doctors.append(doctor)

    cursor.close()
    return list_doctors

def Search_Doctor(connection, doctor_name):
    """Searches a doctor by name"""
    cursor = connection.cursor()
    cursor.execute("SELECT doctor_id, " \
                    "doctor_name " 
                    "FROM doctor " 
                    "WHERE doctor_name LIKE %s",
                    (f"%{doctor_name}%",)
    )
    doctors = cursor.fetchall()
    list_doctors = []
    

    for info in doctors:
        doctor = Doctor(info[0], info[1])
        list_doctors.append(doctor)

    cursor.close()
    return list_doctors

def Search_Doctor_Patient(connection, doctor_id):
    """Search for a doctor's patients"""
    cursor = connection.cursor()
    cursor.execute("SELECT patient_id, "
                   "patient_name " 
                   "FROM patient " 
                   "WHERE doctor_id = %s",
                    (doctor_id,)
    )
    patients = cursor.fetchall()
    list_patients = []

    for info in patients:
        patient = Patient(info[0], info[1])
        list_patients.append(patient)

    cursor.close()
    return list_patients

def Search_Doctor_ID(connection, doctor_id):
    """Searches a doctor by the doctor's id"""
    cursor = connection.cursor()
    cursor.execute("SELECT doctor_id, "
                   "doctor_name " 
                   "FROM doctor " 
                   "WHERE doctor_id = %s",
                    (doctor_id,)
    )
    doctor = cursor.fetchone()
    cursor.close()

    if doctor is None:
        return None
    return Doctor(doctor[0], doctor[1])    
    

def Search_Doctor_Department(connection, doctor_id):
    """Searches a doctor's department by id"""
    cursor = connection.cursor()
    cursor.execute("SELECT department.department_id, "
                   "department.department_name " 
                   "FROM department " 
                   "JOIN doctor "
                   "ON department.department_id =doctor.department_id "
                   "WHERE doctor.doctor_id = %s "
                   "LIMIT 1",
                   (doctor_id,)
    )
    department = cursor.fetchone()
    cursor.close()

    if department is None:
        return None
    return Department(department[0], department[1])