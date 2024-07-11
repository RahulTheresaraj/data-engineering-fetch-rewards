import subprocess
import json

def run_script(script_name, input_data=None, expect_json_output=False):
    try:
        result = subprocess.run(
            ['python', script_name],
            input=json.dumps(input_data) if input_data else None,
            capture_output=True,
            text=True,
            check=True
        )
        if result.stderr:
            print(f"Error running {script_name}:", result.stderr)
        if expect_json_output:
            return json.loads(result.stdout) if result.stdout else None
        else:
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        raise

if __name__ == "__main__":
    run_script('scripts/initialize_db.py', expect_json_output=False)
    sqs_messages = run_script('scripts/read_sqs.py', expect_json_output=True)
    processed_messages = run_script('scripts/process_data.py', input_data=sqs_messages, expect_json_output=True)
    run_script('scripts/write_to_postgres.py', input_data=processed_messages, expect_json_output=False)
    print("ETL process completed")
