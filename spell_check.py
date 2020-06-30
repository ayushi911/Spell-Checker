import enchant #enchant is a module in python used check spelling of a word and give suggestions
import nltk #natural language toolkit
import re #primarily used for string searching and manipulation
nltk.download('words')#module of library nltk
from nltk.corpus import words
#taking the input
text = open('para.txt')#openning the text file

sg = ""#empty string
for i in text:
    if (i!="."):
        sg=sg+i
text=sg

text = re.split('; |,|, |\?|\? |\:|\: |!|! |\*|\n',text)#split using multiple delimiters

final=""#empty string
for i in text:
    final=final+i+" "
text=final#string which do not contain the above characters
text=text.split(" ")
text=text[:-1]#list of words

def spellcheck(text):
       
        for word in text:
            if word!="":#to remove the empty strings
                # Using 'en_US' dictionary
                d = enchant.Dict("en_US")
                #get suggestions for the input word
                suggestions = d.suggest(word)
                #check if the word exists in the dictionary
                word_exists = d.check(word)
               
                if not word_exists:
                        #get suggestions for the input word if the word doesn't exist in the dictionary
                        suggestions = d.suggest(word)

                        print ("input:", word)
                        print("suggestions:", suggestions)
        return
spellcheck(text)
