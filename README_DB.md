
# Database Schema Design
## Session Table: To store session information.

- session_id (Primary Key): A unique identifier for each session.
- start_timestamp: Timestamp for the session's start.
- end_timestamp: Timestamp for the session's end.
- language: Language of the session.
- files_processed: Number of files processed in the session.

## File Progression Table: To store information about the progression of each file in a session.

- file_id (Primary Key): A unique identifier for each file.
- session_id (Foreign Key): Links to the session_id in the Session table.
- file_name: Name of the file being processed.
- status: Current status of the file (e.g., 'pending', 'processing', 'completed').
- progress_percentage: Progress percentage of the file processing.

## Deploying on Scaleway Cloud

# Connect to your Scaleway Managed Database:

Use Scaleway's console to create a managed PostgreSQL database if you haven't already.
Obtain the connection details (hostname, port, username, password) from the Scaleway console.
Upload the SQL File:

Upload create_db.sql to your cloud server or any machine that can connect to the database.
Execute the SQL File:

Connect to your PostgreSQL database using a tool like psql or PgAdmin.
Run the create_db.sql script. In psql, you can do this with \i path/to/create_db.sql.

```sql
-- Create the database
CREATE DATABASE text_processing_db;

-- Switch to the new database
\c text_processing_db;

-- Create the Session table
CREATE TABLE session (
    session_id SERIAL PRIMARY KEY,
    start_timestamp TIMESTAMP NOT NULL,
    end_timestamp TIMESTAMP,
    language VARCHAR(50),
    files_processed INTEGER
);

-- Create the File Progression table
CREATE TABLE file_progression (
    file_id SERIAL PRIMARY KEY,
    session_id INTEGER REFERENCES session(session_id),
    file_name VARCHAR(255),
    status VARCHAR(50),
    progress_percentage INTEGER
);

```