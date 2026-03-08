from googletrans import Translator, LANGUAGES

translator = Translator()


# 3.1 Переклад
async def TransLate(text, lang):

    try:

        lang_code = await CodeLang(lang)

        result = await translator.translate(text, dest=lang_code)

        return result.text

    except Exception as e:

        return f"Помилка перекладу: {e}"


# 3.2 Визначення мови
async def LangDetect(txt):

    try:

        result = await translator.detect(txt)

        return result.lang, result.confidence

    except Exception:

        return "unknown", 0


# 3.3 Код мови
async def CodeLang(lang):

    lang = lang.lower()

    if lang in LANGUAGES:
        return lang

    for code, name in LANGUAGES.items():

        if name.lower() == lang:
            return code

    return None