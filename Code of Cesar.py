alphabet_zifry ="абвгдеєжзиіїйклмнопрстуфхцщьюяабвгдеєжзиіїйклмнопрстуфхцщьюяabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz123456789123456789"
zbilshenya = int(input("Збільши на :"))
message = input('Текст:').upper()
widpovid = ''
for i in message:
    old_letter = alphabet_zifry.find(i)
    new_letter = old_letter + zbilshenya
    if i in alphabet_zifry:
        widpovid += alphabet_zifry[new_letter]
    else:
        widpovid += i
print(widpovid)
