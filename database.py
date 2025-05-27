# from functools import partialmethod
# import sqlalchemy
# from sqlalchemy import create_engine, text
# import os


# my_secret = os.environ['GOOGLE_MYSQL_DB']


# engine = create_engine(my_secret)

# # Test the connection by trying to connect
# try:
#     with engine.connect() as connection:
#         print("Connection successful!")
#         # You can also execute a test query
#         result = connection.execute(text("SELECT * from jobs"))
#         #print(result.all()[0])
#         result_dicts = []
#         for row in result.all():
#             result_dicts.append(dict(zip(result.keys(), row)))
#         print(result_dicts)    
#         #print(result.all())  # Should print (1,)
#         #print(type(result))
#         #print(type(result.all()))
#         #print(result.all())
# except Exception as e:
#     print(f"Connection failed: {e}")

# def load_data_from_db():
#   with engine.connect() as conn:
#     # Execute a SQL query to select all rows from the 'posts' table
#     result = conn.execute(text("SELECT * FROM jobs"))

#     # Fetch column names from the query result
#     columns = result.keys()  

#     # Convert the query result into a list of dictionaries, with column names as keys
#     result_dicts = [dict(zip(columns, row)) for row in result.fetchall()]

#     # Print the list of dictionaries representing the query result
#     return result_dicts

# def load_job_fromDB(id):
#     # Connecting to the database and executing the query
#     with engine.connect() as conn:
#         # Executing SQL query with a placeholder for the job ID
#         result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {"val": id})

#         # Fetching the first row
#         row = result.fetchone()

#         # Check if row is found
#         if row is None:
#             return None
#         else:
#             # Convert row into a dictionary using column names as keys
#             return dict(zip(result.keys(), row))

# def push_application_data_to_db(id, data):
#     with engine.connect() as conn:
#         query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
#         conn.execute(query, {
#             "job_id": id,
#             "full_name": data['full_name'],
#             "email": data['email'],
#             "linkedin_url": data['linkedin_url'],
#             "education": data['education'],
#             "work_experience": data['work_experience'],
#             "resume_url": data['resume_url']
#         })

# if __name__=="__main__":
#     result1 = load_data_from_db()
#     print(result1[1])

# the following is after creating database on azure

from functools import partialmethod # Still not used here
import os
import pymysql

# --- Retrieve credentials from environment variables ---
DB_HOST = os.environ.get('AZURE_DB_HOST')
DB_USER = os.environ.get('AZURE_DB_USER')
DB_PASSWORD = os.environ.get('AZURE_DB_PASSWORD')
DB_NAME = os.environ.get('AZURE_DB_NAME') # Database name
SSL_CA_PATH = os.environ.get('SSL_CA_PATH')

# --- SSL Configuration ---
# Use the correct CA certificate name for Azure Flexible Server


# --- Basic Validation (Important for Debugging) ---
if not all([DB_HOST, DB_USER, DB_PASSWORD, DB_NAME]):
    print("CRITICAL ERROR: One or more database environment variables (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) are not set.")
    exit(1)

if not os.path.exists(SSL_CA_PATH):
    print(f"CRITICAL ERROR: SSL CA certificate file not found at '{SSL_CA_PATH}'. "
          "Ensure it's in your project (e.g., DigiCertGlobalRootCA.crt.pem) and the path is correct.")
    exit(1)

ssl_args = {'ssl_ca': SSL_CA_PATH}
db_connection = None # Rename to avoid conflict if you use 'connection' elsewhere

def get_db_connection():
    """Establishes and returns a database connection."""
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=3306,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor, # This makes fetchall() return list of dicts
            ssl=ssl_args
        )
        print(f"Successfully connected to database: {DB_NAME} on {DB_HOST}")
        return conn
    except pymysql.Error as e:
        print(f"Error connecting to MySQL Database: {e}")
        # Consider how you want to handle this error. Re-raise? Return None?
        # For now, let's re-raise so the caller knows connection failed.
        raise

def load_data_from_db():
    """Loads all jobs from the database."""
    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor: # Using DictCursor means results are already dicts
            cursor.execute("SELECT * FROM jobs")
            result_dicts = cursor.fetchall() # fetchall() with DictCursor returns list of dicts
            return result_dicts
    except pymysql.Error as e:
        print(f"Error loading data from DB: {e}")
        return [] # Return empty list on error or handle differently
    finally:
        if conn and conn.open:
            conn.close()
            print("load_data_from_db: Database connection closed.")

def load_job_from_db(job_id):
    """Loads a specific job by its ID from the database."""
    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor: # Using DictCursor
            # Use %s as placeholder for PyMySQL, and pass values as a tuple
            cursor.execute("SELECT * FROM jobs WHERE id = %s", (job_id,))
            row = cursor.fetchone() # fetchone() with DictCursor returns a single dict or None
            return row # This is already a dictionary or None
    except pymysql.Error as e:
        print(f"Error loading job ID {job_id} from DB: {e}")
        return None # Return None on error or handle differently
    finally:
        if conn and conn.open:
            conn.close()
            print(f"load_job_from_db (ID: {job_id}): Database connection closed.")

def push_application_data_to_db(job_id, data):
    """Pushes application data for a specific job ID to the database."""
    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            query = """
                INSERT INTO applications
                (job_id, full_name, email, linkedin_url, education, work_experience, resume_url)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            # Ensure the order of values in the tuple matches the query
            values = (
                job_id,
                data['full_name'],
                data['email'],
                data['linkedin_url'],
                data['education'],
                data['work_experience'],
                data['resume_url']
            )
            cursor.execute(query, values)
            conn.commit() # IMPORTANT: Commit changes for INSERT, UPDATE, DELETE
            print(f"Application for job ID {job_id} successfully submitted.")
            return True # Indicate success
    except pymysql.Error as e:
        print(f"Error pushing application data for job ID {job_id} to DB: {e}")
        if conn: # Rollback if connection exists and there was an error
            conn.rollback()
        return False # Indicate failure
    finally:
        if conn and conn.open:
            conn.close()
            print(f"push_application_data_to_db (Job ID: {job_id}): Database connection closed.")

# --- Main execution / Test ---
if __name__ == "__main__":
    print("--- Testing load_data_from_db ---")
    all_jobs = load_data_from_db()
    if all_jobs:
        print(f"Found {len(all_jobs)} jobs.")
        # Print the first job if available
        if len(all_jobs) > 0:
            print("First job:", all_jobs[0])
        # Print the second job if available
        if len(all_jobs) > 1:
             print("Second job:", all_jobs[1])
    else:
        print("No jobs found or error occurred.")

    print("\n--- Testing load_job_from_db (assuming job with ID 1 exists) ---")
    job_id_to_load = 1 # Change this to an ID you know exists
    specific_job = load_job_from_db(job_id_to_load)
    if specific_job:
        print(f"Job with ID {job_id_to_load}:", specific_job)
    else:
        print(f"Job with ID {job_id_to_load} not found or error occurred.")

    print("\n--- Testing push_application_data_to_db (example) ---")
    example_job_id = 1 # Assuming job ID 1 exists
    example_application_data = {
        'full_name': 'Test Applicant',
        'email': 'test@example.com',
        'linkedin_url': 'https://linkedin.com/in/testapplicant',
        'education': 'BS in Computer Science',
        'work_experience': '2 years as a Developer',
        'resume_url': 'https://example.com/resume.pdf'
    }
    # Make sure example_job_id exists in your 'jobs' table before running this
    # or the foreign key constraint will fail if you have one.
    # success = push_application_data_to_db(example_job_id, example_application_data)
    # if success:
    # print("Test application submitted.")
    # else:
    # print("Test application submission failed.")