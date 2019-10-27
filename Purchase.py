import PySimpleGUI as sg

# There were no explanations about the exact input,
# so I've made a simple GUI to fulfill the homework requirements

layout = [
    [sg.Text('one item price is X dollars Y cents,\
     calculate price for N items')],
    [sg.Text('X', size=(15, 1)), sg.InputText('')],
    [sg.Text('Y', size=(15, 1)), sg.InputText('')],
    [sg.Text('N', size=(15, 1)), sg.InputText('')],
    [sg.Submit()]
]

window = sg.Window('Task 2').Layout(layout)
button, values = window.Read()
summary = int(values[0]) * 100 + int(values[1])
final_summary = int(values[2]) * summary
dollar = final_summary // 100
cent = final_summary % 100
sg.Popup('Total cost: ', dollar, ' dollars ', cent, 'cents')
