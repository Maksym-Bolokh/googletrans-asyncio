import asyncio
import re
from translator import LangDetect
from sync_translate import sync_translate
from async_translate import async_translate


def read_text(filename):

    try:
        with open(filename, "r", encoding="utf-8") as file:

            text = file.read()

        sentences = re.split(r'[.!?]\s+', text)

        sentences = [s.strip() for s in sentences if s.strip()]

        return text, sentences

    except Exception as e:

        print("Помилка читання файлу:", e)

        return None, []


def main():

    filename = "data/Steve_Jobs.txt"
    target_lang = "et"   # мова перекладу

    text, sentences = read_text(filename)

    if not text:
        return

    print("Файл:", filename)
    print("Кількість символів:", len(text))
    print("Кількість речень:", len(sentences))

    import asyncio
    lang, conf = asyncio.run(LangDetect(text))

    print("Мова тексту:", lang)
    print("Confidence:", conf)

    print("\nОРИГІНАЛЬНИЙ ТЕКСТ:\n")
    print(text)

    # Синхронний переклад
    sync_result, sync_time = sync_translate(sentences, target_lang)

    print("\nПереклад (синхронний):\n")
    print(" ".join(sync_result))

    print("\nЧас синхронного перекладу:", sync_time)

    # Асинхронний переклад
    async_result, async_time = asyncio.run(
        async_translate(sentences, target_lang)
    )

    print("\nПереклад (асинхронний):\n")
    print(" ".join(async_result))

    print("\nЧас асинхронного перекладу:", async_time)


if __name__ == "__main__":
    main()