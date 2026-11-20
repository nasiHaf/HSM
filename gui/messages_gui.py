from datetime import datetime
import streamlit as st
from functions.patient_func import *
from functions.doctor_func import *
from functions.message_func import *

def messages_gui(connection):
    st.title("Messages")

    # Select user
    user = st.selectbox("Who is searching?",
                        ["Patient", 
                         "Doctor"
                        ]
    )

    #If the user is a patient
    if user == "Patient":
        #box to search patient name
        patient_name = st.text_input("Enter Patient name:")
        if st.button("Search Patient"):
            patient_name = patient_name.strip()

            #get a list of optional patients
            patients = Search_Patient(connection, patient_name)

            if patients:
                # Create choices using patient name and ID
                patient_options = { f"{patient.patient_name} "
                                    f"(ID:{patient.patient_id})"
                                    :patient.patient_id for patient in patients
                                }

                st.session_state["patient_options"] = patient_options
            else:
                st.error("Patient not found, try again!") 
                
        if "patient_options" in st.session_state:
            patient_options = st.session_state["patient_options"]

            selected_patient = st.selectbox("Choose patient:",
                                            list(patient_options.keys()),
                                            index=None,
                                            placeholder="Select a patient"
                                            )
            
            # Save patient as logged-in user
            if selected_patient is not None:
                selected_patient_id = patient_options[selected_patient]    
                st.session_state["current_user_id"] = selected_patient_id
                st.success(f"Logged in: {selected_patient}")

        if "current_user_id" in st.session_state:
            patient_id = st.session_state["current_user_id"]
            doctor = Search_Patient_Doctor(connection, patient_id)

            if doctor:
                st.write(f"Your doctor: {doctor.doctor_name} "
                         f"(ID:{doctor.doctor_id})"
                        )

                # Save doctor as receiver
                st.session_state["receiver_id"] = (doctor.doctor_id)

                #include previous messages
                conversation = get_messages(patient_id, doctor.doctor_id)
                st.subheader(f"Conversation with Dr. {doctor.doctor_name}")
                
                for message in conversation:
                    timestamp = message["timestamp"].strftime("%d/%m/%Y %H:%M")
                    if message["sender_id"] == patient_id:
                        st.write(f"**You**({timestamp})")
                    else:
                        st.write(f"**Doctor**({timestamp})")

                    # Display text if there is text
                    if message["message"]:
                            st.write(message["message"])

                    # Display image if there is an image
                    if message["image"]:
                            st.image(message["image"])

                # write message to your doctor or attach a image
                message = st.text_area("Write your message:")
                image = st.file_uploader("Attach an image:", type = ["jpg", "jpeg", "png"])

                #Send the message
                if st.button("Send Message"):
                    if message.strip() or image:
                        send_message(patient_id,
                                     doctor.doctor_id,
                                     message,
                                     image,
                                     datetime.now()
                                     )
                        st.success("Message sent!")
                    else:
                        st.warning("Please write a message or attach an image.")
            else:
                st.error("No doctor found for this patient.")


    elif user == "Doctor":
        doctor_name = st.text_input("Enter Doctor name:")

        if st.button("Search Doctor"):
            doctor_name = doctor_name.strip()
            doctors = Search_Doctor(connection, doctor_name)

            if doctors:
                # Create choices using doctor name and ID
                doctor_options = {f"{doctor.doctor_name} "
                                  f"(ID:{doctor.doctor_id})":
                                  doctor.doctor_id for doctor in doctors
                                  }
                # Save doctor options
                st.session_state["doctor_options"] = doctor_options
            else:
                st.error("Doctor not found, try again!")

        # Show doctor selection after searching
        if "doctor_options" in st.session_state:
            doctor_options = st.session_state["doctor_options"]

            selected_doctor = st.selectbox("Choose Doctor:",
                                            list(doctor_options.keys()),
                                            index=None,
                                            placeholder="Select a Doctor"
                                            )
            
            # Save doctor as logged-in user
            if selected_doctor is not None:
                selected_doctor_id = doctor_options[selected_doctor]
                st.session_state["current_user_id"] = selected_doctor_id
                st.success(f"Logged in: {selected_doctor}")

        # Doctor is logged in
        if ("current_user_id" in st.session_state):
            doctor_id = st.session_state["current_user_id"]

            # Find all patients belonging to this doctor
            patients = Search_Doctor_Patient(connection, doctor_id)

            if patients:
                # Create choices using patient name and ID
                patient_options = {f"{patient.patient_name} "
                                   f"(ID:{patient.patient_id})":
                                   patient.patient_id for patient in patients
                                   }

                # Choose which patient to message
                selected_patient = st.selectbox("Choose patient:",list(patient_options.keys()),
                                                index=None,
                                                placeholder="Select a patient"
                                                )

                if selected_patient is not None:
                    selected_patient_id = patient_options[selected_patient]

                    # Save patient as receiver
                    st.session_state["receiver_id"] = selected_patient_id

                    #include previous messages
                    conversation = get_messages(selected_patient_id, doctor_id)

                    st.subheader(f"Conversation with {selected_patient}:")
                    for message in conversation:
                        timestamp = message["timestamp"].strftime("%d/%m/%Y %H:%M")

                        if message["sender_id"] == selected_patient_id:
                            st.write(f"**Patient** ({timestamp})")
                        else:
                            st.write(f"**You** ({timestamp})")

                        # Display text if there is text
                        if message["message"]:
                            st.write(message["message"])

                        # Display image if there is an image
                        if message["image"]:
                            st.image(message["image"])

                    # Write message or attach an image
                    message = st.text_area("Write your message:")

                    image = st.file_uploader("Attach an image:", type = ["jpg", "jpeg", "png"])

                    if st.button("Send Message"):
                        if message.strip() or image: 
                            send_message(doctor_id,
                                         selected_patient_id,
                                         message,
                                         image,
                                         datetime.now()
                                        )

                            st.success("Message sent!")

                        else:
                            st.warning("Please write a message or attach an image.")
            else:
                st.error("No patients found for this doctor.")