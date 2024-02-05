from tkinter import *
root = Tk() #creates the main window for our application
root.title("To-Do List App") #sets the title
def add_task(): #ADDS THE TASK
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
def delete_task(): #DELETES THE TASK
    selected_task = listbox.curselection()
    listbox.delete(selected_task)
entry = Entry(root, width=40)
listbox = Listbox(root, selectmode=SINGLE, height=10, width=40)
add_button = Button(root, text="Add Task", command=add_task)
delete_button = Button(root, text="Delete Task", command=delete_task)
# THE ABOVE CODE LINES WILL CREATE THE INTERFACE COMPONENTS
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
listbox.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
add_button.grid(row=2, column=0, padx=10, pady=10)
delete_button.grid(row=2, column=1, padx=10, pady=10)

# THE ABOVE CODES WILL LOOK INTO THE PLACEMENT OF THE COMPONENTS
root.mainloop()