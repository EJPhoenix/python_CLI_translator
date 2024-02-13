from translate import Translator

translator = Translator(to_lang='zh')

with open('ADD FILE', mode ='r') as my_file:
    text = my_file.read()
    translation = translator.translate(text)
    print(translation)
    with open('ADD FILE', mode='w') as my_file2:
        my_file2.write(translation)



# if __name__ == '__main__':
#     print_hi('PyCharm')