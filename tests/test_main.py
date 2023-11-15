import re

def update_code_formatting(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()

    # Replace tabs with 4 spaces for indentation
    contents = contents.replace('\t', '    ')

    # Add consistent spacing around operators and after commas
    contents = re.sub(r'(\S)([+\-*/%=])(\S)', r'\1 \2 \3', contents)
    contents = re.sub(r'(\S),(\S)', r'\1, \2', contents)

    # Convert variable and function names to lowercase with underscores
    contents = re.sub(r'([A-Z])', lambda x: x.group(1).lower(), contents)
    contents = re.sub(r'([a-z])([A-Z])', r'\1_\2', contents)

    # Add a blank line between function definitions
    contents = re.sub(r'\n\s*def', '\n\n\ndef', contents)

    with open(file_path, 'w') as file:
        file.write(contents)

# Call the function with the file path
update_code_formatting('tests/test_main.py')
