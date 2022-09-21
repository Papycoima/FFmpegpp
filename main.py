import subprocess
import PySimpleGUI as sg
from PySimpleGUI import theme_previewer, theme

sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '#1b2029',
                                            'TEXT': '#abafc9',
                                            'INPUT': '#30334a',
                                            'TEXT_INPUT': '#abafc9',
                                            'SCROLL': '#99CC99',
                                            'BUTTON': ('#abafc9', '#4b5075'),
                                            'PROGRESS': ('#D1826B', '#CC8019'),
                                            'BORDER': 0, 'SLIDER_DEPTH': 0,
                                            'PROGRESS_DEPTH': 0, }

#theme_previewer()
theme('MyCreatedTheme')

Video_Directory = ''
Bitrate = ''
Framerate = ''
Format = ''
Output_Directory = ''
File_Name = ''

mainWindowIcon_20 = b'iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAASLSURBVDhPrZVbaBRXGMe/ue3MzuzsNdm4bm6mpmmxJjZptQWxsSpY2ogGBMXiS/skpUhLGwulD31rH4Q8SKEPvVCRUqgoVZpClZoQVKwk5GYwyZo1bmYvs8nu7Ewyu7Oz0+9MY1uKj/6H/w7755wf35xzvhkKnoY+5imgQfaUpeoTgZemLlPFckmcSc6Ffrh4ZXnX/q1xzdL2LWvL9SlNqdfKWhSHPXY9uo43fXwo3/wZOzhybk+DP3qyXqqL+nl/lKaoqF4x6qxaTbozPuMIgnA9KAWaTd3s8LAe8DAcUHg5eD0WVgahfMsw5YiDNM/w3V5WeEfm5T6E7tokb9oSFkPy0MgoPZ98aB46uKfLy3k7CIijOWDRFPXvg3EVEcL5ltuUI/Qp50cM2jTN9PTcbDGV1R2cCD6PBL/dHoWhWzcqbx/qKzREwqRqSCcMeDTWPFYtNq1usIC1vBBWW8eomvcN5fyoRjL69Ovv/ej3+bcH/Yy5ur4KV+9eh8Gfv6kdP/iW8kxzY7xaq8LCfBqW5tXJUPvcTSaQDLmwKg8RtXXaEFdPqvbkKZIR0eRHDkjRklX0zipzMHDuc+jt2al0b3uuRS/rMLuQhInxxIPGLnmIEeCUZVtAVVmsbMucyevH9YByAdeg36WhXKBq5CGjZyGRfQANQRF6X+2Jq4YKM4sJGB4dy7ZuD5/nfM6H69YaVMo2hHOtyQprHi2Glr7D/dnukjbkAjNGFhQtDaVaCQ7390Faz8DsUgKGrt3U4luD54QQdaZULtH6uglSOpayabu/EFn8GmHdLuU/coHpUgaWSwrky3nImTmYTy/C0O+3ysGY96y0iR7AteUKRgmopUDWdpwjK/ULgwjb6RL+pw1gGvDQQkpLwWLuEQzfmLAZH3zpa4LTOUMVVX0FrKR3xa7CYTV6/wuE7XZnP0EuUEFgCoFLK8sweeehU4HKWb7FfDejZ4LZUg7YbAAOvvaKGNvBfY+wvWQO5dDQGIjDye4TEPPHSOTqbyCuX6qgwPJMCdbM8ldWU7Yfq46ltQxUl0TjhbaOC5JPENrCre1kPGd5a6IeufpsXTv4eRk627eR2JV75OmPpJ5AMTbsMeULavz+yxh11RwHAiuNZm/nrvHGpkgEs3YHM2xLGBtPDLy4o20/Q9MHRE4EzC3snikc85JboZyNTqwxhVgmdq/DduwuNPhXN1eE9cCxWDzYQ2BkHGk5mfdBZ2dLCe8ubCPn8PY8klmGBFavxVSl8k9Y7wHyny2LQK1T61pA2Z00Fuu8nAAhr9sgd+fVxAcXpy9/guc2gj0PkkeEosb8OT0rfHrtD1hkmFMyXZOq3yLsKJlBVGMtsKQ1j8PZIQMf0efxQ3OwkTTA7Uszv5zAsVuLZhHi/s0QEcMwmhjbPJWZOlLL30swzl66B7eGnCkFTRrcRpNHYNEUW/XkBDX6vhCGySuzvx7D5fhnS3NGDjssB/dXJ8HmVKDz1pUnv7HPCGRtZXQ9VxFU62yhAAPCm1hZF8nQDejHL1dismkebkE4/HQ+AQM8jTsTokyq+BevNPPw7pRXlQAAAABJRU5ErkJggg=='


colonna_sinistra = [[sg.FileBrowse(button_text='Choose Video', key='video-get', file_types=(('Video Files', '.mp4'), ('Video Files', '.mkv'),),
                                   pad=(25, 125), size=(15, 1), enable_events=True)],
                    [sg.Text(f'{Video_Directory}', visible=True, key='video-dir', pad=((0, 0), (0, 100)), tooltip='File Info')]]
colonna_destra = [[sg.Text('Bitrate'), sg.InputText(size=(5, 1), key='bitrate'), sg.Text('kbits/s')],
                  [sg.Text('Framerate'), sg.InputText(size=(5, 1), key='framerate')],
                  [sg.Text('Format'), sg.OptionMenu(values=('.mp4', '.mkv'), key='format')],
                  [sg.Text('Output')],
                  [sg.FolderBrowse('Select', key='select'), sg.Text('', key='video-go')],
                  [sg.Text('File Name'), sg.InputText('', key='filename', size=(25, 1))],
                  [sg.Button('Convert!', key='convert')],
                  [sg.Text(f'', key='video-done')]]


layout = [[sg.Column(colonna_sinistra, size=(200, 300)), sg.VSeparator(), sg.Column(colonna_destra, pad=(50, 0))]]



window = sg.Window('Ffmpeg++', layout, resizable=False, use_custom_titlebar=True, titlebar_background_color='', titlebar_icon=mainWindowIcon_20, keep_on_top=True, titlebar_font=(sg.DEFAULT_FONT, 12, 'bold'))


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
