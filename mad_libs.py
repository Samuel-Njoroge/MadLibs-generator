#Importing modules
#tkinter - A GUI Python library used to build GUI applications
from tkinter import * 

#Creating a display window

root = Tk()
root.geometry('300x300')
root.title('Mad Libs Generator')
Label(root, text= 'Mad Libs Generator \n Have Fun!' , font = 'arial 20 bold').pack()
Label(root, text = 'Click Any One :', font = 'arial 15 bold').place(x=40, y=80)

#Function
def madlib1():
    animals = input('Enter an animal name: ')
    profession = input('Enter a profession name: ')
    cloth = input('Enter a piece of cloth name:  ')
    things = input('Enter a thing name: ')
    name = input('Enter a name: ')
    place = input('Enter a place name: ')
    verb = input('Enter a verb in ing form: ')
    food = input('Food name: ')
    print('say ' + food + ', the photographer said as the camera flashed! '
     + name + ' and I had gone to ' + place 
     +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as '
      + animals + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' 
      + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')

def madlib2():
   
    adjactive = input('enter adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name :')
    place = input('enter a place name : ')
    person= input('enter a person name : ')
    adjactive1 = input('enter a adjactive : ')
    insect= input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')
    print('Last night I dreamed I was a ' +adjactive+ ' butterfly with ' + color+ ' splocthes that looked like '+thing+ ' .I flew to ' + place+ ' with my bestfriend and '+person+ ' who was a '+adjactive1+ ' ' +insect +' .We ate some ' +food+ ' when we got there and then decided to '+verb+ ' and the dream ended when I said-- lets ' +verb+ '.')
def madlib3():
    person = input('enter person name: ')
    color = input('enter color : ')
    foods = input('enter food name : ')
    adjective = input('enter aa adjective name: ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name: ')
    things = input('enter a thing name : ')
   
    print('Today we picked apple from '+person+ "'s Orchard. I had no idea there were so many different varieties of apples. I ate " +color+ ' apples straight off the tree that tested like '+foods+ '. Then there was a '+adjective+ ' apple that looked like a ' + thing + '.When our bag were full, we went on a free hay ride to '+place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '. I can hardly wait to get home and cook with the apples. We are going to make appple '+food+ ' and '+things+' pies!.')  


#Defining buttons
Button(root, text= 'The Photographer', font ='arial 15', command= madlib1, bg = 'ghost white').place(x=60, y=120)
Button(root, text= 'apple and apple', font ='arial 15', command = madlib3 , bg = 'ghost white').place(x=70, y=180)
Button(root, text= 'The Butterfly', font ='arial 15', command = madlib2, bg = 'ghost white').place(x=80, y=240)

root.mainloop()


"""Tk() - window creating
geometry() -To set the width and height of the window
title() -To give the title of the window
Label() - To display text that users cant able to modify
root is the name which we give to our window
text Takes the text we want to display on the label
font - To set the size and type of fonts
pack organized widget in block
input() - Takes the input from the user
print() - Print the text given in it.
Button() - To display buttons on our tkinter window

command is called when the button is click and it is used to call the function

root.mainloop()-To run our program
place() - To place widgets in a specific position"""