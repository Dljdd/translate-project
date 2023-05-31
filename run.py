from easygoogletranslate import EasyGoogleTranslate

translator = EasyGoogleTranslate(
    source_language='en',
    target_language='de',
    timeout=10
)

while True:
    user_inp = input("Enter a phrase to translate (or 'q' to quit): ")
    
    if user_inp.lower() == 'q':
        break

    result = translator.translate(user_inp)
    print(result)

print("You have successfully exited the app")