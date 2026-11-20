from db_connect import connect_clinic
from functions.appointment_func import *
from classes import *
import pytest

@pytest.fixture
def connection():
    connection = connect_clinic()
    yield connection
    connection.close()

def test_view_appointments(connection):
    appointments = View_Appointments(connection)
    #Tests
    assert isinstance(appointments, list)
    assert all(isinstance(appointment[0], Appointment)
                and isinstance(appointment[1], Patient)
                and isinstance(appointment[2], Doctor)
                for appointment in appointments
    )

def test_view_search_appointment_date(connection):
    appointments = Search_Appointment_Date(connection, '2025-09-03')

    assert isinstance(appointments, list)
    assert all(isinstance(appointment[0], Appointment)
                and isinstance(appointment[1], Patient)
                and isinstance(appointment[2], Doctor)
                for appointment in appointments
    )

def test_view_search_appointment_patient(connection):
    appointments = Search_Appointment_Patient(connection, 1)

    assert isinstance(appointments, list)
    assert all(isinstance(appointment[0], Appointment)
                and isinstance(appointment[1], Patient)
                and isinstance(appointment[2], Doctor)
                for appointment in appointments
    )

def test_view_search_appointment_doctor(connection):
    appointments = Search_Appointment_Doctor(connection, 1)

    assert isinstance(appointments, list)
    assert all(isinstance(appointment[0], Appointment)
                and isinstance(appointment[1], Patient)
                and isinstance(appointment[2], Doctor)
                for appointment in appointments
    )




