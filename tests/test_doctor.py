from db_connect import connect_clinic
from functions.doctor_func import *
from classes import *
import pytest

@pytest.fixture
def connection():
    connection = connect_clinic()
    yield connection
    connection.close()

def test_view_doctors(connection):
    doctors = View_Doctors(connection)

    assert isinstance(doctors, list)
    assert all(isinstance(doctor, Doctor) for doctor in doctors)

def test_search_doctor(connection):
    doctors1 = Search_Doctor(connection, "Britta Svensson")
    doctors2 = Search_Doctor(connection, "Britta")
    doctors3 = Search_Doctor(connection, "Bri")

    #Tests
    assert isinstance(doctors1, list)
    assert all(isinstance(doctor, Doctor) for doctor in doctors1)
    assert isinstance(doctors2, list)
    assert all(isinstance(doctor, Doctor) for doctor in doctors2)
    assert isinstance(doctors3, list)
    assert all(isinstance(doctor, Doctor) for doctor in doctors3)

def test_search_doctor_patient(connection):
    patients = Search_Doctor_Patient(connection, 1)

    #Tests
    assert isinstance(patients, list)
    assert all(isinstance(patient, Patient) for patient in patients)

def test_view_doctors_id(connection):
    doctor = Search_Doctor_ID(connection, 1)

    assert isinstance(doctor, Doctor)
    assert doctor.doctor_name == "Britta Svensson"
    assert doctor.doctor_id == 1

def test_doctor_departments(connection):
    department = Search_Doctor_Department(connection, 1)

    assert isinstance(department, Department)
    assert department.department_name == "Cardiology"
    assert department.department_id == 1

