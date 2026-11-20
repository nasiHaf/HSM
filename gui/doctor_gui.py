import streamlit as st  
from functions.doctor_func import *

def doctor_gui(connection):
    """The options for the Doctor page"""
    doctor_option = st.selectbox("Doctor:", 
                                [
                                "Choose an option",
                                "View Doctors",
                                "Search Doctor",
                                "Search Doctor's Patients",
                                "Search Doctor's Department"
                                ],
                                key="doctor_menu"
    )
    
    #We get a list of all the doctors in the database and prints them in alphabetic order
    if doctor_option == "View Doctors": 
        doctors = View_Doctors(connection)
        if doctors:
            for doctor in doctors:
                st.write(f"Doctor ID: {doctor.doctor_id} | "
                         f"Doctor Name: {doctor.doctor_name}")
        else:
            st.error("No doctors in the database!")

    #Search a doctors name and shows the doctor id and the doctors name
    elif doctor_option == "Search Doctor":
        doctor_name = st.text_input("Enter doctor name:")
        if st.button("Search"):
            #There can be multiple doctors with the same name
            doctors = Search_Doctor(connection, doctor_name)
            if doctors:
                for doctor in doctors:
                    st.write(f"Doctor ID: {doctor.doctor_id} | "
                             f"Doctor Name: {doctor.doctor_name}")
            else:
                st.error("The Doctor was not found, try again!")


    elif doctor_option == "Search Doctor's Patients":
        doctor_id = st.text_input("Enter doctor id:")
        if st.button("Search"):
            try:
                doctor_id = int(doctor_id)
                doctor = Search_Doctor_ID(connection, doctor_id)
                if doctor is None:
                    st.error("Doctor not found. Try again!")
                else:
                    patients = Search_Doctor_Patient(connection, doctor_id)
                    if patients:
                        for patient in patients:
                            st.write(f"Patient ID: {patient.patient_id} | "
                                     f"Patient Name: {patient.patient_name}"
                            )
                    else:
                        st.error("Patients not found. Try again!")
            except ValueError:
                st.error("Please enter a valid Doctor ID.")

    elif doctor_option == "Search Doctor's Department":
        doctor_id = st.text_input("Enter doctor id:")
        if st.button("Search"):
            try:
                doctor_id = int(doctor_id)
                doctor = Search_Doctor_ID(connection, doctor_id)
                if doctor is None:
                    st.error("Doctor not found. Try again!")
                else:
                    department = Search_Doctor_Department(connection, doctor_id)
                    if department:
                        st.write(f"Department ID: {department.department_id} | "
                                 f"Department Name: {department.department_name}"
                            )
                    else:
                        st.error("Department not found, try again!")
            except ValueError:
                st.error("Please enter a valid Doctor ID.")



