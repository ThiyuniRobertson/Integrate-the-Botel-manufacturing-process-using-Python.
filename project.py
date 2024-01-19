from tkinter import *
from PIL import Image, ImageTk
from tkinter import font

def main():
    # Create the main application window
    window = Tk()
    window.title('CT/2017/051 T.S.Robertson')
    window.geometry('800x600')

    # Load the image
    image_path = "image/back.png"  # Replace with the actual path of your image
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    #
    # # Create a label to display the image as a background
    background_label = Label(window, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    our_font = font.Font(family="Helvetica", size='32')

    frame = LabelFrame(window, text='Topic of Manufacturing', padx=40, pady=20, bg="#ffffff")  # frame content padding
    frame.place(x=50, y=60)  # frame padding

    # -------------------------Heading one-----------------------------------------------------------
    heading1 = Label(frame, text='Botel Manufacturing Process',foreground='#0058db', bg="#ffffff", font = ('Popins',18,'bold'))
    heading1.grid(row=0, column=0, padx=5, pady=5, sticky='w')

    # -------------------------Heading two----------------
    heading2 = Label(frame, text='Design Your Own Bottle.', foreground='#0058db', bg="#ffffff", font = ('Popins',14,'bold'))
    heading2.grid(row=2, column=0, padx=5, pady=20, sticky='w')

    option1 = [
        "Black Colour",
        "Blue Colour",
        "Green Colour",
        "Yellow Colour"
    ]

    option2 = [
        "0.5 Liter",
        "1 Liter",
        "1.5 Liter"
    ]

    option3 = [
        "Kids Drinking Bottle",
        "Sport Drinking Bottel",
        "Healthy Drinking Bottle"
    ]

    option4 = [
        "Standard Screw Cap",
        "Push-Pull Cap",
        "Kid-Friendly Cap",
        "Flip-Flop Cap"
    ]

    option5 = [
        "Fun Graphic",
        "Filter"
    ]

    clicked1 = StringVar()
    clicked1.set(option1[0])

    clicked2 = StringVar()
    clicked2.set(option2[0])

    clicked3 = StringVar()
    clicked3.set(option3[0])

    clicked4 = StringVar()
    clicked4.set(option4[0])

    clicked5 = StringVar()
    clicked5.set(option5[0])

    # ------------------------------Label name & drop down-----------------------------------------
    firstSelection = Label(frame, text='Select your Preferred Bottel Color :',bg="#ffffff").grid(row=3, column=0, sticky='w', padx=50, pady=5)
    firstDrop = OptionMenu(frame, clicked1, *option1)
    firstDrop.grid(row=4, column=0, padx=50, sticky='w')
    firstDrop.config(width=20)

    secondSelection = Label(frame, text='Select your Preferred Bottel Size :',bg="#ffffff").grid(row=3, column=1, sticky='w', padx=5, pady=5)
    secondDrop = OptionMenu(frame, clicked2, *option2)
    secondDrop.grid(row=4, column=1, padx=5, pady=5, sticky='w')
    secondDrop.config(width=20)

    thirdSelection = Label(frame, text='Select your Preferred Bottle Type :',bg="#ffffff").grid(row=5, column=0, sticky='w', padx=50, pady=5)
    thirdDrop = OptionMenu(frame, clicked3, *option3)
    thirdDrop.grid(row=6, column=0, padx=50, sticky='w')
    thirdDrop.config(width=20)

    fourthSelection = Label(frame, text='Select your Preferred type of Bottle Cap :',bg="#ffffff").grid(row=5, column=1, sticky='w', padx=5, pady=5)
    fourthDrop = OptionMenu(frame, clicked4, *option4)
    fourthDrop.grid(row=6, column=1, padx=5, pady=5, sticky='w')
    fourthDrop.config(width=20)

    fifthSelection = Label(frame, text='Select your Preferred other option :',bg="#ffffff").grid(row=7, column=0, sticky='w', padx=50, pady=5)
    fifthDrop = OptionMenu(frame, clicked5, *option5)
    fifthDrop.grid(row=8, column=0, padx=50, sticky='w')
    fifthDrop.config(width=20)
#--------------END MAIN FUNCTION----------------------------------------

#--------------------------------Help Butt-Easy_giud---------------------
    def easy_guid():
        helpPop = Toplevel(window)
        helpPop.title('CT/2017/051 Help Option')
        helpPop.geometry('700x150')

        #--------------------Heading Label---------------------------------
        help_Hlabel = Label(helpPop, text='When you Design your own botel you should considering the following Designing condition', padx=5, pady=10,
                           foreground='Red', font=('Popins',10,'bold')).pack()
        #-------------------Condition Label----------------------------------
        help_label1= Label(helpPop, text="1. If you want to design Kid's type Bottel, you should design with Kid's friendly bottel cap.",padx=5, pady=5,
                            font=('Popins',10), anchor='w').pack()
        help_label2 = Label(helpPop, text="2. If you want to design Healthy Drinking bottel, you should design with filter option.",
                            padx=5, pady=5, anchor='w', font=('Popins', 10)).pack()

    # -------------------Submit Button-----------------------------
    helpBut = Button(frame, text='Need Any Help?', command=easy_guid, pady=1, padx=10, bg='#0058db',
                         foreground='#ffffff', font=('Popins', 10, 'bold')).grid(row=9, column=1, padx=10, pady=25, sticky='w')

#---------------END easy_guid FUNCTION-------------------------------------

#-------------------------WHat happen when click the submitBut--------------
    def condtion():
        pop = Toplevel(window)
        pop.title('CT/2017/051 My pop')
        pop.geometry('600x100')

        bottle_type_input = clicked3.get()
        bottle_cap_input = clicked4.get()
        other_option_input = clicked5.get()

        # ---------------------------System design condition checked------------------------------------------
        if ((bottle_type_input == 'Kids Drinking Bottle') and (bottle_cap_input == 'Kid-Friendly Cap') or
                (bottle_type_input == 'Healthy Drinking Bottle') and (bottle_cap_input == 'Filter')):
            pop_label = Label(pop, text='Submited your design', padx=300, pady=40, bg='#ffffff', foreground='Red', font = ('Popins',12,'bold')).pack()
        else:
            pop_label = Label(pop,text='ERORR', bg='#ff8383', padx=300, pady=5, foreground='#ffffff', font=('Times', 16,'bold')).pack()
            pop_label = Label(pop, text='Your design is not agreed with system conditions. Please re-checked it and try.',
                              bg='#ff8383', padx=300, pady=20, foreground='#ffffff', font = ('Popins',12)).pack()

    # -------------------Submit Button-----------------------------
    submitBut = Button(frame, text='submit your design', command=condtion, pady=1, padx=5, bg='#0058db', foreground='#ffffff', font = ('Popins',14,'bold'))\
        .grid(row=9, column=0, padx=50,pady=25,sticky='w')

#------------------END condtion FUNCTION-------------------------------------
#--------------------Run the Tkinter main loop-------------------------------
    window.mainloop()

if __name__ == "__main__":
    main()
