import psycopg2
import json
import sys
import psycopg2.extras

db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

def write_to_postgres(data):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date)
    VALUES %s;
    """
    values = [
        (
            record['user_id'],
            record['device_type'],
            record['masked_ip'],
            record['masked_device_id'],
            record['locale'],
            record['app_version'],
            record['create_date']
        ) for record in data
    ]
    psycopg2.extras.execute_values(cursor, insert_query, values)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    input_data = json.load(sys.stdin)
    write_to_postgres(input_data)
    print("Data written to PostgreSQL")
