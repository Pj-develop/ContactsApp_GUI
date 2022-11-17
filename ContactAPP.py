import PySimpleGUI as sg


Data={"PRIYANSHU JHA":9518476761,"SUNIL KUMAR MEHTA":123456789,"PRINCE":8974563211,"AYUSH TIWARI":1234567899,"ASHUTOSH SHUKLA":1234567889,"AYUSHI BHUTANI":1234567789,"JASPAL":1234566789}

   
def DisplayS():
    Data2=Data
    sg.popup_scrolled(Data2, title="Data Information")
    return Data2

def SearchName():
    layout=[[sg.Text("Enter Name of Student to Search : "),sg.Input(key="Nm1")],
         [sg.Exit(s=15,button_color="tomato"),sg.Button("Search",s=15,button_color="green")]]
    window=sg.Window("Search By Name",layout,modal=True)
    while True:
        event,values=window.read()
        if event in (sg.WINDOW_CLOSED,"Exit"):
            break
        if event=="Search":
            Nm1=values['Nm1']
            for i in Data:
                if Nm1.upper()==i.upper():
                    sg.popup_no_titlebar("The Searach for {} is Found and his Contact No. is {}".format(i,Data[i]))
                    break
                else:
                    sg.popup_error("The Searach for {} is Not Found".format(Nm1))      
    window.close()

def SearchCont():
    layout=[[sg.Text("Enter Contact Number of Student to Search : "),sg.Input(key="Cn1")],
         [sg.Exit(s=15,button_color="tomato"),sg.Button("Search",s=15,button_color="green")]]
    window=sg.Window("Search By Contact Number",layout,modal=True)
    while True:
        event,values=window.read()
        if event in (sg.WINDOW_CLOSED,"Exit"):
            break
        if event=="Search":
            Cn1=int(values['Cn1'])
            for i in Data:
                if Cn1==Data[i]:
                    sg.popup_no_titlebar("The Searach for Contact No. {} is Found and his Name is {}".format(Data[i],i))
                    break
                else:
                    sg.popup_error("The Searach for Contact No. {} is Not Found ".format(Cn1))     
    window.close()

def Extract():
    layout=[[sg.Text("Enter Name of the Student for which Data to be Extracted or Type ALL For Complete Extraction : "),sg.Input(key="out")],
         [sg.Exit(s=15,button_color="tomato"),sg.Button("Extract",s=15,button_color="green")]]
    window=sg.Window("Extraction",layout,modal=True)
    write_data=[]
    outf=open(r'DataExtracted.txt','w')
    while True:
        event,values=window.read()    
        out=values['out']
        if event in (sg.WINDOW_CLOSED,"Exit"):
            window.close()
            break
        if out.upper()=="ALL":
            for i in Data:
                conc=str(i)+','+str(Data[i])+'<----->'
                outf.write(conc)
            outf.close()
            sg.popup_no_titlebar("Files Extracted Successfully and Stored in the Same Directory of the Application")
        elif out.upper() in Data:
            for i in Data:
                if i==out.upper():
                    write_data.append(i)
                    write_data.append(Data[i])
            for k in write_data:
                outf.write(str(k))
            outf.close()
            sg.popup_no_titlebar("Files Extracted Successfully and Stored in the Same Directory of the Application")    
        else:
            sg.popup_error("Inavlid Key Enetered")
        
        
        

    
def Dlt():
    layout=[[sg.Text("Enter Name of the Student to be Deleted from the Database : "),sg.Input(key="popping")],
         [sg.Exit(s=15,button_color="tomato"),sg.Button("Delete",s=15,button_color="green")]]
    window=sg.Window("Deletion",layout,modal=True)
    while True:
        event,values=window.read()
        if event in (sg.WINDOW_CLOSED,"Exit"):
            break
        if event=="Delete":
            popping=values['popping']
            popping=popping.upper()
            x=Data.pop(popping)
            sg.popup_no_titlebar("{}:{} has been deleted from the Databse".format(popping,x))  
    window.close()


    
def Ins():
    layout=[[sg.Text("Enter Name of the Student to be Inserted in the Database : "),sg.Input(key="Ins1")],
            [sg.Text("Enter Contact Number of the Student to be Inserted in the Database : "),sg.Input(key="Ins2")],
         [sg.Exit(s=15,button_color="tomato"),sg.Button("Insert",s=15,button_color="green")]]
    window=sg.Window("Insertion",layout,modal=True)
    while True:
        event,values=window.read()
        if event in (sg.WINDOW_CLOSED,"Exit"):
            break
        if event=="Insert":
            Ins1=values['Ins1']
            Ins2=(values['Ins2'])
            Ins1=Ins1.upper()
            if len(Ins2)>9:
                Data.update({Ins1:Ins2})
                sg.popup_no_titlebar("{}  has been inserted in the Databse".format(Ins1))
            else:sg.popup_error("Invalid Mobile Number, Kindly Re-Check")
            
    window.close()

Menu1=[['About',['Info','Help']]]
layout=[[sg.MenubarCustom(Menu1,tearoff=False)],
    [sg.Text("                                                                                             "),sg.Image('ic.png')],[sg.Text('''                    
 ----------------------------------------------->Forget the Old ways to Save & Store Your Contacts Manually , One Stop Solution to Save Your Contacts <--------------------------------------------- )
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~) VERSION 2.O ( APLHA) (~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~)''')],[sg.Text('''
1. Search by Name
2. Search by Contact Number
3. Dispay All Contact Information
4. Extract Contact Information
5. Register New Contact
6. Delete Registered Contact Details
'''  )],[sg.Text("                                                                                      ")],[sg.Text("Enter the No. to Choose from the above List: "),sg.Input(key="a")],[sg.Exit(s=15,button_color="tomato"),sg.Button("Submit",s=15,button_color="green")]]

window=sg.Window("Contact App", layout)

while True:
    event,values=window.read()
    if event in (sg.WINDOW_CLOSED,"Exit"):
        break
    if event=="Submit":
        ans=int(values['a'])
        if ans==1:
            window.disappear()
            SearchName()
            window.reappear()
        elif ans==2:
            window.disappear()
            SearchCont()
            window.reappear()
        elif ans==3:
            window.disappear()
            DisplayS()
            window.reappear()
        elif ans==4:
            window.disappear()
            Extract()
            window.reappear()
        elif ans==5:
            window.disappear()
            Ins()
            window.reappear()
        elif ans==6:
            window.disappear()
            Dlt()
            window.reappear()
        else:
            sg.popup_error("Invalid Input, Kindly Enter Options from the Above list (1 - 6 ) !!!!!!!!!!!!!!!")
    if event=="Info":
            window.disappear()
            sg.popup_scrolled('''
            Hii, I am Priyanshu Jha
Thankyou You using our App .
Hope we will be resolving issues in this domain.
Let's connect 
https://www.linkedin.com/in/pjDevelop
You can also checkout my Github repository:
https://github.com/pj-develop
''', title="About Us")
            window.reappear()

window.close()


    

