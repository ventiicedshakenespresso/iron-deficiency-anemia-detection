import os
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def reset_program():
    os.execl(sys.executable, sys.executable, *sys.argv)


def exit_program():
    response = messagebox.askokcancel("Confirm Exit", "You sure you want to exit program?")
    if response:
        sys.exit(0)


def clicked_detect():
    hgb_input = hgb_entry.get()
    ferritin_input = ferritin_entry.get()
    tsat_input = tsat_entry.get()

    def tibc_chr():
        predict_enter_button.grid_forget()
        predict_label.grid_forget()

        def clicked_detect2():
            chr_input = chr_entry.get()
            if float(chr_input) <= 28:
                result3_label.config(text="Result: 1")
                result4_label.config(text="Iron deficiency anemia detected\n Initiate Iron Series")
            else:
                result3_label.config(text="Result: 1")
                result4_label.config(text="Iron deficiency anemia detected\n Initiate Maintenance Dosing")

        result_label.config(text="Evaluate TIBC and CHr")
        result2_label.config(text="If TIBC < 200 mcg/dL, evaluate Protein Energy Nutrition")
        chr_title_label = Label(text="Please enter CHr lab value:", width=56, font=("Monaco", 12, "bold"),
                                fg="#F4D58D",
                                bg="#001427")
        chr_title_label.grid(column=1, row=11, columnspan=2, pady=(0, 0), padx=(0, 0), sticky=W)
        chr_label = Label(text="CHr (pg)", width=11, font=("Monaco", 12, "bold"), fg="#F4D58D",
                          bg="#001427")
        chr_label.grid(column=1, row=12, pady=(10, 0), padx=(0, 0), sticky=E)

        chr_entry = Entry(width=17, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427",
                          highlightbackground="#F4D58D")
        chr_entry.grid(column=2, row=12, pady=(10, 0), padx=(0, 10), sticky=W)

        predict2_enter_button = ttk.Button(width=17, text="Detect", command=clicked_detect2,
                                           style='main.TButton')
        predict2_enter_button.grid(column=1, row=13, columnspan=2, pady=(20, 0))

        predict2_label = Label(
            text="Click 'Detect' to determine iron deficiency anemia status\n (No Iron Deficiency Anemia == "
                 "0, Iron Deficiency Anemia == 1)",
            width=80, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427")
        predict2_label.grid(column=1, row=14, columnspan=2)

    try:
        if float(hgb_input) >= 12.0:
            result_label.config(text="Result: 0")
            result2_label.config(text="No iron deficiency anemia detected")
        else:
            if float(ferritin_input) < 800 and float(tsat_input) < 30:
                result_label.config(text="Result: 1")
                result2_label.config(text="Iron deficiency anemia detected\n Iron Series then maintenance dosing")
            elif float(ferritin_input) < 800 and (30 <= float(tsat_input) <= 50):
                tibc_chr()
            elif float(ferritin_input) < 800 and float(tsat_input) > 50:
                tibc_chr()
            elif 800 <= float(ferritin_input) <= 1200 and float(tsat_input) < 30:
                result_label.config(text="Result: 1")
                result2_label.config(text="Iron deficiency anemia detected\n Iron Series then maintenance dosing")
            elif 800 <= float(ferritin_input) <= 1200 and (30 <= float(tsat_input) <= 50):
                result_label.config(text="Result: 1")
                result2_label.config(text="Iron deficiency anemia detected\n Maintenance Dosing")
            elif 800 <= float(ferritin_input) <= 1200 and float(tsat_input) > 50:
                result_label.config(text="Result: 0")
                result2_label.config(text="Iron deficiency anemia NOT detected\nEvaluate ESA dose. No Iron dosing")
            elif float(ferritin_input) > 1200 and float(tsat_input) < 30:
                predict_enter_button.grid_forget()
                predict_label.grid_forget()

                def clicked_detect2():
                    chr_input = chr_entry.get()
                    if float(chr_input) <= 28:
                        result3_label.config(text="Result: 1")
                        result4_label.config(text="Iron deficiency anemia detected\n Initiate Iron Series")
                    else:
                        result3_label.config(text="Result: Needs further evaluation")
                        result4_label.config(text="")

                result_label.config(text="Evaluate CHr")
                result2_label.grid_forget()
                chr_title_label = Label(text="Please enter CHr lab value:", width=56, font=("Monaco", 12, "bold"),
                                        fg="#F4D58D",
                                        bg="#001427")
                chr_title_label.grid(column=1, row=11, columnspan=2, pady=(0, 0), padx=(0, 0), sticky=W)
                chr_label = Label(text="CHr (pg)", width=11, font=("Monaco", 12, "bold"), fg="#F4D58D",
                                  bg="#001427")
                chr_label.grid(column=1, row=12, pady=(10, 0), padx=(0, 0), sticky=E)

                chr_entry = Entry(width=17, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427",
                                  highlightbackground="#F4D58D")
                chr_entry.grid(column=2, row=12, pady=(10, 0), padx=(0, 10), sticky=W)

                predict2_enter_button = ttk.Button(width=17, text="Detect", command=clicked_detect2,
                                                   style='main.TButton')
                predict2_enter_button.grid(column=1, row=13, columnspan=2, pady=(20, 0))

                predict2_label = Label(
                    text="Click 'Detect' to determine iron deficiency anemia status\n (No Iron Deficiency Anemia == "
                         "0, Iron Deficiency Anemia == 1)",
                    width=80, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427")
                predict2_label.grid(column=1, row=14, columnspan=2)
            elif float(ferritin_input) > 1200 and (30 <= float(tsat_input) <= 50):
                result_label.config(text="Result: 0")
                result2_label.config(text="Iron deficiency anemia NOT detected\nEvaluate ESA dose. No Iron dosing")
            elif float(ferritin_input) > 1200 and float(tsat_input) > 50:
                result_label.config(text="Result: 0")
                result2_label.config(text="Iron deficiency anemia NOT detected\nEvaluate ESA dose. No Iron dosing")
    except Exception as e:
        print(e)
        (messagebox.showerror("Input Error", "Please input lab values"))


window = Tk()
window.title("Iron Deficiency Anemia Detection")
window.minsize(width=700, height=800)
window.config(padx=50, pady=50, bg="#001427")

title_label = Label(text="IRON DEFICIENCY ANEMIA DETECTION", width=40, font=("Monaco", 20, "bold", "underline"),
                    fg="#F4D58D", bg="#001427", anchor=CENTER)
title_label.grid(column=1, columnspan=2, row=2, pady=(50, 30), padx=(0, 10))

lab_label = Label(text="Please enter lab values below:", width=56, font=("Monaco", 12, "bold"), fg="#F4D58D",
                  bg="#001427")
lab_label.grid(column=1, row=3, columnspan=2, sticky=W)

hgb_label = Label(text="Hemoglobin (g/dL)", width=19, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427")
hgb_label.grid(column=1, row=4, pady=(20, 0), padx=(0, 0), sticky=E)

hgb_entry = Entry(width=17, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427", highlightbackground="#F4D58D")
hgb_entry.grid(column=2, row=4, pady=(20, 0), padx=(0, 10), sticky=W)

ferritin_label = Label(text="Ferritin (ng/mL)", width=18, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427")
ferritin_label.grid(column=1, row=5, pady=(20, 0), padx=(0, 0), sticky=E)

ferritin_entry = Entry(width=17, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427", highlightbackground="#F4D58D")
ferritin_entry.grid(column=2, row=5, pady=(20, 0), padx=(0, 10), sticky=W)

tsat_label = Label(text="Transferrin Saturation (%)", width=28, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427")
tsat_label.grid(column=1, row=6, pady=(20, 0), padx=(0, 0), sticky=E)

tsat_entry = Entry(width=17, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427", highlightbackground="#F4D58D")
tsat_entry.grid(column=2, row=6, pady=(20, 10), padx=(0, 10), sticky=W)

ttk.Style().configure('main.TButton', font=("Monaco", 12, "bold"), foreground="#F4D58D", background="#001427",
                      activebackground="#001427", activeforeground="#690500",
                      highlightbackground="#001427", highlightforeground="#934B00")

predict_enter_button = ttk.Button(width=17, text="Detect", command=clicked_detect, style='main.TButton')
predict_enter_button.grid(column=1, row=7, columnspan=2, pady=(20, 0))

predict_label = Label(
    text="Click 'Detect' to determine iron deficiency anemia status\n (No Iron Deficiency Anemia == 0, "
         "Iron Deficiency Anemia == 1)",
    width=80, font=("Monaco", 12, "bold"), fg="#F4D58D", bg="#001427")
predict_label.grid(column=1, row=8, columnspan=2)

result_label = Label(text="", width=60, font=("Monaco", 14, "bold"), fg="#F4D58D", bg="#001427")
result_label.grid(column=1, row=9, columnspan=2, pady=(20, 10))
result2_label = Label(text="", width=60, font=("Monaco", 14, "bold"), fg="#F4D58D", bg="#001427")
result2_label.grid(column=1, row=10, columnspan=2, pady=(10, 10))

result3_label = Label(text="", width=60, font=("Monaco", 14, "bold"), fg="#F4D58D", bg="#001427")
result3_label.grid(column=1, row=15, columnspan=2, pady=(20, 10))
result4_label = Label(text="", width=60, font=("Monaco", 14, "bold"), fg="#F4D58D", bg="#001427")
result4_label.grid(column=1, row=16, columnspan=2, pady=(10, 10))

reset_button = ttk.Button(width=17, text="Reset", command=reset_program, style='main.TButton')
reset_button.grid(column=1, row=18, columnspan=2, pady=(20, 30))

exit_button = ttk.Button(width=17, text="Exit Program", command=exit_program, style='main.TButton')
exit_button.grid(column=1, row=19, columnspan=2, pady=(40, 0))

window.mainloop()
