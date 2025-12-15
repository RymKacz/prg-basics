
translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
input_word = input("Enter an English word: ").strip().lower()
if input_word in translations:
   print(f"The Polish word for '{input_word}' is '{translations[input_word]}'.")
else:
   print(f"Sorry, the word '{input_word}' is not in the dictionary.")