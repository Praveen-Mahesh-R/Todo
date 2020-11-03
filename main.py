import PySimpleGUI as sg

def add_task(values):
    task = values['taskname']
    todolist.append(task)
    window.FindElement('taskname').Update(value="")
    window.FindElement('todolist').Update(values=todolist)
    window.FindElement('add_save').Update('Add')

todolist=[]
layout = [
    [sg.Text('Enter the task'),sg.InputText("", key='taskname'),
    sg.Button("Add",key="add_save")],
    [sg.Listbox(values=[], size=(30,10), key='todolist')],

]
window = sg.Window('TodoList', layout)
while True:
    button, values = window.Read()
    if button == 'add_save':
        add_task(values)
    #elif button == 'Exit':
    #    sg.Popup('Names are:',
    #    break
    else:
        break
window.Close()