import os
import shutil
from datetime import datetime

def create_backup():
    # Source folder to backup (e.g., your project logs)
    source_dir = "./source_logs" 
    # Destination folder where backups are stored
    backup_dir = "./system_backups" 
    
    # Create target directories if they don't exist for demo safety
    if not os.path.exists(source_dir): os.makedirs(source_dir)
    if not os.path.exists(backup_dir): os.makedirs(backup_dir)
    
    today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file_name = f"log_backup_{today}"
    
    try:
        shutil.make_archive(os.path.join(backup_dir, backup_file_name), 'zip', source_dir)
        print(f"SUCCESS: System backup created successfully at: {backup_dir}/{backup_file_name}.zip")
    except Exception as e:
        print(f"ERROR: Backup failed due to: {str(e)}")

if __name__ == "__main__":
    create_backup()
