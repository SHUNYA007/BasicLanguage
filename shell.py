import basic

while True:
    text= input('basic >> ')
    tokens,errors=basic.run('<stdin>',text)
    if errors:
        print(errors.as_string())
    else:
        print(tokens)
