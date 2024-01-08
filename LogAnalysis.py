import re
import json
from collections import defaultdict

def parse_log_file(log_file_path):
    with open(log_file_path, 'r') as log_file:
        logs = log_file.readlines()

    parsed_logs = []
    for log in logs:
        parsed_log = parse_log_entry(log)
        if parsed_log:
            parsed_logs.append(parsed_log)

    return parsed_logs

def parse_log_entry(log_entry):
    # Customize this function based on the actual log format you are dealing with
    # For demonstration purposes, let's assume a simple log format like: "timestamp [level] message"
    log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[([A-Z]+)\] (.*)'
    match = re.match(log_pattern, log_entry)
    if match:
        timestamp, log_level, message = match.groups()
        return {'timestamp': timestamp, 'level': log_level, 'message': message}
    else:
        return None

def analyze_logs(logs):
    # Perform analysis based on log levels or any other relevant criteria
    log_statistics = defaultdict(int)

    for log in logs:
        log_level = log['level']
        log_statistics[log_level] += 1

    return log_statistics

def main():
    log_file_path = log_file_path = r'C:\Users\Hemy\Desktop\Hemy\Cybersecurity\logpythonproject\hemyevents.txt'
  # Update with the actual path to your log file
    logs = parse_log_file(log_file_path)

    if logs:
        log_statistics = analyze_logs(logs)
        print("Log Analysis Results:")
        print(json.dumps(log_statistics, indent=2))
    else:
        print("No valid log entries found.")

if __name__ == "__main__":
    main()
