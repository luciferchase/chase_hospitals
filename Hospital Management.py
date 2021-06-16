# import all dependencies
from tkinter import *
from tkinter import messagebox, ttk

import easygui
from PIL import Image, ImageTk
from tkcalendar import Calendar

import mysql.connector as sqlcon
import pyglet
import pyttsx3
import random


# configure text-to-speech
engine = pyttsx3.init()

def speak(text):
    pass
    # engine.setProperty("rate", 150)
    # engine.say(text)
    # engine.runAndWait()


# config main window
pyglet.font.add_file(r"Data\\Miscs\\Evogria.otf")
pyglet.font.load("evogria")

root = Tk()
root.title("Chase Hospitals")
root.iconbitmap(r"Data\\Images\\Icons\\plus.ico")
root.config(bg = "#FFFFFF")
root.state("zoomed")
root.resizable(False, False)

# top frame (constant)
top_frame = LabelFrame(root)
top_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 8)
top_frame.grid_propagate(0)

# title
title = Label(top_frame, text = "Chase Hospitals", font = "evogria 45", 
    bg = "#FFE2E2", width = 42, anchor = CENTER)
title.pack()

# left frame (constant)
left_frame = LabelFrame(root, bg = "#FFE2E2")
left_frame.grid(row = 2, column = 0, padx = 4, pady = 4, columnspan = 3, ipady = 40)

# right frame (varies)
right_frame = LabelFrame(root, width = 979, height = 700, bg = "#FFE2E2")
right_frame.grid(row = 2, column = 4, columnspan = 4)
right_frame.grid_propagate(0)


# define all functions
# clean right frame - use in every button
def clean_right_frame():
    global right_frame

    main_window()

    right_frame.grid_forget()
    right_frame = LabelFrame(root, width = 979, height = 700, bg = "#FFE2E2")
    right_frame.grid(row = 2, column = 4, columnspan = 4)
    right_frame.grid_propagate(0)


# clean left and top frame (for services offered window)
def clean_left_frame():
    global left_frame

    main_window()

    left_frame.grid_forget()
    left_frame = LabelFrame(root, bg = "#FFE2E2")
    left_frame.grid(row = 2, column = 0, padx = 4, pady = 4, columnspan = 3, ipady = 40)
    left_frame.grid_propagate(0)


def clean_top_frame():
    global top_frame

    main_window()

    top_frame.grid_forget()
    top_frame = LabelFrame(root, bg = "#FFE2E2")
    top_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 8)
    top_frame.grid_propagate(0)


# registration main window
def registration_window():
    global registration
    clean_right_frame()

    # highlight clicked button
    registration.grid_forget()
    registration = Button(left_frame, text = "Registration", font = "consolas 19 bold", 
                    width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#2A363B", 
                    fg = "#FF847C", anchor = CENTER, relief = SUNKEN, command = registration_window)
    registration.grid(row = 0, column = 0, columnspan = 3, pady = 5, padx = 20)

    global name_entry
    global age_entry
    global gender_entry
    global contact_entry
    global address_entry
    global blood_group_entry

    # labels
    name_label = Label(right_frame, text = "Name", font = "consolas 25 bold", bg = "#FFE2E2")
    age_label = Label(right_frame, text = "Age", font = "consolas 25 bold", bg = "#FFE2E2")
    gender_label = Label(right_frame, text = "Gender", font = "consolas 25 bold", bg = "#FFE2E2")
    contact_label = Label(right_frame, text = "Contact No.", font = "consolas 25 bold", bg = "#FFE2E2")
    address_label = Label(right_frame, text = "Address", font = "consolas 25 bold", bg = "#FFE2E2")
    blood_group_label = Label(right_frame, text = "Blood Group", font = "consolas 25 bold", bg = "#FFE2E2")

    name_label.grid(row = 0, column = 0, padx = 10, sticky = W)
    age_label.grid(row = 1, column = 0, padx = 10, sticky = W)
    gender_label.grid(row = 2, column = 0, padx = 10, sticky = W)
    contact_label.grid(row = 3, column = 0, padx = 10, sticky = W)
    address_label.grid(row = 4, column = 0, padx = 10, sticky = W)
    blood_group_label.grid(row = 5, column = 0, padx = 10, sticky = W)

    for i in range(6):
        colon = Label(right_frame, text = ":", font = "consolas 25 bold", bg = "#FFE2E2")
        colon.grid(row = i, column = 1, sticky = W)

    # entry fields
    name_entry = Entry(right_frame, font = "consolas 20")
    age_entry = Entry(right_frame, font = "consolas 20")
    gender_entry = Entry(right_frame, font = "consolas 20")
    contact_entry = Entry(right_frame, font = "consolas 20")
    address_entry = Entry(right_frame, font = "consolas 20")
    blood_group_entry = Entry(right_frame, font = "consolas 20")

    name_entry.grid(row = 0, column = 2, columnspan = 3, ipadx = 160, ipady = 5, pady = 20, padx = 10)
    age_entry.grid(row = 1, column = 2, columnspan = 3, ipadx = 160, ipady = 5, pady = 20, padx = 10)
    gender_entry.grid(row = 2, column = 2, columnspan = 3, ipadx = 160, ipady = 5, pady = 20, padx = 10)
    contact_entry.grid(row = 3, column = 2, columnspan = 3, ipadx = 160, ipady = 5, pady = 20, padx = 10)
    address_entry.grid(row = 4, column = 2, columnspan = 3, ipadx = 160, ipady = 5, pady = 20, padx = 10)
    blood_group_entry.grid(row = 5, column = 2, columnspan = 3, ipadx = 160, ipady = 5, pady = 20, padx = 10)

    # submit button
    submit_button = Button(right_frame, text = "Register", font = "consolas 20 bold", 
                    bg = "#FF847C", borderwidth = 7, padx = 10, pady = 4, command = registration_submit)
    submit_button.grid(row = 6, column = 0, columnspan = 4, padx = 10, pady = 54, ipadx = 350)
    submit_button.update()
    speak("Please fill your complete details")


# patient details main window
def patient_details_window():
    clean_right_frame()

    global right_frame
    global patient_details
    global field_to_search
    global search_detail_entry
    global submit_button

    # highlight clicked button
    patient_details.grid_forget()
    patient_details = Button(left_frame, text = "Patient Details", font = "consolas 19 bold", 
                width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#2A363B", fg = "#FF847C", 
                anchor = CENTER, relief = SUNKEN, command = patient_details_window)
    patient_details.grid(row = 1, column = 0, columnspan = 3, pady = 5, padx = 20)

    # search button
    submit_button = Button(right_frame, text = "Search", font = "consolas 17 bold", bg = "#FF847C", 
                borderwidth = 7, padx = 10, pady = 4, command = patient_details_search_submit)
    submit_button.grid(row = 2, column = 0, columnspan = 4, padx = 10, pady = 54, ipadx = 375)

    # select a field to search
    field_to_search_label = Label(right_frame, text = "Field", font = "consolas 19 bold", bg = "#FFE2E2")
    search_detail_label = Label(right_frame, text = "Details", font = "consolas 19 bold", bg = "#FFE2E2")

    field_to_search_label.grid(row = 0, column = 0, padx = 5, sticky = W)
    search_detail_label.grid(row = 1, column = 0, padx = 5, sticky = W)

    for j in range(2):
        colon = Label(right_frame, text = ":", font = "consolas 20 bold", bg = "#FFE2E2")
        colon.grid(row = j, column = 1, sticky = W)

    field_to_search_options = ["PID", "Name", "Age", "Gender", "Contact", "Address", "Blood Group"]

    field_to_search = StringVar()
    field_to_search.set("Name")

    field_to_search_menu = OptionMenu(right_frame, field_to_search, *field_to_search_options)
    field_to_search_menu.config(width = 62, height = 1, font = "consolas 15 bold")
    field_to_search_menu.grid(row = 0, column = 2, columnspan = 3, padx = 15, pady = 5, sticky = W)

    search_detail_entry = Entry(right_frame, font = "consolas 17")
    search_detail_entry.grid(row = 1, column = 2, ipadx = 230, ipady = 5, padx = 15, pady = 10)
    submit_button.update()
    speak("Pleast enter details of the patient you want to see")


# display patient details after search
def display_patient_details_after_search():
    global searched_patient_details
    global patient_details
    global resized_profile_pic_final
    global display_profile_pic

    clean_right_frame()

    # highlight clicked button
    patient_details.grid_forget()
    patient_details = Button(left_frame, text = "Patient Details", font = "consolas 19 bold", 
                width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#2A363B", fg = "#FF847C", 
                anchor = CENTER, relief = SUNKEN, command = patient_details_window)
    patient_details.grid(row = 1, column = 0, columnspan = 3, pady = 5, padx = 20)

    # select a random image for profile pic
    profile_pic_1 = Image.open(r"Data\\Images\\Profile Pics\\dp1.png")
    profile_pic_2 = Image.open(r"Data\\Images\\Profile Pics\\dp2.png")
    profile_pic_3 = Image.open(r"Data\\Images\\Profile Pics\\dp3.png")
    profile_pic_4 = Image.open(r"Data\\Images\\Profile Pics\\dp4.png")
    profile_pic_5 = Image.open(r"Data\\Images\\Profile Pics\\dp5.png")

    profile_pics = [profile_pic_1, profile_pic_2, profile_pic_3, profile_pic_4, profile_pic_5]

    random_profile_pic = random.choice(profile_pics)

    resized_profile_pic = random_profile_pic.resize((100, 100), Image.ANTIALIAS)
    resized_profile_pic_final = ImageTk.PhotoImage(resized_profile_pic)

    display_profile_pic = Label(right_frame, image = resized_profile_pic_final, 
                width = 100, bd = 2, relief = SOLID, anchor = CENTER)
    display_profile_pic.grid(row = 0, column = 0, padx = 5, pady = 5, columnspan = 4)

    # display details
    name_label = Label(right_frame, text = searched_patient_details[1], font = "evogria 30", bg = "#FFE2E2", 
                width = 40, anchor = CENTER)
    pid_label = Label(right_frame, text = searched_patient_details[0], font = "evogria 22", bg = "#FFE2E2", 
                width = 47, anchor = CENTER)

    name_label.grid(row = 1, column = 0, padx = 5, pady = 3, columnspan = 4)
    pid_label.grid(row = 2, column = 0, padx = 5, pady = 3, columnspan = 4)

    # blank label
    blank_label = Label(right_frame, text = "", bg = "#FFE2E2")
    blank_label.grid(row = 3, pady = 5)

    for i in range(6):
        blank_label = Label(right_frame, text = "", bg = "#FFE2E2")
        blank_label.grid(row = i + 4, column = 0, padx = 20)

    # labels
    age_label = Label(right_frame, text = "Age", font = "consolas 19 bold", 
            bg = "#FFE2E2", width = 13, anchor = E)

    gender_label = Label(right_frame, text = "Gender", font = "consolas 19 bold", 
            bg = "#FFE2E2", width = 13, anchor = E)

    contact_label = Label(right_frame, text = "Contact", font = "consolas 19 bold", 
            bg = "#FFE2E2", width = 13, anchor = E)

    address_label = Label(right_frame, text = "Address", font = "consolas 19 bold", 
            bg = "#FFE2E2", width = 13, anchor = E)

    blood_group_label = Label(right_frame, text = "Blood Group", font = "consolas 19 bold", 
            bg = "#FFE2E2", width = 13, anchor = E)

    appointment_label = Label(right_frame, text = "Appointment", font = "consolas 19 bold", 
            bg = "#FFE2E2", width = 13, anchor = E)

    age_label.grid(row = 4, column = 1, pady = 3, sticky = W)
    gender_label.grid(row = 5, column = 1, pady = 3, sticky = W)
    contact_label.grid(row = 6, column = 1, pady = 3, sticky = W)
    address_label.grid(row = 7, column = 1, pady = 3, sticky = W)
    blood_group_label.grid(row = 8, column = 1, pady = 3, sticky = W)
    appointment_label.grid(row = 9, column = 1, pady = 3, sticky = W)

    for i in range(6):
        colon = Label(right_frame, text = ":", font = "consolas 20 bold", bg = "#FFE2E2")
        colon.grid(row = i + 4, column = 2, sticky = W)

    # get appointment details
    if (len(searched_patient_details) == 7):
        details = "No appointments yet"
    else:
        details = "You have an appointment with {} on {}".format(searched_patient_details[7],
                                                                 searched_patient_details[8])

    # display details
    patient_details_age_label = Label(right_frame, text = searched_patient_details[2], 
            font = "consolas 19 bold", bg = "#FFE2E2", width = 15, anchor = W)

    patient_details_gender_label = Label(right_frame, text = searched_patient_details[3], 
            font = "consolas 19 bold", bg = "#FFE2E2", width = 15, anchor = W)

    patient_details_contact_label = Label(right_frame, text = searched_patient_details[4], 
            font = "consolas 19 bold", bg = "#FFE2E2", width = 15, anchor = W)

    patient_details_address_label = Label(right_frame, text = searched_patient_details[5], 
            font = "consolas 19 bold", bg = "#FFE2E2", width = 15, anchor = W)

    patient_details_blood_group_label = Label(right_frame, text = searched_patient_details[6],
            font = "consolas 19 bold", bg = "#FFE2E2", width = 15, anchor = W)

    patient_details_appointment_label = Label(right_frame, text = details, font = "consolas 19 bold", 
            bg = "#FFE2E2", width = 15, anchor = W, wraplength = 225, justify = LEFT)

    patient_details_age_label.grid(row = 4, column = 2, padx = 5, pady = 3)
    patient_details_gender_label.grid(row = 5, column = 2, padx = 5, pady = 3)
    patient_details_contact_label.grid(row = 6, column = 2, padx = 5, pady = 3)
    patient_details_address_label.grid(row = 7, column = 2, padx = 5, pady = 3)
    patient_details_blood_group_label.grid(row = 8, column = 2, padx = 5, pady = 3)
    patient_details_appointment_label.grid(row = 9, column = 2, padx = 5, pady = 3)


# doctor"s details main window
def doctors_details_window():
    doctor_id_values, doctor_name_values, doctor_age_values, \
    doctor_contact_values, doctor_specialisation_values, \
    doctor_qualification_values = doctor_details_values()

    global doctor_details
    clean_right_frame()

    # highlight clicked button
    doctor_details.grid_forget()
    doctor_details = Button(left_frame, text = "Doctor Details", font = "consolas 19 bold", 
            width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#2A363B", fg = "#FF847C", 
            anchor = CENTER, relief = SUNKEN, command = patient_details_window)
    doctor_details.grid(row = 2, column = 0, columnspan = 3, pady = 5, padx = 20)

    # Doctors details
    sno_id = 1
    doctor_id_attribute = Label(right_frame, text = "ID", font = "evogria 17", width = 4, 
            anchor = CENTER, bg = "#FFE2E2")
    doctor_id_attribute.grid(row = 0, column = 0)
    for i in doctor_id_values:
        value = Label(right_frame, text = i, font = "consolas 14", bg = "#FFE2E2")
        value.grid(row = sno_id, column = 0)
        sno_id += 1

    sno_name = 1
    doctor_name_attribute = Label(right_frame, text = "Name", font = "evogria 17", width = 10, 
            anchor = CENTER, bg = "#FFE2E2")
    doctor_name_attribute.grid(row = 0, column = 1)
    for i in doctor_name_values:
        value = Label(right_frame, text = i, font = "consolas 14", bg = "#FFE2E2")
        value.grid(row = sno_name, column = 1)
        sno_name += 1

    sno_age = 1
    doctor_age_attribute = Label(right_frame, text = "Age", font = "evogria 17", width = 4, 
            anchor = CENTER, bg = "#FFE2E2")
    doctor_age_attribute.grid(row = 0, column = 2)
    for i in doctor_age_values:
        value = Label(right_frame, text = i, font = "consolas 14", bg = "#FFE2E2")
        value.grid(row = sno_age, column = 2)
        sno_age += 1

    sno_contact = 1
    doctor_contact_attribute = Label(right_frame, text = "Contact Number", font = "evogria 17", 
            width = 15, anchor = CENTER, wraplength = 100, justify = "center", bg = "#FFE2E2")
    doctor_contact_attribute.grid(row = 0, column = 3)
    for i in doctor_contact_values:
        value = Label(right_frame, text = i, font = "consolas 14", bg = "#FFE2E2")
        value.grid(row = sno_contact, column = 3)
        sno_contact += 1

    sno_specialisation = 1
    doctor_specialisation_attribute = Label(right_frame, text = "Specialistaion", font = "evogria 17", 
            width = 15, anchor = CENTER, bg = "#FFE2E2")
    doctor_specialisation_attribute.grid(row = 0, column = 4)
    for i in doctor_specialisation_values:
        value = Label(right_frame, text = i, font = "consolas 14", anchor = W, bg = "#FFE2E2")
        value.grid(row = sno_specialisation, column = 4)
        sno_specialisation += 1

    sno_qualification = 1
    doctor_qualification_attribute = Label(right_frame, text = "Qualification", font = "evogria 17", 
            width = 15, anchor = CENTER, bg = "#FFE2E2")
    doctor_qualification_attribute.grid(row = 0, column = 5)
    for i in doctor_qualification_values:
        value = Label(right_frame, text = i, font = "consolas 14", anchor = W, wraplength = 200, 
            justify = "center", bg = "#FFE2E2")
        value.grid(row = sno_qualification, column = 5)
        sno_qualification += 1

    doctor_qualification_attribute.update()
    speak("We have one of the best Doctors of the World")


# modify details main window
def modify_details_window():
    global modify_details
    global check_pid_modify

    # get back to main menu
    home_submit()

    # check patient id
    check_pid_modify = easygui.enterbox(title = "Modify Details", msg = "Enter your PID")

    operation = """SELECT *
				FROM patient_details"""
    cursor.execute(operation)
    data = cursor.fetchall()
    existing_pid = []
    for i in data:
        existing_pid.append(str(i[0]))

    if (check_pid_modify in existing_pid):
        clean_right_frame()

        # highlight clicked button
        modify_details.grid_forget()
        modify_details = Button(left_frame, text = "Modify Details", font = "consolas 19 bold", width = 27, 
                    padx = 10, pady = 4, borderwidth = 7, bg = "#2A363B", fg = "#FF847C", anchor = CENTER, 
                    relief = SUNKEN, command = modify_details_window) 
        modify_details.grid(row = 4, column = 0, columnspan = 3, pady = 5, padx = 20)

        modify_details_after_verification()

    else:
        messagebox.showerror("Modify Details", "PID given is wrong")
        return ()


# modify details after verifying
def modify_details_after_verification():
    global old_details_frame
    global update_frame
    global field_to_update
    global updated_detail_entry
    global old_details

    # fetch old details of the patient
    operation = """SELECT *
				FROM patient_details
				WHERE pid = {}""".format(check_pid_modify)
    cursor.execute(operation)
    data = cursor.fetchone()

    old_details = [str(i) for i in data]
    for i in old_details[3]:
        if (i == "M"):
            old_details[1] = "Mr. " + old_details[1]
        else:
            old_details[1] = "Miss. " + old_details[1]

    # define frame
    # old details frame
    old_details_frame = LabelFrame(right_frame, height = 362, width = 1000, text = "Old Records", bg = "#FFE2E2")
    old_details_frame.grid(row = 0, column = 0, rowspan = 7, columnspan = 3, padx = 7)
    old_details_frame.grid_propagate(0)

    # update frame
    update_frame = LabelFrame(right_frame, height = 283, width = 1000, text = "Update Record", bg = "#FFE2E2")
    update_frame.grid(row = 8, column = 0, rowspan = 3, columnspan = 3, pady = 5, padx = 7)
    update_frame.grid_propagate(0)

    # old details
    # labels
    pid_label = Label(old_details_frame, text = "PID", font = "consolas 19 bold", bg = "#FFE2E2")
    name_label = Label(old_details_frame, text = "Name", font = "consolas 19 bold", bg = "#FFE2E2")
    age_label = Label(old_details_frame, text = "Age", font = "consolas 19 bold", bg = "#FFE2E2")
    gender_label = Label(old_details_frame, text = "Gender", font = "consolas 19 bold", bg = "#FFE2E2")
    contact_label = Label(old_details_frame, text = "Contact No.", font = "consolas 19 bold", bg = "#FFE2E2")
    address_label = Label(old_details_frame, text = "Address", font = "consolas 19 bold", bg = "#FFE2E2")
    blood_group_label = Label(old_details_frame, text = "Blood Group", font = "consolas 19 bold", bg = "#FFE2E2")

    pid_label.grid(row = 0, column = 0, padx = 5, pady = 3, sticky = W)
    name_label.grid(row = 1, column = 0, padx = 5, pady = 3, sticky = W)
    age_label.grid(row = 2, column = 0, padx = 5, pady = 3, sticky = W)
    gender_label.grid(row = 3, column = 0, padx = 5, pady = 3, sticky = W)
    contact_label.grid(row = 4, column = 0, padx = 5, pady = 3, sticky = W)
    address_label.grid(row = 5, column = 0, padx = 5, pady = 3, sticky = W)
    blood_group_label.grid(row = 6, column = 0, padx = 5, pady = 3, sticky = W)

    for i in range(7):
        colon = Label(old_details_frame, text = ":", font = "consolas 20 bold", bg = "#FFE2E2")
        colon.grid(row = i, column = 1, sticky = W)

    # old details
    display_old_pid = Button(old_details_frame, text = old_details[0], font = "consolas 19 bold", 
                    width = 27, padx = 10, borderwidth = 1, bg = "#FFE2E2", relief = GROOVE, anchor = W)

    display_name_pid = Button(old_details_frame, text = old_details[1], font = "consolas 19 bold", 
                    width = 27, padx = 10, borderwidth = 1, bg = "#FFE2E2", relief = GROOVE, anchor = W)

    display_age_pid = Button(old_details_frame, text = old_details[2], font = "consolas 19 bold", 
                    width = 27, padx = 10, borderwidth = 1, bg = "#FFE2E2", relief = GROOVE, anchor = W)

    display_gender_pid = Button(old_details_frame, text = old_details[3], font = "consolas 19 bold", 
                    width = 27, padx = 10, borderwidth = 1, bg = "#FFE2E2", relief = GROOVE, anchor = W)

    display_contact_pid = Button(old_details_frame, text = old_details[4], font = "consolas 19 bold", 
                    width = 27, padx = 10, borderwidth = 1, bg = "#FFE2E2", relief = GROOVE, anchor = W)

    display_address_pid = Button(old_details_frame, text = old_details[5], font = "consolas 19 bold", 
                    width = 27, padx = 10, borderwidth = 1, bg = "#FFE2E2", relief = GROOVE, anchor = W)

    display_blood_group_pid = Button(old_details_frame, text = old_details[6], 
                    font = "consolas 19 bold", width = 27, padx = 10, borderwidth = 1, 
                    bg = "#FFE2E2", relief = GROOVE, anchor = W)

    display_old_pid.grid(row = 0, column = 2, columnspan = 3, padx = 20, ipadx = 120)
    display_name_pid.grid(row = 1, column = 2, columnspan = 3, padx = 20, ipadx = 120)
    display_age_pid.grid(row = 2, column = 2, columnspan = 3, padx = 20, ipadx = 120)
    display_gender_pid.grid(row = 3, column = 2, columnspan = 3, padx = 20, ipadx = 120)
    display_contact_pid.grid(row = 4, column = 2, columnspan = 3, padx = 20, ipadx = 120)
    display_address_pid.grid(row = 5, column = 2, columnspan = 3, padx = 20, ipadx = 120)
    display_blood_group_pid.grid(row = 6, column = 2, columnspan = 3, padx = 20, ipadx = 120)

    # update details
    field_to_update_label = Label(update_frame, text = "Field", font = "consolas 19 bold", bg = "#FFE2E2")
    updated_detail_label = Label(update_frame, text = "New Details", font = "consolas 19 bold", bg = "#FFE2E2")

    field_to_update_label.grid(row = 0, column = 0, padx = 5, sticky = W)
    updated_detail_label.grid(row = 1, column = 0, padx = 5, sticky = W)

    for i in range(2):
        colon = Label(update_frame, text = ":", font = "consolas 20 bold", bg = "#FFE2E2")
        colon.grid(row = i, column = 1, sticky = W)

    field_to_update_options = ["Name", "Age", "Gender", "Contact", "Address", "Blood Group"]
    field_to_update = StringVar()
    field_to_update.set("Name")

    field_to_update_menu = OptionMenu(update_frame, field_to_update, *field_to_update_options)
    field_to_update_menu.config(width = 55, height = 1, font = "consolas 15 bold")
    field_to_update_menu.grid(row = 0, column = 2, columnspan = 3, padx = 15, pady = 5, sticky = W)

    updated_detail_entry = Entry(update_frame, font = "consolas 17")
    updated_detail_entry.grid(row = 1, column = 2, ipadx = 193, ipady = 5, padx = 15, pady = 10)

    # update button
    submit_button = Button(update_frame, text = "Update", font = "consolas 17 bold", bg = "#FF847C", 
                        borderwidth = 7, padx = 10, pady = 4, command = modify_submit)
    submit_button.grid(row = 5, column = 0, columnspan = 4, padx = 10, pady = 54, ipadx = 360)

    submit_button.update()
    speak("Please select the field that you want to change")


# about us window
def about_window():
    global about
    global display_profile_pic1
    global display_profile_pic2
    global display_profile_pic3
    global final_img1
    global final_img2
    global final_img3
    clean_right_frame()

    # highlight clicked button
    about.grid_forget()
    about = Button(left_frame, text = "About", font = "consolas 19 bold", width = 27, padx = 10, pady = 4,
                   borderwidth = 7, bg = "#2A363B", fg = "#FF847C", anchor = CENTER, relief = SUNKEN,
                   command = about_window)
    about.grid(row = 6, column = 0, pady = 5, padx = 20)

    # title
    about_title = Label(right_frame, text = "About Us", font = "evogria 26 bold", 
                    width = 44, anchor = CENTER, bg = "#FFE2E2")
    about_title.grid(row = 0, column = 0, padx = 5, pady = 5)

    # main content
    details_1 = str(
            "Talking about the features of this Hospital Management System, " + 
            "this project is aimed for a completely " +
            "computerised management of our fictional hospital CHASE HOSPITALS. " + 
            "A patient can register themselves, view their details " +
            "and modify their details as well. They can see the Details of Doctors, " + 
            "view the Services offered by the hospital. " +
            "They can also make an appointment to a particular doctor."
        )

    details_2 = str(
            "This project is created by Udit Pati and Robin Vats " + 
            "as part of their 12th CS project 2020 - 2021, under " +
            "the able and very helpful guidance of PGT Mr. ML Meena Sir, " + 
            "Kendriya Vidyalaya No. 2 Delhi Cantt. All codes in this file " +
            "is completely written by Udit Pati and Robin Vats only. " + 
            "All images and icons used under CC license."
        )

    about_project_label = Label(right_frame, text = "About Project", 
                    font = "evogria 18", bg = "#FFE2E2")
    about_project_label.grid(row = 1, column = 0, pady = 5, padx = 10, sticky = W)

    display_details_1 = Label(right_frame, text = details_1, font = "consolas 14", 
                    bg = "#FFE2E2", wraplength = 850, justify = LEFT)
    display_details_1.grid(row = 2, column = 0, rowspan = 4, sticky = W, pady = 10, padx = 10)

    about_developers_label = Label(right_frame, text = "About Developers", 
                    font = "evogria 18", bg = "#FFE2E2")
    about_developers_label.grid(row = 6, column = 0, pady = 10, padx = 10, sticky = W)

    display_details_2 = Label(right_frame, text = details_2, font = "consolas 14", 
                    bg = "#FFE2E2", wraplength = 850, justify = LEFT)
    display_details_2.grid(row = 7, column = 0, rowspan = 4, sticky = W, padx = 10, pady = 10)

    img3 = Image.open(r"Data\\Images\\Profile Pics\\meena_sir.jpg")
    img1 = Image.open(r"Data\\Images\\Profile Pics\\lucifer.jpg")
    img2 = Image.open(r"Data\\Images\\Profile Pics\\vats.jpg")

    resized_img1 = img1.resize((175, 175), Image.ANTIALIAS)
    resized_img2 = img2.resize((175, 175), Image.ANTIALIAS)
    resized_img3 = img3.resize((175, 175), Image.ANTIALIAS)

    final_img1 = ImageTk.PhotoImage(resized_img1)
    final_img2 = ImageTk.PhotoImage(resized_img2)
    final_img3 = ImageTk.PhotoImage(resized_img3)

    display_profile_pic1 = Label(right_frame, image = final_img1, bd = 2, relief = SOLID)
    display_profile_pic1.grid(row = 11, column = 0, padx = 30, pady = 5, sticky = W)

    display_profile_pic2 = Label(right_frame, image = final_img2, bd = 2, relief = SOLID)
    display_profile_pic2.grid(row = 11, column = 0, pady = 5)

    display_profile_pic3 = Label(right_frame, image = final_img3, bd = 2, relief = SOLID)
    display_profile_pic3.grid(row = 11, column = 0, padx = 60, pady = 5, sticky = E)

    about_title_lucifer = Label(right_frame, text = "Udit Pati", 
                    font = "evogria 16", anchor = CENTER, bg = "#FFE2E2")
    about_title_lucifer.grid(row = 12, column = 0, padx = 70, sticky = W)

    about_title_vats = Label(right_frame, text = "Robin Vats", 
                    font = "evogria 16", anchor = CENTER, bg = "#FFE2E2")
    about_title_vats.grid(row = 12, column = 0, padx = 5)

    about_title_meena_sir = Label(right_frame, text = "M L Meena Sir", font = "evogria 16", anchor = CENTER,
                                  bg = "#FFE2E2")
    about_title_meena_sir.grid(row = 12, column = 0, padx = 70, sticky = E)

    about_title_meena_sir.update()
    speak("This project is made by Udit and Robin under the guidance of M L Meena Sir PGT(Computer Science)")


# appointment window
def appointment_window():
    global appointment
    global check_pid

    # get back to main menu
    home_submit()

    # check patient id
    check_pid = easygui.enterbox(title = "Check PID", msg = "Enter your PID")
    operation = """SELECT * FROM PATIENT_DETAILS"""
    cursor.execute(operation)
    data = cursor.fetchall()
    existing_pid = []
    for i in data:
        existing_pid.append(str(i[0]))
        
    if (check_pid in existing_pid):
        clean_right_frame()
        # highlight clicked button
        appointment.grid_forget()
        appointment = Button(left_frame, text = "Appointment", font = "consolas 19 bold", 
                width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#2A363B", fg = "#FF847C", 
                anchor = CENTER, relief = SUNKEN, command = appointment_window)
        appointment.grid(row = 3, column = 0, columnspan = 3, pady = 5, padx = 20)
        appointing_the_doctor()

    else:
        messagebox.showerror("Modify Details", "PID given is wrong")
        speak("You Are Not An Existing Patient Please Register Yourself")
        return ()


date = "Pick Date"


# appointing the doctor
def appointing_the_doctor():
    global existing_doctors
    global doctor_frame
    global field_to_update
    global date_entry
    global date_pick
    global doctor_name

    # selecting doctor
    doctor_frame = LabelFrame(right_frame, height = 372, width = 1000, 
        text = "Doctor and Date select", bg = "#FFE2E2")
    doctor_frame.grid(row = 0, column = 0, rowspan = 7, columnspan = 3, padx = 7)
    doctor_frame.grid_propagate(0)

    # collecting doctors names
    operation = """SELECT * FROM doctor_details"""
    cursor.execute(operation)
    data = cursor.fetchall()

    existing_doctors = {}

    for i in data:
        existing_doctors[i[0]] = i[1]

    doctor_name = StringVar()
    doctor_name.set("Doctors")

    doctor_label = Label(doctor_frame, text = "Doctor", font = "consolas 25 bold", bg = "#FFE2E2")
    date_label = Label(doctor_frame, text = "Date", font = "consolas 25 bold", bg = "#FFE2E2")
    doctor_label.grid(row = 0, column = 0, columnspan = 3, padx = 10, sticky = W)
    date_label.grid(row = 1, column = 0, columnspan = 3, padx = 10, sticky = W)

    for i in range(2):
        colon = Label(doctor_frame, text = ":", font = "consolas 20 bold", bg = "#FFE2E2")
        colon.grid(row = i, column = 3, sticky = W)

    date_pick = Button(doctor_frame, text = date, font = "consolas 15 bold", width = 57, command = get_date)
    date_pick.grid(row = 1, column = 4, columnspan = 3, padx = 15, pady = 20, sticky = W)

    doctor_select = OptionMenu(doctor_frame, doctor_name, *list(existing_doctors.values()))
    doctor_select.config(width = 54, height = 1, font = "consolas 15 bold")
    doctor_select.grid(row = 0, column = 4, columnspan = 3, padx = 15, pady = 20, sticky = W)

    submit_button = Button(doctor_frame, text = "Submit", font = "consolas 20 bold", bg = "#FF847C", width = 55,
                           borderwidth = 7, padx = 10, pady = 4, command = appointment_submit)
    submit_button.grid(row = 6, column = 0, columnspan = 7, padx = 10, pady = 54)

    submit_button.update()
    speak("Please select the doctor and time to meet")


# date picker
def get_date():
    global date
    global date_pick

    def cal_done():
        top.withdraw()
        root.quit()

    root = Tk()
    root.withdraw()  # keep the root window from appearing

    top = Toplevel(root)
    style = ttk.Style(top)
    style.theme_use("alt")
    style.configure("style.TButton", font = "evogria 20 bold", background = "#FF847C", width = 20)
    style.map("TButton", background = [("active", "#2A363B")], foreground = [("active", "#FF847C")])

    cal = Calendar(top, font = "Arial 14", selectmode = "day", cursor = "hand2")
    cal.pack(fill = "both", expand = True)
    ttk.Button(top, text = "ok", style = "style.TButton", command = cal_done).pack()

    root.mainloop()

    date = cal.selection_get()

    date_pick.grid_forget()
    date_pick = Button(doctor_frame, text = date, font = "consolas 15 bold", width = 57, command = get_date)
    date_pick.grid(row = 1, column = 4, columnspan = 3, padx = 15, pady = 20, sticky = W)

    return date


# services window
def service_window():
    clean_left_frame()
    clean_top_frame()
    home_submit()
    
    global services_offered_frame
    global rooms
    global testing_labs
    global intensive_care_units
    global pharmacy
    global operation_theatre
    global home

    top_frame = LabelFrame(root)
    top_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 8)
    top_frame.grid_propagate(0)

    services_offered_frame = LabelFrame(root, bg = "#FFE2E2")
    services_offered_frame.grid(row = 2, column = 0, padx = 4, pady = 4, columnspan = 2, ipady = 30)

    # title
    title = Label(top_frame, text = "Services Offered", font = "evogria 45", 
                  bg = "#FFE2E2", width = 42, anchor = CENTER)
    title.pack()

    rooms = Button(services_offered_frame, text = "Rooms", font = "consolas 21 bold", width = 25, padx = 12, 
            pady = 10, borderwidth = 7, bg = "#FF847C", anchor = CENTER, command = rooms_window)

    testing_labs = Button(services_offered_frame, text = "Testing Labs", font = "consolas 21 bold", width = 25, 
            padx = 12, pady = 10, borderwidth = 7, bg = "#FF847C", 
            anchor = CENTER, command = testing_window)

    intensive_care_units = Button(services_offered_frame, text = "Intensive Care Units", font = "consolas 21 bold", 
            width = 25, padx = 12, pady = 10, borderwidth = 7, bg = "#FF847C", 
            anchor = CENTER, command = ICU_window)

    pharmacy = Button(services_offered_frame, text = "Pharmacy", font = "consolas 21 bold", width = 25, padx = 12, 
            pady = 10, borderwidth = 7, bg = "#FF847C", anchor = CENTER, command = pharmacy_window)

    operation_theatre = Button(services_offered_frame, text = "Operation Theatre", font = "consolas 21 bold", 
            width = 25, padx = 12, pady = 10, borderwidth = 7, bg = "#FF847C", 
            anchor = CENTER, command = operation_window)

    home = Button(services_offered_frame, text = "Home", font = "consolas 21 bold", width = 25, padx = 12, 
            pady = 10, borderwidth = 7, bg = "#FF847C", anchor = CENTER, 
            command = home_submit_services_offered)

    rooms.grid(row = 0, column = 0, columnspan = 3, pady = 10, padx = 20)
    testing_labs.grid(row = 1, column = 0, columnspan = 3, pady = 10, padx = 20)
    intensive_care_units.grid(row = 2, column = 0, columnspan = 3, pady = 10, padx = 20)
    pharmacy.grid(row = 3, column = 0, columnspan = 3, pady = 10, padx = 20)
    operation_theatre.grid(row = 4, column = 0, columnspan = 3, pady = 10, padx = 20)
    home.grid(row = 5, column = 0, columnspan = 3, pady = 10, padx = 20)


def rooms_window():
    clean_right_frame()
    
    wards_detail, rooms_detail, number_of_bed_detail, \
    number_of_nurse_on_assistance, specialisations_of_wards = room_values()

    # Doctors details
    sno_ward = 1
    wards_detail_attribute = Label(right_frame, text = "Wards", 
                font = "evogria 17", width = 10, anchor = CENTER, bg = "#FFE2E2")
    wards_detail_attribute.grid(row = 0, column = 0)
    
    for i in wards_detail:
        value = Label(right_frame, text = i, font = "consolas 13", bg = "#FFE2E2")
        value.grid(row = sno_ward, column = 0)
        sno_ward += 1

    sno_rooms = 1
    rooms_details_attribute = Label(right_frame, text = "Room No", 
                font = "evogria 17", width = 9, anchor = CENTER, bg = "#FFE2E2")
    rooms_details_attribute.grid(row = 0, column = 1)
    
    for i in rooms_detail:
        value = Label(right_frame, text = i, font = "consolas 13", bg = "#FFE2E2")
        value.grid(row = sno_rooms, column = 1)
        sno_rooms += 1

    sno_number_of_bed = 1
    no_of_bed_attribute = Label(right_frame, text = "No. of Bed", 
                font = "evogria 17", width = 11, wraplength = 100, 
                justify = CENTER, anchor = CENTER, bg = "#FFE2E2")
    no_of_bed_attribute.grid(row = 0, column = 2)
    
    for i in number_of_bed_detail:
        value = Label(right_frame, text = i, font = "consolas 13", bg = "#FFE2E2")
        value.grid(row = sno_number_of_bed, column = 2)
        sno_number_of_bed += 1

    sno_number_of_assistance = 1
    number_of_assistance_attribute = Label(right_frame, text = "Number of Assistants", 
            font = "evogria 17", width = 12, anchor = CENTER, wraplength = 200, 
            justify = "center", bg = "#FFE2E2")
    number_of_assistance_attribute.grid(row = 0, column = 3)
    
    for i in number_of_nurse_on_assistance:
        value = Label(right_frame, text = i, font = "consolas 13", bg = "#FFE2E2")
        value.grid(row = sno_number_of_assistance, column = 3)
        sno_number_of_assistance += 1

    sno_specialisations = 1
    specialisations_of_wards_attribute = Label(right_frame, text = "Specialistaion", 
                    font = "evogria 17", width = 15, anchor = CENTER, bg = "#FFE2E2")
    specialisations_of_wards_attribute.grid(row = 0, column = 4)
    
    for i in specialisations_of_wards:
        value = Label(right_frame, text = i, font = "consolas 13", wraplength = 297, 
            justify = CENTER, anchor = W, bg = "#FFE2E2")
        value.grid(row = sno_specialisations, column = 4)
        sno_specialisations += 1


def testing_window():
    clean_top_frame()
    home_submit()

    global urine_test
    global blood_test
    global research
    global central
    global resized_images

    top_frame = LabelFrame(root)
    top_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 8)
    top_frame.grid_propagate(0)

    left_frame = LabelFrame(root, bg = "#FFE2E2")
    left_frame.grid(row = 2, column = 0, padx = 4, pady = 4, columnspan = 2, ipady = 30)

    # title
    title = Label(top_frame, text = "Laboratories", font = "evogria 45", 
        bg = "#FFE2E2", width = 42, anchor = CENTER)
    title.pack()

    urine_test = Button(left_frame, text = "Urine Test Lab", font = "consolas 19 bold", width = 27, 
                        padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                        anchor = CENTER, command = urine_test_window)

    blood_test = Button(left_frame, text = "Blood Test Lab", font = "consolas 19 bold", width = 27, 
                        padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                        anchor = CENTER, command = blood_test_window)

    research = Button(left_frame, text = "Research Lab", font = "consolas 19 bold", width = 27, 
                        padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                        anchor = CENTER, command = research_window)

    central = Button(left_frame, text = "Central Lab", font = "consolas 19 bold", width = 27, 
                        padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                        anchor = CENTER, command = central_window)

    Home = Button(left_frame, text = "Home", font = "consolas 19 bold", width = 27, padx = 10, 
                        pady = 4, borderwidth = 7, bg = "#FF847C", anchor = CENTER, 
                        command = home_submit_services_offered)

    urine_test.grid(row = 0, column = 0, columnspan = 3, pady = 30, padx = 20)
    blood_test.grid(row = 1, column = 0, columnspan = 3, pady = 30, padx = 20)
    research.grid(row = 2, column = 0, columnspan = 3, pady = 30, padx = 20)
    central.grid(row = 3, column = 0, columnspan = 3, pady = 30, padx = 20)
    Home.grid(row = 4, column = 0, columnspan = 3, pady = 31, padx = 20)


def urine_test_window():
    global display_img
    global status_bar
    global num
    global resized_images
    
    clean_right_frame()

    img1 = Image.open(r"Data\\Images\\Services\\urine_test_photo1.jpg")
    img2 = Image.open(r"Data\\Images\\Services\\urine_test_photo2.jpg")
    img3 = Image.open(r"Data\\Images\\Services\\urine_test_photo3.jpg")
    img4 = Image.open(r"Data\\Images\\Services\\urine_test_photo2.png")

    resized_img1 = img1.resize((865, 610), Image.ANTIALIAS)
    resized_img2 = img2.resize((865, 610), Image.ANTIALIAS)
    resized_img3 = img3.resize((865, 610), Image.ANTIALIAS)
    resized_img4 = img4.resize((865, 610), Image.ANTIALIAS)

    final_img1 = ImageTk.PhotoImage(resized_img1)
    final_img2 = ImageTk.PhotoImage(resized_img2)
    final_img3 = ImageTk.PhotoImage(resized_img3)
    final_img4 = ImageTk.PhotoImage(resized_img4)
    resized_images = [final_img1, final_img2, final_img3, final_img4]

    display_img = Label(right_frame, image = final_img1)
    display_img.grid(row = 0, column = 0, rowspan = 3, columnspan = 3)

    status_bar = Label(right_frame, text = ("Image 1 of " + str(len(resized_images))), bd = 2, 
                relief = SUNKEN, anchor = E)
    status_bar.grid(row = 5, column = 0, columnspan = 3, sticky = W + E)

    num = 0

    bkwd_button = Button(right_frame, text = "<<", width = 5, 
        borderwidth = 5, command = lambda: backward_button(num))
    bkwd_button.grid(row = 4, column = 0)

    exit_button = Button(right_frame, text = "Exit Program", width = 10, borderwidth = 5, command = home_submit)
    exit_button.grid(row = 4, column = 1, pady = 10)

    fwd_button = Button(right_frame, text = ">>", width = 5, 
        borderwidth = 5, command = lambda: forward_button(num))
    fwd_button.grid(row = 4, column = 2)


def blood_test_window():
    global display_img
    global status_bar
    global num
    global resized_images
    
    clean_right_frame()

    img1 = Image.open(r"Data\\Images\\Services\\blood_test_photo1.jpg")
    img2 = Image.open(r"Data\\Images\\Services\\blood_test_photo2.jpg")
    img3 = Image.open(r"Data\\Images\\Services\\bloodtest_photo3.jpg")
    img4 = Image.open(r"Data\\Images\\Services\\blood_test_photo4.jpg")

    resized_img1 = img1.resize((865, 610), Image.ANTIALIAS)
    resized_img2 = img2.resize((865, 610), Image.ANTIALIAS)
    resized_img3 = img3.resize((865, 610), Image.ANTIALIAS)
    resized_img4 = img4.resize((865, 610), Image.ANTIALIAS)

    final_img1 = ImageTk.PhotoImage(resized_img1)
    final_img2 = ImageTk.PhotoImage(resized_img2)
    final_img3 = ImageTk.PhotoImage(resized_img3)
    final_img4 = ImageTk.PhotoImage(resized_img4)
    resized_images = [final_img1, final_img2, final_img3, final_img4]

    display_img = Label(right_frame, image = final_img1)
    display_img.grid(row = 0, column = 0, rowspan = 3, columnspan = 3)

    status_bar = Label(right_frame, text = ("Image 1 of " + str(len(resized_images))), bd = 2, relief = SUNKEN,
                       anchor = E)
    status_bar.grid(row = 5, column = 0, columnspan = 3, sticky = W + E)

    num = 0

    bkwd_button = Button(right_frame, text = "<<", width = 5, 
        borderwidth = 5, command = lambda: backward_button(num))
    bkwd_button.grid(row = 4, column = 0)

    exit_button = Button(right_frame, text = "Exit Program", width = 10, borderwidth = 5, command = home_submit)
    exit_button.grid(row = 4, column = 1, pady = 10)

    fwd_button = Button(right_frame, text = ">>", width = 5, 
        borderwidth = 5, command = lambda: forward_button(num))
    fwd_button.grid(row = 4, column = 2)


def research_window():
    global display_img
    global status_bar
    global num
    global resized_images
    
    clean_right_frame()

    img1 = Image.open(r"Data\\Images\\Services\\research1.jpg")
    img2 = Image.open(r"Data\\Images\\Services\\research2.jpg")
    img3 = Image.open(r"Data\\Images\\Services\\research3.jpg")

    resized_img1 = img1.resize((865, 610), Image.ANTIALIAS)
    resized_img2 = img2.resize((865, 610), Image.ANTIALIAS)
    resized_img3 = img3.resize((865, 610), Image.ANTIALIAS)

    final_img1 = ImageTk.PhotoImage(resized_img1)
    final_img2 = ImageTk.PhotoImage(resized_img2)
    final_img3 = ImageTk.PhotoImage(resized_img3)
    resized_images = [final_img1, final_img2, final_img3]

    display_img = Label(right_frame, image = final_img1)
    display_img.grid(row = 0, column = 0, rowspan = 3, columnspan = 3)

    status_bar = Label(right_frame, text = ("Image 1 of " + str(len(resized_images))), bd = 2, relief = SUNKEN,
                       anchor = E)
    status_bar.grid(row = 5, column = 0, columnspan = 3, sticky = W + E)

    num = 0

    bkwd_button = Button(right_frame, text = "<<", width = 5, 
        borderwidth = 5, command = lambda: backward_button(num))
    bkwd_button.grid(row = 4, column = 0)

    exit_button = Button(right_frame, text = "Exit Program", width = 10, borderwidth = 5, command = home_submit)
    exit_button.grid(row = 4, column = 1, pady = 10)

    fwd_button = Button(right_frame, text = ">>", width = 5, 
        borderwidth = 5, command = lambda: forward_button(num))
    fwd_button.grid(row = 4, column = 2)


def central_window():
    global display_img
    global status_bar
    global num
    global resized_images
    
    clean_right_frame()

    img1 = Image.open(r"Data\\Images\\Services\\central1.jpg")
    img2 = Image.open(r"Data\\Images\\Services\\central2.jpg")

    resized_img1 = img1.resize((865, 610), Image.ANTIALIAS)
    resized_img2 = img2.resize((865, 610), Image.ANTIALIAS)

    final_img1 = ImageTk.PhotoImage(resized_img1)
    final_img2 = ImageTk.PhotoImage(resized_img2)
    resized_images = [final_img1, final_img2]

    display_img = Label(right_frame, image = final_img1)
    display_img.grid(row = 0, column = 0, rowspan = 3, columnspan = 3)

    status_bar = Label(right_frame, text = ("Image 1 of " + str(len(resized_images))), bd = 2, relief = SUNKEN,
                       anchor = E)
    status_bar.grid(row = 5, column = 0, columnspan = 3, sticky = W + E)

    num = 0

    bkwd_button = Button(right_frame, text = "<<", width = 5, 
        borderwidth = 5, command = lambda: backward_button(num))
    bkwd_button.grid(row = 4, column = 0)

    exit_button = Button(right_frame, text = "Exit Program", width = 10, borderwidth = 5, command = home_submit)
    exit_button.grid(row = 4, column = 1, pady = 10)

    fwd_button = Button(right_frame, text = ">>", width = 5, 
        borderwidth = 5, command = lambda: forward_button(num))
    fwd_button.grid(row = 4, column = 2)


def ICU_window():
    global display_img
    global status_bar
    global num
    global resized_images
    
    clean_right_frame()

    img1 = Image.open(r"Data\\Images\\Services\\icu_image_1.jpg")
    img2 = Image.open(r"Data\\Images\\Services\\icu_image2.jpg")
    img3 = Image.open(r"Data\\Images\\Services\\icu_image3.jpg")

    resized_img1 = img1.resize((865, 610), Image.ANTIALIAS)
    resized_img2 = img2.resize((865, 610), Image.ANTIALIAS)
    resized_img3 = img3.resize((865, 610), Image.ANTIALIAS)

    final_img1 = ImageTk.PhotoImage(resized_img1)
    final_img2 = ImageTk.PhotoImage(resized_img2)
    final_img3 = ImageTk.PhotoImage(resized_img3)
    resized_images = [final_img1, final_img2, final_img3]

    display_img = Label(right_frame, image = final_img1)
    display_img.grid(row = 0, column = 0, rowspan = 3, columnspan = 3)

    status_bar = Label(right_frame, text = ("Image 1 of " + str(len(resized_images))), bd = 2, relief = SUNKEN,
                       anchor = E)
    status_bar.grid(row = 5, column = 0, columnspan = 3, sticky = W + E)

    num = 0

    bkwd_button = Button(right_frame, text = "<<", width = 5, 
        borderwidth = 5, command = lambda: backward_button(num))
    bkwd_button.grid(row = 4, column = 0)

    exit_button = Button(right_frame, text = "Exit Program", width = 10, borderwidth = 5, command = home_submit)
    exit_button.grid(row = 4, column = 1, pady = 10)

    fwd_button = Button(right_frame, text = ">>", width = 5, 
        borderwidth = 5, command = lambda: forward_button(num))
    fwd_button.grid(row = 4, column = 2)


def operation_window():
    global display_img
    global status_bar
    global num
    global resized_images
    
    clean_right_frame()

    img1 = Image.open(r"Data\\Images\\Services\\OT_1.jpg")
    img2 = Image.open(r"Data\\Images\\Services\\OT2.jpg")
    img3 = Image.open(r"Data\\Images\\Services\\OT3.jpg")

    resized_img1 = img1.resize((865, 610), Image.ANTIALIAS)
    resized_img2 = img2.resize((865, 610), Image.ANTIALIAS)
    resized_img3 = img3.resize((865, 610), Image.ANTIALIAS)

    final_img1 = ImageTk.PhotoImage(resized_img1)
    final_img2 = ImageTk.PhotoImage(resized_img2)
    final_img3 = ImageTk.PhotoImage(resized_img3)
    resized_images = [final_img1, final_img2, final_img3]

    display_img = Label(right_frame, image = final_img1)
    display_img.grid(row = 0, column = 0, rowspan = 3, columnspan = 3)

    status_bar = Label(right_frame, text = ("Image 1 of " + str(len(resized_images))), bd = 2, relief = SUNKEN,
                       anchor = E)
    status_bar.grid(row = 5, column = 0, columnspan = 3, sticky = W + E)

    num = 0

    bkwd_button = Button(right_frame, text = "<<", width = 5, 
        borderwidth = 5, command = lambda: backward_button(num))
    bkwd_button.grid(row = 4, column = 0)

    exit_button = Button(right_frame, text = "Exit Program", width = 10, borderwidth = 5, command = home_submit)
    exit_button.grid(row = 4, column = 1, pady = 10)

    fwd_button = Button(right_frame, text = ">>", width = 5, 
        borderwidth = 5, command = lambda: forward_button(num))
    fwd_button.grid(row = 4, column = 2)


def pharmacy_window():
    global display_img
    global status_bar
    global num
    global resized_images
    
    clean_right_frame()

    img1 = Image.open(r"Data\\Images\\Services\\pharmacy_image1.jpg")
    img2 = Image.open(r"Data\\Images\\Services\\pharmacy_image2.jpg")

    resized_img1 = img1.resize((865, 610), Image.ANTIALIAS)
    resized_img2 = img2.resize((865, 610), Image.ANTIALIAS)

    final_img1 = ImageTk.PhotoImage(resized_img1)
    final_img2 = ImageTk.PhotoImage(resized_img2)
    resized_images = [final_img1, final_img2]

    display_img = Label(right_frame, image = final_img1)
    display_img.grid(row = 0, column = 0, rowspan = 3, columnspan = 3)

    status_bar = Label(right_frame, text = ("Image 1 of " + str(len(resized_images))), 
            bd = 2, relief = SUNKEN, anchor = E)
    status_bar.grid(row = 5, column = 0, columnspan = 3, sticky = W + E)

    num = 0

    bkwd_button = Button(right_frame, text = "<<", width = 5, 
        borderwidth = 5, command = lambda: backward_button(num))
    bkwd_button.grid(row = 4, column = 0)

    exit_button = Button(right_frame, text = "Exit Program", width = 10, borderwidth = 5, command = home_submit)
    exit_button.grid(row = 4, column = 1, pady = 10)

    fwd_button = Button(right_frame, text = ">>", width = 5, 
        borderwidth = 5, command = lambda: forward_button(num))
    fwd_button.grid(row = 4, column = 2)


# forward and backward button for image carousel
def forward_button(n):
    global num
    global display_img
    global status_bar
    global resized_images
    global right_frame

    if (num == 1):
        return

    display_img.grid_forget()
    display_img = Label(right_frame, image = resized_images[n + 1])
    display_img.grid(row = 0, column = 0, rowspan = 3, columnspan = 3)

    status_bar.grid_forget()
    status_bar = Label(right_frame, text = ("Image " + str(n + 2) + " of " + str(len(resized_images))), bd = 2,
                       relief = SUNKEN, anchor = E)
    status_bar.grid(row = 5, column = 0, columnspan = 3, sticky = W + E)
    num += 1


def backward_button(n):
    global display_img
    global status_bar
    global num
    global resized_images
    global right_frame

    if (num == 0):
        return

    display_img.grid_forget()
    display_img = Label(right_frame, image = resized_images[n - 1])
    display_img.grid(row = 0, column = 0, rowspan = 3, columnspan = 3)

    status_bar = Label(right_frame, text = ("Image " + str(n) + " of " + str(len(resized_images))), bd = 2,
                       relief = SUNKEN, anchor = E)
    status_bar.grid(row = 5, column = 0, columnspan = 3, sticky = W + E)

    num -= 1


# return to main menu
def home_submit():
    global right_frame
    global resized_logo_main
    clean_right_frame()

    # display logo in main window
    logo_main = Image.open(r"Data\\Images\\Icons\\Logo3.jpg")
    resized_main = logo_main.resize((970, 692), Image.ANTIALIAS)
    resized_logo_main = ImageTk.PhotoImage(resized_main)

    display_logo_main = Label(right_frame, image = resized_logo_main)
    display_logo_main.pack()


# starting window
def main_window():
    global registration
    global patient_details
    global doctor_details
    global appointment
    global modify_details
    global services
    global about

    # define buttons in left frame
    registration = Button(left_frame, text = "Registration", font = "consolas 19 bold", 
                    width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                    anchor = CENTER, command = registration_window)

    patient_details = Button(left_frame, text = "Patient Details", font = "consolas 19 bold", 
                    width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                    anchor = CENTER, command = patient_details_window)

    doctor_details = Button(left_frame, text = "Doctor Details", font = "consolas 19 bold", 
                    width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                    anchor = CENTER, command = doctors_details_window)

    appointment = Button(left_frame, text = "Appointment", font = "consolas 19 bold", 
                    width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                    anchor = CENTER, command = appointment_window)

    modify_details = Button(left_frame, text = "Modify Details", font = "consolas 19 bold", 
                    width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                    anchor = CENTER, command = modify_details_window)

    services = Button(left_frame, text = "Services Offered", font = "consolas 19 bold", 
                    width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                    anchor = CENTER, command = service_window)

    about = Button(left_frame, text = "About", font = "consolas 19 bold", 
                    width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                    anchor = CENTER, command = about_window)

    home = Button(left_frame, text = "Home", font = "consolas 19 bold", 
                    width = 27, padx = 10, pady = 4, borderwidth = 7, bg = "#FF847C", 
                    anchor = CENTER, command = home_submit)

    registration.grid(row = 0, column = 0, columnspan = 3, pady = 5, padx = 20)
    patient_details.grid(row = 1, column = 0, columnspan = 3, pady = 5, padx = 20)
    doctor_details.grid(row = 2, column = 0, columnspan = 3, pady = 5, padx = 20)
    appointment.grid(row = 3, column = 0, columnspan = 3, pady = 5, padx = 20)
    modify_details.grid(row = 4, column = 0, columnspan = 3, pady = 5, padx = 20)
    services.grid(row = 5, column = 0, columnspan = 3, pady = 5, padx = 20)
    about.grid(row = 6, column = 0, columnspan = 3, pady = 5, padx = 20)
    home.grid(row = 7, column = 0, columnspan = 3, pady = 5, padx = 20)


main_window()


# home button for services offered
def home_submit_services_offered():
    global left_frame
    global top_frame
    global right_frame

    left_frame.grid_forget()
    top_frame.grid_forget()

    # top frame (constant)
    top_frame = LabelFrame(root)
    top_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 8)
    top_frame.grid_propagate(0)

    # title
    title = Label(top_frame, text = "Chase Hospitals", font = "evogria 45", 
        bg = "#FFE2E2", width = 42, anchor = CENTER)
    title.pack()

    # left frame (constant)
    left_frame = LabelFrame(root, bg = "#FFE2E2")
    left_frame.grid(row = 2, column = 0, padx = 4, pady = 4, columnspan = 3, ipady = 40)

    home_submit()


# display logo in main window
logo_main = Image.open(r"Data\\Images\\Icons\\Logo3.jpg")
resized_main = logo_main.resize((970, 692), Image.ANTIALIAS)
resized_logo_main = ImageTk.PhotoImage(resized_main)

display_logo_main = Label(right_frame, image = resized_logo_main)
display_logo_main.pack()


# ask MySQL username and password
def ask_MySQL_username_password():
    global MySQL_username
    global MySQL_password

    username_confirm = messagebox.askokcancel("MySQL Username", 
        "Please click on OK if your MySQL username is root")

    if (username_confirm == 0):
        speak("Please enter your MySQL username")
        MySQL_username = easygui.enterbox(title = "MySQL Username", msg = "ENTER YOUR MY-SQL USERNAME: ")

    else:
        MySQL_username = "root"

    speak("Please enter your MySQL password")
    MySQL_password = easygui.passwordbox(title = "MySQL Password", msg = "ENTER YOUR MySQL PASSWORD: ")


ask_MySQL_username_password()


# connect to database
def connect_with_database():
    global dbcon
    global cursor
    dbcon = sqlcon.connect(
        host = "localhost",
        user = MySQL_username,
        password = MySQL_password,
    )
    cursor = dbcon.cursor()

    speak("Successfully established connection with Database")


try:
    connect_with_database()
except:
    speak("Your MySQL username or password is incorrect. Please try again")
    ask_MySQL_username_password()
    connect_with_database()


def create_database_and_table():
    operation = """CREATE DATABASE IF NOT EXISTS chase_hospitals"""
    cursor.execute(operation)

    operation = """USE chase_hospitals"""
    cursor.execute(operation)

    operation = """CREATE TABLE IF NOT EXISTS patient_details(
					pid            BIGINT          NOT NULL  AUTO_INCREMENT    PRIMARY KEY,
					name           VARCHAR(50)     NOT NULL,
					age            INTEGER         NOT NULL,
					gender         VARCHAR(20)     NOT NULL,
					contact        BIGINT          NOT NULL,
					address        VARCHAR(99)     NOT NULL,
					blood_group    VARCHAR(20)     NOT NULL)"""
    cursor.execute(operation)

    operation = """CREATE TABLE IF NOT EXISTS doctor_details(
					did             BIGINT         NOT NULL    PRIMARY KEY,
					name            VARCHAR(50)    NOT NULL,
					age             INTEGER        NOT NULL,
					contact         BIGINT         NOT NULL,
					specialisation  VARCHAR(99)    NOT NULL,
					qualification   VARCHAR(99)    NOT NULL)"""
    cursor.execute(operation)

    operation = """CREATE TABLE IF NOT EXISTS appointment(
					pid                BIGINT      NOT NULL  PRIMARY KEY,
					did                BIGINT      NOT NULL,
					appointment_date   VARCHAR(20) NOT NULL)"""
    cursor.execute(operation)

    operation = """CREATE TABLE IF NOT EXISTS rooms(
					wards                              VARCHAR(20)     NOT NULL PRIMARY KEY,
					rooms_no                           INTEGER         NOT NULL,
					number_of_beds                     INTEGER         NOT NULL,
					number_of_nurse_on_assistance      INTEGER         NOT NULL,
					specialisations_of_wards           VARCHAR(99)     NOT NULL)"""
    cursor.execute(operation)


create_database_and_table()


def insert_bydefault_data():
    operation = """INSERT INTO patient_details VALUES
					(313570101, "Udit Pati", 17, "M", 8375054875, "Delhi", "O+"),
					(313570102, "Robin Vats", 17, "M", 7567563156, "Delhi", "O+"),
					(313570103, "Rahul Roy", 18, "M", 8345671848, "Mumbai", "A+"),
					(313570104, "Aditya Manas", 16, "M", 7534586798, "Jaipur", "B+")"""
    cursor.execute(operation)
    # dbcon.commit()

    operation = """INSERT INTO doctor_details VALUES
                    (101, "Dr. Rakesh Sharma", 35, 7658424743,"Dentist", "Bachelor of Dental Surgery"),
                    (102, "Dr. Patiiii", 67, 9427365092, "Ayurveda", 
                    "Bachelor of Ayurvedic Medicine and Surgery"),
                    (103, "Dr. P.K Sharma", 40, 7248743423, "Medicine", "MBBS Ph.D"),
                    (104, "Dr. K.P Kohli", 44, 8493883433, "Cardiologists", "MBBS M.Phil M.D"),
                    (105, "Dr. S.K Patil", 44, 7839478943, "Surgeon", "MBBS"),
                    (106, "Dr. D.K Tripathi", 46, 9173826433, "Orthopaedics", "MBBS"),
                    (107, "Dr. Rahul Poonia", 30, 9485757483, "Cardiologists", "MBBS"),
                    (108, "Dr. Unnikrishnan", 23, 9876346843, "Osteopathologist", "MBBS DO Phd M.D"),
                    (109, "Dr. Batra", 32, 9874758843, "Radiologist", "MBBS DMSC MMSc"),
                    (110, "Dr. Manoj", 27, 9546738843, "General Surgeon", "MBBS MD(Res) MS MSurg"),
                    (111, "Dr. Yadav", 39, 9578495743, "Medicine", "MM MMed"),
                    (112, "Dr. Pal", 34, 9856784938, "Medicine", "MBBS MMedSc MM"),
                    (113, "Dr. Shukla", 45, 8756493756, "General Surgeon", "MBBS MPhil MChir"),
                    (114, "Dr. Singh", 37, 8564789456, "Ayurveda", "Bachelor of Ayurvedic Medicine"),
                    (115, "Dr. Amit", 38, 8452378940, "Cardiologists", "MBBS MPhil MD D.O"),
                    (116, "Dr. Shyam", 41, 7456328975, "Neurologists", "MBBS MPhil DO")"""
    cursor.execute(operation)

    operation = """INSERT INTO rooms VALUES
					("Blood Bank", 48, 9, 6, "Blood Test Also Available"),
					("CT-Scan", 37, 1, 4, "Machines Are Highly Advanced"),
					("Emergency", 32, 5, 4, "Each Bed Has A Specialist 24*7"),
					("General Ward I", 29, 50, 2, "Each  Has Two Specialist Doctors Available 24*7"),
					("General Ward II", 30, 40, 3, "Each Ward Has Specialist Doctors Available 24*7"),
					("General Ward III", 31, 25, 4, "One Doctor Assigned Three Beds"),
					("ICU", 34, 28, 14, "Pediatrician Also Available"),
					("MI Room", 12, 20, 15, "General Surgeon On 24*7 Duty"),
					("MRI Center", 36, 1, 2, "MRI Technologists Present 24*7"),
					("Orthopaedic Room", 33, 2, 1, "Present Further Examination Of Patients"),
					("Private Room I", 45, 1, 1, "Facilities Available Like Your House"),
					("Private Room II", 46, 1, 1, "All Facilities Available Just Like Your House"),
					("Private Room III", 47, 10, 2, "10 Private Room"),
					("Testing Lab", 44, 4, 3, "24*7 Testing Available"),
					("X-Ray", 35, 1, 2, "X-Ray Report After 10 Minutes")"""
    cursor.execute(operation)
    dbcon.commit()


speak("Do you want to insert some by default data in the database?")
by_default_data_confirm = messagebox.askyesno("Database",
                        "Do you want to insert some BY - DEFAULT DATA in the database?")

if (by_default_data_confirm == 1):
    try:
        insert_bydefault_data()
        speak("Data inserted successfully")
        speak("Welcome to Chase Hospitals. How can I help you?")
    except:
        speak("Data already inserted in the Database")
        speak("Welcome to Chase Hospitals. How can I help you?")
        pass


# register button in registration window (insert data into the database)
def registration_submit():
    global name_entry
    global age_entry
    global gender_entry
    global address_entry
    global blood_group_entry

    # insert data into the database
    name = str(name_entry.get())
    age = str(age_entry.get())
    gender = str(gender_entry.get()[0]).upper()
    contact = str(contact_entry.get())
    address = str(address_entry.get())
    blood_group = str(blood_group_entry.get()).upper()

    data = [name, age, gender, contact, address, blood_group]
    for i in data:
        if (i == contact):
            if (len(i) != 10):
                messagebox.showerror("Database", "Please enter valid Contact Number")
                return
        elif (i == blood_group):
            valid_blood_group = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
            if (i not in valid_blood_group):
                messagebox.showerror("Database", "PLease enter valid Blood Group")
                return
        elif (len(i) == 0):
            messagebox.showerror("Database", "Please fill all Details")
            return

    operation = """INSERT INTO patient_details(name, age, gender, contact, address, blood_group) VALUES
					("{}", {}, "{}", {}, "{}", "{}")""".format(name, age, gender, contact, 
                        address, blood_group)
    cursor.execute(operation)
    dbcon.commit()

    # clear the entry boxes
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    gender_entry.delete(0, END)
    contact_entry.delete(0, END)
    address_entry.delete(0, END)
    blood_group_entry.delete(0, END)

    # get patient id
    operation = """SELECT *
				FROM patient_details"""
    cursor.execute(operation)
    data = cursor.fetchall()
    pid = str(data[-1][0])

    speak("Record added successfully!")
    messagebox.showinfo("Database", "Your PID is: {}".format(pid))


# search button in patient details window
num = 3


def patient_details_search_submit():
    global num
    global field_to_search
    global search_detail_entry
    global field_to_search_2
    global search_detail_entry_2
    global field_to_search_3
    global search_detail_entry_3
    global searched_patient_details

    # search details
    field_to_search_value = field_to_search.get()
    search_value = search_detail_entry.get()

    # check if value is empty
    if (search_value == ""):
        return

    # chnage value if field is blood group
    if (field_to_search_value == "Blood Group"):
        field_to_search_value = "blood_group"

    # check if multiple values are present
    if (num == 3):
        # fetch values from database
        operation = """SELECT *
					FROM patient_details
					WHERE {} LIKE "%{}%"
					""".format(field_to_search_value, search_value)
        cursor.execute(operation)
        data = cursor.fetchall()

        if (len(data) == 0):
            speak("Record Not Found")
            messagebox.showinfo("Database", "Record not found")
            return

        elif (len(data) > 1):
            speak("{} records found. Please enter additional details to narrow down the search".format(
                len(data)))
            multiple_fields_search_patient_details(num)
            num += 3
            return

    elif (num == 6):
        # search details
        field_to_search_value_2 = field_to_search_2.get()
        search_value_2 = search_detail_entry_2.get()

        if (field_to_search_value_2 == "Blood Group"):
            field_to_search_value_2 = "blood_group"

        operation = """SELECT *
				FROM patient_details
				WHERE {} LIKE "%{}%"
				AND {} LIKE "%{}%"
				""".format(field_to_search_value, search_value, field_to_search_value_2, search_value_2)
        cursor.execute(operation)
        data = cursor.fetchall()

        if (len(data) == 0):
            speak("Record Not Found")
            messagebox.showinfo("Database", "Record not found")
            return

        elif (len(data) > 1):
            speak("{} records found. Please enter additional details to narrow down the search".format(
                len(data)))
            multiple_fields_search_patient_details(num)
            num += 3
            return

    else:
        # search details
        field_to_search_value_2 = field_to_search_2.get()
        field_to_search_value_3 = field_to_search_3.get()
        search_value_2 = search_detail_entry_2.get()
        search_value_3 = search_detail_entry_3.get()

        if (field_to_search_value_3 == "Blood Group"):
            field_to_search_value_3 = "blood_group"

        operation = """SELECT *
				FROM patient_details
				WHERE {} LIKE "%{}%"
				AND {} LIKE "%{}%"
				AND {} LIKE "%{}%"
				""".format(field_to_search_value, search_value, field_to_search_value_2, search_value_2,
                           field_to_search_value_3, search_value_3)
        cursor.execute(operation)
        data = cursor.fetchall()

        if (len(data) == 0):
            speak("Record Not Found")
            messagebox.showinfo("Database", "Record not found")
            return

        elif (len(data) > 1):
            speak("Numerous records found. Please check your details")
            messagebox.showinfo("Database", "Numerous records found. Please check your details")
            return

    if (len(data) == 1):
        searched_patient_details = [str(i) for i in data[0]]

        # fetch appointment details
        operation = """SELECT did, appointment_date
					FROM appointment
					WHERE pid = {}""".format(searched_patient_details[0])
        cursor.execute(operation)
        records = cursor.fetchall()

        if (len(records) != 0):
            operation = """SELECT name
						FROM doctor_details
						WHERE did = {}""".format(int(records[0][0]))
            cursor.execute(operation)
            doctor_name = cursor.fetchall()
            records = [doctor_name[0][0], records[0][1]]
            searched_patient_details.extend(records)

        display_patient_details_after_search()
        return


# display multiple fields to search if multiple values are fetched
def multiple_fields_search_patient_details(num):
    global field_to_search
    global search_detail_entry
    global field_to_search_2
    global search_detail_entry_2
    global field_to_search_3
    global search_detail_entry_3
    global submit_button

    submit_button.grid_forget()

    # select a field to search
    field_to_search_label = Label(right_frame, text = "Field", font = "consolas 19 bold", bg = "#FFE2E2")
    search_detail_label = Label(right_frame, text = "Details", font = "consolas 19 bold", bg = "#FFE2E2")

    field_to_search_label.grid(row = num, column = 0, padx = 5, sticky = W)
    search_detail_label.grid(row = 1 + num, column = 0, padx = 5, sticky = W)

    for j in range(2):
        colon = Label(right_frame, text = ":", font = "consolas 20 bold", bg = "#FFE2E2")
        colon.grid(row = j + num, column = 1, sticky = W)

    field_to_search_options = ["PID", "Name", "Age", "Gender", "Contact", "Address", "Blood Group"]

    if (num == 3):
        field_to_search_2 = StringVar()
        field_to_search_2.set("Name")

        field_to_search_menu_2 = OptionMenu(right_frame, field_to_search_2, *field_to_search_options)
        field_to_search_menu_2.config(width = 62, height = 1, font = "consolas 15 bold")
        field_to_search_menu_2.grid(row = num, column = 2, columnspan = 3, padx = 15, pady = 5, sticky = W)

        search_detail_entry_2 = Entry(right_frame, font = "consolas 17")
        search_detail_entry_2.grid(row = 1 + num, column = 2, ipadx = 230, ipady = 5, padx = 15, pady = 10)

    elif (num == 6):
        field_to_search_3 = StringVar()
        field_to_search_3.set("Name")

        field_to_search_menu_3 = OptionMenu(right_frame, field_to_search_3, *field_to_search_options)
        field_to_search_menu_3.config(width = 62, height = 1, font = "consolas 15 bold")
        field_to_search_menu_3.grid(row = num, column = 2, columnspan = 3, padx = 15, pady = 5, sticky = W)

        search_detail_entry_3 = Entry(right_frame, font = "consolas 17")
        search_detail_entry_3.grid(row = 1 + num, column = 2, ipadx = 230, ipady = 5, padx = 15, pady = 10)

    # search button
    submit_button = Button(right_frame, text = "Search", font = "consolas 17 bold", bg = "#FF847C", 
                    borderwidth = 7, padx = 10, pady = 4, command = patient_details_search_submit)
    submit_button.grid(row = 2 + num, column = 0, columnspan = 4, padx = 10, pady = 54, ipadx = 375)


# backend data for doctor details
def doctor_details_values():
    operation = """SELECT * FROM doctor_details"""
    cursor.execute(operation)
    data = cursor.fetchall()

    doctor_id_values = []
    doctor_name_values = []
    doctor_age_values = []
    doctor_contact_values = []
    doctor_specialisation_values = []
    doctor_qualification_values = []

    for i in data:
        doctor_id_values.append(i[0])
        doctor_name_values.append(i[1])
        doctor_age_values.append(i[2])
        doctor_contact_values.append(i[3])
        doctor_specialisation_values.append(i[4])
        doctor_qualification_values.append(i[5])

    return (
        doctor_id_values, doctor_name_values, doctor_age_values, 
        doctor_contact_values, doctor_specialisation_values,
        doctor_qualification_values)


# update button in modify details window
def modify_submit():
    global resized_logo_main
    global display_logo_main

    # get values
    field_to_update_value = field_to_update.get()
    new_record = updated_detail_entry.get()

    # check if value is empty
    if (new_record == ""):
        speak("Please enter some value to update")
        return

    # change value if field is blood group or name
    if (field_to_update_value == "Blood Group"):
        field_to_update_value = "blood_group"

    # insert data into the database
    operation = """UPDATE patient_details
					SET {} = "{}"
					WHERE pid = {}
					""".format(field_to_update_value, new_record, check_pid_modify)
    cursor.execute(operation)
    dbcon.commit()

    # return to main menu
    speak("Record updated successfully")
    messagebox.showinfo("Database", "Record updated successfully")
    clean_right_frame()

    # display logo in main window
    logo_main = Image.open(r"Data\\Images\\Icons\\Logo3.jpg")
    resized_main = logo_main.resize((970, 692), Image.ANTIALIAS)
    resized_logo_main = ImageTk.PhotoImage(resized_main)

    display_logo_main = Label(right_frame, image = resized_logo_main)
    display_logo_main.pack()


# submitting the appointment details
def appointment_submit():
    global doctor_name
    global existing_doctors
    global check_pid
    global date

    doctor_name_value = doctor_name.get()
    for key in existing_doctors:
        if (existing_doctors[key] == doctor_name_value):
            did = key

    # check for existing data
    operation = """SELECT pid FROM appointment"""
    cursor.execute(operation)
    data = cursor.fetchall()

    for i in data:
        if (i[0] == int(check_pid)):
            operation = """DELETE FROM appointment
							WHERE pid = {}""".format(check_pid)
            cursor.execute(operation)
            dbcon.commit()

    operation = """INSERT INTO appointment VALUES
					({}, {}, "{}")""".format(check_pid, did, date)

    cursor.execute(operation)
    dbcon.commit()

    detail_frame = LabelFrame(right_frame, text = "Details of your appointment", height = 275, 
                              width = 1000, bg = "#FFE2E2")
    detail_frame.grid(row = 8, column = 0, rowspan = 5, columnspan = 3, padx = 4, pady = 5)
    detail_frame.grid_propagate(0)

    details = str(
        "Your appointment with {} has been approved on " +
        "{}. You must follow all the norms of the hospital. " +
        "Mask, face shield, gloves and hand santizers are compulsory. " +
        "The health and safety of our patients, families, and staff members is our top priority. " +
        "By following all these essential steps we all can stop corona together"
    ).format(existing_doctors[did], date)

    details_label = Label(detail_frame, text = details, font = "consolas 16 bold", bg = "#FFE2E2", 
                          wraplength = 850, justify = LEFT)
    details_label.grid(row = 0, column = 0, columnspan = 3, rowspan = 4)

    home_button = Button(detail_frame, text = "Home", font = "consolas 20 bold", width = 55, bg = "#FF847C",
                         borderwidth = 7, padx = 10, pady = 4, command = home_submit)
    home_button.grid(row = 5, column = 0, columnspan = 3, pady = 10, padx = 10)
    speak("Your appointment is fixed")


# fetch room values
def room_values():
    operation = """SELECT * FROM rooms"""
    cursor.execute(operation)
    data = cursor.fetchall()

    wards_detail = []
    rooms_detail = []
    number_of_bed_detail = []
    number_of_nurse_on_assistance = []
    specialisations_of_wards = []

    for i in data:
        wards_detail.append(i[0])
        rooms_detail.append(i[1])
        number_of_bed_detail.append(i[2])
        number_of_nurse_on_assistance.append(i[3])
        specialisations_of_wards.append(i[4])

    return (wards_detail, rooms_detail, number_of_bed_detail, 
        number_of_nurse_on_assistance, specialisations_of_wards)


root.mainloop()
