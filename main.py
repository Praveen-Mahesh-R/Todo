import PySimpleGUI as sg
from os import path

def add_task(values):
    task = values['taskname']
    if task not in todolist:
        todolist.append(task)
        window.FindElement('taskname').Update(value="")
        window.FindElement('todolist').Update(values=todolist)
        window.FindElement('add_save').Update('Add')
    else:
        window.FindElement('taskname').Update(value="")

def edit_tasks(values):
    edit_val = values['todolist'][0]
    window.FindElement('taskname').Update(value=edit_val)
    todolist.remove(edit_val)
    window.FindElement('add_save').Update('Save')

def delete_tasks(values):
    delete_val = values['todolist'][0]
    todolist.remove(delete_val)
    window.FindElement('todolist').Update(values=todolist)

def check_file():
    value = path.exists("listfile.txt")
    return value

def update_file(values):
        with open("listfile.txt",'w') as file:
            for task in todolist:
                file.write("%s\n" % task)

def find_file_values():
    templist = []
    if c == True:
        with open("listfile.txt", 'r') as file:
            for content in file:
                templist.extend(content.split())
    return templist

c = check_file()

todolist = find_file_values()

layout = [
    [sg.Text('Enter the task'),sg.InputText("", key='taskname'),
    sg.Button("Add",key="add_save")],
    [sg.Listbox(values=todolist, size=(30,10), key='todolist'),
     sg.Button("Edit"),
     sg.Button("Delete")],
    [sg.Button("Save and Quit")]
    ]

window = sg.Window('TodoList', layout)

while True:
    button, values = window.Read()
    if button == 'add_save':
        add_task(values)
    elif button == 'Edit':
        edit_tasks(values)
    elif button == 'Delete':
        delete_tasks(values)
    elif button == "Save and Quit":
        update_file(values)
        break
    else:
        break
window.Close()