"""This program is designed for the checking the pollution emission of a Car.
The user finds the different fields where car information is stored.
A logic is defined, which takes the levels of pollution from the user and checks it and
automatically informs the user about the range of their car's pollution and lets them know
if the levels are good or hazardous to the environment.
This program can be used to identify pollution levels and help in taking necessary prevention steps
to avoid any further pollution caused.

Authors: Karishma Thumu         (00097811)
         Arun Sai Thirunaharoju (00096794)

Email id: karishma.thumu@stud.th-deg.de
          arun.thirunaharoju@stud.th-deg.de
"""

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

"""creating the main window, 
where the user finds different options that asks for the information about the car
and user has to fill in that data in order to find the level of pollution his car is emitting.
 """
window = Tk()
window.title("Car Pollution Check")  # setting the title for the window
window.geometry('750x500')  # defining the window size
cars = ["Audi", "BMW", "Mercedes-Benz", "Volkswagen"]  # defining a list for the car brands

""" adding a label to the window by
creating a label using label class and
also using font parameter for font type and font size.
setting the position of the label on the window using grid function
Spacing to added to controls to make it looks well organized using padx and pady properties. 
"""
lbl = Label(window, text="Enter Car Information", font=("Times new roman Bold", 20))
lbl.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# creating label to save owner name
lbl1 = Label(window, text="Owner Name", font=("Times new roman", 11))
lbl1.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# taking the user input using entry class by creating a text box
txt1 = Entry(window, width=15)
txt1.grid(row=1, column=1, sticky=W)  # adding it to the window by specifying the location of the entry
txt1.focus()

# Creating the label for registration number of a car and taking the input from the user using entry class
lbl2 = Label(window, text="Vehicle Registration Number", font=("Times new roman", 11))
lbl2.grid(row=2, column=0, sticky=W, padx=5, pady=5)
txt2 = Entry(window, width=15)
txt2.grid(row=2, column=1, sticky=W)
txt2.focus()

"""creating a label for the car class,
where with the help of combo class, 
the user can choose the class he owns from the given options,
if not he can select 'others'.
 """
lbl3 = Label(window, text="Class of the Car", font=("Times new roman", 11))
lbl3.grid(row=3, column=0, sticky=W, padx=5, pady=5)
combo3 = Combobox(window)
combo3['values'] = ("B", "B1", "C1", "D1", "Others")
combo3.current()
combo3.grid(row=3, column=1, sticky=W)
combo3['width'] = 7

"""creating a label for the Brand of the Car,
where the 'cars' list created for the car brand is used to give
the user options to choose by using combo class. """
lbl4 = Label(window, text="Brand Name", font=("Times new roman", 11))
lbl4.grid(row=4, column=0, sticky=W, padx=5, pady=5)
combo4 = Combobox(window)
combo4['values'] = cars
combo4.current()
combo4.grid(row=4, column=1, sticky=W)
combo4['width'] = 15

# creating a label for saving the model of the car with entry
lbl5 = Label(window, text="Model Name", font=("Times new roman", 11))
lbl5.grid(row=5, column=0, sticky=W, padx=5, pady=5)
txt5 = Entry(window, width=15)
txt5.grid(row=5, column=1, sticky=W)
txt5.focus()

"""creating a label with radiobuttons,
to input the fuel type which the car runs on, 
with 'Radiobutton' class where the user can select his car fuel, either Benzin or Diesel. """
lbl6 = Label(window, text="Engine Type", font=("Times new roman", 11))
lbl6.grid(row=6, column=0, sticky=W, padx=5, pady=5)
var_1 = StringVar()
rad1 = Radiobutton(window, text="Benzin", value="Benzin", variable=var_1)
rad2 = Radiobutton(window, text="Diesel", value="Diesel", variable=var_1)
rad1.grid(column=1, row=6, sticky=W)
rad2.grid(column=2, row=6, sticky=W)

"""creating a label for the car purchase year using a spinbox class.
The spin box field is set to range over 40 years from 1980 till 2020.
A default value is set to the spinbox.
"""
lbl7 = Label(window, text="Year of Purchase", font=("Times new roman", 11))
lbl7.grid(row=7, column=0, sticky=W, padx=5, pady=5)
var_2 = StringVar()
var_2.set(1995)
spin7 = Spinbox(window, from_=1980, to=2020, width=8, textvariable=var_2)
spin7.grid(row=7, column=1, sticky=W)

# Creating the label with radiobuttons, where the emission ranges are selected
lbl8 = Label(window, text="Emission Levels (in percentage)", font=("Times new roman", 11))
lbl8.grid(row=8, column=0, sticky=W, padx=5, pady=5)
var_3 = StringVar()
rad3 = Radiobutton(window, text="0-25", value="0-25", variable=var_3)
rad4 = Radiobutton(window, text="26-75", value="26-75", variable=var_3)
rad5 = Radiobutton(window, text="above 75", value="above 75", variable=var_3)
rad3.grid(row=8, column=1, sticky=W)
rad4.grid(row=8, column=2, sticky=W)
rad5.grid(row=8, column=3, sticky=W)

# adding an additional entry field to the label "Brand Name"
txt9 = Entry(window, width=15)
txt9.grid(row=4, column=2, sticky=W, padx=4, pady=4)

"""defining a function for adding a new brand
to the combo set of values for the label 'Brand Name,
which is not in the list of values that have been defined. 
"""


def brand():
    cars.append(txt9.get())
    global combo4
    combo4["values"] = cars
    combo4.current(4)
    combo4.grid(column=1, row=4, sticky=W)
    messagebox.showinfo("Success", "Your car brand has been added !")  # shows a messagebox when the user adds the brand


# Button to add car brand
btn_2 = Button(window, text="Add Car Brand", command=brand)
btn_2.grid(row=4, column=3, sticky=W)

"""
Defining a function to be executed when Submit button is clicked.
The fields with the data is displayed on the console.
 """


def terminal():
    messagebox.showinfo("Message title", "Data Saved")  # a box pops up showing that the given data is saved
    print("Name:    " + txt1.get())  # take the user entry text using get function
    print("Vehicle Number:  " + txt2.get())
    print("Class:   " + combo3.get())
    print("Brand:   " + combo4.get())
    print("Model:   " + txt5.get())
    print("Fuel:    " + var_1.get())
    print("Purchase Year:   " + var_2.get())
    print("Pollution range: " + var_3.get())

    """
    Creating a second window 
    where the entire car information given is displayed 
    along with the Pollution level message.
    """
    display = Tk()
    display.title("Car Emission Details")
    display.geometry('600x400')
    label_1 = Label(display, text="Emission Details", font=("Times new roman", 11))
    label_1.grid(row=0, column=0, sticky=W, padx=5, pady=5)
    label_1 = Label(display, text="Name:" + txt1.get(), font=("Times new roman", 11))
    label_1.grid(row=1, column=0, sticky=W, padx=5, pady=5)
    label_1 = Label(display, text="Vehicle Number:" + txt2.get(), font=("Times new roman", 11))
    label_1.grid(row=2, column=0, sticky=W, padx=5, pady=5)
    label_1 = Label(display, text="Car Class:" + combo3.get(), font=("Times new roman", 11))
    label_1.grid(row=3, column=0, sticky=W, padx=5, pady=5)
    label_1 = Label(display, text="Brand:" + combo4.get(), font=("Times new roman", 11))
    label_1.grid(row=4, column=0, sticky=W, padx=5, pady=5)
    label_1 = Label(display, text="Model:" + txt5.get(), font=("Times new roman", 11))
    label_1.grid(row=5, column=0, sticky=W, padx=5, pady=5)
    label_1 = Label(display, text="Fuel:" + var_1.get(), font=("Times new roman", 11))
    label_1.grid(row=6, column=0, sticky=W, padx=5, pady=5)
    label_1 = Label(display, text="Year of Purchase:" + var_2.get(), font=("Times new roman", 11))
    label_1.grid(row=7, column=0, sticky=W, padx=5, pady=5)
    label_1 = Label(display, text="Pollution range:" + var_3.get(), font=("Times new roman", 11))
    label_1.grid(row=8, column=0, sticky=W, padx=5, pady=5)

    """
    Program for printing the respective messages
    for their corresponding pollution ranges
    depending on the emission levels selected by the user in the main window
    """
    if var_3.get() == "0-25":
        label_1 = Label(display, text="Very Good! Your car has low Emissions. ", font=("Times new roman", 11))
        label_1.grid(row=11, column=0, sticky=W, padx=5, pady=5)
        # print the predefined message on the console for the selected emission range
        print("Very Good! Your car has low Emissions.")
    elif var_3.get() == "26-75":
        label_1 = Label(display, text="Tolerable! Your car has moderate Emissions. ", font=("Times new roman", 11))
        label_1.grid(row=11, column=0, sticky=W, padx=5, pady=5)
        print("Tolerable! Your car has Moderate Emissions.")
    else:
        label_1 = Label(display, text="Beware! Your car has high Emissions. ", font=("Times new roman", 11))
        label_1.grid(row=11, column=0, sticky=W, padx=5, pady=5)
        print("Beware! Your car has High Emissions")


# a blank label to place Submit button in a organised position
lbl = Label(window, text="    ", font=("Times new roman", 11))
lbl.grid(row=9, column=0)

"""
Adding button to display Submit option 
and linking the function defined above
by specifying it
"""
button_3 = Button(window, text="Submit", command=terminal)
button_3.grid(row=10, column=1)

window.mainloop()

