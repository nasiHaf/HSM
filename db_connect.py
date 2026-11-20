import mysql.connector

def connect_clinic():
    """Connects to the database"""
    config = {
            'user': 'clinic_user',
            'password': 'clinic',
            'host': '127.0.0.1', #Localhost
            'database': 'clinic_db',
            'raise_on_warnings': True
            }    
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            return connection
    #If we don't get a connection an errormessage is displayed
    except mysql.connector.Error as err: 
        print(f"Error: {err}")
        return None