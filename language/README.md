# Language Manager Documentation

This README provides detailed instructions on how to use the `languageManager` and `createLanguagePackFromPack`

## Table of Contents

- [Introduction](#introduction)
- [languageManager](#languagemanager)

  - [Usage](#usage)

- [LanguagePacks](#language-packs)

- [createLanguagePackFromPack](#createlanguagepackfrompack)
  - [Usage](#usage-1)

---

## Introduction

The `languageManager` is a class that let's you load multiple language packs, change languages and makes getting right messages simple.

The `createLanguagePackFromPack` will load a ready language pack and promt you to enter translations text by text.

---

## `languageManager`

The `languageManager` is the core utility for managing language packs. It provides methods to load language packs, switch between them, and retrieve translations. It makes sure there is only one instance of it.

### Usage

1. **Import the `languageManager`:**

   ```python
    lm = LanguageManager(
        languagePacks_path="path/to/folder/with/packs",
        languages_prefixes=["PL", "EN"],
        default_lang="EN",
        postfix="pack",
        debug_mode=True
    )
   ```

   Now languageManager loaded all `.json` files that are named: `"languagePrefix+postfix+.json"` from languagePacks_path directory e.g. `PLpack.json`

   default_lang is langugage that is now set. If language is changed and appropriate lang pack does not contain said phrase (`debug_mode` must be set at `False`) (key) phrase from default pack will be loaded

   `debug_mode` - if true: in case of missing key form current language pack error will be shown, otherwise phrase from default lang will be shown

2. **Set lanuage**

   ```python
    lm.set_language("PL")
   ```

3. **Printing phrases**

   ```python
    print(lm.get("testLanguageManagerPY.firstMessage"))
   ```

   using `languageManager.get()` one has to use dots to separate "levels" of json file

---

### Language Packs

Here I will also very briefly explain language packs

We will store them in `.json` files. Why? Because this fantastic piece of enginerring is so great. We dont have to write our own dictionary based system. Parsing those things is a nightmare. Json parser are ready to use, lighweight, with python very easy to use.

So lanugage packs should be named e.g. `PLpack.json` where:

1. `PL` - stands for language and is a prefix that will be used to acces that language in code
2. `pack` - a postfix that as a author od this piece of code have chosen to make my life easier in future. All packs should end like that
   .
3. `.json` - file format

ALL PACKS SHALL BE NAMED LIKE THIS!

Language pack should start with this key:

```json
"LanguagePackInfo":
{
    "Nazwa": "Polski",
    "Wersja": "1.0.0",
    "DataWydania": "13.05.2025"

},
```

One can add whetewher he wants, it does not matter - include author name,email ...

## `createLanguagePackFromPack`

### Prevention of merge confits within language packs

The `createLanguagePackFromPack` function allows you to create a new language pack by extending or modifying an existing one.

### Usage

I believe that main function with all promts are self explanatory

For further assistance, refer to the source code or contact the project maintainers.
