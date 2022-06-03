"""
BANK DB MANAGEMENT SYSTEM
developed by Shreyansh Padarha
"""

"""
------------
|Calculator|
------------
"""


# CLICKING BUTTONS (NUMBERS) FUNCTION
# function for selecting number on the button and displaying it


def button_click(number):
    # fetching the number in the box currently
    current = e.get()

    # for deleting pre-existing values inside the e box : e.delete(0, END)
    e.delete(0, END)

    # for inserting value which has been entered
    e.insert(0, str(current) + str(number))


'''
CLEAR BUTTON FUNCTION
function for clearing values inside the box when the clear button is clicked
'''


def clear():
    e.delete(0, END)


'''
ADD BUTTON FUNCTION
function for adding the values in the box when add button is clicked
'''


def add():
    # fetching number present in the entry box
    first_number = e.get()

    # variables needed to be assigned as global variables so that they can be reused later in button_equal func.
    global f_num
    global math

    # assigning this value, which will be used later in equatinf function (conditional statements)
    math = 'addition'
    # assigning the variable and typecasting it for further mathamatical treatment.
    f_num = int(first_number)

    # clearing the value currently inside the entry box
    e.delete(0, END)


'''
SUBTRACT BUTTON FUNCTION
function for subtracting the values in the box when equal button is clicked
'''


def subtract():
    # fetching number present in the entry box
    first_number = e.get()

    # variables needed to be assigned as global variables so that they can be reused later in button_equal func
    global f_num
    global math

    # assigning this value, which will be used later in equatinf function (conditional statements)
    math = 'subtraction'
    # assigning the variable and typecasting it for further mathamatical treatment.
    f_num = int(first_number)

    # clearing the value currently inside the entry box
    e.delete(0, END)


'''
MULTIPLY BUTTON FUNCTION
function for multiplying the values in the box when equal button is clicked
'''


def multiply():
    # fetching number present in the entry box
    first_number = e.get()

    # variables needed to be assigned as global variables so that they can be reused later in button_equal func
    global f_num
    global math

    # assigning this value, which will be used later in equatinf function (conditional statements)
    math = 'multiplication'
    # assigning the variable and typecasting it for further mathamatical treatment.
    f_num = int(first_number)

    # clearing the value currently inside the entry box
    e.delete(0, END)


'''
DIVIDE BUTTON FUNCTION
function for dividing the values in the box when equal button is clicked
'''


def divide():
    # fetching number present in the entry box
    first_number = e.get()

    # variables needed to be assigned as global variables so that they can be reused later in button_equal func
    global f_num
    global math

    # assigning this value, which will be used later in equatinf function (conditional statements)
    math = 'division'
    # assigning the variable and typecasting it for further mathamatical treatment.
    f_num = int(first_number)

    # clearing the value currently inside the entry box
    e.delete(0, END)


'''
EQUAL BUTTON FUNCTION
function for equating the values in the box when equal button is clicked
'''


def equal():
    # fetching the second number entered in the entry box
    second_number = e.get()

    # clearing the value currently inside the entry box
    e.delete(0, END)

    # using conditional statements, and operators for performing calculations

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == 'subtraction':
        e.insert(0, f_num - int(second_number))
    if math == 'multiplication':
        e.insert(0, f_num * int(second_number))
    if math == 'division':
        e.insert(0, int(f_num) / int(second_number))


'''
MAIN DRIVER CODE FOR CALCULATOR (incorporating all functions)
'''



def calculator():
    # instantizing Tk() under the object name calc
    calc = Tk()
    # Title for calculator window
    calc.title("CALCULATOR")
    # ICII has its theme colour as Deep Saffron orange, hex code : #F99D27
    calc['background'] = '#F99D27'

    # creating an entry widget for entering numbers
    # e needs to be a global variable as its being referenced in other functions
    global e
    e = Entry(calc, width=35, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    # --------------------- Defining respective buttons ------------------------------------------
    button_1 = Button(calc, text="1", padx=40, pady=20, command=lambda: button_click(1))
    button_1.config(font=("Arial", 14, 'bold'))
    button_2 = Button(calc, text="2", padx=40, pady=20, command=lambda: button_click(2))
    button_2.config(font=("Arial", 14, 'bold'))
    button_3 = Button(calc, text="3", padx=40, pady=20, command=lambda: button_click(3))
    button_3.config(font=("Arial", 14, 'bold'))
    button_4 = Button(calc, text="4", padx=40, pady=20, command=lambda: button_click(4))
    button_4.config(font=("Arial", 14, 'bold'))
    button_5 = Button(calc, text="5", padx=40, pady=20, command=lambda: button_click(5))
    button_5.config(font=("Arial", 14, 'bold'))
    button_6 = Button(calc, text="6", padx=40, pady=20, command=lambda: button_click(6))
    button_6.config(font=("Arial", 14, 'bold'))
    button_7 = Button(calc, text="7", padx=40, pady=20, command=lambda: button_click(7))
    button_7.config(font=("Arial", 14, 'bold'))
    button_8 = Button(calc, text="8", padx=40, pady=20, command=lambda: button_click(8))
    button_8.config(font=("Arial", 14, 'bold'))
    button_9 = Button(calc, text="9", padx=40, pady=20, command=lambda: button_click(9))
    button_9.config(font=("Arial", 14, 'bold'))
    button_0 = Button(calc, text="0", padx=40, pady=20, command=lambda: button_click(0))
    button_0.config(font=("Arial", 14, 'bold'))

    button_add = Button(calc, text="+", padx=39, pady=20, command=add)
    button_add.config(font=("Arial", 14, 'bold'))
    button_equal = Button(calc, text="=", padx=91, pady=20, command=equal)
    button_equal.config(font=("Arial", 14, 'bold'))
    button_clear = Button(calc, text="Clear", padx=79, pady=20, command=clear)
    button_clear.config(font=("Arial", 14, 'bold'))

    button_subtract = Button(calc, text="-", padx=41, pady=20, command=subtract)
    button_subtract.config(font=("Arial", 14, 'bold'))
    button_multiply = Button(calc, text="*", padx=40, pady=20, command=multiply)
    button_multiply.config(font=("Arial", 14, 'bold'))
    button_divide = Button(calc, text="/", padx=41, pady=20, command=divide)
    button_divide.config(font=("Arial", 14, 'bold'))

    # --------------------- Placing the buttons on the screen -------------------------

    # first row buttons
    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    # second row buttons
    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    # third row buttons
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    # fourth row buttons
    button_0.grid(row=4, column=0)
    button_clear.grid(row=4, column=1, columnspan=2)

    # fifth row buttons
    button_add.grid(row=5, column=0)
    button_equal.grid(row=5, column=1, columnspan=2)

    # sixt row buttons
    button_subtract.grid(row=6, column=0)
    button_multiply.grid(row=6, column=1)
    button_divide.grid(row=6, column=2)

    # running the continous tkinter (pop-up) loop for calcualtor window
    calc.mainloop()


"""
----------------------------
|Simple Interest Calculator|
----------------------------
"""


# for calculating simple interest
def calc_SI():
    # instantizing Tk() under the object name result_si
    result_si = Tk()
    # Title for window
    result_si.title("RESULTING SI")
    # background colour for reult_si window
    result_si['background'] = '#F99D27'

    # getting and fetching values from entry widgets
    principle = float(p_entry.get())
    roi = float(r_entry.get())
    time = float(t_entry.get())

    global Simple_Int
    # =========================== Computing Simple Interest ===========================
    Simple_Int = (float(principle) * float(roi) * float(time)) / 100
    Final_Amount = float(principle) + float(Simple_Int)

    # ======== Result output in text form =====================
    FA_text = "Final Amount after " + str(roi) + " years is ₹" + str(Final_Amount)
    SI_text = "Simple Interest Earned during " + str(roi) + " years is ₹" + str(Simple_Int)

    # ============ labels for displaying output in new popup window ========
    fa_label = Label(result_si, text=FA_text, fg='black', bg='#F99D27')
    fa_label.config(font=("Arial", 30, 'bold'))
    fa_label.grid(row=0, column=0, columnspan=2, )

    si_label = Label(result_si, text=SI_text, fg='black', bg='#F99D27')
    si_label.config(font=("Arial", 30, 'bold'))
    si_label.grid(row=1, column=0, columnspan=2, )

    # ================== button to exit result_si window with destroy method of tkinter ============
    leave_btn = Button(result_si, text="EXIT", command=result_si.destroy, fg='#B02A30', bg='white')
    leave_btn.config(font=("Arial", 30, 'bold'))
    leave_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=186, ipady=15)

    p_entry.delete(0, END)
    r_entry.delete(0, END)
    t_entry.delete(0, END)

    # running the continous tkinter (pop-up) loop for result_si window
    result_si.mainloop()


def Simple_Interest():
    # as the SI window will be used while computing and displaying in another function we'll set it as global var.
    global SI
    # instantizing Tk() under the object name SI
    SI = Tk()

    # Title for calculator window
    SI.title("SIMPLE INTEREST CALCULATOR")

    # ICII has its theme colour as Deep Saffron orange, hex code : #F99D27
    SI['background'] = '#F99D27'

    # window size being established
    SI.geometry('700x360')

    # _____________________________Labels and entry widgets for inputting values___________________________

    # assigning the entries as global variables so that the inputs can be used in other user-def functions.
    global p_entry
    global r_entry
    global t_entry

    # ************************* PRINCIPLE ACCOUNT *********************

    # Label widget to show where to enter values
    p_label = Label(SI, text="Principle Amount : ", fg='black', bg='#F99D27')
    p_label.config(font=("Arial", 30, 'bold'))
    p_label.grid(row=0, column=0)

    # Entry box widget to enter principle amount
    p_entry = Entry(SI, width=20, justify='center', fg='#B02A30', bg='white')
    p_entry.config(font=("Arial", 30, 'bold'))
    p_entry.grid(row=0, column=1, pady=10, ipady=9)

    # ************************* RATE OF INTEREST *********************

    # Label widget to show where to enter values
    r_label = Label(SI, text="Rate Of Interest(%) : ", fg='black', bg='#F99D27')
    r_label.config(font=("Arial", 30, 'bold'))
    r_label.grid(row=1, column=0)

    # Entry box widget to enter rate of interest
    r_entry = Entry(SI, width=20, justify='center', fg='#B02A30', bg='white')
    r_entry.config(font=("Arial", 30, 'bold'))
    r_entry.grid(row=1, column=1, pady=10, ipady=9)

    # ************************* Time Period *********************

    # Label widget to show where to enter values
    t_label = Label(SI, text="Time Period (years) : ", fg='black', bg='#F99D27')
    t_label.config(font=("Arial", 30, 'bold'))
    t_label.grid(row=2, column=0)

    # Entry box widget to enter time period
    t_entry = Entry(SI, width=20, justify='center', fg='#B02A30', bg='white')
    t_entry.config(font=("Arial", 30, 'bold'))
    t_entry.grid(row=2, column=1, pady=10, ipady=9)

    # _____________________________Calculate Button___________________________

    calc_btn = Button(SI, text="CALCULATE", command=calc_SI, fg='#B02A30', bg='white')
    calc_btn.config(font=("Arial", 30, 'bold'))
    calc_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=186, ipady=15)


"""
------------------------------
|Compound Interest Calculator|
------------------------------
"""


def calc_CI():
    # instantizing Tk() under the object name result_ci
    result_ci = Tk()
    # Title for window
    result_ci.title("RESULTING CI")
    # background colour for reult_ci window
    result_ci['background'] = '#F99D27'

    # getting and fetching values from entry widgets
    principle_ci = float(p__entry.get())
    roi_ci = float(r__entry.get())
    time_ci = float(t__entry.get())

    # =========================== Computing Compound Interest ===========================

    Final_Amount_ = float(principle_ci) * (pow((1 + float(roi_ci) / 100), float(time_ci)))
    Compound_Int = float(Final_Amount_ - principle_ci)

    # ======== Result output in text form =====================
    FA_text_ci = "Final Amount after " + str(roi_ci) + " years is ₹" + str(Final_Amount_)
    CI_text_ci = "Conpound Interest Earned during " + str(roi_ci) + " years is ₹" + str(Compound_Int)

    # ============ labels for displaying output in new popup window ========
    fa_label_ci = Label(result_ci, text=FA_text_ci, fg='black', bg='#F99D27')
    fa_label_ci.config(font=("Arial", 30, 'bold'))
    fa_label_ci.grid(row=0, column=0, columnspan=2, )

    si_label_ci = Label(result_ci, text=CI_text_ci, fg='black', bg='#F99D27')
    si_label_ci.config(font=("Arial", 30, 'bold'))
    si_label_ci.grid(row=1, column=0, columnspan=2, )

    # ================== button to exit result_si window with destroy method of tkinter ============
    leave_btn_ci = Button(result_ci, text="EXIT", command=result_ci.destroy, fg='#B02A30', bg='white')
    leave_btn_ci.config(font=("Arial", 30, 'bold'))
    leave_btn_ci.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=186, ipady=15)

    p__entry.delete(0, END)
    r__entry.delete(0, END)
    t__entry.delete(0, END)

    # running the continous tkinter (pop-up) loop for result_ci window
    result_ci.mainloop()


def Compound_Interest():
    # as the CI window will be used while computing and displaying in another function we'll set it as global var.
    global CI
    # instantizing Tk() under the object name CI
    CI = Tk()

    # Title for calculator window
    CI.title("COMPOUND INTEREST CALCULATOR")

    # ICII has its theme colour as Deep Saffron orange, hex code : #F99D27
    CI['background'] = '#F99D27'

    # window size being established
    CI.geometry('700x360')

    # _____________________________Labels and entry widgets for inputting values___________________________

    # assigning the entries as global variables so that the inputs can be used in other user-def functions.
    global p__entry
    global r__entry
    global t__entry

    # ************************* PRINCIPLE ACCOUNT *********************

    # Label widget to show where to enter values
    p__label = Label(CI, text="Principle Amount : ", fg='black', bg='#F99D27')
    p__label.config(font=("Arial", 30, 'bold'))
    p__label.grid(row=0, column=0)

    # Entry box widget to enter principle amount
    p__entry = Entry(CI, width=20, justify='center', fg='#B02A30', bg='white')
    p__entry.config(font=("Arial", 30, 'bold'))
    p__entry.grid(row=0, column=1, pady=10, ipady=9)

    # ************************* RATE OF INTEREST *********************

    # Label widget to show where to enter values
    r__label = Label(CI, text="Rate Of Interest(%) : ", fg='black', bg='#F99D27')
    r__label.config(font=("Arial", 30, 'bold'))
    r__label.grid(row=1, column=0)

    # Entry box widget to enter rate of interest
    r__entry = Entry(CI, width=20, justify='center', fg='#B02A30', bg='white')
    r__entry.config(font=("Arial", 30, 'bold'))
    r__entry.grid(row=1, column=1, pady=10, ipady=9)

    # ************************* Time Period *********************

    # Label widget to show where to enter values
    t__label = Label(CI, text="Time Period (years) : ", fg='black', bg='#F99D27')
    t__label.config(font=("Arial", 30, 'bold'))
    t__label.grid(row=2, column=0)

    # Entry box widget to enter time period
    t__entry = Entry(CI, width=20, justify='center', fg='#B02A30', bg='white')
    t__entry.config(font=("Arial", 30, 'bold'))
    t__entry.grid(row=2, column=1, pady=10, ipady=9)

    # _____________________________Calculate Button___________________________

    calc__btn = Button(CI, text="CALCULATE", command=calc_CI, fg='#B02A30', bg='white')
    calc__btn.config(font=("Arial", 30, 'bold'))
    calc__btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=186, ipady=15)


"""
-----------------------
|Create Account Button|
-----------------------
"""


def Create_ACC():
    # instantizing Tk() under the object name ca (Create Account)
    global ca
    ca = Tk()
    ca.title("CREATING NEW ACCOUNT")
    ca.geometry('540x810')
    ca['background'] = '#F99D27'

    bank_db = sqlite3.connect('bank_database.db')

    # create cursor
    b = bank_db.cursor()
    # -------------------------Label Personal details : to contain Personal Details-----------------------
    personal = LabelFrame(ca, text='Personal Details', bg='#F99D27', fg='#005B75')
    personal.config(font=("Arial", 35, 'bold'))
    personal.grid(row=1, column=0, padx=20, pady=10, columnspan=2)

    # ------------------------------------creating entry widgets (personal detaisl)----------------------

    global f_name
    global l_name
    global address
    global city
    global state
    global zipcode
    global acc

    f_name = Entry(personal, width=20, justify='center', fg='#B02A30', bg='white')
    f_name.config(font=("Arial", 25, 'bold'))
    f_name.grid(row=0, column=1, padx=20, pady=10)

    l_name = Entry(personal, width=20, justify='center', fg='#B02A30', bg='white')
    l_name.config(font=("Arial", 25, 'bold'))
    l_name.grid(row=1, column=1, padx=20, pady=10)

    address = Entry(personal, width=20, justify='center', fg='#B02A30', bg='white')
    address.config(font=("Arial", 25, 'bold'))
    address.grid(row=2, column=1, padx=20, pady=10)

    city = Entry(personal, width=20, justify='center', fg='#B02A30', bg='white')
    city.config(font=("Arial", 25, 'bold'))
    city.grid(row=3, column=1, padx=20, pady=10)

    state = Entry(personal, width=20, justify='center', fg='#B02A30', bg='white')
    state.config(font=("Arial", 25, 'bold'))
    state.grid(row=4, column=1, padx=20, pady=10)

    zipcode = Entry(personal, width=20, justify='center', fg='#B02A30', bg='white')
    zipcode.config(font=("Arial", 25, 'bold'))
    zipcode.grid(row=5, column=1, padx=20, pady=10)

    # --------------------------------creating text box labels (personal details)-------------------

    f_name_label = Label(personal, text='First Name', fg='black', bg='#F99D27')
    f_name_label.config(font=("Arial", 25, 'bold'))
    f_name_label.grid(row=0, column=0, pady=(10, 0))

    l_name_label = Label(personal, text='Last Name', fg='black', bg='#F99D27')
    l_name_label.config(font=("Arial", 25, 'bold'))
    l_name_label.grid(row=1, column=0)

    address_label = Label(personal, text='Address', fg='black', bg='#F99D27')
    address_label.config(font=("Arial", 25, 'bold'))
    address_label.grid(row=2, column=0)

    city_label = Label(personal, text='City', fg='black', bg='#F99D27')
    city_label.config(font=("Arial", 25, 'bold'))
    city_label.grid(row=3, column=0)

    state_label = Label(personal, text='State', fg='black', bg='#F99D27')
    state_label.config(font=("Arial", 25, 'bold'))
    state_label.grid(row=4, column=0)

    zipcode_label = Label(personal, text='Zipcode', fg='black', bg='#F99D27')
    zipcode_label.config(font=("Arial", 25, 'bold'))
    zipcode_label.grid(row=5, column=0)

    # -------------------------Label Account Type : to contain Radiobuttons-----------------------

    # NOTE : Faced too many glitches and bugs so had to use a loophole.

    # forming frame for account type selections
    a_type = LabelFrame(ca, text='Account Type', bg='#F99D27', fg='#005B75')
    a_type.config(font=("Arial", 35, 'bold'))
    a_type.grid(row=2, column=0, padx=15, pady=10, ipadx=5, columnspan=2)

    # list for options in dropdown menu
    options = [
        'Current Account',
        'Savings Account',
        'Fixed Deposit Account',
        'Recurring Deposit Account',
        'DEMAT Account',
        'NRI Account'
    ]

    # clicking specifics in the dropdown
    clicked = StringVar()
    clicked.set(options[0])

    drop = OptionMenu(a_type, clicked, *options)
    drop.config(width=22, font=("Arial", 25, 'bold'), background='#F5F5F5', foreground='black')
    drop.grid(row=0, column=0, ipady=10, padx=30, )

    acc = Entry(a_type, width=20, justify='center', fg='#B02A30', bg='white')
    acc.config(font=("Arial", 25, 'bold'))
    acc.grid(row=0, column=1, padx=20, pady=10, ipady=10, ipadx=23)

    # on how to enter value in a entry box of account type
    def sel():
        if len(acc.get()) == 0:
            acc.insert(0, clicked.get())
        else:
            acc.delete(0, END)
            acc.insert(0, clicked.get())

    # select button
    sel = Button(a_type, text="Select", command=sel, fg='#B02A30', bg='white')
    sel.config(font=("Arial", 35, 'bold'))
    sel.grid(row=1, column=1, columnspan=1, pady=15, padx=25, ipadx=60, ipady=6)

    # --------------------------------------Initial balance : Entry and Label widget----------------------

    global initial_balance

    initial_balance_label = Label(ca, text='Initial Balance(₹) : ', fg='black', bg='#F99D27')
    initial_balance_label.config(font=("Arial", 29, 'bold'))
    initial_balance_label.grid(row=3, column=0, padx=2)

    initial_balance = Entry(ca, width=12, justify='center', fg='#B02A30', bg='white')
    initial_balance.config(font=("Arial", 20, 'bold'))
    initial_balance.grid(row=3, column=1, padx=3, ipady=10, ipadx=40)

    # --------------------------------------Submit Button--------------------------------------

    submit_btn = Button(ca, text="Submit", command=submit_ca, fg='#B02A30', bg='white')
    submit_btn.config(font=("Arial", 35, 'bold'))
    submit_btn.grid(row=4, column=0, columnspan=2, pady=15, padx=25, ipadx=80, ipady=6)

    ####################################################################################################

    # Committing Changes to the databaase
    bank_db.commit()

    # closing connection with the database
    bank_db.close()

    # running the continous tkinter (pop-up) loop for ca window
    ca.mainloop()


def submit_ca():
    # creating a database or connecting to an existing one
    bank_db = sqlite3.connect('bank_database.db')

    # create cursor
    b = bank_db.cursor()

    # Insert Into Table
    b.execute(
        "INSERT INTO details VALUES (:f_name, :l_name, :address, :city, :state, :zipcode,:Account_Type,:Account_balance)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get(),
            'Account_Type': acc.get(),
            'Account_balance': initial_balance.get()
        })

    # Commit Changes : anytime we make a change, we want to commit it
    bank_db.commit()

    # close connection
    bank_db.close()

    # Clear Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    initial_balance.delete(0, END)

    global Additional
    Additional = Tk()
    Additional['background'] = '#F99D27'
    Additional.geometry("400x120")
    Additional.title("SELECT AN OPTION")

    # exiting popup of asking to continue and then exiting crearting account portal
    def exit_ca():
        Additional.destroy()
        ca.destroy()

    # function created for the process of destroying additional popup window for avoiding paranthesis bug
    def destroy():
        Additional.destroy()

    another_btn = Button(Additional, text="CREATE another account", command=destroy, fg='#107C10', bg='white')
    another_btn.config(font=("Arial", 16, 'bold'))
    another_btn.grid(row=1, column=0, pady=10, padx=25, ipadx=60, ipady=6)

    exit_btn = Button(Additional, text="EXIT account creation portal", command=exit_ca, fg='#E13102', bg='white')
    exit_btn.config(font=("Arial", 16, 'bold'))
    exit_btn.grid(row=2, column=0, pady=5, padx=25, ipadx=50, ipady=6)

    Additional.mainloop()


"""
----------------------------
|Display all records Button|
----------------------------
"""



def display():
    all_records = Tk()
    all_records.title("RECORDS")
    all_records['background'] = '#F99D27'
    all_records.geometry('390x210')

    # creating a database or connecting to an existing one
    bank_db = sqlite3.connect('bank_database.db')

    # create cursor
    b = bank_db.cursor()

    # --------------------------------- Querying the database ---------------------------------------------

    # sql3lite specifc syntax : oid, selects the primary key
    # reasoning : if there are 20 ppl with the name john, then each one needs to be given its unique importance
    b.execute("SELECT *,oid FROM details")
    # for fetching all records present in the bank_database.db
    records = b.fetchall()

    # creating a scrollbar widget int the master all_records
    records_scroll_bar = Scrollbar(all_records)
    # placing the scrollbar widget on the right. , fill =Y represents filling only vertically (on y axis)
    records_scroll_bar.pack(side=RIGHT, fill=Y)

    '''

    - creating a widget (displayable) which can be used to store all the items that will be scrolled through.
    - yscrollcommand is for designating which scrollbar will the list be present in and in which orientaion the 
       list must be scrolled.

    '''
    # Listbox widget is used to display various
    records_list = Listbox(all_records, yscrollcommand=records_scroll_bar.set, bg='#F99D27', fg='black', width=50)

    # ________________________looping through results for count________________________

    # in mysql a tupple is created for each row entry, with all column values becoming elements.
    # tuple for each entry = (f_name, l_name, address, city, state, zipcode, Account_Type, Account_balance, oid)

    # record[0] is the 1st element of each automatic tuple created, which is the first name of the account holder
    # record[1] is the 2nd element of each automatic tuple created, which is the second name of the account holder
    # record[8] is the 9th element aka oid in this situation.

    for record in records:
        records_list.insert(END, "[ID :" + str(record[8]) + "]  " + str(record[0]) + " " + str(record[1]))

    # ________________________ inserting or customising the listbox on the all_records window_______

    # inserting the record_list in the window, fill indicates the area to cover, in this case x and y
    records_list.config(font=("Arial", 25, 'bold'))
    records_list.pack(side=LEFT, fill=BOTH)

    # for viewing the lisbox widget in tandom with the scroll bar
    records_scroll_bar.config(command=records_list.yview)

    # Committing Changes to the databaase
    bank_db.commit()

    # closing connection with the database
    bank_db.close()

    # running the continous tkinter (pop-up) loop for all_records window
    all_records.mainloop()


"""
-----------------------
|Deposit Money Button|
-----------------------
"""

"""
created by Shreyansh Padarha
"""


def deposit_confirmed():
    # creating a database or connecting to an existing one
    global new_balance
    bank_db = sqlite3.connect('bank_database.db')

    # create cursor
    b = bank_db.cursor()

    record_id = select_box_entry.get()  # the box beside ENTER ID NO.

    b.execute("SELECT * FROM details WHERE oid=" + record_id)
    records = b.fetchall()

    # looping through deta
    for record in records:
        new_balance = int(record[7]) + int(amt_dpd.get())

    b.execute("""UPDATE details SET
            Account_balance = :new_account_balance
            WHERE oid = :oid """,
              {'new_account_balance': new_balance,
               'oid': record_id
               })
    # Committing Changes to the databaase
    bank_db.commit()

    # closing connection with the database
    bank_db.close()

    # instantizing Tk() under the object name deposit_window
    deposit_window = Tk()
    # Title for window
    deposit_window.title("AMOUNT DEPOSITED")
    # saffron orange background colour for the depost_window popup
    deposit_window['background'] = '#F99D27'

    # variables which are created for storing the string values for labels to be displayed
    confirmation = "₹" + str(amt_dpd.get()) + " has been deposited."
    net_blnc = "Net balance :   " + "₹" + str(new_balance)

    # Label widgets to display the amount deposited and net balance
    confirmation_label = Label(deposit_window, text=confirmation, fg='black', bg='#F99D27')
    confirmation_label.config(font=("Arial", 30, 'bold'))
    confirmation_label.grid(row=0, column=0, columnspan=2, )

    netbalance_label = Label(deposit_window, text=net_blnc, fg='black', bg='#F99D27')
    netbalance_label.config(font=("Arial", 30, 'bold'))
    netbalance_label.grid(row=1, column=0, columnspan=2, )

    def destroy_deposits():
        deposit_window.destroy()
        deposited.destroy()

    # ================== button to exit deposit_window with destroy method of tkinter ============
    leave_btn_dp = Button(deposit_window, text="EXIT", command=destroy_deposits, fg='#B02A30', bg='white')
    leave_btn_dp.config(font=("Arial", 30, 'bold'))
    leave_btn_dp.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=80, ipady=7)

    # running the continous tkinter (pop-up) loop for deposit_window window
    deposit_window.mainloop()


"""
created by Shreyansh Padarha
"""


def deposit():
    # creating a database or connecting to an existing one
    bank_db = sqlite3.connect('bank_database.db')

    # create cursor
    b = bank_db.cursor()

    global deposited
    deposited = Tk()
    deposited.title("DEPOSIT AMOUNT")
    deposited.geometry('600x150')
    deposited['background'] = '#F99D27'

    global amt_dpd

    amt_dpd_label = Label(deposited, text='Amount to be deposited(₹) : ', fg='black', bg='#F99D27')
    amt_dpd_label.config(font=("Arial", 25, 'bold'))
    amt_dpd_label.grid(row=0, column=0, padx=2)

    amt_dpd = Entry(deposited, width=12, justify='center', fg='#B02A30', bg='white')
    amt_dpd.config(font=("Arial", 20, 'bold'))
    amt_dpd.grid(row=0, column=1, padx=3, pady=7, ipady=10, ipadx=40)

    confirm = Button(deposited, text='DEPOSIT', command=deposit_confirmed, fg='#005B75', bg='white')
    confirm.config(font=("Arial", 24, 'bold'))
    confirm.grid(row=1, column=0, columnspan=2, padx=3, pady=6, ipady=13, ipadx=90)

    # running the continous tkinter (pop-up) loop for deposited window
    deposited.mainloop()

    # Committing Changes to the databaase
    bank_db.commit()

    # closing connection with the database
    bank_db.close()


"""
-----------------------
|Withdraw Money Button|
-----------------------
"""

"""
created by Shreyansh Padarha
"""


def withdraw_confirmed():
    # creating a database or connecting to an existing one
    global new__balance
    bank_db = sqlite3.connect('bank_database.db')

    # create cursor
    b = bank_db.cursor()

    record_id = select_box_entry.get()  # the box beside ENTER ID NO.

    b.execute("SELECT * FROM details WHERE oid=" + record_id)
    records = b.fetchall()

    # looping through deta
    for record in records:
        new__balance = int(record[7]) - int(amt_wdw.get())

    b.execute("""UPDATE details SET
            Account_balance = :new_account_balance
            WHERE oid = :oid """,
              {'new_account_balance': new__balance,
               'oid': record_id
               })

    # Committing Changes to the databaase
    bank_db.commit()

    # closing connection with the database
    bank_db.close()

    # instantizing Tk() under the object name withdraw_window
    withdraw_window = Tk()
    # Title for window
    withdraw_window.title("AMOUNT WITHDRAWN")
    # saffron orange background colour for the withdraw_window popup
    withdraw_window['background'] = '#F99D27'

    # variables which are created for storing the string values for labels to be displayed
    confirmation_wd = "₹" + str(amt_wdw.get()) + " has been withdrawn."
    net__blnc = "Net balance :   " + "₹" + str(new__balance)

    # Label widgets to display the amount withdrawn and net balance
    confirmation__label = Label(withdraw_window, text=confirmation_wd, fg='black', bg='#F99D27')
    confirmation__label.config(font=("Arial", 30, 'bold'))
    confirmation__label.grid(row=0, column=0, columnspan=2, )

    netbalance__label = Label(withdraw_window, text=net__blnc, fg='black', bg='#F99D27')
    netbalance__label.config(font=("Arial", 30, 'bold'))
    netbalance__label.grid(row=1, column=0, columnspan=2, )

    def destroy__withdraw():
        withdraw_window.destroy()
        withdrawn.destroy()

    # ================== button to exit deposit_window with destroy method of tkinter ============
    leave__btn_dp = Button(withdraw_window, text="EXIT", command=destroy__withdraw, fg='#B02A30', bg='white')
    leave__btn_dp.config(font=("Arial", 30, 'bold'))
    leave__btn_dp.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=80, ipady=7)

    # running the continous tkinter (pop-up) loop for withdraw_window window
    withdraw_window.mainloop()


"""
created by Shreyansh Padarha
"""


def withdraw():
    # creating a database or connecting to an existing one
    bank_db = sqlite3.connect('bank_database.db')

    # create cursor
    b = bank_db.cursor()

    global withdrawn
    withdrawn = Tk()
    withdrawn.title("WITHDRAW AMOUNT")
    withdrawn.geometry('600x150')
    withdrawn['background'] = '#F99D27'

    global amt_wdw

    amt_wdw_label = Label(withdrawn, text='Amount to be withdrawn(₹) : ', fg='black', bg='#F99D27')
    amt_wdw_label.config(font=("Arial", 25, 'bold'))
    amt_wdw_label.grid(row=0, column=0, padx=2)

    amt_wdw = Entry(withdrawn, width=12, justify='center', fg='#B02A30', bg='white')
    amt_wdw.config(font=("Arial", 20, 'bold'))
    amt_wdw.grid(row=0, column=1, padx=3, pady=7, ipady=10, ipadx=40)

    confirmation = Button(withdrawn, text='WITHDRAW', command=withdraw_confirmed, fg='#005B75', bg='white')
    confirmation.config(font=("Arial", 24, 'bold'))
    confirmation.grid(row=1, column=0, columnspan=2, padx=3, pady=6, ipady=13, ipadx=90)

    # running the continous tkinter (pop-up) loop for withdrawn window
    withdrawn.mainloop()

    # Committing Changes to the databaase
    bank_db.commit()

    # closing connection with the database
    bank_db.close()


"""
------------------------------
|Edit Personal Details Button|
------------------------------
"""

"""
created by Shreyansh Padarha
"""


# creating an edit function to update a record
def edit_box():
    global editor
    editor = Tk()
    editor.title("UPDATE/EDIT ACCOUNT DETIALS")
    editor.geometry('690x550')
    editor['background'] = '#F99D27'

    # ---------------------------------------------------------------------------------------------------
    # creating a database or connecting to an existing one
    bank_db = sqlite3.connect('bank_database.db')

    # create cursor
    b = bank_db.cursor()

    record_id = select_box_entry.get()  # the box beside ENTER ID NO.

    # Query the database
    # sql3lite specifc syntax : oid, selects the primary key
    b.execute("SELECT * FROM details WHERE oid=" + record_id)

    # for fetching all records present in the database
    records = b.fetchall()

    # Create global variables for text box names
    global f_name_editorr
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    global acc_type_editor
    global acc_bnc_editor

    # ------------------------------------creating entry widgets------------------------------------

    f_name_editor = Entry(editor, width=20, justify='center', fg='#B02A30', bg='white')
    f_name_editor.config(font=("Arial", 25, 'bold'))
    f_name_editor.grid(row=0, column=1, padx=20, pady=7)

    l_name_editor = Entry(editor, width=20, justify='center', fg='#B02A30', bg='white')
    l_name_editor.config(font=("Arial", 25, 'bold'))
    l_name_editor.grid(row=1, column=1, padx=20, pady=7)

    address_editor = Entry(editor, width=20, justify='center', fg='#B02A30', bg='white')
    address_editor.config(font=("Arial", 25, 'bold'))
    address_editor.grid(row=2, column=1, padx=20, pady=7)

    city_editor = Entry(editor, width=20, justify='center', fg='#B02A30', bg='white')
    city_editor.config(font=("Arial", 25, 'bold'))
    city_editor.grid(row=3, column=1, padx=20, pady=7)

    state_editor = Entry(editor, width=20, justify='center', fg='#B02A30', bg='white')
    state_editor.config(font=("Arial", 25, 'bold'))
    state_editor.grid(row=4, column=1, padx=20, pady=7)

    zipcode_editor = Entry(editor, width=20, justify='center', fg='#B02A30', bg='white')
    zipcode_editor.config(font=("Arial", 25, 'bold'))
    zipcode_editor.grid(row=5, column=1, padx=20, pady=7)

    account_type = Entry(editor, justify='center', width=12, fg='#B02A30', bg='white')
    account_type.config(font=("Arial", 25, 'bold'))
    account_type.grid(row=6, column=1, padx=20, pady=10, ipadx=100)

    current_balance = Entry(editor, justify='center', width=12, fg='#B02A30', bg='white')
    current_balance.config(font=("Arial", 25, 'bold'))
    current_balance.grid(row=7, column=1, padx=20, pady=10)

    # ------------------------------------creating label widgets------------------------------------

    f_name_label = Label(editor, text='First Name', fg='black', bg='#F99D27')
    f_name_label.config(font=("Arial", 25, 'bold'))
    f_name_label.grid(row=0, column=0, pady=10)

    l_name_label = Label(editor, text='Last Name', fg='black', bg='#F99D27')
    l_name_label.config(font=("Arial", 25, 'bold'))
    l_name_label.grid(row=1, column=0, pady=7)

    address_label = Label(editor, text='Address', fg='black', bg='#F99D27')
    address_label.config(font=("Arial", 25, 'bold'))
    address_label.grid(row=2, column=0, pady=7)

    city_label = Label(editor, text='City', fg='black', bg='#F99D27')
    city_label.config(font=("Arial", 25, 'bold'))
    city_label.grid(row=3, column=0, pady=7)

    state_label = Label(editor, text='State', fg='black', bg='#F99D27')
    state_label.config(font=("Arial", 25, 'bold'))
    state_label.grid(row=4, column=0, pady=7)

    zipcode_label = Label(editor, text='Zipcode', fg='black', bg='#F99D27')
    zipcode_label.config(font=("Arial", 25, 'bold'))
    zipcode_label.grid(row=5, column=0, pady=7)

    account_type_label = Label(editor, text='Account Type : ', fg='black', bg='#F99D27')
    account_type_label.config(font=("Arial", 25, 'bold'))
    account_type_label.grid(row=6, column=0, padx=10, pady=7, ipadx=20)

    current_balance_label = Label(editor, text='Current Balance(₹) : ', fg='black', bg='#F99D27')
    current_balance_label.config(font=("Arial", 25, 'bold'))
    current_balance_label.grid(row=7, column=0, padx=10, pady=7)

    # looping through results, and inserting values of existing records
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
        account_type.insert(0, record[6])
        current_balance.insert(0, record[7])

        # for disabling the entry widgets as account type and balance shouldn't be mamipulated
        account_type.configure(state=tk.DISABLED)
        current_balance.configure(state=tk.DISABLED)

    # ------------------------------------Create a Save button, to save edited record---------------------------------

    save_btn = Button(editor, text="Save Record", command=edit_deets, fg='#B02A30', bg='white')
    save_btn.config(font=("Arial", 35, 'bold'))
    save_btn.grid(row=8, column=0, columnspan=2, pady=15, padx=25, ipadx=80, ipady=6)


"""
created by Shreyansh Padarha
"""


def edit_deets():
    # creating a database or connecting to an existing one
    bank_db = sqlite3.connect('bank_database.db')

    # create cursor
    b = bank_db.cursor()

    record_id = select_box_entry.get()  # the box beside ENTER ID NO.

    b.execute("""UPDATE details SET  
        first_name= :first,
        last_name = :last,
        address = :address,
        city = :city, 
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid """,

              {'first': f_name_editor.get(),
               'last': l_name_editor.get(),
               'address': address_editor.get(),
               'city': city_editor.get(),
               'state': state_editor.get(),
               'zipcode': zipcode_editor.get(),
               'oid': record_id
               })

    # Committing Changes to the databaase
    bank_db.commit()

    # closing connection with the database
    bank_db.close()


"""
-------------------------------
|Display Account Details Button|
-------------------------------
"""

"""
created by Shreyansh Padarha
"""


def display_acc_deets():
    disp = Tk()
    disp.title("ACCOUNT DETIALS")
    disp.geometry('780x460')
    disp['background'] = '#F99D27'

    # creating a database or connecting to an existing one
    bank_db = sqlite3.connect('bank_database.db')

    # create cursor
    b = bank_db.cursor()

    record_id = select_box_entry.get()  # the box beside ENTER ID NO.

    b.execute("SELECT * FROM details WHERE oid=" + record_id)

    # for fetching all records present in the database
    records = b.fetchall()

    # looping through all tuples within the sqllite db and selecting each tuple and fetching information within
    global first_name, last_name, address, city, zipcode, account_type, account_balance, state
    for each_record in records:
        first_name = str(each_record[0])
        last_name = str(each_record[1])
        address = str(each_record[2])
        city = str(each_record[3])
        state = str(each_record[4])
        zipcode = str(each_record[5])
        account_type = str(each_record[6])
        account_balance = str(each_record[7])

    # -----------------------creating label widgets for data classification/tyype----------------------------

    f_name_label = Label(disp, text='First Name', fg='black', bg='#F99D27')
    f_name_label.config(font=("Arial", 25, 'bold'))
    f_name_label.grid(row=0, column=0, pady=10)

    l_name_label = Label(disp, text='Last Name', fg='black', bg='#F99D27')
    l_name_label.config(font=("Arial", 25, 'bold'))
    l_name_label.grid(row=1, column=0, pady=7)

    address_label = Label(disp, text='Address', fg='black', bg='#F99D27')
    address_label.config(font=("Arial", 25, 'bold'))
    address_label.grid(row=2, column=0, pady=7)

    city_label = Label(disp, text='City', fg='black', bg='#F99D27')
    city_label.config(font=("Arial", 25, 'bold'))
    city_label.grid(row=3, column=0, pady=7)

    state_label = Label(disp, text='State', fg='black', bg='#F99D27')
    state_label.config(font=("Arial", 25, 'bold'))
    state_label.grid(row=4, column=0, pady=7)

    zipcode_label = Label(disp, text='Zipcode', fg='black', bg='#F99D27')
    zipcode_label.config(font=("Arial", 25, 'bold'))
    zipcode_label.grid(row=5, column=0, pady=7)

    account_type_label = Label(disp, text='Account Type : ', fg='black', bg='#F99D27')
    account_type_label.config(font=("Arial", 25, 'bold'))
    account_type_label.grid(row=6, column=0, padx=10, pady=7, ipadx=70)

    current_balance_label = Label(disp, text='Current Balance(₹) : ', fg='black', bg='#F99D27')
    current_balance_label.config(font=("Arial", 25, 'bold'))
    current_balance_label.grid(row=7, column=0, padx=10, pady=7)

    # -----------------------creating label widgets for data entry for particular accounts----------------------

    f_name_editor = Label(disp, width=20, text=first_name, fg='#B02A30', bg='white')
    f_name_editor.config(font=("Arial", 25, 'bold'))
    f_name_editor.grid(row=0, column=1, padx=20, pady=7)

    l_name_editor = Label(disp, width=20, text=last_name, fg='#B02A30', bg='white')
    l_name_editor.config(font=("Arial", 25, 'bold'))
    l_name_editor.grid(row=1, column=1, padx=20, pady=7)

    address_editor = Label(disp, width=20, text=address, fg='#B02A30', bg='white')
    address_editor.config(font=("Arial", 25, 'bold'))
    address_editor.grid(row=2, column=1, padx=20, pady=7)

    city_editor = Label(disp, width=20, text=city, fg='#B02A30', bg='white')
    city_editor.config(font=("Arial", 25, 'bold'))
    city_editor.grid(row=3, column=1, padx=20, pady=7)

    state_editor = Label(disp, width=20, text=state, fg='#B02A30', bg='white')
    state_editor.config(font=("Arial", 25, 'bold'))
    state_editor.grid(row=4, column=1, padx=20, pady=7)

    zipcode_editor = Label(disp, width=20, text=zipcode, fg='#B02A30', bg='white')
    zipcode_editor.config(font=("Arial", 25, 'bold'))
    zipcode_editor.grid(row=5, column=1, padx=20, pady=7)

    account_type = Label(disp, text=account_type, width=12, fg='#B02A30', bg='white')
    account_type.config(font=("Arial", 25, 'bold'))
    account_type.grid(row=6, column=1, padx=10, pady=7, ipadx=100)

    current_balance = Label(disp, text=account_balance, width=12, fg='#B02A30', bg='white')
    current_balance.config(font=("Arial", 25, 'bold'))
    current_balance.grid(row=7, column=1, padx=20, pady=7)

    # ok button which will destroy d_popup and return to bank window.
    exit_btn = Button(disp, text="EXIT", command=disp.destroy, fg='#005B75', bg='white')
    exit_btn.config(font=("Arial", 25, 'bold'))
    exit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=110, ipadx=30, ipady=4)

    # Committing Changes to the databaase
    bank_db.commit()

    # closing connection with the database
    bank_db.close()


"""
-----------------------
|Delete Account Button|
-----------------------
"""

"""
created by Shreyansh Padarha
"""


def delete_click():
    # creating a database or connecting to an existing one
    bank_db = sqlite3.connect('bank_database.db')

    # create cursor
    b = bank_db.cursor()

    b.execute("DELETE FROM details WHERE oid=" + select_box_entry.get())

    # function created for the process of destroying d_popup window for avoiding paranthesis bug
    def destroy():
        d_popup.destroy()

    # creating an additional popup to give confirmation to user that the account has been deleted.
    d_popup = Tk()
    d_popup.title("DELETED ACCOUNT CONFIRMATION")
    d_popup['background'] = '#F99D27'
    d_popup.geometry('315x68')

    # label which will show the statement
    confirmation_label = Label(d_popup, text="Account has been deleted.", fg='black', bg='#F99D27')
    confirmation_label.config(font=("Arial", 16, 'bold'))
    confirmation_label.grid(row=0, column=0)

    # ok button which will destroy d_popup and return to bank window.
    ok_btn = Button(d_popup, text="OK", command=destroy, fg='#005B75', bg='white')
    ok_btn.config(font=("Arial", 16, 'bold'))
    ok_btn.grid(row=1, column=0, pady=3, padx=110, ipadx=12, ipady=2)

    # Committing Changes to the databaase
    bank_db.commit()

    # closing connection with the database
    bank_db.close()


"""
------------------
|MAIN DRIVER CODE|
------------------
"""

"""
Created by Shreyansh Padarha
"""

# Importing modules/libraries that will be continously used within the program
from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import tkinter.font as font
import tkinter as tk

# ____________________________________Tkinter : Creating window and adding specifics______________________

# instantizing Tk() under the object name bank
bank = Tk()

# Title for bank window
bank.title("IMOBILE MANAGEMENT SYSTEM")

# Icon to be displayed on top left of window
bank.iconbitmap('ICICI.ico')  # note : jupyter specific glitch : doesnt open file, even after resizing.

# window size being established
bank.geometry(('700x810'))

# ICII has its theme colour as Deep Saffron orange, hex code : #F99D27
bank['background'] = '#F99D27'

# ____________________________________ICICI LOGO : TOP OF WINDOW_____________________________________

# Creating Image variable to be inserted
image = (Image.open("ICICI_Bank_Logo.png"))
# resizing image for accordance with the window [used pillow module for inserting the image]
resize_image = image.resize((670, 100))
img = ImageTk.PhotoImage(resize_image)
# Placing the image according to requirment.
Label(image=img, bg='#F99D27').grid(row=0, column=0, columnspan=3, pady=15)

# ____________________________________MYSQL DATABASE RELATED ESTABLISHMENTS______________________________

# creating or establishing connection to an existing database
bank_db = sqlite3.connect('bank_database.db')

# create cursor : for operating and controling items and commands inside mysql database
b = bank_db.cursor()

# ________________________________ CREATING TABLE INSIDE DB TO STORE DETAILS____________________________

# COMMENTED OUT AS TABLE HAS ALREADY BEEN CREATED IN TEST RUNS AND DEBUGGING RUNS

'''
b.execute("""CREATE TABLE details (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer,
        Account_Type text,
        Account_balance integer
        )""")

'''

# __________________defining style/ font with which the widgets(labels) are depicted____________

Calcis_Font = font.Font(size=15, weight='bold')
Create_Account_Font = font.Font(size=25, weight='bold')

# ________________________________________________TOOLS FRAME_____________________________________________

# create a frame widget inside which all the calculators will be inserted
tools = LabelFrame(bank, text='TOOLS', bg='#B02A30')
tools['font'] = Calcis_Font
tools.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

# calculator button
calc_btn = Button(tools, text="Calculator", command=calculator, fg='#005B75', bg='white')
calc_btn['font'] = Calcis_Font
calc_btn.grid(row=1, column=0, padx=10, pady=10, ipady=15)

# simple interest button
SI_btn = Button(tools, text="Simple Interest Calculator", command=Simple_Interest, fg='#005B75', bg='white')
SI_btn['font'] = Calcis_Font
SI_btn.grid(row=1, column=1, padx=10, pady=10, ipady=15)

# compound interest button
CI_btn = Button(tools, text="Compound Interest Calculator", command=Compound_Interest, fg='#005B75', bg='white')
CI_btn['font'] = Calcis_Font
CI_btn.grid(row=1, column=2, padx=10, pady=10, ipady=15)

# __________________________________BUTTONS WHICH DONT REQUIRE INPUTS (IDS)_________________________________

# Create Account Button
create_btn = Button(bank, text="Create Account", command=Create_ACC, fg='#B02A30', bg='white')
create_btn['font'] = Create_Account_Font
create_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=186, ipady=15)

# Display All Records Button : Displaying all bank acount names and respective IDS
all_deets_btn = Button(bank, text="Display All Records", command=display, fg='#B02A30', bg='white')
all_deets_btn['font'] = Create_Account_Font
all_deets_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=25, ipadx=165, ipady=15)

# __________________________________SELECTING OR INPUTTNG ID__________________________________

# ENTER ID NO. LABEL : to show where to enter ID
select_box_label = Label(bank, text="ENTER ID NO.", fg='black', bg='#F99D27')
select_box_label['font'] = Create_Account_Font
select_box_label.grid(row=5, column=0)

# Entry box widget to enter ID No. for further applicaton
select_box_entry = Entry(bank, width=5, justify='center', fg='#B02A30', bg='white')
select_box_entry['font'] = Create_Account_Font
select_box_entry.grid(row=5, column=1, ipady=9)

# ____________________________Creating buttons which require ID INPUTS___________________________________________

# Deposit Money Button
deposit_btn = Button(bank, text="Deposit Money", command=deposit, fg='#B02A30', bg='white')
deposit_btn['font'] = Create_Account_Font
deposit_btn.grid(row=6, column=0, padx=1, pady=10, ipadx=61, ipady=15)

# Withdraw Money Button
withdraw_btn = Button(bank, text="Withdraw Money", command=withdraw, fg='#B02A30', bg='white')
withdraw_btn['font'] = Create_Account_Font
withdraw_btn.grid(row=6, column=1, padx=1, pady=10, ipadx=40, ipady=15)

# Display Acount Details Button
display_btn = Button(bank, text="Display Acount Details", command=display_acc_deets, fg='#B02A30', bg='white')
display_btn['font'] = Create_Account_Font
display_btn.grid(row=7, column=0, padx=10, pady=10, ipadx=20, ipady=15)

# Edit Personal Details Button
edit_btn = Button(bank, text="Edit Personal Details", command=edit_box, fg='#B02A30', bg='white')
edit_btn['font'] = Create_Account_Font
edit_btn.grid(row=7, column=1, padx=10, pady=10, ipadx=20, ipady=15)

# Delete Account Button
delete_btn = Button(bank, text="Delete Account", command=delete_click, fg='#B02A30', bg='white')
delete_btn['font'] = Create_Account_Font
delete_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=25, ipadx=186, ipady=15)

creatorLabel = Label(bank, text="Created by Shreyansh Padarha", fg='black', bg='#F99D27')
creatorLabel['font'] = font.Font(size=16, weight='bold')
creatorLabel.grid(row=9, column=0, columnspan=2, sticky='e', ipady='10')

# ____________________________Finishing Formalities___________________________________________


# Committing Changes to the databaase
bank_db.commit()

# closing connection with the database
bank_db.close()

# running the continous tkinter (pop-up) loop for bank window
bank.mainloop()
