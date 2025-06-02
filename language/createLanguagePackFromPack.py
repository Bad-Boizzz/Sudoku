
#!/usr/bin/env python3
import json

def escape_value(val: str) -> str:
    return val.encode('unicode_escape').decode('ascii')

def update_nested_dict(d, parent_key="")->None: 
    for key, value in d.items():
        full_key = f"{parent_key}.{key}" if parent_key else key

        if isinstance(value, dict):
            print(f"\n-- Wchodzę do '{full_key}' --")
            update_nested_dict(value, full_key)
        else:
            display = escape_value(value)
            prompt = f"'{full_key}' [{display}]: "
            new_value = input(prompt)
      
            if new_value == "":
                continue
            new_value = new_value.strip()
            if new_value:
                d[key] = new_value

def update_json_file(input_file:str, output_file:str)->None:
    print(f"\033[31mtworze plik: {output_file} na podstawie {input_file}\033[0m ")

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Plik nie znaleziony: {input_file}")
        return
    except json.JSONDecodeError:
        print(f"Niepoprawny JSON w pliku: {input_file}")
        return

    print("Wciśnij Enter, by zostawić obecną wartość.")
    update_nested_dict(data)

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"\nZapisano zaktualizowany plik: {output_file}")
    except Exception as e:
        print(f"Błąd zapisu: {e}")

if __name__ == "__main__":
    # Podaj tu ścieżki do plików:
    input_file = "languagePacks/SamplesForTesting/PLpack.json"
    output_file = "languagePacks/SamplesForTesting/ENpack.json"
    update_json_file(input_file, output_file)

