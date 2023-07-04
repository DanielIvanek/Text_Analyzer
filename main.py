"""
projekt_1.py: 
author: Daniel Ivánek   
email: ivanek.daniel99@gmail.com
discord: notme1275
"""
import task_template
import re
# print(task_template.TEXTS)
slice_line =  "-" * 30

Registered_accounts = {"bob" : "123" , "ann" : "pass123" , 
                       "mike" : "password123", "liz" : "pass123"}

# Vyzadat si prihlasovaci jmeno a heslo
# Zadat jmeno a heslo
#  IF jmeno se shoduje s heslem:
        # ----------------------------------------
        # Welcome to the app, bob
        # We have 3 texts to be analyzed.
        # ----------------------------------------
# Else:
        # unregistered user, terminating the program..
# Vyber text od 1 do 3
#  IF text neni v seznamu textu:
        # Sdel mu to a ukonci program(Nahradit smyckou for)
#  ELIF zada neco jineho nez cislo ukonci program(nahradit smyckou for)
# Pro zvoleny text vypocitej -  
                            # počet slov,
                            # počet slov začínajících velkým písmenem,
                            # počet slov psaných velkými písmeny,
                            # počet slov psaných malými písmeny,
                            # počet čísel (ne cifer),
                            # sumu všech čísel (ne cifer) v textu.
# Vytiskni vysledek

login_name = input("Zadej prihlasovaci jmeno: ")
login_password = (input("Zadej heslo: "))  

for _ in range(3):
        if login_name in Registered_accounts and login_password == (Registered_accounts[login_name]):
                print(f""" {slice_line}
                Welcome to the app, {login_name}
                We have 3 texts to be analyzed.
                {slice_line}                     
                        """ )
                break
        else: 
                print("Nesprávné údaje")
                login_name = input("Zadej prihlasovaci jmeno: ")
                login_password = (input("Zadej heslo: ")) 
                if _ == 2 and login_name not in Registered_accounts and login_password != (Registered_accounts[login_name]):
                        print("unregistered user, terminating the program..")
                        quit()


print(f""" {slice_line}
Welcome to the app, {login_name}
We have 3 texts to be analyzed.
{slice_line}                     
         """ )

text_selection = int(input("Enter a number btw. 1 and 3 to select: ")) - 1
print(slice_line)
words_title_case_number = 0
splited_text = task_template.TEXTS[text_selection].split()



if text_selection < 1 or text_selection > 3:
       print("Neplatná volba")
       quit()
else:
  
       words_count = len(re.findall(r'\w+',task_template.TEXTS[text_selection]))
       print(f"There are {words_count} words in the selected text.")

       words_title_case = [title_pismeno.istitle() for title_pismeno in splited_text]
       words_title_case_number = words_title_case.count(True)     
       print(f"There are {words_title_case_number} titlecase words.")

       words_upper_case_words = (re.findall(r'\b[A-Z]+\b',task_template.TEXTS[text_selection] ))
       words_upper_case_numbers = [upper_word.isupper() for upper_word in words_upper_case_words]
       print(f"There are {words_upper_case_numbers.count(True)} uppercase words.")
       
       words_lower_case_words = (re.findall(r'\b[a-z]+\b',task_template.TEXTS[text_selection] ))
       words_lower_case_numbers = [lower_word.islower() for lower_word in words_lower_case_words]
       print(f"There are {words_lower_case_numbers.count(True)} lowercase words.")
       
       numeric_strings = re.findall(r'\b\d+\b(?!N)', task_template.TEXTS[text_selection])
       print(f"There are {len(numeric_strings)} numeric strings.")  

       numbers_sum = sum(int(number) for number in numeric_strings)
       print(f"The sum of all the numbers {numbers_sum}")

       print(slice_line)
       print("LEN|  OCCURENCES  |NR.")
       print(slice_line)

    


    

    



    



