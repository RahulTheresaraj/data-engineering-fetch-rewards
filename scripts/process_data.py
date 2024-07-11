import hashlib
import json
import sys

def mask_value(value):
    return hashlib.sha256(value.encode()).hexdigest()

def flatten_json(json_obj):
    flat_dict = {}
    for key, value in json_obj.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                flat_dict[f"{key}_{sub_key}"] = sub_value
        else:
            flat_dict[key] = value
    return flat_dict

def convert_app_version(version):
    try:
        if isinstance(version, str) and '.' in version:
            return int(version.split('.')[0])
        return int(version)
    except (ValueError, TypeError):
        return 0

def process_data(messages):
    processed_messages = []
    for message in messages:
        flat_message = flatten_json(message)
        processed_message = {
            'user_id': flat_message.get('user_id', 'unknown_user'),
            'device_type': flat_message.get('device_type', 'unknown_device'),
            'masked_ip': mask_value(flat_message.get('ip', '0.0.0.0')),
            'masked_device_id': mask_value(flat_message.get('device_id', 'unknown_device')),
            'locale': flat_message.get('locale', 'unknown_locale'),
            'app_version': convert_app_version(flat_message.get('app_version', 0)),
            'create_date': flat_message.get('create_date', '1970-01-01')
        }
        processed_messages.append(processed_message)
    return processed_messages

if __name__ == "__main__":
    input_data = json.load(sys.stdin)
    processed_messages = process_data(input_data)
    print(json.dumps(processed_messages))  # Send output to next script
