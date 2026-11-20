from db_connect import connect_clinic
from functions.clinic_func import *
from classes import *
import pytest

@pytest.fixture
def connection():
    connection = connect_clinic()
    yield connection
    connection.close()

def test_view_clinics(connection):
    clinics = View_Clinics(connection)
    #Tests
    assert isinstance(clinics, list)
    assert all(isinstance(clinic, Clinic) for clinic in clinics)

def test_search_clinic(connection):
    clinics1 = Search_Clinic(connection, 'Karolinska Sjukhuset')
    clinics2 = Search_Clinic(connection, 'Karolinska')
    clinics3 = Search_Clinic(connection, 'Kar')

    #Tests
    assert isinstance(clinics1, list)
    assert all(isinstance(clinic, Clinic) for clinic in clinics1)
    assert isinstance(clinics2, list)
    assert all(isinstance(clinic, Clinic) for clinic in clinics2)
    assert isinstance(clinics3, list)
    assert all(isinstance(clinic, Clinic) for clinic in clinics3)

def test_search_clinics_departments(connection):
    departments = Search_Clinics_Departments(connection,1)

    #Tests
    assert isinstance(departments, list)
    assert all(isinstance(department,Department)for department in departments)
