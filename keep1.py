from google.cloud import translate_v2
from google.cloud import translate

def translate_text(text, target_language, source_language=None):
    translate_client = translate_v2.Client()
    result = translate_client.translate(text, target_language=target_language, source_language=source_language)
    return result

text = "As you can see, this is only returning a single word. The dictionary lookup on the google translate page must be an additional call to a different service (not part of the translate service)"
# text = "machine is running"
text2 = "to run"
text3 = "the run"
result = translate_text(text, 'ru', 'en')
print(result)
result = translate_text(text2, 'ru', 'en')
print(result)
result = translate_text(text3, 'ru', 'en')
print(result)

#
# # To Print all the languages that google
# # translator supports
# import googletrans
# from googletrans import Translator
#
# print(googletrans.LANGUAGES)
#
# # Translator method for translation
# translator = Translator()
#
# # short form of english in which
# # you will speak
# from_lang = 'en'
#
# # In which we want to convert, short
# # form of hindi
# to_lang = 'hi'
# get_sentence = "hello, world"
# # text_to_translate = translator.translate(get_sentence,
# #                                          src=from_lang,
# #                                          dest=to_lang)
# #
# # # Storing the translated text in text
# # # variable
# # text = text_to_translate
# # print(text)
#
# googletrans.Translator.detect(googletrans.Translator(), get_sentence)

from os import environ

# from google.cloud import translate
#
with open("project_id token") as token_file:
    project_id = token_file.read()

assert project_id
parent = f"projects/{project_id}"
client = translate.TranslationServiceClient()
#
# response = client.get_supported_languages(parent=parent, display_language_code="en")
# languages = response.languages
#
# # print(f" Languages: {len(languages)} ".center(60, "-"))
# # for language in languages:
# #     print(f"{language.language_code}\t{language.display_name}")
#
#

target_language_code = "ru"

response = client.translate_text(
    contents=[text],
    target_language_code=target_language_code,
    parent=parent,
)

for translation in response.translations:
    print(translation.translated_text)
#
#
#
#
#
#
# def detect_language(text):
#     response = client.detect_language(parent=parent, content=text)
#
#     for languages in response.languages:
#         confidence = languages.confidence
#         language_code = languages.language_code
#         print(
#             f"Confidence: {confidence:6.1%}",
#             f"Language: {language_code}",
#             text,
#             sep=" | ",
#         )
#
#
# sentences = (
#     "Hola Mundo!",
#     "Hallo Welt!",
#     "Bonjour le Monde !",
# )
# for sentence in sentences:
#     detect_language(sentence)


