from tkinter import *
import random
import sys 

def madlibs1():
    #printing the title
    print("\nTour the campus")
    #mad libs paragraph name: tour the campus
    #author: lovetoknow.com
    #inputs required for the paragraph
    pro_noun = input('Enter a Proper Noun: ')
    adj = input('Enter an Adjective: ')
    fam_person = input('Enter the name of a Famous Person: ')
    noun = input('Enter a noun: ')
    num = input('Enter a number: ')
    adj2 = input('Enter an Adjective: ')
    plant = input('Enter the name of a Plant: ')
    place = input('Enter a Place: ')
    adverb = input('Enter an Adverb: ')
    pro_noun2 = input('Enter a Proper Noun: ')
    verb = input('Enter a Verb: ')
    interj = input('Enter an Interjection: ')
    song = input('Enter a Song: ')
    adj3 = input('Enter an Adjective: ')
    adj4 = input('Enter an Adjective: ')
    pru_noun = input('Enter a Plural Noun: ')
    verb2 = input('Enter a verb: ')

    #the following line will integrate all the inputs with the paragraph
    print(f'''Welcome to the University of {pro_noun}. Our {adj} campus was founded by {fam_person} and built in 1806. 
We begin at our {noun} building. This building houses {num} classrooms. 
To your left, the {adj2} dormitory is visible just beyond the {plant}. 
Our students come from all over the {place} because we {adverb} accept anyone who applies.
 We will end the tour here at {pro_noun2} hall which houses the Admissions Office. 
Feel free to {verb} an application. {interj} folks, you’re in for a treat! 
The marching band is practicing our Alma Mater, {song} Notice how they march in a {adj3} formation,
it is the signature move of our University. Financial aid is available to all {adj4} applicants.
More information is available on our website, {pru_noun}.com. Thank you for {verb2} with us today.''') 

def madlibs2():
    #printing the title
    print("\nVacation")
    #mad libs paragraph name: vacation
    #author: madlibs.com
    #inputs for the paragraph
    adj = input('Enter an Adjective: ')
    adj2 = input('Enter an Adjective: ')
    noun  = input('Enter a Noun: ')
    noun2 = input('Enter a Noun: ')
    pru_noun = input('Enter a Plural Noun: ')
    game = input('Enter the Name of a Game: ')
    pru_noun2 = input('Enter a Plural Noun: ')
    verb_ing = input("Enter a Verb ending with 'ing': ")
    verb_ing2 = input("Enter a Verb ending with 'ing': ")
    pru_noun3 = input('Enter a Plural Noun: ')
    noun3 = input('Enter a Noun: ')
    plant = input('Enter the name of a plant: ')
    body_part = input('Enter the name of a BodyPart: ')
    place = input('Enter the Name of a Place :')
    verb_ing3 = input("Enter a verb ending with 'ing': ")
    adj3 = input('Enter an Adjective: ')
    num = input('Enter a Number: ')
    pru_noun4 = input('Enter a Plural Noun: ')

    #the following line integrates the above taken inputs into the paragraph and prints it.
    print(f'''A vacation is when you take a trip to some {adj} place with your {adj2} family. 
Usually you go to some place that is near a/an {noun} or up on a/an {noun2}. 
A good vacation place is one where you can ride {pru_noun} or play {game} or go hunting for {pru_noun2}. 
I like to spend my time {verb_ing} or {verb_ing2}. When parents go on a vacation, 
they spend their time eating three {pru_noun3} a day, and fathers play golf, and mothers sit around {verb_ing3}. 
Last summer, my little brother fell in a/an {noun3} and got poison {plant} all over his {body_part}. 
My family is going to go to (the) {place}, and I will practice {verb_ing3}. 
Parents need vacations more than kids because parents are always very {adj3} and 
because they have to work {num} hours every day all year making enough {pru_noun4} to pay for the vacation.''')

def madlibs3():
    #printing the title
    print("\nA Day at the Zoo")
    #name of the paragraph: a day at the zoo
    #author: unknown
    #the following are the inputs required for the paragraph
    adjective1 = input('Enter an adjective: ')
    noun1 = input('Enter a noun: ')
    verb1 = input('Enter a verb (in past tense): ')
    adverb1 = input('Enter an adverb (corresponding to the verb entered above): ')
    adjective2 = input('Enter an adjective: ')
    noun2 = input('Enter a noun: ')
    noun3 = input('Enter a noun: ')
    adjective3 = input('Enter an adjective: ')
    verb2 = input('Enter a verb: ')
    adverb2 = input('Enter an adverb: ')
    verb3 = input('Enter a verb (in past tense): ')
    adjective4 = input('Enter an adjective: ')

    #the following line integrates the above taken inputs into the paragraph and prints it.
    print(f'''Today I went to the zoo. I saw a(n) {adjective1} {noun1} jumping up and down in its tree. 
He {verb1} {adverb1} through the large tunnel that led to its {adjective2} {noun2}. 
I got some peanuts and passed them through the cage to a gigantic gray {noun3} towering above my head. 
Feeding that animal made me hungry. I went to get a {adjective3} scoop of ice cream. 
It filled my stomach. Afterwards I had to {verb2} {adverb2} to catch our bus. 
When I got home I {verb3} my mom for a {adjective4} day at the zoo.''')

#defining a function which select's a random paragraph
def random_pick():
    c = random.choice([1,2,3])
    if c == 1:
        madlibs1()
    elif c == 2:
        madlibs2()
    elif c == 3:
        madlibs3()

#function to add a exit button
def exit():
    sys.exit(0)

#defining the window
window = Tk()

#setting the window's dimensions
window.geometry('400x460')
window.configure(bg='sky blue')

#giving the window a title
window.title("Mad Libs Generator")

#changing the windows icon
p1 = PhotoImage(file="icon.png")
window.iconphoto(False,p1)

#the main heading 
Label(window, text= 'Mad Libs Generator' , font = 'arial 25 bold', bg='sky blue').pack()
Label(window, text = 'Choose Any One!', font = 'arial 17 bold',bg='sky blue').place(x=100, y=80)

#defining the buttons
Button(window, text= "Tour the Campus", font ='arial 15', command= madlibs1, bg = 'light green').place(x=100, y=120)
Button(window, text= "Vacation", font ='arial 15', command = madlibs2 , bg = 'light green').place(x=100, y=180)
Button(window, text= 'A Day at the Zoo', font ='arial 15', command = madlibs3, bg = 'light green').place(x=100, y=240)
Button(window, text= 'A Random Paragraph', font ='arial 15', command = random_pick, bg = 'light green').place(x=100, y=300)
Button(window, text= 'Exit', font ='arial 15', command = exit, bg = 'ghost white').place(x=325, y=400)

#running the window
window.mainloop()