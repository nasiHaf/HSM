import streamlit as st  
from functions.patient_func import *

def patient_gui(connection):   
    """The options for the patient page"""
    patient_option = st.selectbox("Patient:",
                                [
                                "Choose an options", 
                                "View Patients", 
                                "Search Patient",
                                "Search Patient's Doctor",
                                "Search Diagnoses"
                                ],
                                key="patient_menu"
    )
    #We get a list of the patients and prints the patient in alphabetic order
    if patient_option == "View Patients":
        patients = View_Patients(connection)
        if patients:
            for patient in patients:
                st.write(f"Patient ID: {patient.patient_id} | "
                         f"Patient Name: {patient.patient_name}")
        else:
            st.error("No patients in the database!")

    #Search a patient name and prints it if it exists
    elif patient_option == "Search Patient":
        patient_name = st.text_input("Enter patient name:")
        if st.button("Search"):
            #There can be multiple patients with the same name, or we search first name or surname
            patient_name = patient_name.strip()
            patients = Search_Patient(connection, patient_name)
            if patients:
                for patient in patients:
                    st.write(f"Patient ID: {patient.patient_id} | "
                             f"Patient Name: {patient.patient_name}")
            else:
                st.error("Patient not found, try again!")

    #Search a patient's doctor
    elif patient_option == "Search Patient's Doctor":
        patient_id = st.text_input("Enter patient ID: ")
        if st.button("Search"):
            try:
                patient_id = int(patient_id)
                patient = Search_Patient_ID(connection, patient_id)
                if patient is None:
                    st.error("Patient not found. Try again!")
                else:
                    doctor = Search_Patient_Doctor(connection, patient_id)
                    st.write(f"Doctor ID: {doctor.doctor_id} | "
                             f"Doctor Name: {doctor.doctor_name}")
            except ValueError:
                st.error("Please enter a valid Patient ID.")


    #Search a patient id and get the diagnoses the patient have
    elif patient_option == "Search Diagnoses":
        patient_id = st.text_input("Enter patient ID: ")
        if st.button("Search"):
            try:
                #covert the input to a int
                patient_id = int(patient_id)
                patient = Search_Patient_ID(connection, patient_id)
                if patient is None:
                    st.error("Patient not found. Try again!")
                else:
                    diagnoses = Search_Diagnosis_Patient(connection, patient_id)
                    if diagnoses:
                        for diagnosis in diagnoses:
                            st.write(f"Diagnosis: {diagnosis.diagnosis_name}| "
                                     f"Observation: {diagnosis.observation}")
                    else:
                        st.error("The patient doesn't have any diagnoses")
            except ValueError:
                st.error("Please enter a valid Patient ID.")