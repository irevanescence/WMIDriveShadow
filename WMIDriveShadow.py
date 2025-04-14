import wmi
import datetime
import os

log_file = r"C:\Scripts\ShadowCopy.log"
drive_letters = ["C", "D", "F", "G"]

def ensure_log_directory():
    """Ensure the log file directory exists."""
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

def log_message(message):
    """Log a message with a timestamp to the log file."""
    try:
        with open(log_file, "a") as f:
            f.write(f"{datetime.datetime.now()}: {message}\n")
    except Exception as e:
        print(f"Failed to write to log file: {str(e)}")

def is_valid_drive(drive_letter):
    """Check if the drive exists and is a fixed disk."""
    try:
        return os.path.exists(f"{drive_letter}:\\")
    except:
        return False

def create_shadow_copy():
    """Attempt to create shadow copies for specified drives."""
    ensure_log_directory()
    log_message("Starting WMI shadow copy attempt for multiple drives")
    
    try:
        c = wmi.WMI()
        log_message("WMI connection established")
        shadow_class = c.Win32_ShadowCopy

        for letter in drive_letters:
            if not is_valid_drive(letter):
                log_message(f"Drive {letter}:\\ does not exist or is invalid")
                continue
                
            drive = f"{letter}:\\"
            try:
                log_message(f"Attempting shadow copy for drive {drive}")
                result, = shadow_class.Create(Volume=drive, Context="ClientAccessible")
                if result == 0:
                    log_message(f"Shadow copy created successfully for {drive}")
                else:
                    error_codes = {
                        1: "Invalid provider registration",
                        2: "Provider not found",
                        5: "Access denied",
                        8: "Provider failure",
                        9: "Operation timed out"
                    }
                    error_msg = error_codes.get(result, "Unknown error")
                    log_message(f"Failed to create shadow copy for {drive}. Return code: {result} ({error_msg})")
            except Exception as e:
                log_message(f"Error creating shadow copy for {drive}: {str(e)}")
    except Exception as e:
        log_message(f"General error: {str(e)}")

if __name__ == "__main__":
    try:
        create_shadow_copy()
    except KeyboardInterrupt:
        log_message("Script interrupted by user")
    except Exception as e:
        log_message(f"Unexpected error: {str(e)}")