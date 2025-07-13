import tkinter as tk
import random
import datetime
import calendar

font = ("Arial", 14)

root = tk.Tk()
root.title("to do app")
root.geometry("400x800")
root.configure(bg="lightblue")


label = tk.Label(root, text="ciao benvenuto nella tua to do list", font=font, )
label.pack(pady=5)
def Aggiorna_tempo():
    now = datetime.datetime.now()
    time_label.config(text=now.strftime("%H:%M:%S"), anchor="w")
    root.after(1000, Aggiorna_tempo)
time_label = tk.Label(root, text="", font=font, anchor="w")
time_label.pack(pady=5)



Aggiorna_tempo()



name = tk.Entry(root, font=font)
name.pack(pady=5)
name.focus_set()

submit_button = tk.Button(root, text="invia nome", font=font)
submit_button.pack(pady=5)
def submit_name():
    user_name = name.get()
    if user_name:
        label.config(text=f"ciao {user_name}, benvenuto nella tua to do list")
        name.delete(0, tk.END)
    else:
        label.config(text="per favore inserisci un nome")
submit_button.config(command=submit_name)
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        label.config(text="per favore inserisci un compito")
task_entry = tk.Entry(root, font=font)
task_entry.pack(pady=5)
add_task_button = tk.Button(root, text="aggiungi compito", font=font, command=add_task)
add_task_button.pack(pady=5)
tasks_listbox = tk.Listbox(root, font=font, width=50, height=10)
tasks_listbox.pack(pady=5)
def remove_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        label.config(text="per favore seleziona un compito da rimuovere")
remove_task_button = tk.Button(root, text="rimuovi compito", font=font, command=remove_task)
remove_task_button.pack(pady=5)
def clear_tasks():
    tasks_listbox.delete(0, tk.END)
    label.config(text="tutti i compiti sono stati rimossi")
clear_tasks_button = tk.Button(root, text="rimuovi tutti i compiti", font=font, command=clear_tasks)
clear_tasks_button.pack(pady=5)

def salva_file():
    with open("tasks.txt", "w") as file:
        tasks = tasks_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")
    label.config(text="compiti salvati nel file tasks.txt")
save_button = tk.Button(root, text="salva compiti", font=font, command=salva_file)
save_button.pack(pady=5)
def completa_task():
    selected = tasks_listbox.curselection()
    if selected:
        task = tasks_listbox.get(selected)
        tasks_listbox.delete(selected)
        tasks_listbox.insert(selected, f"✔️ {task}")
    else:
        label.config(text="seleziona un compito da completare")

completa_button = tk.Button(root, text="Segna completato", font=font, command=completa_task)
completa_button.pack(pady=5)


    





root.mainloop()