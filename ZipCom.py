import PySimpleGUI as sg
from zip_creator import make_archive


sg.theme('DarkGreen4')
label1 = sg.Text("Select files to Kompress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Kompress",button_color='red')
output_but = sg.Text(key='output')
exit_button = sg.Button("EX1T", button_color='red',key='exit')

window1 = sg.Window('Kompress into Zip',
                    layout=[[label1], [input1, choose_button1],
                            [label2],[input2, choose_button2],
                            [compress_button, output_but],
                            [exit_button]])

while True:
    try:
        event, values = window1.read()

        filepaths = values['files'].split(';')
        folders = values['folder']
        window1['output'].update(value="Compression completed!")
    except TypeError:
        print()
    match event:
        case "exit":
            break


    make_archive(filepaths,folders)

window1.close()