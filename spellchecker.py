import datetime
import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        txtIn.lower()
        if language == "italian":
            with open("Italian.txt", "r") as f:
                wordList = f.read().splitlines()  #ho creato una lista del dizionario splittato
            txtIn.strip("\n")
            txtIn = replaceChars(txtIn)
            frase = txtIn.split(" ")
            sbagliate = []

            tic = datetime.datetime.now()
            for i in frase:
                i = i.strip("\n")
                if wordList.__contains__(i):
                    pass
                else:
                    sbagliate.append(i)
            print("Nella tua frase ci sono "+ str(len(sbagliate)) +" parole sbagliate")
            for i in sbagliate:
                print(i)

            toc = datetime.datetime.now()
            print("il tuo programma ci ha impiegato" + str((toc-tic)))

            listaSbagliate = []
            tic = datetime.datetime.now()
            for i in frase:
                trovato = 0
                i = i.strip("\n")
                for parola in wordList:
                    if i == parola:
                        trovato =1
                if trovato ==0:
                    listaSbagliate.append(i)

            print("Nella tua frase ci sono "+str(len(listaSbagliate))+" parole sbagliate")
            for i in listaSbagliate:
                print(i)
            toc = datetime.datetime.now()
            print("Il tuo programma ci ha impiegato "+str(toc-tic))


            listaSb = []
            tic = datetime.datetime.now()
            meta = int((len(wordList)/2))
            for i in frase:
                i = i.strip("\n")
                trovato = 0
                if i == wordList[meta]:
                    trovato = 1
                elif i > wordList[meta]:
                    for x in range(meta, len(wordList)):
                        if i == wordList[x]:
                            trovato = 1
                else:
                    for x in range(0, meta):
                        if i == wordList[x]:
                            trovato = 1

                if trovato == 0:
                    listaSb.append(i)

            print("Nella tua frase ci sono " + str(len(listaSb)) + " parole sbagliate")
            for i in listaSb:
                print(i)
            toc = datetime.datetime.now()
            print("Il tuo programma ci ha impiegato " + str(toc - tic))

        elif language == "english":
            with open("English.txt", "r") as f:
                wordList = f.read().splitlines()  #ho creato una lista del dizionario splittato
            txtIn.strip("\n")
            txtIn = replaceChars(txtIn)
            frase = txtIn.split(" ")
            sbagliate = []

            tic = datetime.datetime.now()
            for i in frase:
                i = i.strip("\n")
                if wordList.__contains__(i):
                    pass
                else:
                    sbagliate.append(i)
            print("Nella tua frase ci sono "+ str(len(sbagliate)) +" parole sbagliate")
            for i in sbagliate:
                print(i)

            toc = datetime.datetime.now()
            print("il tuo programma ci ha impiegato" + str((toc-tic)))

            listaSbagliate = []
            tic = datetime.datetime.now()
            trovato = 0
            for i in frase:
                for parola in wordList:
                    if i == parola:
                        trovato = 1
            if trovato == 0:
                listaSbagliate.append(i)
            print("Nella tua frase ci sono " + str(len(listaSbagliate)) + " parole sbagliate")
            toc = datetime.datetime.now()
            print("Il tuo programma ci ha impiegato " + str(toc - tic))
            listaSbagliate= []
            tic = datetime.datetime.now()
            meta = int((len(wordList) / 2))
            for i in txtIn:
                trovato = 0
                if i == wordList[meta]:
                    trovato = 1
                elif i > wordList[meta]:
                    for x in range(meta, len(wordList)):
                        if i == wordList[x]:
                            torvato = 1
                else:
                    for x in range(0, meta):
                        trovato = 1

                if trovato == 0:
                    listaSbagliate.append(i)

            print("Nella tua frase ci sono " + str(len(listaSbagliate)) + " parole sbagliate")
            toc = datetime.datetime.now()
            print("Il tuo programma ci ha impiegato " + str(toc - tic))

            listaSb = []
            tic = datetime.datetime.now()
            meta = int((len(wordList) / 2))
            for i in frase:
                i = i.strip("\n")
                trovato = 0
                if i == wordList[meta]:
                    trovato = 1
                elif i > wordList[meta]:
                    for x in range(meta, len(wordList)):
                        if i == wordList[x]:
                            trovato = 1
                else:
                    for x in range(0, meta):
                        if i == wordList[x]:
                            trovato = 1

                if trovato == 0:
                    listaSb.append(i)

            print("Nella tua frase ci sono " + str(len(listaSb)) + " parole sbagliate")
            for i in listaSb:
                print(i)
            toc = datetime.datetime.now()
            print("Il tuo programma ci ha impiegato " + str(toc - tic))

        else:
            with open("Spanish.txt", "r") as f:
                wordList = f.read().splitlines()  # ho creato una lista del dizionario splittato
            txtIn.strip("\n")
            txtIn = replaceChars(txtIn)
            frase = txtIn.split(" ")
            sbagliate = []

            tic = datetime.datetime.now()
            for i in frase:
                i = i.strip("\n")
                if wordList.__contains__(i):
                    pass
                else:
                    sbagliate.append(i)
            print("Nella tua frase ci sono " + str(len(sbagliate)) + " parole sbagliate")
            for i in sbagliate:
                print(i)

            toc = datetime.datetime.now()
            print("il tuo programma ci ha impiegato" + str((toc - tic)))

            listaSbagliate = []
            tic = datetime.datetime.now()
            trovato = 0
            for i in frase:
                for parola in wordList:
                    if i == parola:
                        trovato = 1
            if trovato == 0:
                listaSbagliate.append(i)
            print("Nella tua frase ci sono " + str(len(listaSbagliate)) + " parole sbagliate")
            toc = datetime.datetime.now()
            print("Il tuo programma ci ha impiegato " + str(toc - tic))
            listaSbagliate = []
            tic = datetime.datetime.now()
            meta = int((len(wordList) / 2))
            for i in txtIn:
                trovato = 0
                if i == wordList[meta]:
                    trovato = 1
                elif i > wordList[meta]:
                    for x in range(meta, len(wordList)):
                        if i == wordList[x]:
                            torvato = 1
                else:
                    for x in range(0, meta):
                        trovato = 1

                if trovato == 0:
                    listaSbagliate.append(i)

            print("Nella tua frase ci sono " + str(len(listaSbagliate)) + " parole sbagliate")
            toc = datetime.datetime.now()
            print("Il tuo programma ci ha impiegato " + str(toc - tic))

            listaSb = []
            tic = datetime.datetime.now()
            meta = int((len(wordList) / 2))
            for i in frase:
                i = i.strip("\n")
                trovato = 0
                if i == wordList[meta]:
                    trovato = 1
                elif i > wordList[meta]:
                    for x in range(meta, len(wordList)):
                        if i == wordList[x]:
                            trovato = 1
                else:
                    for x in range(0, meta):
                        if i == wordList[x]:
                            trovato = 1

                if trovato == 0:
                    listaSb.append(i)

            print("Nella tua frase ci sono " + str(len(listaSb)) + " parole sbagliate")
            for i in listaSb:
                print(i)
            toc = datetime.datetime.now()
            print("Il tuo programma ci ha impiegato " + str(toc - tic))

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars="\\'*_{}[]()><#-.!$%^;,=?"
    for c in chars:
        text = text.replace(c, "")
    return text

