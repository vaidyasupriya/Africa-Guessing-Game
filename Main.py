from tkinter import *
from tkinter import ttk


# Opens country file
countryFile = open('AfricanCountries','r')
OgList = countryFile.readlines()
countries = []
for country in OgList:
    countries.append((country[:-1]).upper())


# Some Colours
bgColour = '#121212'
btnStaticColour = '#293556'
btnActiveColour = '#2e4583'
fontColour = '#cadeed'





# Setting Up Main Window
window = Tk()
window.geometry('1200x800')
window.title("Africa Game")

# Window.resizable(False,False)
window.config(bg=bgColour)
icon = PhotoImage(file='AfricaImage.png')
window.iconphoto(True, icon)




# Setting Up Main Frame Inside Window
mainFrame = Frame(window)
mainFrame.pack(expand=1,fill=BOTH)




# Buttom Functions
def submit(event):
    global rowCounter
    global columnCounter

    # Fetches user input and capitalises it and clears the entry box
    countryName = (countryEntry.get()).upper()
    countryEntry.delete(0,END)

    # Checks if input is a valid country and isn't already guessed
    if (countryName in countries) and (countryName not in inputs):
        inputs.append(countryName)

        # Checks for the next available on the grid
        if columnCounter>2:
            columnCounter = 0
            rowCounter += 1

        # Makes a label with the name of the country and makes it green
        countryNameLabel = Label(tableFrame,
                                 text=countryName,
                                 font=('Comic Sans',15,'bold'),
                                 foreground='green',
                                 background=bgColour)
        
        # Adds that label to the next available space on the grid
        countryNameLabel.grid(column=columnCounter,
                              row=rowCounter,
                              sticky='nsew',
                              padx=10)

        columnCounter += 1

# A function the destroys the current page before displaying the next page
def deletePage():
    for frame in mainFrame.winfo_children():
        frame.destroy()

# Opens the next page
def openPage(page):
    deletePage()
    page()




# Making Page 1
def menuPage():

    global inputs
    global rowCounter
    global columnCounter

    rowCounter = 0
    columnCounter = 0
    inputs = []
    # Setting Up Page 1
    page1 = Frame(mainFrame)
    page1.pack(expand=1,fill=BOTH)
    page1.config(bg=bgColour)

    pg1Title = Label(page1, 
                  text='AFRICA QUIZ',
                  font=('Comic Sans',50,'bold'),
                  bg=bgColour,
                  fg=fontColour).pack(pady=80)


    # Making A grid for all of the Buttons
    pg1btnGrid = Frame(page1,bg=bgColour,pady=100)

    pg1btnGrid.columnconfigure(0, weight=1)
    pg1btnGrid.columnconfigure(1, weight=1)
    pg1btnGrid.columnconfigure(2, weight=1)


    # Making Buttons and assigning them their properties and functions
    playBtn = Button(pg1btnGrid,
                      text='PLAY',
                      font=('Comic Sans',20),
                      width=20,
                      fg=fontColour,
                      bg=btnStaticColour,
                      activebackground=btnActiveColour,
                      relief=FLAT,
                      command=lambda: openPage(gamePage))

    scoresBtn = Button(pg1btnGrid,
                       text='SCORE',
                       font=('Comic Sans',20),
                       width=20,
                       fg=fontColour,
                       bg=btnStaticColour,
                       activebackground=btnActiveColour,
                       relief=FLAT,
                       command=lambda: openPage(scorePage))

    quitBtn = Button(pg1btnGrid,
                     text='QUIT',
                     font=('Comic Sans', 20),
                     width=20,
                     fg=fontColour,
                     bg=btnStaticColour,
                     activebackground=btnActiveColour,
                     relief=FLAT,
                     command=window.destroy)

    # Adding the buttons to the grid
    playBtn.grid(row=0,column=0,sticky='nsew',pady=5)
    scoresBtn.grid(row=1,column=0,sticky='nsew',pady=5)
    quitBtn.grid(row=2,column=0,sticky='nsew',pady=5)


    pg1btnGrid.pack()




# Makes Page 2 (game page)
def gamePage():

    global countryEntry
    global tableFrame

    page2 = Frame(mainFrame,bg=bgColour)
    page2.pack(expand=1,fill=BOTH)

    pg2Title = Label(page2, 
                  text='Enter African Country',
                  font=('Comic Sans',30,'bold'),
                  bg=bgColour,
                  fg=fontColour).pack(pady=20)


    # Adding input box for country names
    countryEntry = Entry(page2,
                         font=('Comic Sans',20))
    countryEntry.pack()

    
    #Making a grid for all of the buttons
    pg2btnGrid = Frame(page2,bg=bgColour)

    pg2btnGrid.columnconfigure(0, weight=1)
    pg2btnGrid.columnconfigure(1, weight=1)


    resetBtn = Button(pg2btnGrid,
                     text='FINISH',
                     font=('Comic Sans', 20),
                     width=10,
                     fg=fontColour,
                     bg=btnStaticColour,
                     activebackground=btnActiveColour,
                     relief=FLAT,
                     command=lambda: openPage(resultsPage))
    
    resetBtn.grid(row=0,column=0,sticky='nsew',padx=5,pady=20)

    pg2btnGrid.pack()

    tableFrame = Frame(page2,bg=bgColour)
    tableFrame.columnconfigure(0,weight=1)
    tableFrame.columnconfigure(1,weight=1)
    tableFrame.columnconfigure(2,weight=1)
    tableFrame.pack(expand=1,fill=BOTH)

# Making page 4 (score page)
def scorePage():
    page3 = Frame(mainFrame,bg=bgColour)
    page3.pack(expand=1,fill=BOTH)

    scoreFile = open('scores','r')

    pg3Title = Label(page3, 
                  text='Previous Scores',
                  font=('Comic Sans',30,'bold'),
                  bg=bgColour,
                  fg=fontColour).pack(pady=80)
    
    #opens the score file and displays all of the scores
    scores = scoreFile.readlines()
    for score in scores:
        scoreLabel = Label(page3,text=(score[:-1])
                           ,foreground=fontColour,
                           font=('Comic Sans',15,'bold'),
                           bg=bgColour)
        scoreLabel.pack(pady=10)
    

    menuBtn = Button(page3,
                      text='BACK TO MENU',
                      font=('Comic Sans',20),
                      width=20,
                      fg=fontColour,
                      bg=btnStaticColour,
                      activebackground=btnActiveColour,
                      relief=FLAT,
                      command=lambda: openPage(menuPage))
    
    menuBtn.pack(pady=80)


# Makes page 4 (results page)
def resultsPage():

    page4 =  Frame(mainFrame,bg=bgColour)
    page4.pack(expand=1,fill=BOTH)

    scoreFrame = Frame(page4,bg=bgColour)
    scoreFrame.columnconfigure(0,weight=2)
    scoreFrame.columnconfigure(1,weight=1)

    scoreTextLabel = Label(scoreFrame,text='SCORE: ',
                           font=('Comic Sans',30,'bold'),
                           background=bgColour,
                           foreground=fontColour)
    
    scoreNumberLabel = Label(scoreFrame,text=(f'{str(len(inputs))}/54'),
                             font=('Comic Sans',30,'bold'),
                             background=bgColour,
                             foreground=fontColour)
    
    scoreFile = open('scores','a')
    scoreFile.writelines(f'{str(len(inputs))}/54\n')
    scoreFile.close
    
    scoreTextLabel.grid(row=0,column=0)
    scoreNumberLabel.grid(row=0,column=1)

    scoreFrame.pack(pady=20)

    countryListFrame = Frame(page4,bg=bgColour)
    countryListFrame.columnconfigure(0,weight=1)
    countryListFrame.columnconfigure(1,weight=1)
    countryListFrame.columnconfigure(2,weight=1)

    scoreColumnCounter = 0
    scoreRowCounter = 0

    for country in countries:
        if country in inputs:
            countryLabel = Label(countryListFrame,
                                 text=country,
                                 foreground='green',
                                 font=('Comic Sans',15,'bold'),
                                 bg=bgColour)
        else:
            countryLabel = Label(countryListFrame,
                                 text=country,
                                 foreground='red',
                                 font=('Comic Sans',15,'bold'),
                                 bg=bgColour)
        
        if scoreColumnCounter>2:
            scoreColumnCounter = 0
            scoreRowCounter += 1
        
        countryLabel.grid(row=scoreRowCounter,
                          column=scoreColumnCounter,
                          sticky='nsew',
                          padx=10)

        scoreColumnCounter+=1

    countryListFrame.pack(fill=BOTH,expand=1)

    menuBtn = Button(page4,
                      text='BACK TO MENU',
                      font=('Comic Sans',20),
                      width=20,
                      fg=fontColour,
                      bg=btnStaticColour,
                      activebackground=btnActiveColour,
                      relief=FLAT,
                      command=lambda: openPage(menuPage))
    
    menuBtn.pack(pady=20)


window.bind('<Return>',submit)

menuPage()
window.mainloop()