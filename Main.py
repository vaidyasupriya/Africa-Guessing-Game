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


# User Name entry function
def nameSubmit(event):
    userName = nameEntry.get()
    score = len(inputs)
    if score < 10:
        record = f'0{score},{userName}\n'
    else:
        record = f'{score},{userName}\n'
    scoreFile = open('scores','a')
    scoreFile.writelines(record)
    scoreFile.close
    openPage(menuPage)
    


# Country Name entry function
def submit(event): 
    global rowCounter
    global columnCounter

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
                                 foreground='green',
                                 background=bgColour)
        
        # Adds that label to the next available space on the grid
        countryNameLabel.grid(column=columnCounter,
                              row=rowCounter,
                              sticky='nsew',
                              padx=10)

        columnCounter += 1
        if len(inputs)==54:
            openPage(resultsPage)



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
    page1 = Frame(mainFrame)
    page1.pack(expand=1,fill=BOTH)
    page1.config(bg=bgColour)

    pg1Title = Label(page1, 
                  text='AFRICA QUIZ',
                  font=('Comic Sans',50,'bold'),
                  bg=bgColour,
                  fg=fontColour).pack(pady=40,expand=1)


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
                       command=lambda: openPage(leaderBoardPage))

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


    pg1btnGrid.pack(expand=1)




# Makes Page 2 (game page)
def gamePage():

    # Attaching key binds to functions
    window.unbind('<Return>')
    window.bind('<Return>',submit)

    global liveScore
    global countryEntry
    global tableFrame

    # Setting up page 2
    page2 = Frame(mainFrame,bg=bgColour)
    page2.pack(expand=1,fill=BOTH)

    liveScoreFrame = Frame(page2,bg=bgColour)
    liveScoreFrame.pack()

    liveScore = Label(liveScoreFrame,
                      text=(f'{len(inputs)}/54'),
                      font=('Comic Sans',20,'bold'),
                      bg=bgColour,
                      fg=fontColour)
    liveScore.pack(pady=5)

    page2Title = Label(page2,
                       text='Enter African Country',
                       font=('Comic Sans',20,'bold'),
                       bg=bgColour,
                       fg=fontColour)
    page2Title.pack(pady=5)

    countryEntry = Entry(page2,
                         font=('Comic Sans',20))
    countryEntry.pack(pady=10)

    resetBtn = Button(page2,
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
    tableFrame = Frame(page2,bg=bgColour)
    tableFrame.columnconfigure(0,weight=1)
    tableFrame.columnconfigure(1,weight=1)
    tableFrame.columnconfigure(2,weight=1)
    tableFrame.pack(expand=1,fill=BOTH)


# Makes page 3 (results page)
def resultsPage():

    # Setting up page 3
    page3 =  Frame(mainFrame,bg=bgColour)
    page3.pack(expand=1,fill=BOTH)

    
    scoreNumberLabel = Label(page3,text=(f'{str(len(inputs))}/54'),
                             font=('Comic Sans',30,'bold'),
                             background=bgColour,
                             foreground=fontColour)
    scoreNumberLabel.pack(pady=40,expand=1)
    

    countryListFrame = Frame(page3,bg=bgColour)
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

    page3BtnGrid = Frame(page3,bg=bgColour)
    page3BtnGrid.columnconfigure(0,weight=1)
    page3BtnGrid.columnconfigure(1,weight=1)
    page3BtnGrid.pack(expand=1,fill=X)
    menuBtn = Button(page3BtnGrid,
                      text='MENU',
                      font=('Comic Sans',20),
                      width=20,
                      fg=fontColour,
                      bg=btnStaticColour,
                      activebackground=btnActiveColour,
                      relief=FLAT,
                      command=lambda: openPage(menuPage))
    
    menuBtn.grid(row=0,column=0,pady=20)

    saveBtn = Button(page3BtnGrid,
                      text='SAVE',
                      font=('Comic Sans',20),
                      width=20,
                      fg=fontColour,
                      bg=btnStaticColour,
                      activebackground=btnActiveColour,
                      relief=FLAT,
                      command=lambda: openPage(saveResultsPage))
    
    saveBtn.grid(row=0,column=1,pady=20)



# Making page 4 (Save Results Page)

def saveResultsPage():

    # Attaching key binds to functions
    window.unbind('<Return>')
    window.bind('<Return>',nameSubmit)

    global nameEntry

    # Setting up page 4
    page4 = Frame(mainFrame,bg=bgColour)
    page4.pack(expand=1,fill=BOTH)

    page4Title = Label(page4,
                       text='Enter Your Name',
                       font=('Comic Sans',30,'bold'),
                       fg=fontColour,
                       bg=bgColour)
    page4Title.pack(pady=20,expand=1)


    nameEntry = Entry(page4,
                      font=('Comic Sans',20))
    nameEntry.pack(pady=20,expand=1)



    


# Making page 5 (leaderboard Page)
def leaderBoardPage():

    # Setting up page 5
    page5 = Frame(mainFrame,bg=bgColour)
    page5.pack(expand=1,fill=BOTH)

    page5Title = Label(page5,
                       text='LEADER BOARD',
                       font=('Comic Sans',30,'bold'),
                       fg=fontColour,
                       bg=bgColour)
    page5Title.pack(pady=20)


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

    tree = ttk.Treeview(page5)

    tree['columns'] = ('Name','Score')
    tree.column('#0',width=0,stretch=NO)
    tree.column('Name',anchor=CENTER)
    tree.column('Score',anchor=CENTER)

    tree.heading('#0',text='',anchor=W)
    tree.heading('Name',text='Name',anchor=CENTER)
    tree.heading('Score',text='Score',anchor=CENTER)

    scoreFile = open('scores','r')
    records = scoreFile.readlines()
    records.sort(reverse=True)
    for i in range(len(records)):
        record = records[i].split(',')
        tree.insert(parent='',index=END, iid=i, text='',values=(record[1][:-1],(f'{record[0]}/54')))

    tree.pack(expand=1,fill=BOTH)

    menuBtn = Button(page5,
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