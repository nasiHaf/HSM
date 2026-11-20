"""This is the Healthcare Management System, enter: 'streamlit run main.py' 
in terminal to run the program.
To check tests enter: 'python -m pytest' in the terminal
"""
import streamlit as st
from db_connect import *
from gui import *
from functions import *


def ManagementSystem(connection):
    """Creates the main page of the Healthcare Management System with the first options"""

    #Title
    st.set_page_config(page_title="Healthcare Management System",
        layout="wide"
    )
    st.title("Healthcare Management System")

    #Sidebar with options
    st.sidebar.title("Menu")
    option = st.sidebar.selectbox("Choose an option:",
                                [
                                "Patient", 
                                "Doctor", 
                                "Appointment", 
                                "Clinic",
                                "Messages"
                                ],
                                key="option_menu"
    )

    #Options for Patient
    if option == "Patient":
        patient_gui(connection)

    #Options for Doctor
    elif option == "Doctor":
        doctor_gui(connection)

    #Options for Appointment  
    elif option == "Appointment":
        appointment_gui(connection)

    #Options for Clinic  
    elif option == "Clinic":
        clinic_gui(connection)

    # Options for Messages
    elif option == "Messages":
        messages_gui(connection)


def main():
    """The main function runs the connection and starts the GUI"""
    #get the connection to the database 
    connection = connect_clinic()  
    #If we don't have a connection we will not run the program, we also close the connection after running
    if connection:
        ManagementSystem(connection)
        connection.close()


if __name__ == "__main__":
    main()
