def check_vowels(string):
   # vowels
   vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
   # iterating over the string
   for char in string:
      if char not in vowels:
        print("Vowel in string")
      break
   else:
      print("Vowel not in string")


string = str(input("Enter string:"))
check_vowels(string)
