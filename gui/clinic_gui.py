import streamlit as st  
from functions.clinic_func import *

def clinic_gui(connection):
    """The options for the Clinic page"""

    clinic_option = st.selectbox("Clinic:", 
                                [
                                "Choose an option",
                                "View Clinics",
                                "Search Clinic",
                                "Search Departments"
                                ],
                                key="clinic_menu"
    )

    #We get a list of all the clinics in the database in alphabetic order
    if clinic_option == "View Clinics": 
        clinics = View_Clinics(connection)
        if clinics:
            for clinic in clinics:
                st.write(f"Clinic ID: {clinic.clinic_id} | "
                         f"Clinic Name: {clinic.clinic_name} | "
                         f"Clinic Address: {clinic.clinic_address}"
                         )
        else:
            st.error("No clinics in the database!")

    #Search a clinic by name
    elif clinic_option == "Search Clinic":
        clinic_name = st.text_input("Enter clinic name: ")
        if st.button("Search "):
            clinic_name = clinic_name.strip()
            clinics = Search_Clinic(connection, clinic_name)
            if clinics:
                for clinic in clinics:
                    st.write(f"Clinic ID: {clinic.clinic_id} | "
                             f"Clinic Name: {clinic.clinic_name} | "
                             f"Clinic Address: {clinic.clinic_address}"
                    )
            else:
                st.error("Clinic not found, try again!")



    #Search a clinic in the database and get the different departments of that clinic
    elif clinic_option == "Search Departments": 
        clinic_id = st.text_input("Enter clinic id: ")
        if st.button("Search "):
            departments = Search_Clinics_Departments(connection,clinic_id)
            if departments:
                for department in departments:
                    st.write(f"Department ID: {department.department_id} | "
                             f"Department Name: {department.department_name}")
            else:
                st.error("Clinic not found, try again!")