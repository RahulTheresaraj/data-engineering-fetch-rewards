# Fetch Rewards
## Data Engineering Take Home: ETL off an SQS Queue

This project is the solution for the Data Engineering assignment. It involves reading JSON data from an AWS SQS Queue, transforming the data by masking personal identifiable information (PII), and writing the data to a PostgreSQL database. The entire process is executed using Docker containers to simulate AWS and PostgreSQL environments locally.

## Project Structure

```plaintext
data-takehome/
│
├── docker-compose.yml
├── README.md
├── requirements.txt
├── scripts/
│   ├── initialize_db.py
│   ├── read_sqs.py
│   ├── process_data.py
│   ├── write_to_postgres.py
│   └── etl_process.py
