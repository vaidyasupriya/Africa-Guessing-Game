from tkinter import *
from tkinter import ttk


# Opens country file
countryFile = open('AfricanCountries','r')
OgList = countryFile.readlines()
countries = []
for country in OgList:
    countries.append((country[:-1]).upper())




# Some Colours
bgColour = '#262A33'
btnStaticColour = '#054D82'
btnActiveColour = '#098EF0'
fontColour = '#FAFFF8'
correctFontColour = '#43FFAF'
wrongFontColour = '#FF4D50'




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


# User Name entry function
def nameSubmit(event):
    userName = nameEntry.get()
    score = len(inputs)
    if score < 10:
        record = f'0{score},{userName},{gameMode}\n'
    else:
        record = f'{score},{userName},{gameMode}\n'
    scoreFile = open('scores','a')
    scoreFile.writelines(record)
    scoreFile.close
    openPage(menuPage)
    


# Country Name entry function
def submit(event): 
    global rowCounter
    global columnCounter
    global totalLives
    global livesLeft

    # Fetches user input and capitalises it and clears the entry box
    countryName = (countryEntry.get()).upper()
    countryEntry.delete(0,END)

    # Checks if input is a valid country and isn't already guessed
    if (countryName in countries) and (countryName not in inputs):
        inputs.append(countryName)

        liveScore.config(text=(f'{len(inputs)}/54'))

        # Checks for the next available on the grid
        if columnCounter>2:
            columnCounter = 0
            rowCounter += 1

        # Makes a label with the name of the country and makes it green
        countryNameLabel = Label(tableFrame,
                                 text=countryName,
                                 font=('Comic Sans',15,'bold'),
                                 foreground=correctFontColour,
                                 background=bgColour)
        
        # Adds that label to the next available space on the grid
        countryNameLabel.grid(column=columnCounter,
                              row=rowCounter,
                              sticky='nsew',
                              padx=10)

        columnCounter += 1
        if len(inputs)==54:
            openPage(resultsPage)
    elif (lives == True) and (countryName not in inputs):
        totalLives -= 1
        livesLeft.config(text=(f'Lives: {totalLives}'))

        if columnCounter>2:
            columnCounter = 0
            rowCounter += 1
        
        countryNameLabel = Label(tableFrame,
                                 text=countryName,
                                 font=('Comic Sans',15,'bold'),
                                 foreground=wrongFontColour,
                                 background=bgColour)
        
        # Adds that label to the next available space on the grid
        countryNameLabel.grid(column=columnCounter,
                              row=rowCounter,
                              sticky='nsew',
                              padx=10)

        columnCounter += 1
        if totalLives == 0:
            openPage(resultsPage)


def difficultyEasy():
    global lives
    global gameMode
    gameMode = "EASY"
    lives = False
    
    openPage(gamePage)

def difficultyMedium():
    global totalLives
    global lives
    global gameMode
    gameMode = "MEDIUM"

    lives = True
    totalLives = 5
    openPage(gamePage)

def difficultyHard():
    global totalLives
    global lives
    global gameMode
    gameMode = "HARD"

    lives = True
    totalLives = 1
    openPage(gamePage)


# A function the destroys the current page before displaying the next page
def deletePage():
    for frame in mainFrame.winfo_children():
        frame.destroy()



# Opens the next page
def openPage(page):
    deletePage()
    page()





# Making Page 1 (menu page)
def menuPage():

    global inputs
    global rowCounter
    global columnCounter

    rowCounter = 0
    columnCounter = 0
    inputs = []

    # Setting Up Page 1
    page1 = Frame(mainFrame,bg=bgColour)
    page1.pack(expand=1,fill=BOTH)

    page1Title = Label(page1, 
                  text='AFRICA QUIZ',
                  font=('Comic Sans',50,'bold'),
                  bg=bgColour,
                  fg=fontColour)
    page1Title.pack(pady=40,expand=1)


    # Making A grid for all of the Buttons
    page1btnGrid = Frame(page1,bg=bgColour,pady=100)

    page1btnGrid.columnconfigure(0, weight=1)
    page1btnGrid.columnconfigure(1, weight=1)
    page1btnGrid.columnconfigure(2, weight=1)


    # Making Buttons and assigning them their properties and functions
    playBtn = Button(page1btnGrid,
                      text='PLAY',
                      font=('Comic Sans',20),
                      width=20,
                      fg=fontColour,
                      bg=btnStaticColour,
                      activebackground=btnActiveColour,
                      relief=FLAT,
                      command=lambda: openPage(dificultyPage))

    scoresBtn = Button(page1btnGrid,
                       text='SCORE',
                       font=('Comic Sans',20),
                       width=20,
                       fg=fontColour,
                       bg=btnStaticColour,
                       activebackground=btnActiveColour,
                       relief=FLAT,
                       command=lambda: openPage(leaderBoardPage))

    quitBtn = Button(page1btnGrid,
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


    page1btnGrid.pack(expand=1)

# Makes Page 2 (dificulty page)
def dificultyPage():

    # Setting Up page 2
    page2 = Frame(mainFrame,bg=bgColour)
    page2.pack(expand=1,fill=BOTH)

    page2Title = Label(page2, 
                  text='CHOOSE DIFICULTY',
                  font=('Comic Sans',40,'bold'),
                  bg=bgColour,
                  fg=fontColour)
    
    page2Title.pack(pady=30)

    # Making A grid for all of the Buttons
    page2btnGrid = Frame(page2,bg=bgColour,pady=100)

    page2btnGrid.rowconfigure(0, weight=1)
    page2btnGrid.rowconfigure(1, weight=1)
    page2btnGrid.rowconfigure(2, weight=1)

    easy = Button(page2btnGrid,
                  text="EASY",
                  font=('Comic Sans',20),
                  width=20,
                  fg=fontColour,
                  bg='#00BB00',
                  command=difficultyEasy)
    
    medium = Button(page2btnGrid,
                  text="MEDIUM",
                  font=('Comic Sans',20),
                  width=20,
                  fg=fontColour,
                  bg='#BBB000',
                  command=difficultyMedium)
    
    hard = Button(page2btnGrid,
                  text="HARD",
                  font=('Comic Sans',20),
                  width=20,
                  fg=fontColour,
                  bg='#BB0000',
                  command=difficultyHard)

    easy.grid(row=0,column=0,sticky='nsew',pady=5)
    medium.grid(row=1,column=0,sticky='nsew',pady=5)
    hard.grid(row=2,column=0,sticky='nsew',pady=5)

    page2btnGrid.pack(expand=1)

# Makes Page 3 (game page)
def gamePage():

    # Attaching key binds to functions
    window.unbind('<Return>')
    window.bind('<Return>',submit)

    global liveScore
    global livesLeft
    global countryEntry
    global tableFrame

    # Setting up page 3
    page3 = Frame(mainFrame,bg=bgColour)
    page3.pack(expand=1,fill=BOTH)



    updatingFrame = Frame(page3,bg=bgColour)
    updatingFrame.pack(fill=X)

    if lives == True:
        updatingFrame.columnconfigure(0,weight=1)
        updatingFrame.columnconfigure(1,weight=1)

        livesLeft = Label(updatingFrame,
                      text=(f'Lives: {totalLives}'),
                      font=('Comic Sans',20,'bold'),
                      bg=bgColour,
                      fg=fontColour)
        
        liveScore = Label(updatingFrame,
                      text=(f'{len(inputs)}/54'),
                      font=('Comic Sans',20,'bold'),
                      bg=bgColour,
                      fg=fontColour)
        
        livesLeft.grid(row=0,column=0,sticky='nsew',pady=5)
        liveScore.grid(row=0,column=1,sticky='nsew',pady=5)
    else:
        liveScore = Label(updatingFrame,
                          text=(f'{len(inputs)}/54'),
                          font=('Comic Sans',20,'bold'),
                          bg=bgColour,
                          fg=fontColour)
        liveScore.pack(pady=5)

    page3Title = Label(page3,
                       text='Enter African Country',
                       font=('Comic Sans',20,'bold'),
                       bg=bgColour,
                       fg=fontColour)
    page3Title.pack(pady=5)

    countryEntry = Entry(page3,
                         font=('Comic Sans',20))
    countryEntry.pack(pady=10)

    resetBtn = Button(page3,
                     text='FINISH',
                     font=('Comic Sans', 20),
                     width=10,
                     fg=fontColour,
                     bg=btnStaticColour,
                     activebackground=btnActiveColour,
                     relief=FLAT,
                     command=lambda: openPage(resultsPage))
    
    resetBtn.pack(pady=15)

    # Makes Frame for Country names
    tableFrame = Frame(page3,bg=bgColour)
    tableFrame.columnconfigure(0,weight=1)
    tableFrame.columnconfigure(1,weight=1)
    tableFrame.columnconfigure(2,weight=1)
    tableFrame.pack(expand=1,fill=BOTH)


# Makes page 4 (results page)
def resultsPage():

    # Setting up page 4
    page4 =  Frame(mainFrame,bg=bgColour)
    page4.pack(expand=1,fill=BOTH)

    
    scoreNumberLabel = Label(page4,text=(f'{str(len(inputs))}/54'),
                             font=('Comic Sans',30,'bold'),
                             background=bgColour,
                             foreground=fontColour)
    scoreNumberLabel.pack(pady=40,expand=1)
    

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
                                 foreground=correctFontColour,
                                 font=('Comic Sans',15,'bold'),
                                 bg=bgColour)
        else:
            countryLabel = Label(countryListFrame,
                                 text=country,
                                 foreground=wrongFontColour,
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

    page4BtnGrid = Frame(page4,bg=bgColour)
    page4BtnGrid.columnconfigure(0,weight=1)
    page4BtnGrid.columnconfigure(1,weight=1)
    page4BtnGrid.pack(expand=1,fill=X)
    menuBtn = Button(page4BtnGrid,
                      text='MENU',
                      font=('Comic Sans',20),
                      width=20,
                      fg=fontColour,
                      bg=btnStaticColour,
                      activebackground=btnActiveColour,
                      relief=FLAT,
                      command=lambda: openPage(menuPage))
    
    menuBtn.grid(row=0,column=0,pady=20)

    saveBtn = Button(page4BtnGrid,
                      text='SAVE',
                      font=('Comic Sans',20),
                      width=20,
                      fg=fontColour,
                      bg=btnStaticColour,
                      activebackground=btnActiveColour,
                      relief=FLAT,
                      command=lambda: openPage(saveResultsPage))
    
    saveBtn.grid(row=0,column=1,pady=20)



# Making page 5 (Save Results Page)

def saveResultsPage():

    # Attaching key binds to functions
    window.unbind('<Return>')
    window.bind('<Return>',nameSubmit)

    global nameEntry

    # Setting up page 4
    page5 = Frame(mainFrame,bg=bgColour)
    page5.pack(expand=1,fill=BOTH)

    page5Title = Label(page5,
                       text='Enter Your Name',
                       font=('Comic Sans',30,'bold'),
                       fg=fontColour,
                       bg=bgColour)
    page5Title.pack(pady=20,expand=1)


    nameEntry = Entry(page5,
                      font=('Comic Sans',20))
    nameEntry.pack(pady=20,expand=1)



    


# Making page 6 (leaderboard Page)
def leaderBoardPage():

    # Setting up page 5
    page6 = Frame(mainFrame,bg=bgColour)
    page6.pack(expand=1,fill=BOTH)

    page6Title = Label(page6,
                       text='LEADER BOARD',
                       font=('Comic Sans',30,'bold'),
                       fg=fontColour,
                       bg=bgColour)
    page6Title.pack(pady=20)


    style = ttk.Style()

    style.theme_use('default')
    style.configure("Treeview.Heading",
                    font=('Comic Sans',20,'bold'),
                    rowheight=50,
                    background=bgColour,
                    foreground = fontColour)
    
    style.configure("Treeview",
                    background=bgColour,
                    foreground = fontColour,
                    fieldbackground=bgColour,
                    rowheight=35,
                    font=('Comic Sans',15))
    style.map("Treeview")

    tree = ttk.Treeview(page6)

    tree['columns'] = ('Name','Score','Dificulty')
    tree.column('#0',width=0,stretch=NO)
    tree.column('Name',anchor=CENTER)
    tree.column('Score',anchor=CENTER)
    tree.column('Dificulty',anchor=CENTER)

    tree.heading('#0',text='',anchor=W)
    tree.heading('Name',text='Name',anchor=CENTER)
    tree.heading('Score',text='Score',anchor=CENTER)
    tree.heading('Dificulty',text='Dificulty',anchor=CENTER)

    scoreFile = open('scores','r')
    records = scoreFile.readlines()
    records.sort(reverse=True)
    for i in range(len(records)):
        record = records[i].split(',')
        print(record)
        tree.insert(parent='',index=END, iid=i, text='',values=(record[1],(f'{record[0]}/54'),(f'{record[2][:-1]}')))

    tree.pack(expand=1,fill=BOTH)

    menuBtn = Button(page6,
                      text='MENU',
                      font=('Comic Sans',20),
                      width=20,
                      fg=fontColour,
                      bg=btnStaticColour,
                      activebackground=btnActiveColour,
                      relief=FLAT,
                      command=lambda: openPage(menuPage))
    
    menuBtn.pack(pady=20)




# Binds the enter key to do the submit() function

menuPage()
window.mainloop()