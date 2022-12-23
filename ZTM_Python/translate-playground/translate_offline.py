from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('test.txt', 'r') as file:
        file_content = file.read()
except FileNotFoundError as e:
    print('check your file path silly')

translation = translator.translate(file_content)
