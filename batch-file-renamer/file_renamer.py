import os

def batch_rename():
    folder_path = input("Enter the full path to the folder ")
        
    print("\nChoose a renaming operation:")
    print("1. Add a Prefix")
    print("2. Remove a specific word")
    print("3. Change file extension")
    operation = input("Enter your choice (1-3): ").strip()
    
    
    if operation == '1':
        modifier = input("Enter the prefix to add: ")
    elif operation == '2':
        modifier = input("Enter the word to remove from filenames: ")
    elif operation == '3':
        modifier = input("Enter the new extension (e.g., .png, .bak): ")
        if not modifier.startswith('.'):
            modifier = '.' + modifier 
    else:
        print("Invalid choice")
        operation = '1'
        modifier = input("Enter the prefix to add: ")

    
    changes = []
    for file in os.listdir(folder_path):
        old_path = os.path.join(folder_path, file)
        if os.path.isfile(old_path):
            name, ext = os.path.splitext(file)
            
            if operation == '1':
                new_name = f"{modifier}{name}{ext}"
            elif operation == '2':
                new_name = f"{name.replace(modifier, '')}{ext}"
            elif operation == '3':
                new_name = f"{name}{modifier}" 
            
            new_path = os.path.join(folder_path, new_name)
            
           
            if old_path != new_path:
                changes.append((old_path, new_path))
    
    
    if not changes:
        print("No files need renaming with the current settings.")
        return
        
    print("\n--- Preview of Changes ---")
    for old, new in changes:
        print(f"'{os.path.basename(old)}' -> '{os.path.basename(new)}'")
    
   
    print("\n--- Renaming Files ---")
    for old_path, new_path in changes:
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {os.path.basename(old_path)}")
            
        except OSError as e:
            print(f"✗ Error renaming {os.path.basename(old_path)}: {e}")
    
    print(f"\nOperation complete. Successfully renamed files")

if __name__ == "__main__":
    batch_rename()