import os
import csv
import glob
from language.LanguageManager import LanguageManager
import time


# Filenames


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

all_languages = ["PL","EN", "PLSLASK","ES","PT","RU","DE"]
lm = LanguageManager(
        languagePacks_path="language/languagePacks",
        languages_prefixes=all_languages,
        default_lang="PL",
        postfix="pack",
        debug_mode=False
    )

default_settings_file = 'settings.csv'

# Default settings values
default_settings = {
    'settings.color': '1',
    'settings.language': 'polish.csv',  # Default language file
    'settings.level': '1'
}

current_dir = os.path.dirname(os.path.abspath(__file__))

# ---------- Settings handling ----------

def initialize_settings(filename=default_settings_file):
    """
    Create the settings file with default values if it doesn't exist.
    """
    path = os.path.join(current_dir, filename)
    if not os.path.exists(path):
        save_settings(default_settings, filename)


def load_settings(filename=default_settings_file):
    """
    Load settings from CSV into a dict. Initialize if missing.
    """
    initialize_settings(filename)
    settings = {}
    path = os.path.join(current_dir, filename)
    with open(path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2:
                settings[row[0].strip()] = row[1].strip()
    return settings


def save_settings(settings_dict, filename=default_settings_file):
    """
    Save settings dict back to CSV (overwriting).
    """
    path = os.path.join(current_dir, filename)
    with open(path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in settings_dict.items():
            writer.writerow([key, value])


def change_setting(key, value, filename=default_settings_file):
    """
    Change a single setting and save.
    """
    settings = load_settings(filename)
    old = settings.get(key)
    settings[key] = value
    save_settings(settings, filename)
    return old, value

# ---------- Translations handling ----------

# def load_translations(lang_file):
#     """
#     Load translation pairs from a CSV file into a dict.
#     Supports .txt fallback by converting to .csv if needed.
#     CSV format: key,value  (all keys must start with 'settings.')
#     """
#     translations = {}
#     path = os.path.join(current_dir, lang_file)
#     if not os.path.exists(path):
#         base, ext = os.path.splitext(lang_file)
#         alt_file = base + '.csv'
#         alt_path = os.path.join(current_dir, alt_file)
#         if os.path.exists(alt_path):
#             lang_file = alt_file
#             path = alt_path
#         else:
#             raise FileNotFoundError(f"Translation file '{lang_file}' not found.")
#     with open(path, mode='r', newline='', encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile)
#         for row in reader:
#             if len(row) >= 2:
#                 key = row[0].strip()
#                 if not key.startswith('settings.'):
#                     key = 'settings.' + key
#                 translations[key] = row[1].strip()
#     return translations

# ---------- Utility ----------

def list_language_files(directory=current_dir, pattern='*.csv'):
    """List available translation files in directory."""
    return [os.path.basename(f) for f in glob.glob(os.path.join(directory, pattern))]

# ---------- Interactive menu ----------

def interactive_settings_menu():
    """
    Show and edit settings using translated text from the language file.
    """
    
    while True:
        print(lm.get("settings.title"))
        print(lm.get("settings.available_languages") + str(all_languages) )
        print(lm.get("settings.current_language") + lm.current_lang)
        agrest=input(lm.get("settings.change_prompt")).strip().lower()
        if agrest != 'y':
            print(lm.get("settings.exit"))
            break
        agrest=input(lm.get("settings.enter_language")).strip().upper()
        if agrest not in all_languages:
            print(lm.get("settings.invalid_language").format(agrest, all_languages ))
            time.sleep(3)
            clear()
            continue
        lm.set_language(agrest)
        print(lm.get("settings.language_set") + lm.current_lang)
        time.sleep(1)
        
        break
        # Display current settings with translated labels and values
        # print(translations['settings.menu.current_settings'])
        # keys = list(settings_dict.keys())
        # for idx, key in enumerate(keys, start=1):
        #     label = translations.get(key, key)
        #     raw_val = settings_dict[key]
        #     display_val = translations.get(f"settings.value.{raw_val}", raw_val)
        #     print(f"  {idx}. {label} = {display_val}")
        # print(f"  0. {translations['settings.menu.exit']}")

        # choice = input(translations['settings.prompt.select_setting'] + ' ').strip()
        # if choice == '0':
        #     # Exit menu immediately
        #     break

        # try:
        #     idx = int(choice) - 1
        #     if idx < 0 or idx >= len(keys):
        #         raise ValueError
        #     key = keys[idx]
        # except ValueError:
        #     print(translations['settings.message.invalid_choice'])
        #     continue

        # # Determine new value for the chosen setting
        # if key == 'settings.language':
        #     # List translation files, excluding the settings file itself
        #     langs = [f for f in list_language_files(pattern='*.csv') if f != default_settings_file]
        #     if not langs:
        #         print(translations['settings.message.no_languages'])
        #         continue
        #     print(translations['settings.list.available_languages'])
        #     for i, lang in enumerate(langs, start=1):
        #         print(f"  {i}. {lang}")
        #     sel = input(translations['settings.prompt.select_language'] + ' ').strip()
        #     try:
        #         li = int(sel) - 1
        #         if li < 0 or li >= len(langs):
        #             raise ValueError
        #         new_val = langs[li]
        #     except ValueError:
        #         print(translations['settings.message.invalid_choice'])
        #         continue
        # else:
        #     prompt = translations['settings.prompt.enter_new_value'].format(
        #         key=translations.get(key, key),
        #         value=translations.get(f"settings.value.{settings_dict[key]}", settings_dict[key])
        #     )
        #     new_val = input(prompt + ' ').strip()

        # # Change the setting
        # change_setting(key, new_val)

        # # Clear console after change
        # os.system('cls' if os.name == 'nt' else 'clear')

        # # Reload settings and translations if language changed
        # settings_dict = load_settings()
        # if key == 'settings.language':
        #     translations = load_translations(settings_dict['settings.language'])

# ---------- Main entry ----------
def main_settings():
    # Load settings
    
    # Load translations based on language setting
    # translations = load_translations(settings.get('settings.language', default_settings['settings.language']))
    
    # Run interactive menu
    interactive_settings_menu()
    #main()

if __name__ == '__main__':
    main_settings()
