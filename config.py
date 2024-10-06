import os
from dotenv import load_dotenv

if 'JSON_FILE_PATH' not in os.environ:
    load_dotenv()

def get_json_file_path():
    return os.getenv('JSON_FILE_PATH', 'data.json')
