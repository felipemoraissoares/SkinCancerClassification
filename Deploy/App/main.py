from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import Screen, ScreenManager

from plyer import filechooser

caminho = ""
class GerenciadorJanela(ScreenManager):
    pass

class JanelaLogin(Screen):
    pass

class JanelaCarregaImagem(Screen):
    pass

class JanelaClassifica(Screen):
    pass

class JanelaEscolherImagem(Screen):
    def file_fire_select(self, *args):
        file_selected = args[1][0]
        caminho = file_selected
        self.ids.path.text = caminho

        try:
            self.ids.my_image.source = file_selected
            print(type(file_selected))
        except:
            print("Erro ao colocar imagem")
        print(caminho)
        print(type(file_selected))

class MeuApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        self.title = 'Skin Lesion Detector'
        return Builder.load_file('app.kv')

    def fechar(self):
        self.stop()

    def classificar(self):
        print("felipe")

    def carregar_img(self):
        filechooser.open_file(on_selection=self.selected)
        print(f"teste = {caminho}")

    def selected(self, selection):
        if selection:
            #self.root.ids.my_image.source = selection[0]
            print(type(selection[0]))

if __name__ == '__main__':
    MeuApp().run()


