text = str(input('digite algo aqui:'))

print(f"o tipo de {text} e {type(text)}")
print("comten espaco?",text.isspace())
print("e alfabetico",text.isalpha())
print("e alfanumerico?",text.isalnum())
print("esta em maiusculas",text.isupper())
print("esta em maiusculas",text.islower())
print("esta capitalizado?",text.istitle())