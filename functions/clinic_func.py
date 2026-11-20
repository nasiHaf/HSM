from classes import *

def View_Clinics(connection):
    """Creates a list of all the clinics as clinic object from the database"""
    cursor = connection.cursor()
    cursor.execute("SELECT clinic_id, " 
                   "clinic_name, " 
                   "clinic_address "
                   "FROM clinic "
                   "ORDER BY clinic_name DESC"
                   )
    clinics = cursor.fetchall()
    list_clinics = []
    for info in clinics:
        #create a clinic object
        clinic = Clinic(info[0], info[1], info[2])
        list_clinics.append(clinic)
    cursor.close()
    return list_clinics


def Search_Clinic(connection,clinic_name):
    """Search clinic by name"""
    cursor = connection.cursor()
    cursor.execute("SELECT clinic_id, "
                    "clinic_name, "
                    "clinic_address "
                    "FROM clinic "
                    "WHERE clinic_name LIKE %s",
                    (f"%{clinic_name}%",)
    )
    
    clinics = cursor.fetchall()
    list_clinics = []

    for info in clinics:
        #create a clinic object and add to the list
        clinic = Clinic(info[0], info[1], info[2])
        list_clinics.append(clinic)

    cursor.close()
    return list_clinics

def Search_Clinics_Departments(connection,clinic_id):
    """Search a clinic and get all department that are in this clinic"""
    cursor = connection.cursor()
    cursor.execute("SELECT department_id, department_name "
                    "FROM clinic "
                    "JOIN department "
                    "ON clinic.clinic_id = department.clinic_id "
                    "WHERE clinic.clinic_id = %s",
                    (clinic_id,)
                    )
    departments = cursor.fetchall()
    list_departments = []
    
    for info in departments:
            department = Department(info[0], info[1])
            list_departments.append(department)
    return list_departments