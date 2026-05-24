from pathlib import Path
def overwrite_all_files(directory_path, new_content, file_pattern='*'):
    root_dir = Path(directory_path)
    
    for file_path in root_dir.rglob(file_pattern):
        
        if file_path.is_file():
            try:
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Successfully overwrote: {file_path}")
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

overwrite_all_files('./Downloads', 'This is the new, overwritten content.')
