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

def graphwrite():
       words_lengths = {}

       for word in splited_text:
               length = len(word)
               if length in words_lengths:
                       words_lengths[length] += 1
               else:
                      words_lengths[length] = 1

       max_length = max(words_lengths.keys())

       for length in range(1, max_length + 1):
                count = words_lengths.get(length, 0)
                line = f"{length:2d}| {'*' * count} |{count}."
                print(f"{length:3d}|{'*' * count:15s}|{count:2d}")



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

slice_line = "-" * 40

def prihlasujici_fce():

        valid_login = False

        for _ in range(3):
                login_name = input("Zadej přihlašovací jméno: ")
                login_password = input("Zadej heslo: ")

                if login_name in Registered_accounts and login_password == Registered_accounts[login_name]:
                        valid_login = True
                        print(f"""
                {slice_line}
                Welcome to the app, {login_name}
                We have 3 texts to be analyzed.
                {slice_line}
                """)
                        break
                else:
                        print("Neplatné přihlašovací údaje")

                if not valid_login:
                        print("Třikrát jste zadal(a) neplatné přihlašovací údaje. Ukončuji program.")
                        exit()


text_selection = int(input("Enter a number btw. 1 and 3 to select: ")) - 1
print(slice_line)




if text_selection + 1 < 1 or text_selection + 1 > 3:
       print("Neplatná volba")
       quit()
else:
       words_title_case_number = 0
       splited_text = task_template.TEXTS[text_selection].split()
        
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

        #Cast vykresleni grafu..........
       graphwrite()


       

       
       
                


        
       
       

    


    

    



    



