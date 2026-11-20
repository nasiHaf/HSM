"""Classes representing entities in the healthcare database."""

class Patient:
  def __init__(self,patient_id, patient_name):
    self.patient_id = patient_id
    self.patient_name = patient_name

class Doctor:
  def __init__(self, doctor_id, doctor_name):
    self.doctor_id = doctor_id
    self.doctor_name = doctor_name

class Appointment:
  def __init__(self, patient_id,doctor_id, appointment_time):
    self.patient_id =patient_id
    self.doctor_id = doctor_id
    self.appointment_time = appointment_time

class Department:
  def __init__(self,department_id, department_name):
    self.department_id = department_id
    self.department_name = department_name

class Clinic:
  def __init__(self, clinic_id, clinic_name, clinic_address):
    self.clinic_id = clinic_id
    self.clinic_name = clinic_name
    self.clinic_address = clinic_address

class Diagnosis:
    def __init__(self, diagnosis_name, observation):
      self.diagnosis_name = diagnosis_name
      self.observation = observation