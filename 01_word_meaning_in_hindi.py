from gtts import gTTS
import os
import json

try:
    with open("hindi_english_dict.json",'r') as f:
         words=json.load(f)


except FileNotFoundError:
         
    words={
        "madad":"help",
        "paani":"water",
        "aag":"fire",
        "billi":"cat",
        'kursi':"chair",
        "khidki":"window",
        "kutta":"dog",}


def yesnocheck(msg):
    ans=input(msg).lower()

    while ans!="yes" and ans!="no":
          print("please enter input in yes/no only ")
          ans=input(msg).lower()

    return ans


def optcheck(msg,opt1,opt2):
    ans=input(msg).lower()

    while ans!=opt1 and ans!=opt2:
          print(f"please enter input in {opt1}/{opt2} only ")
          ans=input(msg).lower()

    return ans






again="yes"
while again=="yes":
    word=input("Enter the word in Hindi or English: ").lower()
    
    #print("The meaning of your word is:",words.get(word)) gets only if word is in Hindi

    if words.get(word) is not None:
        print("The meaning of your word in English is:",words.get(word).capitalize())
        
    elif word in words.values():
            for k in words:
                if word==words[k]:
                    print("The meaning of your word in Hindi is:",k.capitalize())
                    print(v)
                    
    else:
        print("Word not found in dictionary.")
        wordtemp=word
        
    again=yesnocheck("Do you want to search another word? (yes/no): ")
    
    if again!="yes":
        wish=yesnocheck(f'Do you want to add {word} word to the dictionary? (yes/no): ')

        while wish=="yes":
            w=optcheck('What language is this word(H/E) : ',opt1="h",opt2="e")
            if w=="h":
                new_hindi=wordtemp.lower()
                new_english=input("Enter the meaning of the word in English: ").lower()
                words[new_hindi]=new_english
            else:

                
                new_english=wordtemp.lower()
                new_hindi=input('Enter the meaning of the word in Hindi').lower()
                words[new_hindi]=new_english
                

            with open("hindi_english_dict.json", "w") as f:
                json.dump(words, f, indent=4)
            print("New word added successfully!")
            print("Updated dictionary:",words)


            wish=yesnocheck('Do you want to add another word? (yes/no): ')
            if wish!="yes":
                again=yesnocheck("Do you want to search another word? (yes/no): ")
                
                if again!="yes":
                      break

        again=yesnocheck('Do you want to pronounce out loud the dictonary: ')
        if again=="yes":
            read=""
            for k,v in words.items():
                 read+=f"{k} means {v} in english. "
            tts=gTTS(text=read,lang="hi")
            tts.save("words.mp3")
            os.startfile("words.mp3")
        again=yesnocheck('Do You want to search another word? (yes/no): ')

                 
        
        
print("Thank you for using the Hindi/English dictionary!")

    #gets both Hindi and English meanings
        
    #print("The meaning of your word is:",words[word]) #gives error if word not found