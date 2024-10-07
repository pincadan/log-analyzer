import re

# Function to analyze log file
def analyze_log(file_path):
    # Open the log file
    with open(file_path, 'r') as file:
        # Read the file line by line
        for line in file:
            # Use regular expressions to extract useful information
            match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (.+) (.+) (.+)', line)
            if match:
                # Extract the date, time, IP address, and message from the log line
                date = match.group(1)
                time = match.group(2)
                ip = match.group(3)
                message = match.group(4)
                # Print the extracted information
                print(f"Date: {date}, Time: {time}, IP: {ip}, Message: {message}")

# Main function
def main():
    # Get the log file path from the user
    file_path = input("Enter the log file path: ")
    # Analyze the log file
    analyze_log(file_path)

# Run the main function
if __name__ == "__main__":
    main()