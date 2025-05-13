import os

def loadSettings():
    settings = 'settings.txt'

    # Check does file exist
    if not os.path.exists(settings):
        # Default content
        defaultData = [
            "color : 1\n",
            "language : polish.txt\n",
            "level : 1\n"
        ]
        # Creat file and save default content
        with open(settings, 'w') as f:
            f.writelines(defaultData)
    else:
        # loading data if file exist
        with open(settings, 'r') as f:
            content = f.read()
        # print(content)
        return content

def editSettings():







if __name__ == "__main__":
    settings = loadSettings()

# print("Ustawienia")
# print("1. Ustawienia graficzne")
# print("2. Język")
# print("3. Poziom trudności")
# print("4. Powrót")