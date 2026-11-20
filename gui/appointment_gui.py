import streamlit as st  
from functions.appointment_func import *
from functions.doctor_func import Search_Doctor_ID
from functions.patient_func import Search_Patient_ID
from datetime import datetime


def appointment_gui(connection):
    """The options for the Appointment page"""    
    appointment_option = st.selectbox("Appointment:", 
                                        [
                                        "Choose an option",
                                        "View Appointments",
                                        "Search Appointments by Date",
                                        "Search Appointment by Patient",
                                        "Search Appointment by Doctor"
                                        ],
                                        key="appointment_menu"
    )
    
    #Prints all the appointments ever in order of time
    if appointment_option == "View Appointments": 
        appointments = View_Appointments(connection)
        if appointments:
            for appointment, patient, doctor in appointments:
                st.write(f"Patient Name: {patient.patient_name} | "
                         f"Doctor Name: {doctor.doctor_name} | "
                         f"Appointment time: {appointment.appointment_time}")
        else:
            st.error("No appointments in the database!")

    #Searches for all the appointments on one day YYYY-MM-DD, so we get the time of the appointments
    elif appointment_option == "Search Appointments by Date":
        appointment_date = st.text_input("Enter date:")           
        if st.button("Search"):
            try:
                #change the type to DATETIME
                appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d").date()
                appointments = Search_Appointment_Date(connection, appointment_date)
                if appointments:
                    for appointment, patient, doctor in appointments:
                        st.write(f"Patient Name: {patient.patient_name} | "
                                 f"Doctor Name: {doctor.doctor_name} | "
                                 f"Appointment time: {appointment.appointment_time}")
                else:
                    st.error("No appointments were found.")
            except ValueError:
                st.error("Please enter a valid date in the format YYYY-MM-DD.")

    #Searches for all the appointments for a Patient
    elif appointment_option == "Search Appointment by Patient":
        try:
            patient_id = st.text_input("Enter patient ID:")
            if st.button("Search"):
                #change the type to int
                patient_id =int(patient_id)
                patient = Search_Patient_ID(connection, patient_id)
                if patient is None:
                    st.error("Patient not found. Try again!")
                else:
                    appointments = Search_Appointment_Patient(connection, patient_id)
                    if appointments:
                        for appointment, patient, doctor in appointments:
                            st.write(f"Patient Name: {patient.patient_name} | "
                                     f"Doctor Name: {doctor.doctor_name} | "
                                     f"Appointment time: {appointment.appointment_time}")
                    else:
                        st.error("Appointments not found. Try again!")
        except ValueError:
            st.error("Please enter a valid Patient ID.")

#Searches for all the appointments for a Doctor
    elif appointment_option == "Search Appointment by Doctor":
        try:
            doctor_id = st.text_input("Enter doctor ID:")
            if st.button("Search"):
                #change the type to int
                doctor_id =int(doctor_id)
                doctor = Search_Doctor_ID(connection, doctor_id)
                if doctor is None:
                    st.error("Doctor not found. Try again!")
                else:
                    appointments = Search_Appointment_Doctor(connection, doctor_id)
                    if appointments:
                        for appointment, patient, doctor in appointments:
                            st.write(f"Patient Name: {patient.patient_name} | "
                                     f"Doctor Name: {doctor.doctor_name} | "
                                     f"Appointment time: {appointment.appointment_time}")
                    else:
                        st.error("Appointments not found. Try again!")
        except ValueError:
            st.error("Please enter a valid Doctor ID.")