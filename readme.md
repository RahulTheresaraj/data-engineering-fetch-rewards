# Fetch Rewards
## Data Engineering Take Home: ETL off an SQS Queue

This project is the solution for the Data Engineering assignment. It involves reading JSON data from an AWS SQS Queue, transforming the data by masking personal identifiable information (PII), and writing the data to a PostgreSQL database. The entire process is executed using Docker containers to simulate AWS and PostgreSQL environments locally.

## Project Structure

```plaintext

├── docker-compose.yml
├── README.md
├── requirements.txt
├── scripts/
│   ├── initialize_db.py
│   ├── read_sqs.py
│   ├── process_data.py
│   ├── write_to_postgres.py
│   └── etl_process.py
```

## Prerequisites

- Docker
- Docker Compose
- Python 3.x
- AWS CLI Local


## Setup

### 1. Clone this repo

```bash
git clone <repository_url>
cd data-takehome
```

### 2. Create and Start Docker Services

Make sure you have Docker and Docker Compose installed. Then, start the Docker services:

```bash
docker-compose up -d
```
This will start the LocalStack and PostgreSQL containers.

### 3. Install Required Python Packages

Install the necessary Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Ensure the SQS Queue Exists

Create the SQS queue in the LocalStack instance:

```bash
awslocal sqs create-queue --queue-name login-queue
```

## Running the ETL Process

Run the ETL process using the following command:

```bash
python scripts/etl_process.py
```
This script orchestrates the entire ETL process, performing the following steps:

1. **Initialize the PostgreSQL Database**: Run `initialize_db.py` to create the required table if it does not exist.
2. **Read Messages from SQS**: Run `read_sqs.py` to read JSON data from the SQS queue.
3. **Process the Data**: Run `process_data.py` to mask PII fields (`device_id` and `ip`), and flatten the JSON data.
4. **Write the Data to PostgreSQL**: Run `write_to_postgres.py` to insert the processed data into the PostgreSQL database.

## Checking messages loaded in Postgres

To validate the messages loaded in Postgres:

### 1. Connect to the PostgreSQL Database

```bash
psql -h localhost -p 5432 -U postgres -d postgres
```
When prompted, enter the password: `postgres`.

### 2. Run the Query to View Data

```sql
SELECT * FROM user_logins;
```
This query will display the data inserted by the ETL process.

### 3. Exit `psql`

To exit `psql`, type:

```plaintext
\q
```
## Scripts Overview

### `initialize_db.py`
Initializes the PostgreSQL database and creates the `user_logins` table if it does not exist.

### `read_sqs.py`
Reads messages from the SQS queue and returns them as a list of JSON objects.

### `process_data.py`
Processes the JSON objects by masking PII (device_id and IP) and flattening the JSON structure.

### `write_to_postgres.py`
Writes the processed data to the `user_logins` table in PostgreSQL.

### `etl_process.py`
Orchestrates the entire ETL process by running the above scripts in sequence and passing data between them in-memory.

## Notes

- Ensure Docker and Docker Compose are running properly.
- Make sure the SQS queue is created before running the ETL process.
- The ETL process uses in-memory data passing and does not create or print intermediate JSON files.

## Troubleshooting

If you encounter any issues with Docker or the services, try restarting the Docker services:

```bash
docker-compose down
docker-compose up -d
```
Ensure all required Python packages are installed.

Verify that the SQS queue exists using:

```bash
awslocal sqs list-queues
```





