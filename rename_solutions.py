import os
import re

def rename_solution_files(directory='solutions'):
    # Get all files in the directory
    files = os.listdir(directory)
    
    # Pattern to match: number followed by hyphen and rest of filename
    pattern = r'^(\d+)(-.*\..*$)'
    
    for filename in files:
        match = re.match(pattern, filename)
        if match:
            number, rest = match.groups()
            # Create new filename with 4-digit padding
            new_filename = f'{int(number):04d}{rest}'
            
            # Create full paths
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f'Renamed: {filename} -> {new_filename}')

if __name__ == '__main__':
    rename_solution_files() 