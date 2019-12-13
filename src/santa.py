

from personList import PersonList

import random
import smtplib


#generates a list of who will give to who
def generateSantaList():
    personsList = PersonList()

    persons = personsList.getPersons()
    persons_cpy = persons.copy()
    santa_list = []

    for person in persons:
        matched = False

        while(not matched):
            candidate = random.choice(persons_cpy)
            #check that you dont get yourself as match
            if candidate[0] != person[0]:
                persons_cpy.remove(candidate)
                santa_list.append((person, candidate))
                matched = True

    return santa_list

################################
###EDIT MESSAGE HERE
def contructSantaMessage(name):
    msg = """Subject: Viktigt meddelande fran Tomten

    HOHOHO GOD JUL
    Jag har atit for mycket grot och haller pa o ramnar!!!
    Du maste radda Julen, ge en julklapp till: """ + name + """ 
    da jag maste betala for mina synder

    Med juliga halsningar
    Tomten
    """
    return msg


def sendEmail(recipient, msg):
    ############################
    ##ENTER YOUR MAIL AND APP PASSWORD HERE
    ### you might need to set it up in your google account
    user_name = ""
    password = ""
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(user_name, password)
    server.sendmail(user_name, recipient, msg)


if __name__ == "__main__":
  
    santa_list = generateSantaList()



    for entry in santa_list:

        #entry is in form (("name", "email"),("match name", "match email"))
        sendEmail((entry[0])[1], contructSantaMessage((entry[1])[0]))
