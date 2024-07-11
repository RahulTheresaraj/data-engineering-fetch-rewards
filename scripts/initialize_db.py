import psycopg2

db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

def create_table():
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_logins (
        user_id varchar(128),
        device_type varchar(32),
        masked_ip varchar(256),
        masked_device_id varchar(256),
        locale varchar(32),
        app_version integer,
        create_date date
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("Database initialized and table created")
