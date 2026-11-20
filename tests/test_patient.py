from db_connect import connect_clinic
from functions.patient_func import *
from classes import *
import pytest

#Create a connection, use a test database...
@pytest.fixture
def connection():
    connection = connect_clinic()
    yield connection
    connection.close()

def test_view_patient(connection):
    patients = View_Patients(connection)

    #Tests
    assert isinstance(patients, list)
    assert all(isinstance(patient, Patient) for patient in patients)

def test_search_patient(connection):
    patients1 = Search_Patient(connection, "Anna Persson")
    patients2 = Search_Patient(connection, "Anna")
    patients3 =Search_Patient(connection, "A")

    #Tests
    assert isinstance(patients1, list)
    assert all(isinstance(patient, Patient) for patient in patients1)
    assert isinstance(patients2, list)
    assert all(isinstance(patient, Patient) for patient in patients2)
    assert isinstance(patients3, list)
    assert all(isinstance(patient, Patient) for patient in patients3)

def test_search_patient_doctor(connection):
    doctor = Search_Patient_Doctor(connection, 1)

    assert isinstance(doctor, Doctor)
    assert doctor.doctor_name == 'Britta Svensson'
    assert doctor.doctor_id == 1


def test_search_diagnosis_patient(connection):
    diagnoses = Search_Diagnosis_Patient(connection, 1)

    #Tests
    assert isinstance(diagnoses, list)
    assert all(isinstance(diagnosis, Diagnosis) for diagnosis in diagnoses)

def test_search_patient_id(connection):
    patient = Search_Patient_ID(connection, 1)

    assert isinstance(patient, Patient)
    assert patient.patient_name == "Anna Persson"
    assert patient.patient_id == 1
