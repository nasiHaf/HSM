from classes import *

def View_Patients(connection):
    """Creates a list of all the patients in the database"""
    cursor = connection.cursor()
    cursor.execute("SELECT patient_id, "
                   "patient_name " 
                   "FROM patient "
                   "ORDER BY patient_name ASC"
    )
    patients = cursor.fetchall()

    list_patients = []
    for info in patients:
        #create a patient object
        patient = Patient(info[0], info[1])
        list_patients.append(patient)

    cursor.close()
    return list_patients

def Search_Patient(connection, patient_name):
    """Searches the patient and create patient objects and return a list"""    
    cursor = connection.cursor()
    cursor.execute("SELECT patient_id," \
                    " patient_name "
                    "FROM patient "
                    "WHERE patient_name LIKE %s",
                    (f"%{patient_name}%",)
    )
    
    patients = cursor.fetchall()
    list_patients = []

    for info in patients:
        #create a patient object and add to the list
        patient = Patient(info[0], info[1])
        list_patients.append(patient)

    cursor.close()
    return list_patients

def Search_Patient_Doctor(connection, patient_id):
    """Search a patient's doctor"""
    cursor = connection.cursor()
    cursor.execute("SELECT doctor.doctor_id, doctor.doctor_name " 
                    "FROM doctor " 
                    "JOIN patient "
                    "ON doctor.doctor_id = patient.doctor_id "
                    "WHERE patient_id = %s",
                    (patient_id,)
    )
    doctor = cursor.fetchone()
    cursor.close()

    if doctor is None:
        return None
    return Doctor(doctor[0], doctor[1])


def Search_Diagnosis_Patient(connection, patient_id):
    """Search a patients all diagnoses"""

    cursor = connection.cursor()
    cursor.execute("SELECT appointment.diagnosis,"
                    "appointment.observation "
                    "FROM appointment "
                    "JOIN patient "
                    "ON patient.patient_id = appointment.patient_id "
                    "WHERE patient.patient_id = %s",
                    (patient_id,)
    )
    diagnoses = cursor.fetchall()
    list_diagnoses = []

    for info in diagnoses:
        diagnosis = Diagnosis(info[0], info[1])
        list_diagnoses.append(diagnosis)
    return list_diagnoses


def Search_Patient_ID(connection, patient_id):
    """Searches a patient by id, used in a appointment function"""
    cursor = connection.cursor()
    cursor.execute("SELECT patient_id, patient_name " 
                    "FROM patient " 
                    "WHERE patient_id = %s",
                    (patient_id,)
    )
    patient = cursor.fetchone()
    cursor.close()

    if patient is None:
        return None
    
    return Patient(patient[0], patient[1])