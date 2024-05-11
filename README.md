# Cloud-Based Full-Stack with Flask: Job Advertisement Website
Welcome to our GitHub repository! Here, we've stored all the code for a website we built using a platform called Replit, which is a cloud-based development environment. This website is special because it's not just a regular webpage – it's what we call a "full-stack" webpage. That means it has both a front end (the part you see and interact with) and a back end (the behind-the-scenes part that makes things work).

On the front end, we've used technologies like HTML (which gives the webpage its structure), CSS (which makes it look nice), and JavaScript (which adds interactive features like buttons and animations).



This project is a job advertisement website built using HTML, CSS, JavaScript, and Flask. It allows users to view and apply for job listings posted by employers.
Features
    Job Listings: View a list of available job positions.
    Apply for Jobs: Users can apply for jobs directly through the website.
    Admin Panel: Employers can post new job listings and manage existing ones through an admin panel.

Technologies Used

    Frontend: HTML, CSS, JavaScript
    Backend: Flask
    Database: MySQL
    Cloud Platforms:
        Development: Replit
        Database Hosting: filess.io

Installation

    Clone the repository:

    bash

   git clone

Install dependencies:

bash

pip install -r requirements.txt

Set up MySQL database and configure connection settings in config.py.

Run the application:

bash

    python app.py

    Access the website at http://localhost:5000.


**Prerequisites:**

* Python (https://www.python.org/)
* Replit account (https://replit.com/)
* Dedicated Database Service (recommended)

**Steps:**

1. **Create a Replit:**
   - Sign up for a Replit account or use your existing account.
   - Create a new Replit for your project and select "Flask" as the template.

2. **Install Dependencies:**
   - In your Replit's terminal, install the necessary libraries:

     ```bash
     pip install Flask sqlalchemy [database-connector]  # Replace with your database connector (e.g., pymysql for MySQL)
     ```

**Database Setup (Important Security Note):**

```markdown
## Database Setup

**Security Warning:**

Connecting to a database hosted on Fileless.io is not recommended due to security concerns. Fileless.io is not designed for database management and potentially lacks adequate security measures. Data stored there might be exposed or compromised.

**Recommended Approach:**

1. Use a dedicated database hosting service such as:
   - Google Cloud SQL: [https://cloud.google.com/sql](https://cloud.google.com/sql)
   - Amazon RDS: [https://aws.amazon.com/rds/](https://aws.amazon.com/rds/)
   - Heroku Postgres: [https://devcenter.heroku.com/articles/heroku-postgresql](https://devcenter.heroku.com/articles/heroku-postgresql)
   - DigitalOcean Managed Databases: [https://www.digitalocean.com/products/managed-databases](https://www.digitalocean.com/products/managed-databases)

2. Follow the chosen service's instructions to create a database and obtain your credentials (username, password, host, port, database name).

3. **Do not commit** your database credentials to a public repository (like GitHub). Use secure environment variables on Replit:

   - Go to your Replit project's dashboard.
   - Click on the "Secrets" tab.
   - Create new secrets for each database credential.

4. In your Python code, use the `os` module to access these secrets securely:

   ```python
   import os

   db_username = os.environ.get('DB_USERNAME')
   db_password = os.environ.get('DB_PASSWORD')
   # ... other credentials


Contributing

Contributions are welcome! Please follow the Contributing Guidelines.
License

This project is licensed under the MIT License.
Acknowledgements

    Thanks to Replit for providing a cloud platform for development.
    Thanks to filess.io for hosting the MySQL database.


