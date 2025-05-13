#!/usr/bin/env python3
import json
import os

class LanguageManager:
    _instance = None

    @staticmethod
    def get_instance(languagePacks_path="languagePacks/",
                     languages_prefixes=None,
                     default_lang="PL",
                     postfix="pack",
                     debug_mode=False):
        if LanguageManager._instance is None:
            LanguageManager(
                languagePacks_path,
                languages_prefixes or ["PL", "EN"],
                default_lang,
                postfix,
                debug_mode
            )
        else:
            LanguageManager._instance.debug_mode = debug_mode
        return LanguageManager._instance

    def __init__(self,
                 languagePacks_path="languagePacks/",
                 languages_prefixes=["PL", "EN"],
                 default_lang="PL",
                 postfix="pack",
                 debug_mode=False):
        if LanguageManager._instance is not None:
            return
        if default_lang not in languages_prefixes:
            raise ValueError("default language must be in languages_prefixes")
        self.languagePacks_path = languagePacks_path
        self.languages_prefixes = languages_prefixes
        self.default_lang = default_lang
        self.current_lang = default_lang
        self.debug_mode = debug_mode
        self.translations: dict[str, dict] = {}
        for prefix in self.languages_prefixes:
            path = os.path.join(self.languagePacks_path, f"{prefix}{postfix}.json")
            if not os.path.isfile(path):
                raise FileNotFoundError(f"Missing translation file: {path}")
            with open(path, "r", encoding="utf-8") as f:
                self.translations[prefix] = json.load(f)
        LanguageManager._instance = self

    def set_language(self, lang_code: str):
        if lang_code not in self.translations:
            raise ValueError(f"Language '{lang_code}' not available")
        self.current_lang = lang_code

    def get(self, key: str) -> str:
        parts = key.split(".")
        node = LanguageManager._lookup(self.translations.get(self.current_lang, {}), parts)
        if node is None:
            if self.debug_mode:
                return f"ERROR: missing '{key}' in '{self.current_lang}'"
            node = LanguageManager._lookup(self.translations.get(self.default_lang, {}), parts)
            if node is None:
                return key
        return node

    @staticmethod
    def _lookup(dct: dict, parts: list[str]) -> str | None:
        node = dct
        for p in parts:
            if not isinstance(node, dict):
                return None
            node = node.get(p)
            if node is None:
                return None
        return node

if __name__ == "__main__":
    lm = LanguageManager.get_instance(
        languagePacks_path="languagePacks/SamplesForTesting",
        languages_prefixes=["PL", "EN"],
        default_lang="PL",
        postfix="pack",
        debug_mode=True
    )

   
    print(lm.get("ui.menu.file"))              
    lm.set_language("EN")
    print(lm.get("testLanguageManagerPY.firstMessage"))              
    lm.set_language("PL")
    print(lm.get("testLanguageManagerPY.firstMessage"))   
    print(lm.get("nima")) 
