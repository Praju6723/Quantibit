import re

def extract_emails(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    emails = re.findall(email_pattern, content)
    
    return emails

file_path = 'your_file.txt'  
emails = extract_emails(file_path)
print(emails)
