from ast import And
from faulthandler import cancel_dump_traceback_later
from operator import truediv
from random import shuffle
from tkinter.tix import COLUMN, ROW
import names
from tkinter import *
from PIL import Image, ImageTk
import os

def resize_card(card):
    img = Image.open(card)
    sizedImg = img.resize((75,109))
    global cardImg 
    cardImg = ImageTk.PhotoImage(sizedImg)
    
    return cardImg 

class Game:
    def __init__(self):
        name1 = input("p1 name ")
        self.deck = Deck()
        self.p1 = Player(name1)
        
        #other players
        self.p2 = Player(names.get_first_name())
        self.p3 = Player(names.get_first_name())
        self.p4 = Player(names.get_first_name())

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def drawCards(self):
        
        self.deck.shuffle()
        self.p1.cards = []
        self.p2.cards = []
        self.p3.cards = []
        self.p4.cards = []        
               
        for x in range (13):
            self.p1.cards.append(self.deck.rm_card())
            self.p2.cards.append(self.deck.rm_card())
            self.p3.cards.append(self.deck.rm_card())
            self.p4.cards.append(self.deck.rm_card())

        self.p1.cards.sort()
        self.p2.cards.sort()
        self.p3.cards.sort()
        self.p4.cards.sort()

        self.p1.calcPoints()
        print("Raw points: " + str(self.p1.rawPoints))                           #"♤","♥","♧","♦"
        print("♤: " + str(self.p1.spades))
        print("♥: " + str(self.p1.hearts))
        print("♧: " + str(self.p1.clubs))
        print("♦: " + str(self.p1.diamonds))

    def playGame(self):      
        self.gui()

    def gui(self):
        self.root = Tk()
        self.root.title("PyBridge")
        self.root.geometry("1500x800")
        self.root.configure(background="green")

        self.my_frame = Frame(self.root, bg="green")
        self.my_frame.pack(pady=20)

        self.p1_frame = LabelFrame(self.my_frame, text=self.p1.name, bd=0)
        self.p1_frame.grid(row=2,column=1,padx=20,pady=20)                          #
                                                                                    #    0,1
        self.p2_frame = LabelFrame(self.my_frame, text=self.p2.name, bd=0)          # 1,0   1,2
        self.p2_frame.grid(row=1,column=0,padx=20,pady=20)                          #    2,1
                                                                                    #
        self.p3_frame = LabelFrame(self.my_frame, text=self.p3.name, bd=0)
        self.p3_frame.grid(row=0,column=1,padx=20,pady=20)

        self.p4_frame = LabelFrame(self.my_frame, text=self.p4.name, bd=0)
        self.p4_frame.grid(row=1,column=2,padx=20,pady=20)


        #13 cards for player 1

        self.p1_label1 = Label(self.p1_frame, text='')
        self.p1_label1.grid(row=0,column=0)

        self.p1_label2 = Label(self.p1_frame, text='')
        self.p1_label2.grid(row=0,column=1)

        self.p1_label3 = Label(self.p1_frame, text='')
        self.p1_label3.grid(row=0,column=2)

        self.p1_label4 = Label(self.p1_frame, text='')
        self.p1_label4.grid(row=0,column=3)

        self.p1_label5 = Label(self.p1_frame, text='')
        self.p1_label5.grid(row=0,column=4)

        self.p1_label6 = Label(self.p1_frame, text='')
        self.p1_label6.grid(row=0,column=5)

        self.p1_label7 = Label(self.p1_frame, text='')
        self.p1_label7.grid(row=0,column=6)

        self.p1_label8 = Label(self.p1_frame, text='')
        self.p1_label8.grid(row=0,column=7)

        self.p1_label9 = Label(self.p1_frame, text='')
        self.p1_label9.grid(row=0,column=8)

        self.p1_label10 = Label(self.p1_frame, text='')
        self.p1_label10.grid(row=0,column=9)

        self.p1_label11 = Label(self.p1_frame, text='')
        self.p1_label11.grid(row=0,column=10)

        self.p1_label12 = Label(self.p1_frame, text='')
        self.p1_label12.grid(row=0,column=11)

        self.p1_label13 = Label(self.p1_frame, text='')
        self.p1_label13.grid(row=0,column=12)

        #Other Players

        self.p2_label = Label(self.p2_frame, text='')
        self.p2_label.pack(pady=20, padx=20)

        self.p3_label = Label(self.p3_frame, text='')
        self.p3_label.pack(pady=20, padx=20)

        self.p4_label = Label(self.p4_frame, text='')
        self.p4_label.pack(pady=20, padx=20)


        self.buttonFrame = Frame(self.root, bg="green")
        self.buttonFrame.pack(pady=20)

        #Create Buttons
        dealCardsButton = Button(self.buttonFrame,text="Deal", font=("Helvetica", 14),command=self.guiDealCards)
        dealCardsButton.grid(row=0, column=0)

        passButton = Button(self.buttonFrame, text="Pass", font=("Helvetica", 14))
        passButton.grid(row=0, column=1, padx=10)

        bidButton = Button(self.buttonFrame, text="Bid", font=("Helvetica", 14))
        bidButton.grid(row=0, column=2)

        self.guiBid()

        self.root.mainloop()

    def guiDealCards(self):

        self.drawCards()
        # print(os.listdir())
        global cardImage1, cardImage2, cardImage3, cardImage4, cardImage5,cardImage6,cardImage7,cardImage8,cardImage9,cardImage10,cardImage11,cardImage12,cardImage13
        for x in range(len(self.p1.cards)):
            match x:
                case 0:
                    cardImage1 = resize_card(r"C:/Users/congeza/Desktop/Code\bridge/Cards/{}.png".format(self.p1.cards[x]))
                    self.p1_label1.config(image=cardImage1)
                case 1:
                    cardImage2 = resize_card(r"C:/Users/congeza/Desktop/Code\bridge/Cards/{}.png".format(self.p1.cards[x]))
                    self.p1_label2.config(image=cardImage2)
                case 2:
                    cardImage3 = resize_card(r"C:/Users/congeza/Desktop/Code\bridge/Cards/{}.png".format(self.p1.cards[x]))
                    self.p1_label3.config(image=cardImage3)
                case 3:
                    cardImage4 = resize_card(r"C:/Users/congeza/Desktop/Code\bridge/Cards/{}.png".format(self.p1.cards[x]))
                    self.p1_label4.config(image=cardImage4)
                case 4:
                    cardImage5 = resize_card(r"C:/Users/congeza/Desktop/Code\bridge/Cards/{}.png".format(self.p1.cards[x]))
                    self.p1_label5.config(image=cardImage5)
                case 5:
                    cardImage6 = resize_card(r"C:/Users/congeza/Desktop/Code\bridge/Cards/{}.png".format(self.p1.cards[x]))
                    self.p1_label6.config(image=cardImage6)
                case 6:
                    cardImage7 = resize_card(r"C:/Users/congeza/Desktop/Code\bridge/Cards/{}.png".format(self.p1.cards[x]))
                    self.p1_label7.config(image=cardImage7)
                case 7:
                    cardImage8 = resize_card(r"C:/Users/congeza/Desktop/Code\bridge/Cards/{}.png".format(self.p1.cards[x]))
                    self.p1_label8.config(image=cardImage8)
                case 8:
                    cardImage9 = resize_card(r"C:/Users/congeza/Desktop/Code\bridge/Cards/{}.png".format(self.p1.cards[x]))
                    self.p1_label9.config(image=cardImage9)
                case 9:
                    cardImage10 = resize_card(r"C:/Users/congeza/Desktop/Code\bridge/Cards/{}.png".format(self.p1.cards[x]))
                    self.p1_label10.config(image=cardImage10)
                case 10:
                    cardImage11 = resize_card(r"C:/Users/congeza/Desktop/Code\bridge/Cards/{}.png".format(self.p1.cards[x]))
                    self.p1_label11.config(image=cardImage11)
                case 11:
                    cardImage12 = resize_card(r"C:/Users/congeza/Desktop/Code\bridge/Cards/{}.png".format(self.p1.cards[x]))
                    self.p1_label12.config(image=cardImage12)
                case 12:
                    cardImage13 = resize_card(r"C:/Users/congeza/Desktop/Code\bridge/Cards/{}.png".format(self.p1.cards[x]))
                    self.p1_label13.config(image=cardImage13)
        

        

#image=f"C:\Users\congeza\Desktop\Code\bridge\Cards{self.p1.cards[x]}.png"

        #self.p1_label.config(text=self.p1.cards)
        self.p2_label.config(text="13")
        self.p3_label.config(text="13")
        self.p4_label.config(text="13")

    def guiBid(self):
        self.bid = Bids()             
        self.bidFrame = Frame(self.root, bg="green")                                                                                                  #"♤","♥","♧","♦"
        self.bidFrame.pack(pady=20)
        nT1 = Button(self.bidFrame, text= "1 NT", font=("Helvetica", 12),command=lambda: self.bid.newBid(1,"NT", "p1"))
        nT1.grid(row=1, column=0)
        spade1 = Button(self.bidFrame, text= "1 ♠", font=("Helvetica", 12),command=lambda: self.bid.newBid(1,"♤", "p1"))
        spade1.grid(row=1, column=1)
        heart1 = Button(self.bidFrame, text= "1 ♥", font=("Helvetica", 12),command=lambda: self.bid.newBid(1,"♥", "p1"))
        heart1.grid(row=1, column=2)
        diamond1 = Button(self.bidFrame, text= "1 ♦", font=("Helvetica", 12),command=lambda: self.bid.newBid(1,"♦", "p1"))
        diamond1.grid(row=1, column=3)
        club1 = Button(self.bidFrame, text= "1 ♣", font=("Helvetica", 12),command=lambda: self.bid.newBid(1,"♧", "p1"))
        club1.grid(row=1, column=4)

        nT2 = Button(self.bidFrame, text= "2 NT", font=("Helvetica", 12),command=lambda: self.bid.newBid(2,"NT", "p1"))
        nT2.grid(row=2, column=0)
        spade2 = Button(self.bidFrame, text= "2 ♠", font=("Helvetica", 12),command=lambda: self.bid.newBid(2,"♤", "p1"))
        spade2.grid(row=2, column=1)
        heart2 = Button(self.bidFrame, text= "2 ♥", font=("Helvetica", 12),command=lambda: self.bid.newBid(2,"♥", "p1"))
        heart2.grid(row=2, column=2)
        diamond2 = Button(self.bidFrame, text= "2 ♦", font=("Helvetica", 12),command=lambda: self.bid.newBid(2,"♦", "p1"))
        diamond2.grid(row=2, column=3)
        club2 = Button(self.bidFrame, text= "2 ♣", font=("Helvetica", 12),command=lambda: self.bid.newBid(2,"♧", "p1"))
        club2.grid(row=2, column=4)

        nT3 = Button(self.bidFrame, text= "3 NT", font=("Helvetica", 12),command=lambda: self.bid.newBid(3,"NT", "p1"))
        nT3.grid(row=3, column=0)
        spade3 = Button(self.bidFrame, text= "3 ♠", font=("Helvetica", 12),command=lambda: self.bid.newBid(3,"♤", "p1"))
        spade3.grid(row=3, column=1)
        heart3 = Button(self.bidFrame, text= "3 ♥", font=("Helvetica", 12),command=lambda: self.bid.newBid(3,"♥", "p1"))
        heart3.grid(row=3, column=2)
        diamond3 = Button(self.bidFrame, text= "3 ♦", font=("Helvetica", 12),command=lambda: self.bid.newBid(3,"♦", "p1"))
        diamond3.grid(row=3, column=3)
        club3 = Button(self.bidFrame, text= "3 ♣", font=("Helvetica", 12),command=lambda: self.bid.newBid(3,"♧", "p1"))
        club3.grid(row=3, column=4)

        nT4 = Button(self.bidFrame, text= "4 NT", font=("Helvetica", 12),command=lambda: self.bid.newBid(4,"NT", "p1"))
        nT4.grid(row=4, column=0)
        spade4 = Button(self.bidFrame, text= "4 ♠", font=("Helvetica", 12),command=lambda: self.bid.newBid(4,"♤", "p1"))
        spade4.grid(row=4, column=1)
        heart4 = Button(self.bidFrame, text= "4 ♥", font=("Helvetica", 12),command=lambda: self.bid.newBid(4,"♥", "p1"))
        heart4.grid(row=4, column=2)
        diamond4 = Button(self.bidFrame, text= "4 ♦", font=("Helvetica", 12),command=lambda: self.bid.newBid(4,"♦", "p1"))
        diamond4.grid(row=4, column=3)
        club4 = Button(self.bidFrame, text= "4 ♣", font=("Helvetica", 12),command=lambda: self.bid.newBid(4,"♧", "p1"))
        club4.grid(row=4, column=4)

        nT5 = Button(self.bidFrame, text= "5 NT", font=("Helvetica", 12),command=lambda: self.bid.newBid(5,"NT", "p1"))
        nT5.grid(row=5, column=0)
        spade5 = Button(self.bidFrame, text= "5 ♠", font=("Helvetica", 12),command=lambda: self.bid.newBid(5,"♤", "p1"))
        spade5.grid(row=5, column=1)
        heart5 = Button(self.bidFrame, text= "5 ♥", font=("Helvetica", 12),command=lambda: self.bid.newBid(5,"♥", "p1"))
        heart5.grid(row=5, column=2)
        diamond5 = Button(self.bidFrame, text= "5 ♦", font=("Helvetica", 12),command=lambda: self.bid.newBid(5,"♦", "p1"))
        diamond5.grid(row=5, column=3)
        club5 = Button(self.bidFrame, text= "5 ♣", font=("Helvetica", 12),command=lambda: self.bid.newBid(5,"♧", "p1"))
        club5.grid(row=5, column=4)

        nT6 = Button(self.bidFrame, text= "6 NT", font=("Helvetica", 12),command=lambda: self.bid.newBid(6,"NT", "p1"))
        nT6.grid(row=6, column=0)
        spade6 = Button(self.bidFrame, text= "6 ♠", font=("Helvetica", 12),command=lambda: self.bid.newBid(6,"♤", "p1"))
        spade6.grid(row=6, column=1)
        heart6 = Button(self.bidFrame, text= "6 ♥", font=("Helvetica", 12),command=lambda: self.bid.newBid(6,"♥", "p1"))
        heart6.grid(row=6, column=2)
        diamond6 = Button(self.bidFrame, text= "6 ♦", font=("Helvetica", 12),command=lambda: self.bid.newBid(6,"♦", "p1"))
        diamond6.grid(row=6, column=3)
        club6 = Button(self.bidFrame, text= "6 ♣", font=("Helvetica", 12),command=lambda: self.bid.newBid(6,"♧", "p1"))
        club6.grid(row=6, column=4)

        nT7 = Button(self.bidFrame, text= "7 NT", font=("Helvetica", 12),command=lambda: self.bid.newBid(7,"NT", "p1"))
        nT7.grid(row=7, column=0)
        spade7 = Button(self.bidFrame, text= "7 ♠", font=("Helvetica", 12),command=lambda: self.bid.newBid(7,"♤", "p1"))
        spade7.grid(row=7, column=1)
        heart7 = Button(self.bidFrame, text= "7 ♥", font=("Helvetica", 12),command=lambda: self.bid.newBid(7,"♥", "p1"))
        heart7.grid(row=7, column=2)
        diamond7 = Button(self.bidFrame, text= "7 ♦", font=("Helvetica", 12),command=lambda: self.bid.newBid(7,"♦", "p1"))
        diamond7.grid(row=7, column=3)
        club7 = Button(self.bidFrame, text= "7 ♣", font=("Helvetica", 12),command=lambda: self.bid.newBid(7,"♧", "p1"))
        club7.grid(row=7, column=4)


class Bids:
    suits = ["None","♧","♦","♥","♤","NT"]

    def __init__(self):
        self.currentSuit = "None"
        self.currentNumber = 0
        self.player = "None"
        self.yourTeamHasBid = True             #True if team 1 (p1,p3), false if team 2 (p2,p4)
    
        self.t1Spade = "None"
        self.t1Heart = "None"
        self.t1Diamond = "None"
        self.t1Club = "None"
        self.t1NT = "None"

        self.t2Spade = "None"
        self.t2Heart = "None"
        self.t2Diamond = "None"
        self.t2Club = "None"
        self.t2NT = "None"

    def newBid(self, number, suit, bidder):
        print(number)
        print(suit)
        if (number > self.currentNumber):
            self.changeBid(number,suit,bidder)
        elif(number == self.currentNumber):
            if(self.suits.index(suit) > self.suits.index(self.currentSuit)):
                self.changeBid(number,suit,bidder)
        else:
            print("ERROR ILLEGAL BID")
    
    def changeBid(self,number,suit,bidder):
        self.currentNumber = number
        self.currentSuit = suit
        if(bidder == "p1" or bidder == "p3"):   #Team 1             #"♤","♥","♧","♦"
            if suit == "♤":
                if self.t1Spade == "None":
                    self.t1Spade = bidder
            elif suit == "♥":
                if self.t1Heart == "None":
                    self.t1Heart = bidder
            elif suit == "♦":
                if self.t1Diamond == "None":
                    self.t1Diamond = bidder
            elif suit == "♧":
                if self.t1Club == "None":
                    self.t1Club = bidder
            elif suit == "NT":
                if self.t1NT == "None":
                    self.t1NT = bidder

        elif(bidder == "p2" or bidder == "p4"):     #Team 2
            if suit == "♤":
                if self.t2Spade == "None":
                    self.t2Spade = bidder
            elif suit == "♥":
                if self.t2Heart == "None":
                    self.t2Heart = bidder
            elif suit == "♦":
                if self.t2Diamond == "None":
                    self.t2Diamond = bidder
            elif suit == "♧":
                if self.t2Club == "None":
                    self.t2Club = bidder
            elif suit == "NT":
                if self.t2NT == "None":
                    self.t2NT = bidder

class Player:
    def __init__(self, name):
       self.wins = 0
       self.cards = []
       self.name = name
       self.suitedPoints = -1
       self.rawPoints = -1
       self.spades = -1
       self.hearts = -1
       self.diamonds = -1
       self.clubs = -1

    def calcPoints(self):
        self.calcRawPoints()
        # self.calcSuits()
        self.calcSuitedPoints()
                
    def calcSuits(self):
        self.spades = 0
        self.hearts = 0
        self.diamonds = 0
        self.clubs = 0

        for x in self.cards:

            # print(x.suit)
            if x.suit == 0:                 #"♤","♥","♧","♦"
                self.spades += 1
            elif x.suit == 1:
                self.hearts += 1
            elif x.suit == 2:
                self.clubs += 1
            elif x.suit == 3:
                self.diamonds += 1
    

    def calcRawPoints(self):
        raw = 0
        for x in self.cards:
            # print(x.value)
            if x.value == 11: #Jack
                raw += 1
            if x.value == 12: #Queen
                raw += 2
            if x.value == 13: #King
                raw += 3
            if x.value == 14: #Ace
                raw += 4
        self.rawPoints = raw

    def calcSuitedPoints(self):
        self.calcSuits()
        self.spadePoints = 0
        self.heartPoints = 0
        self.clubPoints = 0
        self.diamondPoints = 0

        voidInSpades = 0
        voidInHearts = 0
        voidInClubs = 0
        voidInDiamonds = 0

               #VOIDS
        if self.spades == 0:     #VOID
            voidInSpades = 1
            self.heartPoints += 3
            self.clubPoints += 3
            self.diamondPoints += 3
        if self.hearts == 0:     #VOID
            voidInHearts = 1
            self.spadePoints += 3
            self.clubPoints += 3
            self.diamondPoints += 3
        if self.clubs == 0:     #VOID
            voidInClubs = 1
            self.spadePoints += 3
            self.heartPoints += 3
            self.diamondPoints += 3
        if self.diamonds == 0:     #VOID
            voidInDiamonds = 1
            self.spadePoints += 3
            self.clubPoints += 3
            self.heartPoints += 3

        numVoids = voidInSpades + voidInClubs + voidInDiamonds + voidInHearts
        if numVoids == 3:
            #GRAND SLAM
            pass
        
        if numVoids == 2:
            if self.clubPoints == 3:
                self.clubPoints = 0
            if self.spadePoints == 3:
                self.spadePoints = 0
            if self.heartPoints == 3:
                self.heartPoints = 0
            if self.diamondPoints == 3:
                self.diamondPoints = 0
        

        if self.spades == 1:        #Singleton
            singleInSpades = 1
            self.heartPoints += 2
            self.clubPoints += 2
            self.diamondPoints += 2
            if self.hasCard(13,0):          #Special Cases
                self.rawPoints -= 3
            if self.hasCard(12,0):
                self.rawPoints -= 2
            if self.hasCard(11,0):
                self.rawPoints -= 1
        if self.hearts == 1:        #Singleton
            singleInHearts = 1
            self.spadePoints += 2
            self.clubPoints += 2
            self.diamondPoints += 2
            if self.hasCard(13,1):          #Special Cases
                self.rawPoints -= 3
            if self.hasCard(12,1):
                self.rawPoints -= 2
            if self.hasCard(11,1):
                self.rawPoints -= 1
        if self.clubs == 1:         #Singleton
            singleInClubs = 1
            self.spadePoints += 2
            self.heartPoints += 2
            self.diamondPoints += 2
            if self.hasCard(13,2):          #Special Cases
                self.rawPoints -= 3
            if self.hasCard(12,2):
                self.rawPoints -= 2
            if self.hasCard(11,2):
                self.rawPoints -= 1
        if self.diamonds == 1:      #Singleton
            singleInDiamonds = 1
            self.spadePoints += 2
            self.clubPoints += 2
            self.heartPoints += 2
            if self.hasCard(13,3):          #Special Cases
                self.rawPoints -= 3
            if self.hasCard(12,3):
                self.rawPoints -= 2
            if self.hasCard(11,3):
                self.rawPoints -= 1

        if self.spades == 2:        #Doubleton
            doubleInSpades = 1
            self.heartPoints += 1
            self.clubPoints += 1
            self.diamondPoints += 1
            if self.hasCard(12,0):
                self.rawPoints -= 2
            if self.hasCard(11,0):
                self.rawPoints -= 1
        if self.hearts == 2:        #Doubleton
            doubleInHearts = 1
            self.spadePoints += 1
            self.clubPoints += 1
            self.diamondPoints += 1
            if self.hasCard(12,1):
                self.rawPoints -= 2
            if self.hasCard(11,1):
                self.rawPoints -= 1
        if self.clubs == 2:         #Doubleton
            doubleInClubs = 1
            self.spadePoints += 1
            self.heartPoints += 1
            self.diamondPoints += 1
            if self.hasCard(12,2):
                self.rawPoints -= 2
            if self.hasCard(11,2):
                self.rawPoints -= 1
        if self.diamonds == 2:      #Doubleton
            doubleInDiamonds = 1
            self.spadePoints += 1
            self.clubPoints += 1
            self.heartPoints += 1
            if self.hasCard(12,3):
                self.rawPoints -= 2
            if self.hasCard(11,3):
                self.rawPoints -= 1

        if self.spades >= 6:
            self.spadePoints +=1
        if self.hearts >= 6:
            self.heartPoints +=1
        if self.clubs >= 6:
            self.clubPoints +=1
        if self.diamonds >= 6:
            self.diamondPoints +=1

        if self.spades >= 7:
            self.spadePoints +=2
        if self.hearts >= 7:
            self.heartPoints +=2
        if self.clubs >= 7:
            self.clubPoints +=2
        if self.diamonds >= 7:
            self.diamondPoints +=2

        self.spadePoints += self.rawPoints
        self.heartPoints += self.rawPoints
        self.clubPoints += self.rawPoints
        self.diamondPoints += self.rawPoints

        print("Spade points:" + str(self.spadePoints))
        print("Heart points:" + str(self.heartPoints))
        print("Diamond points:" + str(self.diamondPoints))
        print("Club points:" + str(self.clubPoints))

    def hasCard(self, rank, suit):
        # print(self.cards)
        try:
            index = self.cards.index(Card(rank,suit))
            return True
        except:
            return False

class Deck:
    def __init__(self):
        self.cards = []
        self.shuffle()
        

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

    def shuffle(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards\
                    .append(Card(i,
                                 j))
        shuffle(self.cards)

class Card:
    # suits = ["spades",
    #          "hearts",
    #          "diamonds",
    #          "clubs"]
    
    suits = ["♤","♥","♧","♦"]

    values = [None, None,"2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.suit < c2.suit:
            return True
        if self.suit == c2.suit:
            if self.value < c2.value:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.suit > c2.suit:
            return True
        if self.suit == c2.suit:
            if self.value > c2.value:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] +\
            self.suits[self.suit]
        return v

    def __eq__(self, other):
        return (self.suit == other.suit and self.value == other.value)


game = Game()
game.playGame()



# Rules of bidding:
#
# 22+ points
# 20-21 points
# 12+ points
#   5 card major
# 15 + points and Balanced
#       4 card diamond
# 6+ suit and <10 points
#
#
#
#
#
#