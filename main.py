import PySimpleGUI as sg

def add_task(values):
    task = values['taskname']
    todolist.append(task)
    window.FindElement('taskname').Update(value="")
    window.FindElement('todolist').Update(values=todolist)
    window.FindElement('add_save').Update('Add')

def edit_tasks(values):
    edit_val = values['todolist'][0]
    window.FindElement('taskname').Update(value=edit_val)
    todolist.remove(edit_val)
    window.FindElement('add_save').Update('Save')

def delete_tasks(values):
    delete_val = values['todolist'][0]
    todolist.remove(delete_val)
    window.FindElement('todolist').Update(values=todolist)

todolist=[]

layout = [
    [sg.Text('Enter the task'),sg.InputText("", key='taskname'),
    sg.Button("Add",key="add_save")],
    [sg.Listbox(values=[], size=(30,10), key='todolist'),
     sg.Button("Edit"),
     sg.Button("Delete")]
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
    else:
        break
window.Close()