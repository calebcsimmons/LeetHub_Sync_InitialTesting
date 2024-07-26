import json
import os, re
from datetime import datetime, timezone
from import_requests import get_submissions  # Import the function from import_requests.py

SUBMISSIONS_FILE = 'processed_submissions.json'
OUTPUT_DIR = 'submissions'
CODE_CONTENT_FILE = 'code_contents.json'

def format_timestamp(timestamp):
    dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    return dt.strftime('%Y-%m-%d %H:%M:%S %Z')

def save_processed_ids(submission_ids):
    with open(SUBMISSIONS_FILE, 'w') as f:
        json.dump(list(submission_ids), f)  # Convert set to list

def load_processed_ids():
    if os.path.exists(SUBMISSIONS_FILE):
        with open(SUBMISSIONS_FILE, 'r') as f:
            try:
                return set(json.load(f))  # Convert list to set
            except json.JSONDecodeError:
                print(f"Warning: {SUBMISSIONS_FILE} is empty or corrupted.")
                return set()
    return set()

def save_code_contents(code_contents):
    with open(CODE_CONTENT_FILE, 'w') as f:
        json.dump(code_contents, f)

def load_code_contents():
    if os.path.exists(CODE_CONTENT_FILE):
        with open(CODE_CONTENT_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print(f"Warning: {CODE_CONTENT_FILE} is empty or corrupted.")
                return {}
    return {}

def create_python_file(submission, subfolder):
    submission_id = submission.get('id')
    title = submission.get('title')
    status = submission.get('status_display')
    code = submission.get('code')
    timestamp = format_timestamp(submission.get('timestamp'))

    # Define the file name and path
    file_name = os.path.join(subfolder, f"{submission_id}.py")
    
    # Debugging statements
    print(f"Creating file: {file_name}")

    # Define header for the file
    header = f"""\
# Title: {title}
# Submission ID: {submission_id}
# Status: {status}
# Date: {timestamp}
"""

    try:
        # Ensure the subfolder exists
        if not os.path.exists(subfolder):
            os.makedirs(subfolder, exist_ok=True)
            print(f"Subfolder does not exist. Created: {subfolder}")
        
        with open(file_name, 'w') as f:
            f.write(header)
            f.write("\n")
            f.write(code)
        print(f"File Creation Successful: {file_name}\n")
    except Exception as e:
        print(f"Error creating file {file_name}: {e}\n")

def normalize_code(code):
    # Remove extra newlines and spaces
    code = re.sub(r'\s+', ' ', code).strip()
    return code

def process_new_submissions():
    # Load previously processed IDs and existing code contents
    processed_ids = load_processed_ids()
    code_contents = load_code_contents()
    
    # Fetch new submissions from the API
    submissions_data = get_submissions(limit=100)  # Adjust limit as needed
    
    if submissions_data:
        submissions = submissions_data.get('submissions_dump', [])
        new_ids = set()
        
        for submission in submissions:
            submission_id = submission.get('id')
            title = submission.get('title')
            code = submission.get('code')

            # Replace invalid characters in title
            safe_title = title.replace('/', '_').replace('\\', '_')
            subfolder = os.path.join(OUTPUT_DIR, safe_title)

            # Ensure subfolder exists
            os.makedirs(subfolder, exist_ok=True)
            
            # Debugging statement
            print(f"Processing submission ID: {submission_id}")
            print(f"Subfolder: {subfolder}")

            # Check for duplicate ID
            if submission_id in processed_ids:
                print(f"Duplicate ID detected: {submission_id}. Skipping submission.\n")
                continue
            
            # Normalize code for comparison
            normalized_code = normalize_code(code)
            
            # Check if title exists in code_contents
            if title in code_contents:
                existing_submission = code_contents[title]
                existing_code = existing_submission.get('code')
                existing_code_id = existing_submission.get('id')
                
                # Normalize existing code for comparison
                normalized_existing_code = normalize_code(existing_code)

                if normalized_existing_code == normalized_code:
                    print(f"Duplicate code detected. Skipping submission ID: {submission_id}.\n")
                    continue  # Skip processing this submission
                else:
                    # Update the code contents with new submission
                    code_contents[title] = {'id': submission_id, 'code': code}
                    new_ids.add(submission_id)
                    create_python_file(submission, subfolder)
            else:
                # Add new title and submission
                code_contents[title] = {'id': submission_id, 'code': code}
                new_ids.add(submission_id)
                create_python_file(submission, subfolder)
        
        # Save updated records
        if new_ids:
            processed_ids.update(new_ids)
            save_processed_ids(processed_ids)
            save_code_contents(code_contents)
            print(f"Processed {len(new_ids)} new submissions.\n")
        else:
            print("No new submissions found.\n")
    else:
        print("Failed to fetch submissions.\n")
        
if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    process_new_submissions()
