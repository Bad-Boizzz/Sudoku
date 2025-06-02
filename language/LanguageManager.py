import json
import os

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
        if default_lang not in languages_prefixes:
            raise ValueError("default_lang must be in languages_prefixes")

        self.languagePacks_path = languagePacks_path
        self.languages_prefixes = languages_prefixes
        self.default_lang = default_lang
        self.current_lang = default_lang
        self.debug_mode = debug_mode
        self.translations: dict[str, dict] = {}

        prev_prefix = None
        for prefix in languages_prefixes:
            path = os.path.join(self.languagePacks_path, f"{prefix}{postfix}.json")
            if not os.path.isfile(path):
                raise FileNotFoundError(f"Missing translation file: {path}")
            with open(path, "r", encoding="utf-8") as f:
                self.translations[prefix] = json.load(f)
            if prev_prefix is not None:
                if self.check_if_same_keys(self.translations[prev_prefix], self.translations[prefix]) is False:
                    raise ValueError(f"Translation files {prev_prefix} and {prefix} have different keys")
            prev_prefix = prefix
            if self.translations[prefix] is None:
                raise ValueError(f"Translation file {path} is empty or invalid")
        self._initialized = True


    def __collect_keys(self, obj, prefix=None, result=None):
        if result is None:
            result = set()
        if prefix is None:
            prefix = ""

        if isinstance(obj, dict):
            for key, val in obj.items():
                new_path = key if prefix == "" else f"{prefix}.{key}"
                result.add(new_path)
                self.__collect_keys(val, new_path, result)

        elif isinstance(obj, list):
            for item in obj:
                self.__collect_keys(item, prefix, result)
        return result
    def check_if_same_keys(self, json1, json2) -> bool:
        keys1 = self.__collect_keys(json1)
        keys2 = self.__collect_keys(json2)
        return keys1 == keys2

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
                return "Ani w " + str({self.current_lang})+" ani w "+ str({self.default_lang})+" nie ma "+str({key})
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
    lm = LanguageManager(
        languagePacks_path="languagePacks/SamplesForTesting",
        languages_prefixes=["PL", "EN"],
        default_lang="EN",
        postfix="pack",
        debug_mode=True
    )

   
    print(lm.get("ui.menu.file"))              
    lm.set_language("EN")
    print(lm.get("testLanguageManagerPY.firstMessage"))              
    lm.set_language("PL")
    print(lm.get("testLanguageManagerPY.firstMessage"))   
    #print(lm.get("nima")) 
