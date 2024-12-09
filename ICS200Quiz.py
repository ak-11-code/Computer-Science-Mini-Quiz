#June 2022
#ICS200 Quiz
#Purpose - A true or false question quiz which allows the user to repeat and/or quit the program additionally, tells the user their score

#Initialize Variables/Constants:
score=0
repeat_quiz="Yes"
continue_quiz=""
answer1=""
answer2=""
answer3=""
answer4=""
answer5=""
answer6=""
answer7=""
answer8=""
answer9=""

#Introduce program to user:
print("Welcome to the true/false quiz!")
print()
print("This quiz will give you a question and you will answer either true or false depending on what you think the answer is.")
print()
print("You will be told what the correct answer is and your score will be stored")
print()
print("You may quit the program after each question if you like or continue on until you have answered all the questions")
print()
print("There are a total of 9 questions")
print()
print("Good Luck!")
print()
print("__________________________________________________________________________________________________________________________\n")
print()

#Input/Process/Output:
#   Ask the user the first question,
    #   if they are correct, add 1 point to (score) and explain the answer;
    #   if incorrect, do not add any points and explain answer
#   After each question, ask user if they would like to continue playing the quiz,
    #   if yes, ask the next question,
    #   if no, do not ask user next question and end the program

while (repeat_quiz=="Yes"):
    score=0
#First Question:
    print("Question 1: All motherboards have the same layout?\n")
    answer1=input("True or False?  ")
    if answer1.capitalize()=="False":
        print("You are correct!\n")
        score+=1
        print("There are many factors that affect the layout of a motherboard. Different models will have different types of motherboards. Size is one of the biggest factors. A phone may have a motherboard that is small and compiled with everything in one area. Smartphone motherboards are sometimes called “logic boards” or “SOC (system on chip)”. This can be compared to the motherboard of a large PC. The motherboard would be very different because it would be more accessible to users so they may input additional items such as graphics cards and sound cards. This question may be true in the sense that the reader interprets the layout of a motherboard as a specified type. Different motherboards have specified types of motherboards with different layouts including ATX motherboard, LPX motherboard, BTX motherboard, Pico BTX motherboard, Mini ITX motherboard, and many more.\n")
        print()

    else:
        print("You are incorrect!\n")
        print("There are many factors that affect the layout of a motherboard. Different models will have different types of motherboards. Size is one of the biggest factors. A phone may have a motherboard that is small and compiled with everything in one area. Smartphone motherboards are sometimes called “logic boards” or “SOC (system on chip)”. This can be compared to the motherboard of a large PC. The motherboard would be very different because it would be more accessible to users so they may input additional items such as graphics cards and sound cards. This question may be true in the sense that the reader interprets the layout of a motherboard as a specified type. Different motherboards have specified types of motherboards with different layouts including ATX motherboard, LPX motherboard, BTX motherboard, Pico BTX motherboard, Mini ITX motherboard, and many more.\n")

#Does user wish to contniue quiz?
    continue_quiz=input("Do you wish to continue the quiz? (Yes or No)  ")

    #Second Question:
    if continue_quiz.capitalize()=="Yes":
        print("Question 2: The software of a computer affect its hardware?\n")
        answer2=input("True or False?  ")

        if answer2.capitalize()=="True":
            print("You are correct!\n")
            score+=1
            print("The software works with the hardware in the sense that it “tells the hardware what to do”. The software is stored on the hardware and if files are downloaded media is not stored properly, may slow down the computer. The question may be false if it is perceived as the software affecting the hardware in a negative way. Viruses affect the software only of the computer, NOT the hardware.\n")
            print()

        else:
            print("You are incorrect!\n")
            print("The software works with the hardware in the sense that it “tells the hardware what to do”. The software is stored on the hardware and if files are downloaded media is not stored properly, may slow down the computer. The question may be false if it is perceived as the software affecting the hardware in a negative way. Viruses affect the software only of the computer, NOT the hardware.\n")

    else:
        print("Thank you for using this program!")

#Does user wish to contniue quiz?
    continue_quiz=input("Do you wish to continue the quiz? (Yes or No)  ")

    #Third Question:
    if continue_quiz.capitalize()=="Yes":
        print("Question 3: Network hubs increase the range of where the wifi can be connected to?\n")
        answer3=input("True or False?  ")

        if answer3.capitalize()=="False":
            print("You are correct!\n")
            score+=1
            print("Hubs are small rectangular devices used to connect many network enabled devices. They do not increase the size of the wifi connectivity but increase the strength of the internet connection. Ethernet hubs connect to a hub, then to a device's NIC using an RJ-45 port. Ethernet hubs were very common and inexpensive but have been replaced by broadband routers. The hubs can be connected to other hubs called daisy chaining to increase the number of devices connected to a hub network. There are 3 types of hubs: passive, active, and intelligent hubs. Passive does not amplify electrical signals of incoming packets. Active performs amplification (similar to a repeater). Intelligent does what an active hub can do but is stackable atop one another and has remote.Active hubs also have management capabilities using Simple Network Management Protocols (SNMPs) and virtual local area networks (VLANs). This answer could be true if the reader mistook the network hubs to be wifi extenders. Wifi extenders increase the range of which the wifi can be connected to in an area.\n")
            print()

        else:
            print("You are incorrect!\n")
            print("Hubs are small rectangular devices used to connect many network enabled devices. They do not increase the size of the wifi connectivity but increase the strength of the internet connection. Ethernet hubs connect to a hub, then to a device's NIC using an RJ-45 port. Ethernet hubs were very common and inexpensive but have been replaced by broadband routers. The hubs can be connected to other hubs called daisy chaining to increase the number of devices connected to a hub network. There are 3 types of hubs: passive, active, and intelligent hubs. Passive does not amplify electrical signals of incoming packets. Active performs amplification (similar to a repeater). Intelligent does what an active hub can do but is stackable atop one another and has remote.Active hubs also have management capabilities using Simple Network Management Protocols (SNMPs) and virtual local area networks (VLANs). This answer could be true if the reader mistook the network hubs to be wifi extenders. Wifi extenders increase the range of which the wifi can be connected to in an area.\n")
    else:
        print("Thank you for using this program!")

#Does user wish to contniue quiz?
    continue_quiz=input("Do you wish to continue the quiz? (Yes or No)  ")

    #Fourth Question:
    if continue_quiz.capitalize()=="Yes":
        print("Question 4: All operating systems have the same functions?\n")
        answer4=input("True or False?  ")

        if answer4.capitalize()=="False":
            print("You are correct!\n")
            score+=1
            print("Each OS has its own set of unique features that allow the computer to run the way it should. Different operating systems will be preferred by different people depending on what their needs and wants are for an OS. MacOS has a variety of function such as; connects with the Cloud to store items, can sync with other Apple devices: Receive notifications; can copy and paste from one device to another; can use iPad as second screen, apps update themselves, has virtual assistant: Siri, built-in security and apps, can use Swift UI to code other apps, works with windows and can boot windows on a Mac. Windows has unique features such as; the desktop is where you can run apps, background, icons, start menu and taskbar, has virtual assistant: Cortana, has a device manager that displays installed hardware, has an option to create disk space using disk cleanup, event viewer shows the events on your computer,stores files on file explorer or OneDrive, and has many built in apps. Linux also carries special functions such as; very similar to Unix operating system, Kernel is responsible for all major activities run by the OS, the system library implements most of the system’s functionalities, the system utility performs specialized individual tasks, can work on different hardware platforms, multi-user: multiple users can access system resources, at the same time, multiprogramming: multiple applications can run at same time, hierarchical file system: standard file structure where files are arranged, shell: special interpreter program used to execute commands of the OS, provides security to passwords and and encrypts Data. Through these few functions, it is possible to say that there are many similarities between the systems; however, they also have their own unique sets of capabilities which is what make them popular.\n")
            print()

        else:
            print("You are incorrect!\n")
            print("Each OS has its own set of unique features that allow the computer to run the way it should. Different operating systems will be preferred by different people depending on what their needs and wants are for an OS. MacOS has a variety of function such as; connects with the Cloud to store items, can sync with other Apple devices: Receive notifications; can copy and paste from one device to another; can use iPad as second screen, apps update themselves, has virtual assistant: Siri, built-in security and apps, can use Swift UI to code other apps, works with windows and can boot windows on a Mac. Windows has unique features such as; the desktop is where you can run apps, background, icons, start menu and taskbar, has virtual assistant: Cortana, has a device manager that displays installed hardware, has an option to create disk space using disk cleanup, event viewer shows the events on your computer,stores files on file explorer or OneDrive, and has many built in apps. Linux also carries special functions such as; very similar to Unix operating system, Kernel is responsible for all major activities run by the OS, the system library implements most of the system’s functionalities, the system utility performs specialized individual tasks, can work on different hardware platforms, multi-user: multiple users can access system resources, at the same time, multiprogramming: multiple applications can run at same time, hierarchical file system: standard file structure where files are arranged, shell: special interpreter program used to execute commands of the OS, provides security to passwords and and encrypts Data. Through these few functions, it is possible to say that there are many similarities between the systems; however, they also have their own unique sets of capabilities which is what make them popular.\n")

    else:
        print("Thank you for using this program!")

#Does user wish to contniue quiz?
    continue_quiz=input("Do you wish to continue the quiz? (Yes or No)  ")

    #Fifth Question:
    if continue_quiz.capitalize()=="Yes":
        print("Question 5: Updating a computer create newer security issues?\n")
        answer5=input("True or False?  ")

        if answer5.capitalize()=="False":
            print("You are correct!\n")
            score+=1
            print("Updating a computer does not create newer security issues. It in fact, does the opposite. Updating computers regularly removes previous bugs in the programs and keeps apps up to date. This reduces the likeness of malware entering the system and allows the system to run better. It is important to update a computer often because the update is meant to make the computer run better. This answer could not be true unless the reader thought of when the software updates. It may not resolve all issues and create a newer glitch but regular updating avoids the possibilities of dealing with these small additional bugs.\n")
            print()

        else:
            print("You are incorrect!\n")
            print("Updating a computer does not create newer security issues. It in fact, does the opposite. Updating computers regularly removes previous bugs in the programs and keeps apps up to date. This reduces the likeness of malware entering the system and allows the system to run better. It is important to update a computer often because the update is meant to make the computer run better. This answer could not be true unless the reader thought of when the software updates. It may not resolve all issues and create a newer glitch but regular updating avoids the possibilities of dealing with these small additional bugs.\n")

    else:
        print("Thank you for using this program!")

#Does user wish to contniue quiz?
    continue_quiz=input("Do you wish to continue the quiz? (Yes or No)  ")

    #Sixth Question:
    if continue_quiz.capitalize()=="Yes":
        print("Question 6: Computers have ways to make them more accessible for people who may have certain disabilities?\n")
        answer6=input("True or False?  ")

        if answer6.capitalize()=="True":
            print("You are correct!\n")
            score+=1
            print("There are many useful tools for people with disabilities to use a computer more comfortably. Ergonomic and adaptive technologies are ways for people with disabilities to use. Some of these tools consist of: Text-to-speech accessibility.  Important for people who have any disabilities and is helpful for people in general to hear a piece of text instead of reading it. Speech-to-text allows the user to command functions by speaking instead of typing or moving a mouse. Adaptive mouse is a device that has a trackball that moves instead of the mouse itself; eliminates the need to move the mice even when dragging; helpful for people who can’t use their hands freely and need assistance to move a traditional mouse. Font control is a way to control the font size on the computer and it allows people who have vision problems to clearly see the text on screen. Color contrast allows people with vision problems when it comes to color (color blindness) to create a theme to change certain colors so that they may see the color more clearly; color contrast can also change the color of the cursor to help see it more clearly. Ergonomic keyboards reduce the strain on the user in contrast to a traditional keyboard; can reduce carpal tunnel syndrome and prevent wrist injuries. Virtual keyboard is an accessibility utility that displays a keyboard on the computer screen and allows people with mobility issues to type in information by using a pointing device or joystick. Sticky keys cause modifier keys to remain active, even after they are pressed and released; makes it easier to use keyboard shortcuts and  helps alleviate some stress on your fingers by not having to press and hold keys to use keyboard shortcuts; helps Windows users with physical disabilities reduce the sort of movement associated with repetitive strain injury. Image magnifier allows visually impaired people to zoom in on an image to see more clearly. There is no way for this answer to be false.\n")
            print()

        else:
            print("You are incorrect!\n")
            print("There are many useful tools for people with disabilities to use a computer more comfortably. Ergonomic and adaptive technologies are ways for people with disabilities to use. Some of these tools consist of: Text-to-speech accessibility.  Important for people who have any disabilities and is helpful for people in general to hear a piece of text instead of reading it. Speech-to-text allows the user to command functions by speaking instead of typing or moving a mouse. Adaptive mouse is a device that has a trackball that moves instead of the mouse itself; eliminates the need to move the mice even when dragging; helpful for people who can’t use their hands freely and need assistance to move a traditional mouse. Font control is a way to control the font size on the computer and it allows people who have vision problems to clearly see the text on screen. Color contrast allows people with vision problems when it comes to color (color blindness) to create a theme to change certain colors so that they may see the color more clearly; color contrast can also change the color of the cursor to help see it more clearly. Ergonomic keyboards reduce the strain on the user in contrast to a traditional keyboard; can reduce carpal tunnel syndrome and prevent wrist injuries. Virtual keyboard is an accessibility utility that displays a keyboard on the computer screen and allows people with mobility issues to type in information by using a pointing device or joystick. Sticky keys cause modifier keys to remain active, even after they are pressed and released; makes it easier to use keyboard shortcuts and  helps alleviate some stress on your fingers by not having to press and hold keys to use keyboard shortcuts; helps Windows users with physical disabilities reduce the sort of movement associated with repetitive strain injury. Image magnifier allows visually impaired people to zoom in on an image to see more clearly. There is no way for this answer to be false.\n")

    else:
        print("Thank you for using this program!")

#Does user wish to contniue quiz?
    continue_quiz=input("Do you wish to continue the quiz? (Yes or No)  ")

    #Seventh Question:
    if continue_quiz.capitalize()=="Yes":
        print("Question 7: Computer waste have negative effects on the planet?\n")
        answer7=input("True or False?  ")

        if answer7.capitalize()=="True":
            print("You are correct!\n")
            score+=1
            print("Computers contain toxic chemicals which can be damaging for people, animals, and the environment. The chemicals can seep into the air causing pollutants and even get into soil and water or contamination of crops that may be planted nearby or in the area in the future. When the soil is contaminated by heavy metals, crops become vulnerable to absorbing these toxins, which can cause many illnesses and doesn’t allow the farmland to be as productive as possible. Animals and wildlife relying on nature for survival will end up consuming affected plants, causing internal health problems. When the heavy metals reach groundwater, they eventually make their way into ponds, streams, rivers and lakes and acidification and toxification are created in the water making it unsafe for animals, plants and communities. Acidification can kill marine and freshwater organisms, disturb biodiversity and harm ecosystems.\n")
            print()

        else:
            print("You are incorrect!\n")
            print("Computers contain toxic chemicals which can be damaging for people, animals, and the environment. The chemicals can seep into the air causing pollutants and even get into soil and water or contamination of crops that may be planted nearby or in the area in the future. When the soil is contaminated by heavy metals, crops become vulnerable to absorbing these toxins, which can cause many illnesses and doesn’t allow the farmland to be as productive as possible. Animals and wildlife relying on nature for survival will end up consuming affected plants, causing internal health problems. When the heavy metals reach groundwater, they eventually make their way into ponds, streams, rivers and lakes and acidification and toxification are created in the water making it unsafe for animals, plants and communities. Acidification can kill marine and freshwater organisms, disturb biodiversity and harm ecosystems.\n")

    else:
        print("Thank you for using this program!")

#Does user wish to contniue quiz?
    continue_quiz=input("Do you wish to continue the quiz? (Yes or No)  ")

    #Eighth Question:
    if continue_quiz.capitalize()=="Yes":
        print("Question 8: Computers are only used in workplaces that require a high degree of educational levels (require a bachelor's, masters, doctorate, etc…)?\n")
        answer8=input("True or False?  ")

        if answer8.capitalize()=="False":
            print("You are correct!\n")
            score+=1
            print("Computers are used in most workplaces for a wide range of reasons. Someone should not feel that they need to have a high level of education to be given access to technology. Technology is meant for the use of everyone equally. The type of career will depend on how the technology is being used.\n")
            print()

        else:
            print("You are incorrect!\n")
            print("Computers are used in most workplaces for a wide range of reasons. Someone should not feel that they need to have a high level of education to be given access to technology. Technology is meant for the use of everyone equally. The type of career will depend on how the technology is being used.\n")

    else:
        print("Thank you for using this program!")

#Does user wish to contniue quiz?
    continue_quiz=input("Do you wish to continue the quiz? (Yes or No)  ")

    #Ninth Question
    if continue_quiz.capitalize()=="Yes":
        print("Question 9: There are laws protecting people against cyberbullying?\n")
        answer9=input("True or False?  ")

        if answer9.capitalize()=="True":
            print("You are correct!\n")
            score+=1
            print("Cyberbullying is a serious crime in Canada. It can have lasting effects on people and unfortunately, occurs oftenly because people think that they are anonymous, protected by a computer screen. They can face serious legal consequences depending on the conduct of the cyberbully. Those involved could be charged with the following offenses under Canada’s Criminal Code: Sharing intimate images without consent, Criminal harassment, Uttering threats, Intimidation, Mischief in relation to data, Unauthorized use of computer, Identity theft, Extortion, False messages, indecent or harassing telephone calls, Counselling suicide, Incitement of hatred, Defamatory libel, Public incitement of hatred, Offence against the person and reputation. Cyberbullying should be taken seriously and those who take part in it should understand that they are not as “anonymous” as they think.\n")
            print()

        else:
            print("You are incorrect!\n")
            print("Cyberbullying is a serious crime in Canada. It can have lasting effects on people and unfortunately, occurs oftenly because people think that they are anonymous, protected by a computer screen. They can face serious legal consequences depending on the conduct of the cyberbully. Those involved could be charged with the following offenses under Canada’s Criminal Code: Sharing intimate images without consent, Criminal harassment, Uttering threats, Intimidation, Mischief in relation to data, Unauthorized use of computer, Identity theft, Extortion, False messages, indecent or harassing telephone calls, Counselling suicide, Incitement of hatred, Defamatory libel, Public incitement of hatred, Offence against the person and reputation. Cyberbullying should be taken seriously and those who take part in it should understand that they are not as “anonymous” as they think.\n")

    else:
        print("Thank you for using this program!")

#Output: Calculate points scored and display their answer
    print("____________________________________________\n")
    print("You got "+str(score)+" out of 9!")
    print("____________________________________________\n")

#After the quiz, ask user if they would like to repeat the quiz
#   if yes, restart the quiz
#   if no, end the quiz/program
    repeat_quiz=input("\nWould you like to try again? Yes or No:  ").capitalize()
    print("")

if (repeat_quiz=="No"):
    print("Thank you for playing this quiz today!")

            
