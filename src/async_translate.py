import asyncio
import time
from translator import TransLate, LangDetect


async def translate_sentence(sentence, target_lang):

    lang, conf = await LangDetect(sentence)

    translation = await TransLate(sentence, target_lang)

    return translation


async def async_translate(sentences, target_lang):

    start = time.time()

    tasks = [translate_sentence(s, target_lang) for s in sentences]

    results = await asyncio.gather(*tasks)

    end = time.time()

    return results, end - start