import mysql.connector

def get_connection():
    """
    Establishes a connection to the MySQL database.
    
    Returns:
        mysql.connector.connection.MySQLConnection: Database connection object or None if connection fails
    """
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="#Harinisri2012",
            database="university_db"
        )
        if con.is_connected():
            return con
        else:
            print("Not connected to database")
            return None
    except mysql.connector.Error as e:
        print(f"Database connection error: {e}")
        return None

def safe_input(prompt, data_type):
    """
    Safely gets user input with type conversion.
    
    Args:
        prompt (str): The prompt to display to the user
        data_type (type): The type to convert the input to
        
    Returns:
        Converted input value of specified type
    """
    try:
        while True:
            val = data_type(input(prompt))
            return val
    except ValueError:
        print("Enter the right data type")
        return safe_input(prompt, data_type)
