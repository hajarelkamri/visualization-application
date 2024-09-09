from excel import  check_credentials, save_credentials
import tkinter.messagebox
from tkinter import *
from tkinter import ttk, filedialog, messagebox, simpledialog

from PIL import ImageTk, Image, ImageDraw, ImageFont
from datetime import *
import time
import matplotlib as plt
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
from random import choice
import seaborn as sns
import os
import warnings


df=None
file_name=None
f1= None

class LoginPage(Frame):
    def __init__(self, parent, app):  # Receive parent frame and app reference
        super().__init__(parent)

        self.parent = parent
        self.app=app
        self.bg_frame = Image.open('images//pop.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.parent, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.place(x=0, y=0, relwidth=1, relheight=1)

        self.lgn_frame = Frame(self.parent, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        self.heading = Label(self.lgn_frame, text="Welcome to SciDataViz", font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white', bd=5, relief=FLAT)
        self.heading.place(x=10, y=30, width=500, height=30)

        self.side_image = Image.open('images//2.jpg')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=10, y=100)

        self.sign_in_image = Image.open('images//hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                   font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)

        self.username_icon = Image.open('images//username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('images//btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)

        # Login button (using command=app.switch_to_signup)

        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff', cursor='hand2',
                            activebackground='#3047ff', fg='white',command=self.log)
        self.login.place(x=20, y=10)

        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?",font=("yu gothic ui", 13, "bold underline"),
                                    fg="white", relief=FLAT,activebackground="#040405", borderwidth=0, background="#040405", cursor="hand2")
        self.forgot_button.place(x=630, y=510)

        self.sign_label = Label(self.lgn_frame, text='Register now !', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)

        self.signup_img = ImageTk.PhotoImage(file='images//register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405",command= app.switch_to_signup)
        self.signup_button_label.place(x=670, y=555, width=111, height=35)

        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)

        # ======== Password icon ================
        self.password_icon = Image.open('images//password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage (file='images//show.png')

        self.hide_image = ImageTk.PhotoImage (file='images//hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,activebackground="white" , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

    def log(self):
        global f1
        f1 = self.username_entry.get()
        f2 = self.password_entry.get()
        if check_credentials(f1, f2):
            tkinter.messagebox.showinfo(title="Connected", message="Successfully connected")
            self.app.switch_to_dash1()
        else:
            tkinter.messagebox.showerror(title="Error",
                                         message="The account does not exist or the credentials are incorrect. Please try again.")



class SignupPage(Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.parent = parent

        self.bg_frame = Image.open('images//pop.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.parent, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.place(x=0, y=0, relwidth=1, relheight=1)

        self.sgn_frame = Frame(self.parent, bg='#040405', width=950, height=600)
        self.sgn_frame.place(x=200, y=70)

        self.side_image = Image.open('images//2.jpg')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.sgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=10, y=100)

        self.sign_up_label = Label(self.sgn_frame, text="Sign Up", font=("yu gothic ui", 17, "bold"), bg="#040405",
                                   fg="white")
        self.sign_up_label.place(x=650, y=30)

        self.heading = Label(self.sgn_frame, text="Welcome to SciDataViz", font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white', bd=5, relief=FLAT)
        self.heading.place(x=10, y=30, width=500, height=30)

        self.email_label = Label(self.sgn_frame, text="Email", bg="#040405", fg="#4f4e4d",
                                 font=("yu gothic ui", 13, "bold"))
        self.email_label.place(x=550, y=100)

        self.email_entry = Entry(self.sgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                 font=("yu gothic ui", 12, "bold"), insertbackground='#6b6a69')
        self.email_entry.place(x=580, y=135, width=270)

        self.email_line = Canvas(self.sgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.email_line.place(x=550, y=159)

        self.username_label = Label(self.sgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=180)

        self.username_entry = Entry(self.sgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), insertbackground='#6b6a69')
        self.username_entry.place(x=580, y=215, width=270)

        self.username_line = Canvas(self.sgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=239)

        self.password_label = Label(self.sgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=260)

        self.password_entry = Entry(self.sgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), insertbackground='#6b6a69')
        self.password_entry.place(x=580, y=295, width=244)

        self.password_line = Canvas(self.sgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=319)

        self.confirm_password_label = Label(self.sgn_frame, text="Confirm Password", bg="#040405", fg="#4f4e4d",
                                            font=("yu gothic ui", 13, "bold"))
        self.confirm_password_label.place(x=550, y=340)

        self.confirm_password_entry = Entry(self.sgn_frame, highlightthickness=0, relief=FLAT, bg="#040405",
                                            fg="#6b6a69", font=("yu gothic ui", 12, "bold"), insertbackground='#6b6a69')
        self.confirm_password_entry.place(x=580, y=375, width=244)

        self.confirm_password_line = Canvas(self.sgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.confirm_password_line.place(x=550, y=399)

        self.register_button = Image.open('images//btn1.png')
        photo = ImageTk.PhotoImage(self.register_button)
        self.register_button_label = Label(self.sgn_frame, image=photo, bg='#040405')
        self.register_button_label.image = photo
        self.register_button_label.place(x=550, y=460)

        self.register = Button(self.register_button_label, text='REGISTER', font=("yu gothic ui", 13, "bold"), width=25,
                               bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',
                               command=self.register_user)
        self.register.place(x=20, y=10)

        self.login_button = Button(self.sgn_frame, text="Already have an account? Login", font=("yu gothic ui", 12),
                                   fg="white", bg="#040405", relief=FLAT, activebackground="#040405", cursor="hand2",
                                   command=app.switch_to_login)
        self.login_button.place(x=580, y=530)

    def register_user(self):
        email = self.email_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match. Please try again.")
        else:
            save_credentials(email, username, password)
            messagebox.showinfo("Success", "Registration successful. You can now log in.")

class Dashboard1(Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.parent = parent

        self.configure(bg='#ffffff')

        self.header = Frame(self.parent, bg='#9561D1')
        self.header.place(x=300, y=0, width=1070, height=60)

        self.logout_text = Button(self.header,text="Logout", bg='#7B39C6', font=("", 13, "bold"), bd=0, fg='white',
                                  cursor='hand2', activebackground='#ffffff',command = exit)
        self.logout_text.place(x=950, y=15)

        self.about_title = Label(self.parent, text="About the Application",
                                 font=("Georgia", 25, "bold"), fg='#FABA6E', bg='#7B39C6')
        self.about_title.place(x=320, y=75)

        self.description = Label(self.parent,
                                 text="SciDataViz est une application de visualisation de\n \n données scientifiques conçue pour vous permettre\n \nd'explorer et d'analyser vos ensembles de données \n\nde manière interactive.\n\nQue vous travailliez avec des données climatiques,\n \ngéospatiales, biomédicales ou d'autres types de \n\ndonnées scientifiques, SciDataViz vous offre une \n\ngamme d'outils de visualisation avancés pour vous \n\naider à tirer des insights précieux.",
                                 font=("Helvetica", 12, "bold"), bg='white', fg='orange', wraplength=400,
                                 justify='left')
        self.description.place(x=320, y=150)

        self.sidebar = Frame(self.parent, bg='#7B39C6')
        self.sidebar.place(x=0, y=0, width=300, height=750)

        self.heading = Label(self.parent, text='Dashboard examples', font=("Georgia", 25, "bold"), fg='#FABA6E', bg='#7B39C6')
        self.heading.place(x=900, y=70)

        self.logoImage = ImageTk.PhotoImage(file='images\\hyy.png')
        self.logo = Label(self.sidebar, image=self.logoImage,  bg='#7B39C6')
        self.logo.place(x=70, y=80)

        self.brandName = Label(self.sidebar, text=f"{f1}", bg='#7B39C6', font=("", 15, "bold"), fg="white")
        self.brandName.place(x=109, y=200)

        self.dashboardImage = ImageTk.PhotoImage(file='images\\dashboard-icon.png')
        self.dashboard = Label(self.sidebar, image=self.dashboardImage, bg='#7B39C6')
        self.dashboard.place(x=35, y=402)

        self.dashboard_text = Button(self.sidebar, text="Data visualization", bg='#7B39C6', font=("", 13, "bold"), bd=0,
                                     cursor='hand2', activebackground='#7B39C6', command=app.switch_to_dash2, fg="white")
        self.dashboard_text.place(x=80, y=402)

        self.manageImage = ImageTk.PhotoImage(file='images\\manage-icon.png')
        self.manage = Label(self.sidebar, image=self.manageImage, bg='#7B39C6')
        self.manage.place(x=35, y=287)

        self.manage_text = Button(self.sidebar, text="Upload Csv file", bg='#7B39C6', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff', command=self.upload_file, fg="white")
        self.manage_text.place(x=80,y=287)

        self.settingsImage = ImageTk.PhotoImage(file='images\\settings-icon.png')
        self.settings = Label(self.sidebar, image=self.settingsImage, bg='#7B39C6')
        self.settings.place(x=35, y=345)

        self.settings_text = Button(self.sidebar, text="Cleaning data", bg='#7B39C6', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff', command=self.clean_first, fg="white")
        self.settings_text.place(x=80, y=345)

        self.ExitImage = ImageTk.PhotoImage(file='images\\exit-icon.png')
        self.Exit = Label(self.sidebar, image=self.ExitImage, bg='#7B39C6')
        self.Exit.place(x=25, y=448)

        self.Exit_text = Button(self.sidebar, text="Exit", bg='#7B39C6', font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff', command=exit, fg="white")
        self.Exit_text.place(x=85, y=462)

        self.clock_image = ImageTk.PhotoImage(file="images\\time.png")
        self.date_time_image = Label(self.sidebar, image=self.clock_image, bg='#7B39C6')
        self.date_time_image.place(x=88, y=20)

        self.date_time = Label(self.parent)
        self.date_time.place(x=115, y=15)
        self.show_time()

        self.pImage=ImageTk.PhotoImage(file="images\\pie-graph1.png")
        self.p=Label(self.parent, image=self.pImage,  bg='white',height=230)
        self.p.place(x=925,y=200)
        self.ppImage = ImageTk.PhotoImage(file="images\\graph.png")
        self.pp = Label(self.parent, image=self.ppImage, bg='white',height=250)
        self.pp.place(x=809, y=485)
        self.pppImage = ImageTk.PhotoImage(file="images\\pip2.jpg")
        self.ppp = Label(self.parent, image=self.pppImage, bg='white')
        self.ppp.place(x=345, y=520)


    def clean_first(self):
        messagebox.showerror("ERROR!", "Please, upload file first!")

    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=("", 13, "bold"), bd=0, bg="#7B39C6", fg="white")
        self.date_time.after(100, self.show_time)

    def upload_file(self):
        global file_name
        file_name = filedialog.askopenfilename(title="Open A File", filetypes=(("CSV files", ".csv"), ("All Files", ".*")))
        if file_name:
            try:
                self.df = pd.read_csv(file_name)
                self.app.switch_to_dash11()
                return file_name
            except (ValueError, FileNotFoundError):
                self.error_info.config(text="file can not be opened!")

class Dashboard11(Frame):
    def __init__(self, parent,app):
        super().__init__( parent)
        self.app=app

        self.parent = parent

        self.df = pd.read_csv(file_name)
        self.configure(bg='#ffffff')


        self.header = Frame(self.parent,  bg='#9561D1')
        self.header.place(x=300, y=0, width=1070, height=60)

        self.logout_text = Button(self.header, text="Logout",bg='#7B39C6', font=("", 13, "bold"), bd=0, fg='white',
                                  cursor='hand2', activebackground='#ffffff',command = exit)
        self.logout_text.place(x=680, y=15)


        self.sidebar = Frame(self.parent,  bg='#7B39C6')
        self.sidebar.place(x=0, y=0, width=300, height=750)


        self.logoImage = ImageTk.PhotoImage(file='images\\hyy.png')
        self.logo = Label(self.sidebar, image=self.logoImage,  bg='#7B39C6')
        self.logo.place(x=70, y=80)

        self.brandName = Label(self.sidebar, text=f"{f1}",  bg='#7B39C6', font=("", 15, "bold"),fg="white")
        self.brandName.place(x=109, y=200)

        self.dashboardImage = ImageTk.PhotoImage(file='images\\dashboard-icon.png')
        self.dashboard = Label(self.sidebar, image=self.dashboardImage,  bg='#7B39C6')
        self.dashboard.place(x=35, y=402)

        self.dashboard_text = Button(self.sidebar, text="Data visualization",  bg='#7B39C6', font=("", 13, "bold"), bd=0,
                                     cursor='hand2', activebackground='#ffffff',command=app.switch_to_dash2,fg='white')
        self.dashboard_text.place(x=80, y=402)

        self.manageImage = ImageTk.PhotoImage(file='images\\manage-icon.png')
        self.manage = Label(self.sidebar, image=self.manageImage,  bg='#7B39C6')
        self.manage.place(x=35, y=287)
        self.manage_text = Button(self.sidebar, text="Upload Csv file",  bg='#7B39C6', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff', command = app.switch_to_dash1,fg='white')
        self.manage_text.place(x=80, y=287)

        self.settingsImage = ImageTk.PhotoImage(file='images\\settings-icon.png')
        self.settings = Label(self.sidebar, image=self.settingsImage, bg='#7B39C6')
        self.settings.place(x=35, y=345)

        self.settings_text = Button(self.sidebar, text="Cleaning data",  bg='#7B39C6', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff', command = self.cleaning,fg='white')
        self.settings_text.place(x=80, y=345)


        self.ExitImage = ImageTk.PhotoImage(file='images\\exit-icon.png')
        self.Exit = Label(self.sidebar, image=self.ExitImage, bg='#7B39C6')
        self.Exit.place(x=25, y=448)

        self.Exit_text = Button(self.sidebar, text="Exit", bg='#7B39C6', font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff',command=exit,fg='white')
        self.Exit_text.place(x=85, y=462)



        self.clock_image = ImageTk.PhotoImage(file="images\\time.png")
        self.date_time_image = Label(self.sidebar, image=self.clock_image, bg='#7B39C6')
        self.date_time_image.place(x=88, y=20)

        self.date_time = Label(self.parent)
        self.date_time.place(x=115, y=15)
        self.show_time()




        # =================================== LEFT FRAME ================================ #
        self.left_frame = Frame(self.parent, bg="white smoke", relief=RIDGE, bd=1)
        self.left_frame.place(x=1090, y=0, width=300, height=1000)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", backgroung="silver", foreground="black", rowheight=25, fieldbackground="white")
        style.map("Treeview", background=[("selected", "medium sea green")])
        style.configure("Treeview.Heading", background="light steel blue", font=("Arial", 10, "bold"))

        self.my_table = ttk.Treeview(self.left_frame)

        scroll_x_label = ttk.Scrollbar(self.left_frame, orient=HORIZONTAL, command=self.my_table.xview)
        scroll_y_label = ttk.Scrollbar(self.left_frame, orient=VERTICAL, command=self.my_table.yview)
        scroll_x_label.pack(side=TOP, fill=X)
        scroll_y_label.pack(side=LEFT, fill=Y)
        self.display_uploaded_file()

        # Measures container

        self.measures_container = Frame(self.parent, bg='#eff5f6')
        self.measures_container.place(x=300, y=60, width=230, height=685)

        self.measure_labels = ['Mean', 'Median', 'Std Deviation', 'Quartiles']
        self.measure_comboboxes = []
        self.zone_labels = {}

        self.label_combobox_map = {}

        for i, label in enumerate(self.measure_labels):
            frame = Frame(self.measures_container,
                          bg='orange')
            frame.pack(side=TOP, fill=BOTH, expand=True)

            measure_label = Label(frame, text=label, bg=frame['bg'], fg='white', padx=10, pady=5)
            measure_label.pack(side=TOP, fill=BOTH)
            measure_label.config(font=("Arial", 12, "bold"), anchor="center")

            # Create Combobox
            measure_combobox = ttk.Combobox(frame, font=("Arial", 10), justify="center", state="readonly")
            measure_combobox.pack(side=TOP, fill=BOTH, padx=10, pady=5)

            # Set Combobox options to the columns of the DataFrame
            measure_combobox["values"] = self.df.columns.tolist()

            # Add Combobox to the list
            self.measure_comboboxes.append(measure_combobox)


            self.zone_labels[label] = frame

            # Map label to combobox
            self.label_combobox_map[label] = measure_combobox

            # Bind the event to the Combobox
            measure_combobox.bind("<<ComboboxSelected>>",
                                  lambda event, lbl=label: self.calculate(lbl, self.label_combobox_map[lbl].get()))


        figure = self.plot_correlation_matrix()
        if figure is not None:
            canvas = FigureCanvasTkAgg(figure, master=self.parent)
            canvas.draw()
            canvas.get_tk_widget().place(x=535, y=90)

    def calculate(self, measure_name, selected_column):
        # Calculate statistical measure for the specified column
        global df
        value = None
        self.df = df
        if self.df is not None:
            if measure_name == 'Mean':
                value = round(self.df[selected_column].mean(),2)
            elif measure_name == 'Median':
                value = round(self.df[selected_column].median(),2)
            elif measure_name == 'Std Deviation':
                value = round(self.df[selected_column].std(),2)
            elif measure_name == 'Quartiles':
                q1 = round(self.df[selected_column].quantile(0.25), 2)
                q2 = round(self.df[selected_column].quantile(0.5), 2)
                q3 = round(self.df[selected_column].quantile(0.75), 2)
                value = (q1, q2, q3)
        else :
            messagebox.showerror("ERROR!", "Please, clean your data first!")

        # Update zone label with calculated value
        if measure_name in self.zone_labels:

            # Create a new label with the calculated value
            label_text = f" {value}" if value is not None else f"N/A"
            label = Label(self.zone_labels[measure_name], text=label_text, bg='orange', fg='#ffffff', font=("yu gothic ui",17,"bold"))
            label.pack(side=TOP, fill=BOTH)

            label.place_configure(relx=0.5, rely=0.7, anchor="center")

    def cleaning(self):
        global file_name
        global df
        df = pd.read_csv(file_name)
        df.drop_duplicates(inplace=True)
        df.dropna(how='all', inplace=True)

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=FutureWarning)
            for column in df.columns:
                if df[column].dtype == 'float64' or df[column].dtype == 'int64':
                    mean_value = df[column].mean()
                    df[column].fillna(mean_value, inplace=True)

        for column in df.select_dtypes(include=['float64', 'int64']).columns:
            df[column] = np.where(df[column] < 0, df[column].mean(), df[column])

        messagebox.showinfo("INFO!", "Cleaning Done!")
        self.display_cleaned_file(df)


    def display_cleaned_file(self,df):
        self.my_table.delete(*self.my_table.get_children())
        self.my_table["column"] = list(df.columns)
        self.my_table["show"] = "headings"
        for column in self.my_table["column"]:
            self.my_table.heading(column, text=column)
        for column_name in self.my_table["column"]:
            self.my_table.column(column_name, width=60)
        df_rows_old = df.to_numpy()
        df_rows_refreshed = [list(item) for item in df_rows_old]
        for row in df_rows_refreshed:
            self.my_table.insert("", "end", values=row)
        # Use grid to place the table
        self.my_table.place(x=5, y=5, width=300, height=755)


    def display_uploaded_file(self):
        global file_name
        self.df = pd.read_csv(file_name)
        self.my_table["column"] = list(self.df.columns)
        self.my_table["show"] = "headings"
        for column in self.my_table["column"]:
            self.my_table.heading(column, text=column)
        for column_name in self.my_table["column"]:
            self.my_table.column(column_name, width=60)
        df_rows_old = self.df.to_numpy()
        df_rows_refreshed = [list(item) for item in df_rows_old]
        for row in df_rows_refreshed:
            self.my_table.insert("", "end", values=row)

        # Use grid to place the table
        self.my_table.place(x=5, y=5, width=300, height=755)

    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=("", 13, "bold"), bd=0, bg='#7B39C6', fg="white")
        self.date_time.after(100, self.show_time)

    def plot_correlation_matrix(self):
        if self.df is not None:
            # Select only numeric columns
            numeric_columns = self.df.select_dtypes(include=[np.number]).columns
            df_numeric = self.df[numeric_columns]

            corr_matrix = np.corrcoef(df_numeric.to_numpy(), rowvar=False)
            plt.figure(figsize=(5.5, 6))
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", xticklabels=numeric_columns,
                        yticklabels=numeric_columns)
            plt.title('Correlation Matrix')
            # Return the figure to display it in the main window
            return plt.gcf()
        else:
            messagebox.showwarning("Warning", "Please upload a file first.")
            return None


BUTTON_FONT = ("Arial", 13, "bold")
LABEL_FONT = ("Arial", 20, "bold")
USER_FONT = ("Arial", 14, "bold")
INFO_FONT = ("Arial", 12, "bold")
SMALL_FONT = ("Arial", 12, "normal")
COLORS = ['green', 'red', 'purple', 'brown', 'blue']


class Dashboard2(Frame):
    def __init__(self, parent,app):
        super().__init__( parent)

        self.parent = parent
        self.configure(background='#eff5f6')
        self.bar_x_label = StringVar()
        self.bar_y_label = StringVar()
        self.scatter_x_name = StringVar()
        self.scatter_y_name = StringVar()
        self.pie_value_name = StringVar()
        self.pie_group_name = StringVar()
        self.line_name = StringVar()



        self.header = Frame(self.parent,   bg='#9561D1')
        self.header.place(x=300, y=0, width=950, height=60)

        self.logout_text = Button(self.header, text="Logout", bg='#7B39C6', font=("", 13, "bold"), bd=0, fg='white',
                                  cursor='hand2', activebackground='#ffffff',command = exit)
        self.logout_text.place(x=680, y=15)


        self.sidebar = Frame(self.parent,bg='#7B39C6')
        self.sidebar.place(x=0, y=0, width=300, height=750)


        self.heading = Label(self.header, text='Dashboard', font=("", 13, "bold"), fg='white', bg='#7B39C6')
        self.heading.place(x=25, y=15)

        #------------------------------------------------------------------------------


        self.bar_heading = Label(self.parent, text="Bar Chart", font=SMALL_FONT, bg="ivory")
        self.bar_heading.place(x=325, y=65, width=365, height=20)

        self.bar_info = Frame(self.parent, bg="ivory")
        self.bar_info.place(x=325, y=85, width=365, height=70)

        self.x_label = Label(self.bar_info, text="XLabel", font=SMALL_FONT, bg="ivory", bd=1)
        self.x_label.grid(row=0, column=0, padx=10)

        self.y_label = Label(self.bar_info, text="YLabel", font=SMALL_FONT, bg="ivory", bd=1)
        self.y_label.grid(row=1, column=0, padx=10)

        self.x_box = ttk.Combobox(self.bar_info, font=SMALL_FONT, justify="center", state="readonly",
                                  textvariable=self.bar_x_label)
        self.x_box.grid(row=0, column=1)

        self.y_box = ttk.Combobox(self.bar_info, font=SMALL_FONT, justify="center", state="readonly",
                                  textvariable=self.bar_y_label)
        self.y_box.grid(row=1, column=1)

        self.bar_draw_button = Button(self.bar_info, text="draw", justify="center", font=INFO_FONT, relief=RIDGE, bd=2,
                                      bg="ivory", cursor="hand2", width=5, command=self.draw_bar_chart)
        self.bar_draw_button.grid(row=0, column=2, padx=10)

        self.bar_clear_button = Button(self.bar_info, text="clean", justify="center", font=INFO_FONT, relief=RIDGE,
                                       bg="ivory", cursor="hand2", bd=2, width=5, command=self.clear_bar)
        self.bar_clear_button.grid(row=1, column=2, padx=10)

        self.top_left = Frame(self.parent, bg="ivory")
        self.top_left.place(x=325, y=155, width=365, height=230)
        self.canvas_1 = Canvas(self.top_left, width=365, height=250, bg="ivory", relief=RIDGE)
        self.canvas_1.pack()
        self.fig_1 = None
        self.output_1 = None

        #------------------------------------------------------------------------------

        self.scatter_heading = Label(self.parent, text="Scatter Plot", font=SMALL_FONT, bg="ivory")
        self.scatter_heading.place(x=720, y=65, width=365, height=20)

        self.scatter_info = Frame(self.parent, bg="ivory")
        self.scatter_info.place(x=720, y=85, width=365, height=70)

        self.scatter_x_label = Label(self.scatter_info, text="XLabel", font=SMALL_FONT, bg="ivory", bd=1)
        self.scatter_x_label.grid(row=0, column=0, padx=10)

        self.scatter_y_label = Label(self.scatter_info, text="YLabel", font=SMALL_FONT, bg="ivory", bd=1)
        self.scatter_y_label.grid(row=1, column=0, padx=10)

        self.scatter_x_box = ttk.Combobox(self.scatter_info, font=SMALL_FONT, justify="center", state="readonly",
                                          textvariable=self.scatter_x_name)
        self.scatter_x_box.grid(row=0, column=1)

        self.scatter_y_box = ttk.Combobox(self.scatter_info, font=SMALL_FONT, justify="center", state="readonly",
                                          textvariable=self.scatter_y_name)
        self.scatter_y_box.grid(row=1, column=1)

        self.scatter_draw_button = Button(self.scatter_info, text="draw", justify="center", font=INFO_FONT,
                                          relief=RIDGE, bd=2, bg="ivory", cursor="hand2", width=5,
                                          command=self.draw_scatter_chart)
        self.scatter_draw_button.grid(row=0, column=2, padx=10)

        self.scatter_clean_button = Button(self.scatter_info, text="clean", justify="center", font=INFO_FONT,
                                           relief=RIDGE, bg="ivory", cursor="hand2", bd=2, width=5,
                                           command=self.clear_scatter)
        self.scatter_clean_button.grid(row=1, column=2, padx=10)

        self.top_right = Frame(self.parent, bg="ivory")
        self.top_right.place(x=720, y=155, width=365, height=230)
        self.canvas_2 = Canvas(self.top_right, width=365, height=250, bg="ivory", relief=RIDGE)
        self.canvas_2.pack()
        self.fig_2 = None
        self.output_2 = None

        #--------------------------------------------------------------------------------------------

        self.pie_heading = Label(self.parent, text="Pie Chart", font=SMALL_FONT, bg="ivory")
        self.pie_heading.place(x=325, y=390, width=365, height=20)

        self.pie_info = Frame(self.parent, bg="ivory")
        self.pie_info.place(x=325, y=410, width=365, height=70)

        self.pie_x_label = Label(self.pie_info, text="Values", font=SMALL_FONT, bg="ivory", bd=1)
        self.pie_x_label.grid(row=0, column=0, padx=10)

        self.pie_y_label = Label(self.pie_info, text="GroupBy", font=SMALL_FONT, bg="ivory", bd=1)
        self.pie_y_label.grid(row=1, column=0, padx=10)

        self.pie_value_box = ttk.Combobox(self.pie_info, font=SMALL_FONT, justify="center", state="readonly",
                                          textvariable=self.pie_value_name)
        self.pie_value_box.grid(row=0, column=1)

        self.pie_group_box = ttk.Combobox(self.pie_info, font=SMALL_FONT, justify="center", state="readonly",
                                          textvariable=self.pie_group_name)
        self.pie_group_box.grid(row=1, column=1)

        self.pie_draw_button = Button(self.pie_info, text="draw", justify="center", font=INFO_FONT, relief=RIDGE,
                                      bd=2, bg="ivory", cursor="hand2", width=5, command=self.draw_pie_chart)
        self.pie_draw_button.grid(row=0, column=2, padx=10)

        self.pie_clear_button = Button(self.pie_info, text="clean", justify="center", font=INFO_FONT, relief=RIDGE,
                                       bg="ivory", cursor="hand2", bd=2, width=5, command=self.clear_pie)
        self.pie_clear_button.grid(row=1, column=2, padx=10)

        self.bottom_left = Frame(self.parent, bg="ivory")
        self.bottom_left.place(x=325, y=480, width=365, height=210)
        self.canvas_3 = Canvas(self.bottom_left, width=365, height=250, bg="ivory", relief=RIDGE)
        self.canvas_3.pack()
        self.fig_3 = None
        self.output_3 = None

        #--------------------------------------------------------------------------------------------

        self.line_heading = Label(self.parent, text="Line Chart", font=SMALL_FONT, bg="ivory")
        self.line_heading.place(x=720, y=390, width=365, height=20)

        self.line_info = Frame(self.parent, bg="ivory")
        self.line_info.place(x=720, y=410, width=365, height=70)

        self.line_box = ttk.Combobox(self.line_info, font=SMALL_FONT, justify="center", state="readonly",
                                     textvariable=self.line_name)
        self.line_box.grid(row=0, column=1)

        self.line_draw_button = Button(self.line_info, text="draw", justify="center", font=INFO_FONT, relief=RIDGE,
                                       bd=2, bg="ivory", cursor="hand2", command=self.draw_line_chart)
        self.line_draw_button.grid(row=0, column=0, padx=10, pady=20)

        self.line_clear_button = Button(self.line_info, text="clean", justify="center", font=INFO_FONT, relief=RIDGE,
                                        bg="ivory", cursor="hand2", bd=2, command=self.clear_line)
        self.line_clear_button.grid(row=0, column=2, padx=10, pady=20)

        self.bottom_right = Frame(self.parent, bg="ivory")
        self.bottom_right.place(x=720, y=480, width=365, height=210)
        self.canvas_4 = Canvas(self.bottom_right, width=365, height=250, bg="ivory", relief=RIDGE)
        self.canvas_4.pack()
        self.fig_4 = None
        self.output_4 = None



        #--------------------------------------------------------------------------------------------


        self.logoImage = ImageTk.PhotoImage(file='images\\hyy.png')
        self.logo = Label(self.sidebar, image=self.logoImage, bg="#7B39C6")
        self.logo.place(x=70, y=80)

        self.brandName = Label(self.sidebar, text=f"{f1}", bg='#7B39C6', font=("", 15, "bold"),fg="white")
        self.brandName.place(x=109, y=200)

        self.dashboardImage = ImageTk.PhotoImage(file='images\\manage-icon.png')
        self.dashboard = Label(self.sidebar, image=self.dashboardImage,bg='#7B39C6')
        self.dashboard.place(x=35, y=287)

        self.dashboard_text = Button(self.sidebar, text="Upload Csv file", bg='#7B39C6', font=("", 13, "bold"), bd=0,
                                     cursor='hand2', activebackground='#ffffff',command = app.switch_to_dash1,fg='white')
        self.dashboard_text.place(x=80,y=287)

        self.manageImage = ImageTk.PhotoImage(file='images\\settings-icon.png')
        self.manage = Label(self.sidebar, image=self.manageImage, bg='#7B39C6')
        self.manage.place(x=35, y=345)



        self.settingsImage = ImageTk.PhotoImage(file='images\\dashboard-icon.png')
        self.settings = Label(self.sidebar, image=self.settingsImage,bg='#7B39C6')
        self.settings.place(x=35, y=402)

        self.settings_text = Button(self.sidebar, text="Export Dashboard", bg='#7B39C6', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff',command=self.export_figures,fg="white")
        self.settings_text.place(x=80, y=402)

        self.ExitImage = ImageTk.PhotoImage(file='images\\exit-icon.png')
        self.Exit = Label(self.sidebar, image=self.ExitImage,bg='#7B39C6')
        self.Exit.place(x=25, y=448)

        self.Exit_text = Button(self.sidebar, text="Exit", bg='#7B39C6', font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff', command=self.ppp,fg="white")
        self.Exit_text.place(x=85, y=462)


        self.clock_image = ImageTk.PhotoImage(file="images\\time.png")
        self.date_time_image = Label(self.sidebar, image=self.clock_image, bg='#7B39C6')
        self.date_time_image.place(x=88, y=20)

        self.date_time = Label(self.parent)
        self.date_time.place(x=115, y=15)
        self.show_time()

        # =================================== LEFT FRAME ================================ #
        self.left_frame = Frame(self.parent, bg="white smoke", relief=RIDGE, bd=1)
        self.left_frame.place(x=1090, y=0, width=300, height=1000)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", backgroung="silver", foreground="black", rowheight=25, fieldbackground="white")
        style.map("Treeview", background=[("selected", "medium sea green")])
        style.configure("Treeview.Heading", background="light steel blue", font=("Arial", 10, "bold"))

        self.my_table = ttk.Treeview(self.left_frame)

        scroll_x_label = ttk.Scrollbar(self.left_frame, orient=HORIZONTAL, command=self.my_table.xview)
        scroll_y_label = ttk.Scrollbar(self.left_frame, orient=VERTICAL, command=self.my_table.yview)
        scroll_x_label.pack(side=TOP, fill=X)
        scroll_y_label.pack(side=LEFT, fill=Y)

        self.file = Button(self.sidebar ,text = "Cleaning Data", bg='#7B39C6', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff', command = app.switch_to_dash11,fg='white')
        self.file.place(x=80,y=345)
        self.receive_uploaded_file()

    def clear_table_data(self):
        self.my_table.delete(*self.my_table.get_children())


    def receive_uploaded_file(self):
        global df
        self.clear_table_data()
        self.my_table["column"] = list(df.columns)
        self.my_table["show"] = "headings"
        for column in self.my_table["column"]:
            self.my_table.heading(column, text=column)
        for column_name in self.my_table["column"]:
            self.my_table.column(column_name, width=60)
        df_rows_old = df.to_numpy()
        df_rows_refreshed = [list(item) for item in df_rows_old]
        for row in df_rows_refreshed:
            self.my_table.insert("", "end", values=row)
        self.my_table.place(x=5, y=5, width=300, height=755)
        try:
            self.fill_scatter_box()
        except TclError:
            pass

        try:
            self.fill_bar_box()
        except TclError:
            pass

        try:
            self.fill_pie_box()
        except TclError:
            pass

        try:
            self.fill_line_box()
        except TclError:
            pass


    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=("", 13, "bold"), bd=0, bg='#7B39C6', fg="white")
        self.date_time.after(100, self.show_time)

    def ppp (self):
        confirm = messagebox.askyesno(title="Visualization", message="Do You Want To Close The App?")
        if confirm > 0:
            root.destroy()
            return
        else:
            pass


    def fill_bar_box(self):
        columns = [item for item in df]
        x_labels = []
        y_labels = []
        for column in columns:
            if df[column].dtype == 'object':
                x_labels.append(column)
            elif df[column].dtype == 'int64' or df[column].dtype == 'float64':
                y_labels.append(column)
        self.x_box["values"] = tuple(x_labels)
        self.x_box.current(0)
        self.y_box["values"] = tuple(y_labels)
        self.y_box.current(0)

    def fill_scatter_box(self):
        columns = [item for item in df]
        x_labels = []
        y_labels = []
        for column in columns:
            if df[column].dtype == 'int64' or df[column].dtype == 'float64':
                x_labels.append(column)
                y_labels.append(column)
        self.scatter_x_box["values"] = tuple(x_labels)
        self.scatter_x_box.current(0)
        self.scatter_y_box["values"] = tuple(y_labels)
        self.scatter_y_box.current(0)

    def fill_pie_box(self):
        columns = [item for item in df]
        x_labels = []
        y_labels = []
        for column in columns:
            if df[column].dtype == 'object':
                x_labels.append(column)
            elif df[column].dtype == 'int64' or df[column].dtype == 'float64':
                y_labels.append(column)
        self.pie_group_box["values"] = tuple(x_labels)
        self.pie_group_box.current(0)
        self.pie_value_box["values"] = tuple(y_labels)
        self.pie_value_box.current(0)

    def fill_line_box(self):
        columns = [item for item in df]
        x_labels = []
        for column in columns:
            if df[column].dtype == 'int64' or df[column].dtype == 'float64':
                x_labels.append(column)
        self.line_box["values"] = tuple(x_labels)
        self.line_box.current(0)

    def draw_bar_chart(self):
        self.fig_1 = Figure(figsize=(4, 2), dpi=100)
        axes = self.fig_1.add_subplot(111)
        axes.bar(df[f"{self.bar_x_label.get()}"], df[f"{self.bar_y_label.get()}"], color=choice(COLORS))
        self.output_1 = FigureCanvasTkAgg(self.fig_1, master=self.canvas_1)
        self.output_1.draw()
        self.output_1.get_tk_widget().pack()
        return self.fig_1

    def clear_bar(self):
        if self.output_1:
            for child in self.canvas_1.winfo_children():
                child.destroy()
        self.output_1 = None

    def draw_scatter_chart(self):
        self.fig_2 = Figure(figsize=(4, 2), dpi=100)
        axes = self.fig_2.add_subplot(111)
        axes.scatter(df[f"{self.scatter_x_name.get()}"], df[f"{self.scatter_y_name.get()}"], c=choice(COLORS))
        self.output_2 = FigureCanvasTkAgg(self.fig_2, master=self.canvas_2)
        self.output_2.draw()
        self.output_2.get_tk_widget().pack()
        return self.fig_2

    def clear_scatter(self):
        if self.output_2:
            for child in self.canvas_2.winfo_children():
                child.destroy()
        self.output_2 = None

    def draw_pie_chart(self):
        # prepare values:
        display = df.groupby([f"{self.pie_group_name.get()}"]).sum(numeric_only=True)
        display = display[f"{self.pie_value_name.get()}"].to_numpy()
        my_labels = list(df[f"{self.pie_group_name.get()}"].unique())
        # visualize:
        self.fig_3 = Figure(figsize=(4, 2), dpi=100)
        axes = self.fig_3.add_subplot(111)
        axes.pie(display, labels=my_labels, shadow=True)
        self.output_3 = FigureCanvasTkAgg(self.fig_3, master=self.canvas_3)
        self.output_3.draw()
        self.output_3.get_tk_widget().pack()
        return self.fig_3

    def clear_pie(self):
        if self.output_3:
            for child in self.canvas_3.winfo_children():
                child.destroy()
        self.output_3 = None

    def draw_line_chart(self):
        self.fig_4 = Figure(figsize=(4, 2), dpi=100)
        axes = self.fig_4.add_subplot(111)
        axes.plot(df[f"{self.line_name.get()}"], c=choice(COLORS))
        self.output_4 = FigureCanvasTkAgg(self.fig_4, master=self.canvas_4)
        self.output_4.draw()
        self.output_4.get_tk_widget().pack()
        return self.fig_4

    def clear_line(self):
        if self.output_4:
            for child in self.canvas_4.winfo_children():
                child.destroy()
        self.output_4 = None


    def export_figures(self):
        # Ask the user to choose the save location and file name
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if not file_path:
            return  # User canceled, do nothing

        # Create a new blank image with the desired size and light background
        combined_image = Image.new('RGB', (800, 600), color='#f0f0f0')

        # Get bytes from memoryview objects
        fig_1_bytes = self.fig_1.canvas.buffer_rgba().tobytes()
        fig_2_bytes = self.fig_2.canvas.buffer_rgba().tobytes()
        fig_3_bytes = self.fig_3.canvas.buffer_rgba().tobytes()
        fig_4_bytes = self.fig_4.canvas.buffer_rgba().tobytes()

        # Create images from bytes
        fig_1_image = Image.frombytes("RGBA", self.fig_1.canvas.get_width_height(), fig_1_bytes)
        fig_2_image = Image.frombytes("RGBA", self.fig_2.canvas.get_width_height(), fig_2_bytes)
        fig_3_image = Image.frombytes("RGBA", self.fig_3.canvas.get_width_height(), fig_3_bytes)
        fig_4_image = Image.frombytes("RGBA", self.fig_4.canvas.get_width_height(), fig_4_bytes)

        # Paste the images onto combined_image
        combined_image.paste(fig_1_image, (0, 100))
        combined_image.paste(fig_2_image, (400, 100))
        combined_image.paste(fig_3_image, (0, 350))
        combined_image.paste(fig_4_image, (400, 350))

        # Add a title to the dashboard
        title_font = ImageFont.truetype("arialbd.ttf", 40)
        draw = ImageDraw.Draw(combined_image)
        # Ask the user to input the title
        title_text = simpledialog.askstring("Title", "Enter the title for the dashboard:")

        title_width = draw.textlength(title_text, font=title_font)
        draw.text(((800 - title_width) // 2, 10), title_text, fill='purple', font=title_font, align="center", fg = 'purple')

        # Get the directory and file name from the full file path
        directory, file_name = os.path.split(file_path)

        # Ensure the directory exists
        os.makedirs(directory, exist_ok=True)

        # Save the combined image with the specified file name
        combined_image.save(os.path.join(directory, file_name))
        messagebox.showinfo("Export Successful", "The figures have been exported successfully.")
        self.clear_bar()
        self.clear_pie()
        self.clear_line()
        self.clear_scatter()

        # Chemin complet de l'image enregistrée
        image_path = os.path.join(directory, file_name)

        # Ouvrir l'image avec PIL
        image = Image.open(image_path)

        # Afficher l'image
        image.show()


class SciVizApp(Tk):
    def __init__(self):
        super().__init__()

        # Create main frame for content
        self.main_frame = Frame(self)
        self.main_frame.pack(side="top", fill="both", expand=True)

        # Create login page instance
        self.login_page = LoginPage(self.main_frame, self)  # Pass app reference
        # Create signup page instance (optional, create on demand)

        # Initially show the login page
        self.current_page = self.login_page
        self.current_page.pack(fill='both', expand=True)

    def switch_to_dash1(self):
        """Switches the current page to the signup page (if not already displayed)."""
        if not isinstance(self.current_page, Dashboard1):
            if hasattr(self, 'dash1_page'):
                del self.dash1_page
        self.dash1_page = Dashboard1(self.main_frame, self)

                # Switch to the dash1 page
        self.current_page.pack_forget()
        self.current_page = self.dash1_page
        self.current_page.pack(fill='both', expand=True)


    def switch_to_login(self):
        """Switches the current page to the signup page (if not already displayed)."""
        if not isinstance(self.current_page, LoginPage):
            # Create signup page instance if needed
            if hasattr(self, 'signup_page'):
                del self.login_page
            self.login_page = LoginPage(self.main_frame, self)

            # Switch pages
            self.current_page.pack_forget()
            self.current_page = self.login_page
            self.current_page.pack(fill='both', expand=True)

    def switch_to_signup(self):
        """Switches the current page to the signup page (if not already displayed)."""
        if not isinstance(self.current_page, SignupPage):

            if hasattr(self, 'signup_page'):
                del self.signup_page
        self.signup_page = SignupPage(self.main_frame, self)

                # Switch to the signup page
        self.current_page.pack_forget()
        self.current_page = self.signup_page
        self.current_page.pack(fill='both', expand=True)

    def switch_to_dash2(self):
        global df
        global file_name
        """Switches the current page to the signup page (if not already displayed)."""
        if isinstance(self.current_page, Dashboard11):
            if df is None:
                messagebox.showerror("ERROR!", "Please, clean your data first!")
                return
        if isinstance(self.current_page, Dashboard1):
            if not file_name:
                messagebox.showerror("ERROR!", "Please, upload file first!")
                return

        if not isinstance(self.current_page, Dashboard2):
            if hasattr(self, 'dash2_page'):
                del self.dash2_page
        self.dash2_page = Dashboard2(self.main_frame, self)
        # Switch to the dash2 page
        self.current_page.pack_forget()
        self.current_page = self.dash2_page
        self.current_page.pack(fill='both', expand=True)



    def switch_to_dash11(self):
        """Switches the current page to the signup page (if not already displayed)."""
        if not isinstance(self.current_page, Dashboard11):
            if hasattr(self, 'dash11_page'):
                del self.dash11_page
        self.dash11_page = Dashboard11(self.main_frame, self)
        # Switch to the dash2 page
        self.current_page.pack_forget()
        self.current_page = self.dash11_page
        self.current_page.pack(fill='both', expand=True)




root = SciVizApp()
root.title("Scientific data visualization application")
root.geometry("1366x780")
root.resizable(0, 0)
root.mainloop()
