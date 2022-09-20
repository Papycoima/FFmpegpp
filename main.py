import subprocess
import PySimpleGUI as sg
from PySimpleGUI import theme_previewer, theme

# theme_previewer()
theme('DarkGray10')

Video_Directory = ''
Bitrate = ''
Framerate = ''
Format = ''
Output_Directory = ''
File_Name = ''

colonna_sinistra = [[sg.FileBrowse('Choose Video', key='video-get', file_types=(('Video Files', '.mp4'),('Video Files', '.mkv'),), pad=(50, 125), size=(10,1), enable_events=True)],
                    [sg.Text(f'{Video_Directory}', visible=True, key='video-dir', pad=((0, 0), (0, 100)), tooltip='Informazioni del file')]]
colonna_destra = [[sg.Text('Bitrate'), sg.InputText(size=(5, 1), key='bitrate'), sg.Text('kbits/s')],
                  [sg.Text('Framerate'), sg.InputText(size=(5, 1), key='framerate')],
                  [sg.Text('Format'), sg.OptionMenu(values=('.mp4', '.mkv'), key='format')],
                  [sg.Text('Output')],
                  [sg.FolderBrowse('Select', key='select'), sg.Text('', key='video-go')],
                  [sg.Text('File Name'), sg.InputText('', key='filename', size=(25, 1))],
                  [sg.Button('Convert!', key='convert')],
                  [sg.Text(f'', key='video-done')]]


layout = [[sg.Column(colonna_sinistra, size=(200, 300)), sg.VSeparator(), sg.Column(colonna_destra, pad=(50, 0))]]

window = sg.Window('Ffmpeg++', layout, resizable=False)


def Convert():
    global Bitrate, Framerate, Output_Directory, File_Name, Format
    Bitrate = window['bitrate'].get()
    Framerate = window['framerate'].get()
    Output_Directory = window['video-go'].get()
    File_Name = window['filename'].get()



while True:
    event, values = window.read()

    if event == 'video-get':
        Video_Directory = (values['video-get'])
        window['video-dir'].update(Video_Directory)

    if event == 'select':
        Output_Directory = (values['select'])


    if event == 'convert':
        Convert()
        print(Framerate)
        print(Bitrate)
        print(Output_Directory)
        Format = (values['format'])
        while True:
            subprocess.run(f'ffmpeg -i "{Video_Directory}" -r {Framerate} -b:v {Bitrate}k -bufsize {Bitrate}k "{Output_Directory}{File_Name}"{Format}')
            break
        window['video-done'].update(Output_Directory + File_Name + Format)
# subprocess.run(['ffmpeg', '-i', r'C:\Users\casca\Desktop\aaaa.mp4', '-r', '30', r'C:\Users\casca\Desktop\sgodompu.mp4'])
    if event == sg.WIN_CLOSED:
        break
