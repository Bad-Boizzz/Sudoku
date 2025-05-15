import os
import csv

FILENAME = 'settings.csv'

# Default settings to use if the file doesn't exist
DEFAULT_SETTINGS = {
    "color": "1",
    "language": "polish.txt",
    "level": "1"
}

def initialize_settings():
    """
    Check if the settings file exists.
    If not, create it with the default settings.
    """
    if not os.path.exists(FILENAME):
        save_settings(DEFAULT_SETTINGS)
        print(f"Created '{FILENAME}' with default settings.")

def load_settings():
    """
    Load all settings from the CSV file into a dictionary.
    If the file does not exist yet, initialize it first.
    Returns:
        dict: A mapping of setting keys to their values.
    """
    initialize_settings()
    settings = {}
    with open(FILENAME, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Each row should have at least two columns: key and value
            if len(row) >= 2:
                key, value = row[0], row[1]
                settings[key] = value
    return settings

def save_settings(settings: dict):
    """
    Write all settings from the dictionary back to the CSV file.
    Overwrites any existing file.
    Args:
        settings (dict): Mapping of keys to values to save.
    """
    with open(FILENAME, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in settings.items():
            writer.writerow([key, value])

def change_setting(key: str, value: str):
    """
    Change a single setting and save the updated file.
    Adds the key if it does not already exist.
    Args:
        key (str): The setting name to change.
        value (str): The new value to assign.
    """
    settings = load_settings()
    old_value = settings.get(key)
    settings[key] = value
    save_settings(settings)
    if old_value is None:
        print(f"Added new setting: '{key}' = '{value}'.")
    else:
        print(f"Updated setting '{key}': '{old_value}' → '{value}'.")

def get_setting(key: str):
    """
    Retrieve the value of a single setting.
    Args:
        key (str): The setting name to retrieve.
    Returns:
        str or None: The setting value, or None if not found.
    """
    settings = load_settings()
    return settings.get(key)

def interactive_settings_menu():
    """
    Display all settings in a numbered list and allow the user
    to choose one to change its value (or exit).
    Loops until the user selects '0' to quit.
    """
    settings = load_settings()
    while True:
        print("\nCurrent settings:")
        for idx, (key, value) in enumerate(settings.items(), start=1):
            print(f"  {idx}. {key} = {value}")
        print("  0. Exit")

        choice = input("Enter the number of the setting to change (or 0 to exit): ").strip()
        if choice == "0":
            print("Exiting settings menu.")
            break

        try:
            idx = int(choice) - 1
            if idx < 0 or idx >= len(settings):
                raise ValueError
            key = list(settings.keys())[idx]
        except ValueError:
            print("Invalid choice. Please enter a valid number.")
            continue

        new_value = input(f"Enter new value for '{key}' (current: {settings[key]}): ").strip()
        change_setting(key, new_value)
        settings = load_settings()  # reload after change

if __name__ == "__main__":
    # Example usage:

    # 1) Launch the interactive menu to view/change settings
    interactive_settings_menu()

    # 2) After exiting, you can still programmatically access settings:
    final_settings = load_settings()
    print("\nFinal settings state:")
    for k, v in final_settings.items():
        print(f"  {k} = {v}")
