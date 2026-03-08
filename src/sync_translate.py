import time
import asyncio
from translator import TransLate, LangDetect


def sync_translate(sentences, target_lang):

    translations = []

    start_time = time.time()

    for sentence in sentences:

        lang, conf = asyncio.run(LangDetect(sentence))

        translated = asyncio.run(TransLate(sentence, target_lang))

        translations.append(translated)

    end_time = time.time()

    return translations, end_time - start_time