import tkinter.messagebox
import tkinter.ttk as tk
from tkinter import *
from tkinter import messagebox
import datetime
import mysql.connector


class LibraryMainPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        root.geometry('1270x800+0+0')
        lbtitle = Label(root, relief=RIDGE, text='LIBRARY MANAGEMENT SYSTEM', bg="red",
                        font=("times new roman", 40, "bold"))
        lbtitle.pack(side=TOP, fill=X)
        # --------------------------Variable Declaration-----------------------#
        self.vMemberType = StringVar()
        self.vCardNo = StringVar()
        self.vFname = StringVar()
        self.vLname = StringVar()
        self.vMobNo = StringVar()
        self.vAddress = StringVar()
        self.vPostCode = StringVar()
        self.vBookId = StringVar()
        self.vBookTitle = StringVar()
        self.vIssueDate = StringVar()
        self.vReturnDate = StringVar()

        # -------------------------Dataframe----------------------------------#
        dataframe = Frame(self.root, bd=20, relief=RIDGE)
        dataframe.place(x=0, y=130, width=1270, height=300)

        # ------------------------DataFrameLeft-------------------------------#

        frameleft = LabelFrame(dataframe, text="MEMBERSHIP INFORMATION", relief=SOLID, bg="powder blue",
                               font=("times new roman", 20, "bold"))
        frameleft.place(x=0, y=5, width=900, height=300)

        lbmemember = Label(frameleft, text="MEMBER TYPE", bg="powder blue", font=("times new roman", 10, "bold"),
                           padx=5, pady=6)
        lbmemember.grid(row=0, column=0, sticky=W)

        combbox = tk.Combobox(frameleft, textvariable=self.vMemberType, font=("times new roman", 10, "bold"),
                              state="readonly", width=25)
        combbox["value"] = ['Student', 'Admin', 'Lecturer']
        combbox.grid(row=0, column=1)

        lblPRN_no = Label(frameleft, text="CARD NO", bg="powder blue", font=("times new roman", 10, "bold"), padx=5,
                          pady=6)
        lblPRN_no.grid(row=1, column=0, sticky=W)

        txtPRN_no = Entry(frameleft, textvariable=self.vCardNo, font=("times new roman", 10, "bold"), width=28)
        txtPRN_no.grid(row=1, column=1)

        lblFname = Label(frameleft, text="FIRST NAME", bg="powder blue", font=("times new roman", 10, "bold"), padx=5,
                         pady=6)
        lblFname.grid(row=2, column=0, sticky=W)

        lblFname = Entry(frameleft, textvariable=self.vFname, font=("times new roman", 10, "bold"), width=28)
        lblFname.grid(row=2, column=1)

        lblLname = Label(frameleft, text="LAST NAME", bg="powder blue", font=("times new roman", 10, "bold"), padx=5,
                         pady=6)
        lblLname.grid(row=3, column=0, sticky=W)

        lblLname = Entry(frameleft, textvariable=self.vLname, font=("times new roman", 10, "bold"), width=28)
        lblLname.grid(row=3, column=1)

        lblMobno = Label(frameleft, text="MOBILE NO", bg="powder blue", font=("times new roman", 10, "bold"), padx=5,
                         pady=6)
        lblMobno.grid(row=4, column=0, sticky=W)

        lblMobno = Entry(frameleft, textvariable=self.vMobNo, font=("times new roman", 10, "bold"), width=28)
        lblMobno.grid(row=4, column=1)

        lblADD = Label(frameleft, text="ADDRESS", bg="powder blue", font=("times new roman", 10, "bold"), padx=5,
                       pady=6)
        lblADD.grid(row=5, column=0, sticky=W)

        lblADD = Entry(frameleft, textvariable=self.vAddress, font=("times new roman", 10, "bold"), width=28)
        lblADD.grid(row=5, column=1)

        lblPostcode = Label(frameleft, text="POST CODE", bg="powder blue", font=("times new roman", 10, "bold"),
                            padx=5,
                            pady=6)
        lblPostcode.grid(row=6, column=0, sticky=W)
        lblIssuedate = Entry(frameleft, textvariable=self.vPostCode, font=("times new roman", 10, "bold"), width=28)
        lblIssuedate.grid(row=6, column=1)

        lblBookid = Label(frameleft, text="BOOK ID", font=("times new roman", 10, "bold"), bg="powder blue",
                          padx=5, pady=6)
        lblBookid.grid(row=0, column=3)
        lblBookid = Entry(frameleft, textvariable=self.vBookId, font=("times new roman", 10, "bold"), width=28)
        lblBookid.grid(row=0, column=4)

        lblBooktitle = Label(frameleft, text="BOOK TITLE", font=("times new roman", 10, "bold"), bg="powder blue"
                             , padx=5, pady=6)
        lblBooktitle.grid(row=1, column=3)
        lblBooktitle = Entry(frameleft, textvariable=self.vBookTitle, font=("times new roman", 10, "bold"), width=28)
        lblBooktitle.grid(row=1, column=4)

        lblIssuedate = Label(frameleft, text="ISSUE DATE", bg="powder blue", font=("times new roman", 10, "bold"),
                             padx=5,
                             pady=6)
        lblIssuedate.grid(row=2, column=3, sticky=W)
        lblIssuedate = Entry(frameleft, textvariable=self.vIssueDate, font=("times new roman", 10, "bold"), width=28)
        lblIssuedate.grid(row=2, column=4)

        lblReturndate = Label(frameleft, text="RETURN DATE", bg="powder blue", font=("times new roman", 10, "bold"),
                              padx=5,
                              pady=6)
        lblReturndate.grid(row=3, column=3, sticky=W)

        lblReturndate = Entry(frameleft, textvariable=self.vReturnDate, font=("times new roman", 10, "bold"), width=28)
        lblReturndate.grid(row=3, column=4)

        # ------------------------DataFrameRight------------------------------#
        frameright = LabelFrame(dataframe, text="BOOK DETAILS", relief=SOLID, bg="powder blue",
                                font=("times new roman", 20, "bold"))
        frameright.place(x=901, y=5, width=320, height=300)

        self.txtBox = Text(frameright, font=("arial", 12, "bold"), width=32, height=16, padx=5, pady=6)
        self.txtBox.grid(row=0, column=2)
        lstScrollbar = Scrollbar(frameright)
        lstScrollbar.grid(row=0, column=1, sticky="ns")

        lstBooks = ['Python', 'C# Beginners', 'Java Foundation', 'PHP for Beginners', 'Python for Data Science',
                    'Python for AI&ML']

        def selectbook(event=""):
            value = str(lstBox.get(lstBox.curselection()))
            length=len(lstBooks)
            x = value
            for i in range(0,length):
                if lstBooks[i]==x:
                    book=lstBooks[i]
                    self.vBookId.set(book[0:3]+"10"+str(i))
                    self.vBookTitle.set(lstBooks[i])
                    issuedate = datetime.datetime.today()
                    tempdate = datetime.timedelta(days=15)
                    returndate = issuedate + tempdate
                    self.vIssueDate.set(str(issuedate))
                    self.vReturnDate.set(str(returndate))

        lstBox = Listbox(frameright, font=("arial", 12, "bold"), width=20, height=16)

        lstBox.bind("<<ListboxSelect>>", selectbook)
        lstBox.grid(row=0, column=0)
        lstScrollbar.config(command=lstBox.yview())

        for item in lstBooks:
            lstBox.insert(END, item)
        # --------------------------FRAMEBUTTON-------------------------------#

        framebutton = Frame(self.root, bd=10, relief=RIDGE, padx=10, bg="powder blue")
        framebutton.place(x=0, y=450, width=1520, height=70)

        btnRegister = Button(framebutton, command=self.addData, text="Register", font=("times new roman", 10, "bold"),
                             bg="grey", width=15,
                             padx=5, pady=6)
        btnRegister.grid(row=10, column=0)

        btnView = Button(framebutton, command=self.show_data, text="View Records", font=("times new roman", 10, "bold"),
                         bg="grey", width=15,
                         padx=5, pady=6)
        btnView.grid(row=10, column=1)

        btnUpdate = Button(framebutton, command=self.update, text="Update Records",
                           font=("times new roman", 10, "bold"), bg="grey",
                           width=15,
                           padx=5, pady=6)
        btnUpdate.grid(row=10, column=2)

        btnDelete = Button(framebutton, command=self.delete, text="Delete Records",
                           font=("times new roman", 10, "bold"), bg="grey",
                           width=15,
                           padx=5, pady=6)
        btnDelete.grid(row=10, column=3)

        btnExit = Button(framebutton, command=self.exit, text="Exit",
                         font=("times new roman", 10, "bold"), bg="grey",
                         width=15,
                         padx=5, pady=6)
        btnExit.grid(row=10, column=4)

        # .................................Frame Details---------------------------------------#

        framedetails = Frame(self.root, bd=10, relief=RIDGE, padx=10, bg="powder blue")
        framedetails.place(x=0, y=500, width=2220, height=1000)

        Tableframe = Frame(framedetails, bd=6, relief=RIDGE, bg="powder blue")
        Tableframe.place(x=0, y=2, width=1300, height=190)
        xscroll = tk.Scrollbar(Tableframe, orient=HORIZONTAL)
        yscroll = tk.Scrollbar(Tableframe, orient=VERTICAL)

        self.library_table = tk.Treeview(Tableframe,
                                         columns=['MEMBER TYPE', 'CARD NO', 'FirstName', 'LastName', 'MOBILE NO',
                                                  'ADDRESS', "POSTCODE", "BOOK ID", "BOOK TITLE", "ISSUE DATE",
                                                  "RETURN DATE"], xscrollcommand=xscroll.set,
                                         yscrollcommand=yscroll.set)
        xscroll.pack(side=TOP, fill=X)
        yscroll.pack(side=LEFT, fill=Y)

        self.library_table.heading("MEMBER TYPE", text="MEMBER TYPE")
        self.library_table.heading("CARD NO", text="CARD NO")
        self.library_table.heading("FirstName", text="FIRST NAME")
        self.library_table.heading("LastName", text="LAST NAME")
        self.library_table.heading("MOBILE NO", text="MOBILE NO")
        self.library_table.heading("ADDRESS", text="ADDRESS")
        self.library_table.heading("POSTCODE", text="POSTCODE")
        self.library_table.heading("BOOK ID", text="BOOK ID")
        self.library_table.heading("BOOK TITLE", text="BOOK TITLE")
        self.library_table.heading("ISSUE DATE", text="ISSUE DATE")
        self.library_table.heading("RETURN DATE", text="RETURN DATE")

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH)

        self.library_table.column("MEMBER TYPE")
        self.library_table.column("CARD NO")
        self.library_table.column("FirstName")
        self.library_table.column("LastName")
        self.library_table.column("MOBILE NO")
        self.library_table.column("ADDRESS")
        self.library_table.column("POSTCODE")
        self.library_table.column("BOOK ID")
        self.library_table.column("BOOK TITLE")
        self.library_table.column("ISSUE DATE")
        self.library_table.column("RETURN DATE")

        self.show_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    def addData(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="admin", database="LibraryDB")
        cursor = conn.cursor()
        cursor.execute("Insert into LibraryTB values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (self.vMemberType.get(), self.vCardNo.get(), self.vFname.get(), self.vLname.get(),
                        self.vMobNo.get(), self.vAddress.get(),
                        self.vPostCode.get(), self.vBookId.get(), self.vBookTitle.get(), self.vIssueDate.get(),
                        self.vReturnDate.get())
                       )
        conn.commit()
        self.show_data()
        messagebox.showinfo("Message", "Data Added Successfully")
        conn.close()

    def show_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="admin", database="LibraryDB")
        cursor = conn.cursor()
        cursor.execute("select * from LibraryTB")
        rows = cursor.fetchall()
        if len(rows) == 0:
            messagebox.showinfo("Message", "No data")
        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="admin", database="LibraryDB")
        cursor = conn.cursor()
        cursor.execute(
            "Update LibraryTB set MEMBER_TYPE=%s,CARD_NO=%s,FNAME=%s,LNAME=%s,MOB_NO=%s,Address=%s,POSTCODE=%s,Bookid=%s,Booktitle=%s,IssueDate=%s,Returndate=%s where CARD_NO=%s",
            (self.vMemberType.get(), self.vCardNo.get(), self.vFname.get(), self.vLname.get(),
             self.vMobNo.get(), self.vAddress.get(),
             self.vPostCode.get(), self.vBookId.get(), self.vBookTitle.get(), self.vIssueDate.get(),
             self.vReturnDate.get(), self.vCardNo.get())
        )
        conn.commit()
        self.show_data()
        messagebox.showinfo("Message", "Data Updated Successfully")
        conn.close()

    def delete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="admin", database="LibraryDB")
        cursor = conn.cursor()
        query = "Delete from LibraryTB where CARD_NO=%s"
        val = (self.vCardNo.get(),)
        cursor.execute(query, val)
        conn.commit()
        messagebox.showinfo("Message", "Data Deleted Successfully")
        self.show_data()

        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        col = content["values"]

        self.vMemberType.set(col[0])
        self.vCardNo.set(col[1])
        self.vFname.set(col[2])
        self.vLname.set(col[3])
        self.vMobNo.set(col[4])
        self.vAddress.set(col[5])
        self.vPostCode.set(col[6])
        self.vBookId.set(col[7])
        self.vBookTitle.set(col[8])
        self.vIssueDate.set(col[9])
        self.vReturnDate.set(col[10])

    def exit(self):
        ex = tkinter.messagebox.askyesno("Message", "Do You Want To Exit")
        if ex > 0:
            self.root.destroy()
            return




if __name__ == "__main__":
    root = Tk()
    obj = LibraryMainPage(root)
    root.mainloop()

