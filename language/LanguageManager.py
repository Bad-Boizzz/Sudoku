#!/usr/bin/env python3
import json
import os
import time
class LanguageManager(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(LanguageManager, cls).__new__(cls)
        return cls._instance

    def __init__(self,
                 languagePacks_path: str = "languagePacks/",
                 languages_prefixes: list[str] = ["PL", "EN"],
                 default_lang: str = "PL",
                 postfix: str = "pack",
                 debug_mode: bool = False):
        if getattr(self, "_initialized", False):
            return
        
        self.languagePacks_path = languagePacks_path
        self.languages_prefixes = languages_prefixes
        if default_lang not in languages_prefixes:
            raise ValueError("default_lang must be in languages_prefixes")

        self.default_lang = default_lang
        self.current_lang = default_lang
        self.debug_mode = debug_mode
        self.translations: dict[str, dict] = {}

        for prefix in languages_prefixes:
            path = os.path.join(self.languagePacks_path, f"{prefix}{postfix}.json")
            if not os.path.isfile(path):
                raise FileNotFoundError(f"Missing translation file: {path}")
            with open(path, "r", encoding="utf-8") as f:
                self.translations[prefix] = json.load(f)

        self._initialized = True


    def set_language(self, lang_code: str):
        if lang_code not in self.translations:
            raise ValueError(f"Language '{lang_code=}' not available")
        self.current_lang = lang_code

    def get(self, key: str) -> str:
        parts = key.split(".")
        node = LanguageManager._lookup(self.translations.get(self.current_lang, {}), parts)
        if node is None:
            
            if self.debug_mode:
                return f"ERROR: missing '{key}' in '{self.current_lang}'"
            node = LanguageManager._lookup(self.translations.get(self.default_lang, {}), parts)
            if node is None:
                return f"Ani w {self.current_lang=} ani w {self.default_lang=} nie ma {key=}"
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

    @property
    def all_languages(self) -> list[str]:
        return list(self.translations.keys())
    @property
    def current_language(self) -> str:
        return self.current_lang
if __name__ == "__main__":
    print("This module is not meant to be run directly. Use it as a library in your application.")