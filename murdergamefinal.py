import time
import sys,time,os

def typewriter (speaking):
    for char in speaking:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)

os.system("cls")

def pr_cyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def pr_light_purple(skk): print("\033[94m {}\033[00m" .format(skk))
def pr_light_blue(skk): print("\033[94m {}\033[00m" .format(skk))
def pr_red(skk): print("\033[91m {}\033[00m".format(skk))
def pr_green(skk): print("\033[92m {}\033[00m" .format(skk))
def pr_yellow(skk): print("\033[93m {}\033[00m" .format(skk))

def game_over():
    print()
    pr_red("---- GAME OVER ----")
    print()
    player = input ("Would you like to try again? [Yes/No] ")
    if player == "yes" or player == "y" or player == "Yes" or player == "Y":
        start_game()
    elif player == "no" or player == "n" or player == "No" or player == "N":
        exit() 
    else:
        print("I'm sorry, I didn't quite catch that. Please try again.")
        game_over()



def pick_up_phone():
    print("You decided to pick up the phone.")
    time.sleep(3)
    pr_yellow("[You got an old mobile phone!]")
    time.sleep(3.5)
    print()
    print()

def pick_up_phone_W():
    speaking = ("\u001b[36m Oh look, I think there's a phone lying there by the bush. Let's check it out. It might be useful.\u001b[37m")
    typewriter(speaking)
    print()
    time.sleep(2.5)
    pr_yellow("[You got an old mobile phone!]")
    time.sleep(3.5)
    print()
    print()

def try_again_2():
    print("I'm afraid I didn't quite understand. Could you say that again? ")
    player = input ("Will you pick it up? ")
    if player == "Yes" or player == "Y" or player == "yes" or player == "y":
        pick_up_phone()

    elif player == "No" or player == "N" or player == "n" or player == "no":
        pick_up_phone_W()

    else:
        try_again_2()


def left_path():
    
    speaking = (" \u001b[36m Alright, let's go left. There's some creepy looking trees and bushes there. Perfect place for Jay to be lurking about.\n\
    You know what I just can't wrap my head around?\n\
    Why drown the poor bastards in coffee? Why in coffee of all things? Why not drown them in water like a normal killer?! \n\
    When we catch him, and I mean WHEN not IF, I am definitely going to ask him about it. \u001b[37m")
    typewriter(speaking)
    print()
    print()
    time.sleep(3)
    print("You ponder Dt. Watson's morals and sanity for a moment.")
    print()
    time.sleep(3.5)
    print("As you walk through the empty park, you notice a little, round-ish object barely poking out of a nearby bush.")
    print()
    time.sleep(2.5)
    print("You wonder what it could be. ")
    print()
    time.sleep(3.5)
    print("Curiosity got the better of you and you decide to go have a look.")
    print()
    time.sleep(3.5)
    print("It's a mobile phone!") 
    print("It looks quite old, like something from the early '00s.")
    print()
    time.sleep(2)



    player = input ("Will you pick it up? [Yes/ No]: ")
    if player == "Yes" or player == "Y" or player == "yes" or player == "y":
        pick_up_phone()
        level_two()

    elif player == "No" or player == "N" or player == "n" or player == "no":
        pick_up_phone_W()
        level_two()

    else:
        try_again_2()
    


def right_path():
    print("You decided to head towards the pond on the right.")
    print()
    time.sleep(2.5)
    print("In the dark, you don't notice that there's an uncovered manhole in your path.")
    time.sleep(2.5)
    print ("You fall into it breaking both your legs and cracking a few ribs.")
    time.sleep(2.5)
    print("The injuries you sustainded put you in the hospital for several weeks.")
    print()
    time.sleep(2.5)
    print("You are taken off the case.")
    print()
    print()
    pr_red("----- GAME OVER ----")

    player = input ("Would you like to try again? [Yes/No] ")
    if player == "yes" or player == "y" or player == "Yes" or player == "Y":
        start_game()
    elif player == "no" or player == "n" or player == "No" or player == "N":
        exit() 

def try_again_1():
    print ("I'm afraid I didn't quite catch that. Could you try again?")
    pr_cyan("Which way should we check out first? It's your call, {}.".format(name))

    left_or_right = input ("Which way do you turn? ")
    if left_or_right == "left" or left_or_right == "Left" or left_or_right == "l" or left_or_right == "L":
        left_path()
    elif left_or_right == "right" or left_or_right == "Right" or left_or_right == "r" or left_or_right == "R":
        right_path()
    else: 
        try_again_1()

# DO NOT CALL! = easter egg - mini game? ASCII? ASCII of a cup off coffee? 


def jay_flat():
    print("You make your way in. ")
    print()
    time.sleep(2)
    interaction_options = [
        "1. Living room.", 
        "2. Kitchen.",
        "3. Bathroom.",
        "4. Bedroom.",
    ]
    print()
    index = 0
    while index < len(interaction_options):
        print(interaction_options [index])
        index += 1
    time.sleep(2)
    
    player = input("Which room would you like to investigate? [1/2/3/4]: ")
    if player == "Living Room" or player == "Living room" or player == "living room" or player == "1":

        print("You make your way to the living room.")
        time.sleep(3)
        print("You have a look around and notice a bookshelf full of books.")
        time.sleep(3)
        print("You skim the book titles. Suprisingly, none of them are about coffee.")
        time.sleep(4)
        print("As you turn around, you notice a photograph wedged in between the cushions of the sofa behind you.")
        time.sleep(4)
        print("You reach in and take it out.")
        time.sleep(2)
        print("It's a photo of Marian with the words 'You'll be awake for good!' written on it.")
        time.sleep(3)
        print("A chill runs down your spine.")
        time.sleep(3)
        print("You decide to turn back and try another room.")
        time.sleep(5)
        jay_flat()

    elif player == "kitchen" or player == "Kitchen" or player == "2":
        print("You make your way to the kitchen.")
        time.sleep(2)
        print("...")
        time.sleep(3)
        print("...")
        time.sleep(3)
        print("You look everywhere but cannot find anything useful to the investigation.")
        time.sleep(4)
        print("Well, if you ignore all the coffee beans scattered around the place.")
        time.sleep(4)
        print("You decide to turn back and look in another room.")
        time.sleep(5)
        jay_flat()
    
    elif player == "bathroom" or player == "Bathroom" or player == "3":
        print("You make your way to the bathroom.")
        time.sleep(2)
        print("As soon as you enter, you notice a lot of old coffee stains on the floor.")
        time.sleep(3)
        print("They must have been here for quite a while.")
        time.sleep(2)
        print("You go slightly further in, and have a look in the sink.")
        time.sleep(3)
        print("There is a bloodied knife in it!")
        time.sleep(2)
        print("You decide to bag it as evidence.")
        time.sleep(2)
        pr_yellow("[You got new evidence!]")
        time.sleep(4)
        print("You decide to look some more in another room.")
        time.sleep(3)
        jay_flat()
    elif player == "bedroom" or player == "Bedroom" or player == "4":
        print("You make your way to the bedroom.")
        time.sleep(2)
        print("Dt. Watson:")
        speaking = ("\u001b[36m Better be careful, you don't know what's waiting behind this door. \u001b[37m")
        typewriter(speaking)
        print()
        print("You take out your baton, just in case, and open the door ever so slowly.")
        time.sleep(3)
        print("There, on the bed, you see the one and only 'Jay', just sitting there.")
        time.sleep(2)
        print("Clearly, he's been waiting for you.")
        time.sleep(3)
        print("Jay:")
        speaking = ("\u001b[32m Took you long enough. \u001b[37m")
        typewriter(speaking)
        print()
        speaking = ("'Hands in the air! Slowly! No sudden movements or I'll whack you!'")
        typewriter(speaking)
        print()
        speaking = (" \u001b[32m Don't worry, I won't resist. I knew you were on to me for a while. \n\
            You're really not so inconspicuous, especially you, Watson. Though you are persistent, I'll give you that. \n\
            Seems you got yourself someone clever enough to actually find me. \u001b[37m")
        typewriter(speaking)
        print()
        print("Dt. Watson:")
        speaking = (" \u001b[36m Why? \u001b[37m")
        typewriter(speaking)
        print()
        print("Jay:")
        speaking = (" \u001b[32m Why, what? Why did I kill? Why did I become the way I am? \u001b[37m")
        typewriter(speaking)
        print()
        print("Dt.Watson:")
        speaking = (" \u001b[36m No, just... why coffee? \u001b[37m")
        typewriter(speaking)
        print()
        print("Jay:")
        speaking = (" \u001b[32m Really, THIS is what you want to know? \n\
            Out of all the possible questions you could ask me right now, this is the one you choose to ask?!\u001b[37m")
        typewriter(speaking)
        print()
        print("Dt. Watson:")
        speaking = (" \u001b[36m Yeah. \u001b[37m")
        typewriter(speaking)
        print()
        print("Jay:")
        speaking = ("\u001b[32m Because I can't stand tea. \u001b[37m")
        typewriter(speaking)
        time.sleep(5)
        print()
        print()
        print("You and your partner arrest Jay.")
        time.sleep(2)
        print("He is currently serving his time for the crimes he has committed.")
        print()
        print()
        time.sleep(5)
        print("Dt Watson:")
        speaking = (" \u001b[36m Thanks {}, I couldn't have done it without you. \u001b[37m".format(name))
        typewriter(speaking)
        print()
        time.sleep(4)
        print()
        print()
        print("....")
        time.sleep(2)
        print()
        print("....")
        time.sleep(2)
        print()
        print("---- SOME TIME LATER ----")
        print()
        time.sleep(3)
        print("You receive a note in the post.")
        time.sleep(3)
        print("It reads:")
        speaking = ("Congratulations on solving the case Detective {}. \n\
            Unfortunately, your accomplishement has been rather detrimental to our efforts. \n\
                We shall pay you a visit in the near future, to ensure such a mishap doesn't repeat itself.".format(name))
        typewriter(speaking) 
        print()       
        time.sleep(5)
        print()
        print()
        print()
        print("---- YOU WON !!! ----")
        time.sleep(5)
        

    else:
        print("I'm sorry, I didn't quite understand. Try again? ")
        jay_flat()

    

def level_five():
    print("You make your way to Jay's flat.")
    time.sleep(2)
    print("You find the door is open.")
    time.sleep(2)
    print("Dt. Watson:")
    speaking = (" \u001b[36m Seems a bit too good to be true. Almost like he wants us to be here. \n\
        Better be on our toes. \u001b[37m ")
    typewriter(speaking)
    print()
    time.sleep(3)
    jay_flat()

def level_four_question():

    print ("How will you persuade her? ") 
    print()
    time.sleep(2)
    interaction_options = [
        "1. Buy her a coffee.", 
        "2. Try to bribe her.",
        "3. Ask her about herself.",
        "4. Schmooze her.",
    ]
    print()
    index = 0
    while index < len(interaction_options):
        print(interaction_options [index])
        index += 1
    time.sleep(2)


    response = input("Which option would you like to try? [1/2/3/4]: ")

    print()
    if response == "1" or response == "option 1" or response == "op1" or response == "coffee":
        speaking = ("\u001b[35m I already have a coffee. Why would I want another one? \u001b[37m")
        typewriter(speaking)
        print()
        time.sleep(2)
        print("Try another option.")
        time.sleep(2)
        level_four_question()
        
    elif response ==  "2" or response == "option 2" or response == "op2":
        print("You tried to bribe the lady with some money, but accidentally pull out an old Blockbuster card from your wallet.")
        speaking = ("\u001b[35m Did you seriously try to bribe me with a Blockbuster card?! What year do you think this is? \n\
        You know what, I'll take it. I still won't talk to you, but I'll take it.\u001b[37m")
        typewriter(speaking)
        print()
        time.sleep(2)
        pr_yellow("[You lost your Blockbuster card]")
        print()
        print("Please try another option.")
        time.sleep(2)
        print()
        level_four_question()

    elif response == "3" or response == "option 3" or response == "op3": 
        speaking = ("\u001b[35m Wouldn't you like to know, pig!. \u001b[37m")
        typewriter(speaking)
        print()
        print("That seems to have angered her.")
        print()
        print("Maybe another option.")
        level_four_question()
          
    elif response == "4" or response == "option 4" or response == "op4":       
        print("You decide to up your charm and schmooze the cafe lady.")
        time.sleep(3)
        print("She is flattered and quite taken with you.")
        time.sleep(2)
        print("She tells you her name is 'Luz'.")
        time.sleep(2)
        print("She also tells you she saw a man rush in and go straight for the bathroom only to come out and leave in a hurry.")
        time.sleep(6)
        print("")
        print("")
        print("You and Dt Watson enter the bathroom and notice some cloth peeking out of the bin.")
        time.sleep(5)
        print("You take a look and it is a pair of navy coloured jeans with what seems to be coffee and blood stains.")
        time.sleep(5)
        print("You decide to take the trousers with you as evidence.")
        time.sleep(4)
        pr_yellow("[You got new evidence!]")
        print("")
        time.sleep(3)
        print("The forensics lab at the station was able to confirm, the blood stains found on the trousers belong to")
        print("two people: Marian I. – Jay's latest victim, and one other, unidentified person.")
        time.sleep(5)
        print()
        print("Dt. Watson:")
        speaking = (" \u001b[36m Hmm, seems we've found our killer. Call it intuition, but I'll bet the other blood sample \n\
        is going to belong to our friend 'Jay'. \n\
        Let's pay him a visit shall we? \u001b[37m")
        typewriter(speaking)
        print()
        time.sleep(4)

        level_five()
    else:
        print("That's not one of the options. Try again.")
        level_four_question()



def level_four():
    print("You and Dt. Watson make your way to the Starbucks.")
    time.sleep(2)
    print("Maybe it's not too late...")
    time.sleep(1.5)
    print()
    print("Inside, you notice a single customer sitting by the window, having a cup of coffee. She seems lost in thought.")
    time.sleep(3)
    print()

    player = input("Question her? [Yes/No] ")
    if player == "No" or player == "no" or player == "N" or player == "n":
        print("You decide not to question the customer.")
        time.sleep(2)
        print("Dt. Watson doesn't question her either.")
        time.sleep(2)
        print("Since you didn't find Jay inside, you decided to return to the station.")
        time.sleep(3)
        print("In the mean time, 'The Coffee Killer' struck again, claiming another innocent life.")
        time.sleep(3.5)
        print("You and Dt.Watson are taken off the case due to your incompetence.")
        print()
        print()
        time.sleep(5)
        game_over()

    elif player == "Yes" or player == "yes" or player == "Y" or player == "y":
        print("You decide to question the lady sitting at the cafe.")
        print()
        speaking = ("'Hi! My name is Dt {} and this is my partner Dt Watson.'".format(name))
        typewriter(speaking)
        print()
        speaking = ("'We were wondering if we could ask you a few questions?'")
        typewriter(speaking)
        print()
        time.sleep(2)
        print("Lady:")
        speaking = (" \u001b[35m I'd rather you left me alone. \n\
        I'm trying to enjoy my coffee and don't have time to be talking to some coppers. \u001b[37m")
        typewriter(speaking)
        print()
        print()
        time.sleep(3)
        print("Looks like you'll have to persuade the lady into talking.")
        time.sleep(3)
        print()
        
        level_four_question()
    else:
        print("I'm sorry, I didn't quite get that. Please try again.")
        level_four()



def level_three():
    jay = [
            "White British",
            "Mid-Twenties",
            "Speaks with a Mancunian accent"
        ]

    player = input("Will you give Alex a call? [Y/N] ")
    if player == "y" or player == "Y" or player == "yes" or player == "Yes":
        print("You decided to follow up on the lead you just received from Razvan, and call Alex.")
        print ()
        print()
        time.sleep(4)

        speaking = (" \u001b[35m Hello? \u001b[37m")
        typewriter(speaking)
        print()
        speaking = ("'Hi there, my name is Dt. {}. Am I speaking with Alex?'".format(name))
        typewriter(speaking)
        print()
        speaking = (" \u001b[35m Yes, this is Alex. How can I help you? \u001b[37m ")
        typewriter(speaking)
        print()
        speaking = ("'One of your neighbours is currently under investigation, and I was hoping you could help me out with the case.'")
        typewriter(speaking)
        print()
        speaking = ("\u001b[35m Oh, wow. Uh ok, but I don't want any trouble. \u001b[37m")
        typewriter(speaking)
        print()
        speaking = ("'Don't worry, you will remain completely anonymous.'")
        typewriter(speaking)
        print()
        time.sleep(1)
        speaking = ("\u001b[35m Ok, then. \u001b[37m")
        typewriter(speaking)
        print()
        speaking = ("'Great. First, could you tell me where you live? We know our suspect is one of your neighbours, but we do not have his address.'")
        typewriter(speaking)
        print()
        speaking = (" \u001b[35m I live at 2 Monck St, S1P 2BW. Flat 32. \u001b[37m")
        typewriter(speaking)
        print()
        speaking = ("'Ok, great! Now, have you seen a man matching this description around your neighbourhood?'")
        typewriter(speaking)
        print()
        time.sleep(2)
        print(jay)
        speaking = (" \u001b[35m Oh, you mean Jay? Yeah, I see him all the time! Such a lovely fella. \n\
        He lives in the flat one floor below mine. I just saw him half an hour ago. He told me he's going to grab a coffee at our local Starbucks. \u001b[37m")
        typewriter(speaking)
        print()
        speaking = ("'Great. Thank you. \n\
        If you remember any other information, please give me a call on this number. Every little helps.'")
        typewriter(speaking)
        print()
        speaking = (" \u001b[35m 'Will do!' \u001b[37m")
        typewriter(speaking)
        print()
        time.sleep(3)
        print()
        print()
        level_four()


    elif player == "n" or player == "N" or player == "no" or player == "No":
        print("Against your better judgement, you decide not to call Alex.")
        time.sleep(2)
        print("Honestly, you don't know why Dt. Watson allowed you to ignore such a lead.")
        time.sleep(3)
        print("Clearly, if this Alex is neighbours with Jay, he might have known something. You could have solved this case perhaps even tonight!")
        time.sleep(5)
        print("Now, because of your and Dt. Watson's incompetence, another victim has been claimed by the infamous 'Coffee Killer'.")
        time.sleep(3)
        print()
        print()
        game_over()
    else:
        print("I'm sorry. I didn't understand. Please try again.")
        time.sleep(3)
        level_three()




def level_two():
    print("Turns out the phone is unlocked and you can browse through it.")
    print()
    time.sleep(3.5)
    print("You find a list of contacts.")
    print()
    print()
    time.sleep(2)
    print("---- CONTACTS ----")
 
    time.sleep(1)
    interaction_options = [
        "1. Dean", 
        "2. Razvan",
        "3. Sam",
        "4. DO NOT CALL!!",
    ]
    index = 0
    while index < len(interaction_options):
        print(interaction_options [index])
        index += 1
    time.sleep(2.5)
    response = input("Which contact would you like to call?: ")
    print()
    if response == "1" or response == "option 1" or response == "op1" or response == "Dean" or response == "dean":
        speaking = ("'This number is no longer in service. Goodbye.'")
        typewriter(speaking)
        print()
        time.sleep(2.5)
        print("You decide to try again.")
        print()
        print()
        level_two()
    elif response ==  "2" or response == "option 2" or response == "op2" or response == "Razvan" or response == "razvan":
        time.sleep(1.5)
        print("It's ringing...")
        print()
        time.sleep(1.5)
        print("...")
        print()

        speaking = (" \u001b[35m Hello? Jay, what are you doing calling me this early in the morning?\n\
        Don't you know I need my beauty sleep?")
        typewriter(speaking)
        print()
        time.sleep(2.5)
        speaking = ("Listen, I don't know what you need all those coffee beans for, but you've literally ran me dry! \n\
        I've none left!")
        typewriter(speaking)
        print()
        time.sleep(2.5)
        
        speaking = ("Ok look, I know someone who might hook you up. \n\
        He's actually your neighbour, Alex \n\
        Lives in the same building, and gets some nice roasts straight from Columbia. \n\
        Quality stuff. \n\
        I'll text you his number.\u001b[37m")
        typewriter(speaking)

        print("")
        time.sleep(5)
        print("You received a text message")
        time.sleep(2)
        print()
        print("Inside you read:")
        print("'Alex - 0755 458 3910'")
        print()
        time.sleep(4)
        level_three()
        
    elif response ==   "3" or response == "option 3" or response == "op3" or response == "Sam": 
        speaking = ("'This number is no longer in service. Goodbye.'")
        typewriter(speaking)
        print()
        time.sleep(2.5)
        print("You decide to try again.")
        print()
        print()
        level_two()
    elif response == "4" or response == "option 4" or response == "op4" or response == "DO NOT CALL" or response == "do not call":       
        print("""\ 
        ──────────────███████──███████
        ──────────████▓▓▓▓▓▓████░░░░░██
        ────────██▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░██
        ──────██▓▓▓▓▓▓████████████░░░░██
        ────██▓▓▓▓▓▓████████████████░██
        ────██▓▓████░░░░░░░░░░░░██████
        ──████████░░░░░░██░░██░░██▓▓▓▓██
        ──██░░████░░░░░░██░░██░░██▓▓▓▓██
        ██░░░░██████░░░░░░░░░░░░░░██▓▓██
        ██░░░░░░██░░░░██░░░░░░░░░░██▓▓██
        ──██░░░░░░░░░███████░░░░██████
        ────████░░░░░░░███████████▓▓██
        ──────██████░░░░░░░░░░██▓▓▓▓██
        ────██▓▓▓▓██████████████▓▓██
        ──██▓▓▓▓▓▓▓▓████░░░░░░████
        ████▓▓▓▓▓▓▓▓██░░░░░░░░░░██
        ████▓▓▓▓▓▓▓▓██░░░░░░░░░░██
        ██████▓▓▓▓▓▓▓▓██░░░░░░████████
        ──██████▓▓▓▓▓▓████████████████
        ────██████████████████████▓▓▓▓██
        ──██▓▓▓▓████████████████▓▓▓▓▓▓██
        ████▓▓██████████████████▓▓▓▓▓▓██
        ██▓▓▓▓██████████████████▓▓▓▓▓▓██
        ██▓▓▓▓██████████──────██▓▓▓▓████
        ██▓▓▓▓████──────────────██████
        ──████
                """)
        
        print()
        print("---- CONGRATULATIONS! ----")
        time.sleep(2)
        print("You found Mario!")
        print()
        time.sleep(5)
        print("Oh no! It's copyrighted material!")

        time.sleep(5)
        game_over()

    

    else:
        print("I'm afraid I didn't understand. Please try again.")
        level_two()

    

def level_one():

    pr_cyan ("Our target goes by the alias 'Jay'.")
    time.sleep(2.5)
    pr_cyan(" He's a notorious killer that murders his victims by drowning them in barrels of coffee. It's really quite gruesome to see.")
    time.sleep(4.5)
    pr_cyan("We just got a tip saying he was last seen wondering around St James' Park area. Probably stalking his next victim. We should go have a look.")
    time.sleep(6)
    print()
    print()
    print()
    print("You get in the patrol car with Dt. Watson and drive to the tip location.")
    time.sleep(4)
    print()
    print("Still driving...")
    time.sleep(4)
    print()
    print("You got stuck in traffic. Typical London.")
    time.sleep(4)
    print()
    print("Ok, great. We finally made it here! Let's hope he's still in the area.")
    print()
    print()
    time.sleep(1.5)
    print(" \u001b[36m Which way should we check out first? It's your call, {}. \u001b[37m [Left/Right] ".format(name))

    left_or_right = input ("Which way do you turn?: ")
    if left_or_right == "left" or left_or_right == "Left" or left_or_right == "l" or left_or_right == "L":
        left_path()
    elif left_or_right == "right" or left_or_right == "Right" or left_or_right == "r" or left_or_right == "R":
        right_path()
    else: 
        try_again_1()

def try_again():
    print ("I'm afraid I didn't quite understand. Could you try again? ")
    response = input("Shall we begin? [Yes/No] ")

    if response == "yes" or response == "Yes" or response == "y" or response == "Y":
        print("Brilliant, let's crack on then.")
        level_one()

    elif response == "no" or response == "No" or response == "n" or response == "N":
        print("Okay, suit yourself.")
    else:
        try_again()

def start_game():
    print("""\ 
    
     
     
                ╔▓███▓
          .,▄▄▄▄▄▒███▄▄╓▄
        ╔╢▒▓██████████████▓▓,
       @║▒▓█████████████████▒µ
       └▒▓██████████████████▓
         ╙▒████████████████▀"
           ╙▓███████████▀╙
             ██████████▀
             ╚▓███████▓
             ║████████▓,                  ╓▓▓▄
           .║▒█████████▓,                ▒████m
           ║▒███████████▓⌐               ║████-
           ▀▓████████████               j▓████▌
           (░▒▒██████████▓▓▓▓███▓▓▓███▓▓▓▓▓▓▓▓▒▒▒#░w
                        ╙▀█▓▒▒▓▓█▒▒█████████▒██▓▒▒▒└
                            └└└└╙╙╙╙╙╙╙▀▌▐███▌└└
                                        █▐███b
                                       ╓▀▐███⌐
                                     .#█▓████▒▄▄╖
                                     └▀█████████▀
                                        ██████▀
                                     .:(▓█████ .«▄
                                ┌╔#╢╢▒▓█████████▓▓▒▒▒M⌐
                            .╓N#╠▒╫▒▓▒▓▓▓█▓▓▓█▒▓▓▓▓▓▓▓▓▒#,
                           mNÑ║║╢▒▓▓▓▓▓▓▓▓▒▒▒█▒▒▓▓▓██▓▓▓▓▒M,
                        .∩┤║║▒▒▒▒▓▓█▓▓▓▓▓▒▒▒█▌▒▒▓▓████████▓▒▄
                    .▄ ┌K║╠║╬╫╫▒▓██▓▓▓█▓▓▒▓▓█▓▓▓█████████▓▓▓█░..:~.
                 (≈▄│╙╙╢▒▒▒▒▒▓▓▓▓▓██████▓▀▀██▀▀██████████████▓▒▄▄#▒M,
                ╔║▒▒▒▒╢▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▀▒▒█████▀▀▓▒▀▀▀▀▀██▓▓█▓▓▓▓▓▓▓▒║,
               │▐║▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒╠║▓▓▓▓▒█▒▓▒║║╫▓╫▒▒▒█▒▓▓▓▓▓▓▓▓▓▓▒║⌐
               ÑÑ╢▒▒▒▒▒▒▒▒▒▒▒▓▓█▒▒▒▀Ñ║║▀▒▓█▓▒▒▓Ñ╠╠▒█▓▒▓▓▓█▓▓▓▒▓▓▓▓▓▓▓▒▒
              #▒╠▒║╢▒▒▒▒▒▓▓████████▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓██████▓█▓█▓▓▓▓▓▓▓▒║▒▒▄
              ▓▓╢▒║║║▒▓██▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████▓████▓█▓▓██████▓▓▒▒█▌
              ▒▒╠▒▓▓██████████████▓▓▒▒▒▓▓▓▓▓██▓▓▓█████████████████████▓▒⌐
             (▒▒▓▓███████████████████▓▓▓█▓▓▓▓▓▓▓████████████████████████M
             (║█▓█████████████████████▓▓▒▒╫▓▓▓▓▓████████████████████████▌
             └║███████████████▓████████▓▒▒▒▒▒▓▒████▓█████████████████████
             (▒██████████▓▒██▒█▒██████▒▒▒▒╠▒▓▓▒▓██████████▓██▓▓██▓███████M
             ║▓▓█████▒██████▓█▓██████▓▒▓███████▓███████▒██████████▓████▓█▓
            .▒▒▓████▒╠║▀║▀▀▀▒▒▓█████▒▓▓████████████████▒▒▒▀▀▒▒▓▒██████▒▒▓█⌐
            ╠▒║▒▓▓▓▓╫▓▒#╠@▄▒████▓█▒▒▓██████████████▓█████▒▒▒╠║╢▓▒▒▒▓▓█▒▒▒▓▌
            ▒▒▒▒▒▓██▓▓█████▓▒▒▒▓▒▒▒▒████████▒███████▒▓▓██▓▓▓▓█████████▒▒▒▓█
           ╓▒╢╫▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓██▒▒▒▓██▓██████▒█▒█████▒▒▓▓▓▓▒▓▓▓▓█████████▓▓▌
          ┌║Ñ║▓▓▒▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▓████████████████▓█▓▒██▓▒▓▓▓▓▓▓▓▓▓▓████▓▒▓,
          ╠║▓▒▓▓▓██████████▓▓▓▓▓▓▒▓███▒║▒▒▒▀▒█▒█▓▓▓█▓█▓▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓████▓Γ
          ╙╠▒╢▓▓█▓▒▒▒▓▓▓▓▒▓▒▓▓▒▒▒▒▒██▓▒██▒▒▒╣▓██▓█▓█▒▒█▓▓▓▓███▓▓▓▓▒▒▒▒▒████▒
           ╙╠╫▒▒█▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒╠║║▒▒▒▒▀▀▀▀▓▀▒▒▀▒▒▒▒▒▓█▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓█▓▓╙
             └└╙▒█║███████▓▒▒▒▒▒▒▒█▒▒║╢▒╢▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒██████▒██╢∩
               (║█╡▓████████▓▒▒▒▒Ñ▒Ñ║║▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▒▒████████║█▌▒⌐
                │▒N▓████████▒║▒▓▓▒▒╠╠▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██▒▓████████▌║▒║▒
                ⌠∩║╢████████▒║▒▒▒▒▒▒▒▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▓▒▒▓▓╫███████▌▒▒▓▌
                (▒▓▒▓█▓▓████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓▓▓▓▓▓▓▓▓▓█▓▓▓▒███████▒█▌█Ñ
                 ║█▒▓█▓▓████▒▒▒▒▓▒▓▒▒▒▒▒▒▒▓▒▓▓▓▓▒▓▓█▓▓█▓▓▓██████████▓▀
                  ║▒█▒█▓▓▓▓▓▒▒╢▒▒▒▒▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▒▒▒██████████.
                  ⌠▒▒▒█▓▒▓▓▓▒▒╢▓▒▒▒▓▓▒▒▓▓▒▓▓▓▓▓▓▓▓▓▒▓█▒▓▒▓██████▓▓█▌::
                   ▒▒▒█▓▒▒▒▒▒║▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒████████▓█M∩∩∩:.
                   ║▒▒▒█▒▒▒▒▒║▒▒▒▓▓▓▓▓██▓▓▓▒▒▓▓▓▓▓▓▓▓▒▓█▒▓██▓▓▓█▌██╡N∩∩∩∩::.
                   │▒▒▒▒▒▒▒▒▒▒▒▒▓██▓▓▒██████████▓▓██▓▓▒▒▒▓█▒▓▓█▒▓█▌║╠╡┤∩∩∩∩∩;:
                    ║▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▒▒▒▒▒▒██▓▓▓▓▓█▒▒▓███▒▒║║╠┤│∩∩∩∩::
                    │║▒▒▒▒▒▒▒▒▒▒▒▓▒║▒▓▒▒▒▒▒▒▓▓▒▓▓▒▒▒▓██▒▒▒▒▓▓▓███▓▒▒▒║╠┤┤∩∩∩∩∩:
                     │║╢▒▒▒▒▒▒▒▒▒▒▓▒▓▓▓▓████████▓▓▓█▓█▒▓▒▓▓▓███▓▓▒▒▒║╠╠╠┤│∩∩∩∩::
                      └╚╢▒▒▒▒▒▒▓██████████████▓██▓██▓███▓▓▓▒▓▓▒▓▒╠╠╚╚╚│∩∩∩∩∩'''
                        └╙▒▓▓▓███▓███████████████████▓██▓█▒█▓▀Ñ│∩∩└└└└''''
                        .#▓▓▓█▓█████████████████████▓██████▀Ñ∩''''
                       #█▓█▓███▓████████████▓██▓▓█████▓▓▓█▓▓▄╖╓,,
                    .#▓▓▓▓██████▓██▓████████████████▓█████▓█▓▒╛²
                  ,▒▓▓▒███▓▓███████▓███████████████████▓██▒╜╙"
                ╒░▒▓▓████████▓████▓█████████████████████╜
              »ⁿK▒▓▓█▓████████████████████████████▒▀Ñ┘
            ./╔▒▒▓▓▒███████▓█████████████████▀╩"
             "" zÅ╙╜╙╩╜Ñ▀▀▀▀▀▀▀╙╙╙▀▀▀╙╙╙╙-'
     """)
    
    speaking = (
        "\u001b[36m Oh, a fresh face! How about that. Welcome to the precinct newbie!\n\
    My name is Detective Watson and I have been assigned to be your partner and mentor for this week.\n\
    You and I are going to be solving a case I've been working on for the past 3 months.\n\
    Perhaps a fresh perspective is just what I need to crack this. \u001b[37m ")
    typewriter(speaking)
    print()
    time.sleep(3)
# give each line an individual print
# in between each time.sleep(amount of seconds)
    global name
    name = input ("Now, first things first. Remind me what your name is again? ")
    time.sleep(1.5)
    speaking = (" \u001b[36m Ah, yes of course. Good to have you with us {}. Let's see if you can prove yourself. \u001b[37m".format(name))
    typewriter(speaking)
    time.sleep(1.5)
    print()
    response = input("Shall we begin? [Yes/No] ")

    if response == "yes" or response == "Yes" or response == "y" or response == "Y":
        print("\u001b[36m Brilliant, let's crack on then. \u001b[37m ")
        print()
        time.sleep(4)
        level_one()

    elif response == "no" or response == "No" or response == "n" or response == "N":
        print("\u001b[36m Okay, suit yourself. \u001b[37m")

    # exit()
    #game closes itself
# #make a loop for the "Are you sure option"
    else:
        # exit()
        try_again()
start_game()
word_list = [
    "coffee",
    "latte",
    "cappuccino",
    "americano",
    "cortado",
    "espresso",
    "decaf",
    "smoothie",
    "sugar",
    "milk",
    "spoon",
    "cup",
    "mug",
    "beans",
    "tea",
    "order",
    "crime",
    "detective",
    "murder",
    "mistery"
]
import sys,time,os
# def typewriter (speaking):
#     for char in speaking:
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         time.sleep(0.07)
import time
import random
def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    speaking = (" Let's play Hangman and see if you are ready to progress in your career! ")
    typewriter(speaking)
    print()
    time.sleep(1.5)
    speaking = (" Remember... If you succed, you will be promoted to sergeant. Good luck! ")
    typewriter(speaking)
    print()
    time.sleep(1.5)
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input(" Please guess a letter or word:  ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(" You already guessed the letter ", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                speaking = (" So you do want this promotion, good job " , guess , " is the word! ")
                typewriter(speaking)
                print()
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                speaking = (" Come on man, you already guessed the word. Just focuse! ", guess)
                typewriter(speaking)
                print()
            elif guess != word:
                print(guess, " is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            speaking = (" Not even close. Maybe you don't want this promotion...  ")
            typewriter(speaking)
            print()
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        speaking = (" Congratulation detective, you have been promoted to sergeant, keep up the good work! ")
        typewriter(speaking)
        print()
    else:
        speaking = (" You ran out of tries detective. The word was  "+ word )
        typewriter(speaking)
        print()
        speaking = (" Apparently you don't want that promotion! ")
        typewriter(speaking)
        print()
        time.sleep(1.5)  
        speaking = (" You can try again when you are ready. Untill then, go solve some more crime! ") 
        typewriter(speaking)
        print()
def display_hangman(tries):
    stages = [ 
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]
def main():
    word = get_word()
    play(word)
    while input("  Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)
if __name__ == "__main__":
    main()



