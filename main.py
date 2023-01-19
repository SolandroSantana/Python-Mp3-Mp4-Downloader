import PySimpleGUI as Sg
from projects.Pytube.Pytube import Mp3Download, Mp4Download


class Program:

    def __init__(self, title, layout, size):

        self.title = title
        self.layout = layout
        self.size = size

        window = Sg.Window(title, layout, size=size)

        while True:
            event, values = window.read()

            if event == Sg.WIN_CLOSED or event == 'Sair':
                break

            if event == 'MP3 Downloader':
                window.hide()
                Program.mp3_window(self)
                window.un_hide()

            if event == 'mp3_down':
                mp3_url = values['mp3_url']
                mp3_dst = values['mp3_dst']

                Mp3Download.Download(Mp3Download, mp3_url, mp3_dst)

                if Mp3Download:
                    Sg.Popup('Mp3 baixado com sucesso!')

            if event == 'MP4 Downloader':
                window.hide()
                Program.mp4_window(self)
                window.un_hide()

            if event == 'mp4_down':

                mp4_url = values['mp4_url']
                mp4_dst = values['mp4_dst']
                mp4_resolution = values['mp4_resolution']

                if mp4_url == '' and mp4_dst == '' and mp4_resolution == '':
                    Sg.popup('Enter the url, the destination folder and the resolution of the video!')
                elif mp4_url == '':
                    Sg.popup('Enter the url!')
                elif mp4_dst == '':
                    Sg.popup('Enter the destination folder of the video!')
                elif mp4_resolution == '':
                    Sg.popup('Select a resolution!')

                try:
                    Mp4Download.Download(Mp4Download, mp4_url, mp4_dst, mp4_resolution)

                    if Mp4Download:
                        Sg.Popup('Vídeo baixado com sucesso!')
                except:
                    Sg.PopupOKCancel('Resolução de video não encontrada. Tente baixar em outra resolução!')

            if event == 'Voltar':
                break

        window.close()

    def menu_window(self):

        Sg.theme('Default')

        layout = [
            [Sg.Button('MP3 Downloader', size=[20, 5]), Sg.Button('MP4 Downloader', size=[20, 5])],
            [Sg.Button('Sair')]
        ]

        column = [[Sg.VPush()],
                  [Sg.Push(), Sg.Column(layout, element_justification='c'), Sg.Push()],
                  [Sg.VPush()]]

        Program('Portfolio Python - Menu', column, [600,400])

    def mp3_window(self):

        Sg.theme('Default')

        layout = [
            [Sg.Text('Selecione a url do audio'), Sg.Input(key='mp3_url')],
            [Sg.Text('Selecione o diretorio para salvar o audio'), Sg.Input(key='mp3_dst'), Sg.FolderBrowse('Selecionar')],
            [Sg.Button('Baixar', key='mp3_down'), Sg.Button('Voltar')]

        ]

        Program('Portfolio Python - MP3 Downloader', layout, [700,100])

    def mp4_window(self):

        Sg.theme('Default')

        layout = [
            [Sg.Text('Selecione a url do video'), Sg.Input(key='mp4_url')],
            [Sg.Text('Selecione o diretorio para salvar o video'), Sg.Input(key='mp4_dst'), Sg.FolderBrowse('Selecionar')],
            [Sg.Text('Selecione a resolução do video:'), Sg.InputCombo(['144p', '240p', '360p', '480p', '720p', '1080p'], key='mp4_resolution')],
            [Sg.ProgressBar(100)],
            [Sg.Button('Baixar', key='mp4_down'), Sg.Button('Voltar')]

        ]

        Program('Portfolio Python - MP4 Downloader', layout, [700,150])


if __name__ == "__main__":
    Program.menu_window(Program)
