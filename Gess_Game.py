
# Import Libraries
from gtts import gTTS
from playsound import playsound
import random
# Create a function to find if a character exists in a string or not
def Search (CHAR,LIST) :
    for i in range(len(LIST)):
        if CHAR == LIST[i]:
            return True,i
    return False,-1
# Creat a list for words that can be selected
selection = [["elephant","cat","dog","lion","horse","tiger"],["lamb","window","cup","bed","fan"],["bag","pen","pencile","book","notebook"],["car","bus","bike","plane","motorbike"]]
# Creat a list for the descriptions of the words
textSelection = ["It is an animal.", "It is an object in home.", "It is a school supplier.","It is a method of transportation. "]
# Select a random word and specify its description
setSelection = random.randint(0,3)
wordSelection = random.randint(0,len(selection[setSelection][:])-1)
print(setSelection)
print(len(selection[setSelection][:]))
The_Word= selection[setSelection][wordSelection]
print (The_Word)
# Specify number of chances you want
Chances = 7 
# Read aloud the text
myText = myText=str (textSelection[setSelection])+ " The Word consists of : "+str(len(The_Word))+"letters. guess what is it ?"
myText=myText+"you have"+ str(Chances)+"chances"
Language="en"
output = gTTS(myText,lang=Language,slow=False)
output.save("output.mp3")
playsound("output.mp3")
rightLetters=0                                 # counter for right letters

#Make a loop to take the input from the user and calculate both of number of chances and number of correct letters
while Chances>0:
    gess=input("Enter a Letter : " )
    Yes_No,INDEX = Search(gess,The_Word)
    if gess=="end":                             # end the programe if the user entered "end" 
        break
    elif Yes_No==True:
        playsound ("right.mp3")
        rightLetters = rightLetters+1
        print (INDEX+1)
        if rightLetters==len(The_Word):
            playsound("win.mp3")
            #ctime.sleep(5)
            break 
    else:
        Chances = Chances-1
        if Chances>0:
            playsound("wrong.mp3")       
            path=str(Chances)+"_chances.mp3"
            playsound(path)
        else :
            playsound("gameover.mp3")
# tell the user about the right answer           
outText="the word is "+ The_Word
output2=gTTS(outText,lang=Language,slow=False)
output2.save("output2.mp3")
playsound("output2.mp3")