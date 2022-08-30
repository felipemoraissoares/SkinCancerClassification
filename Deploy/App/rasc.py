from kivymd.app import MDApp
from kivy.lang import Builder
from plyer import filechooser

import cnn

kv = """
MDCard:
    size_hint: None, None
    size: 400,500
    pos_hint: {"center_x": 0.5, "center_y": 0.5}
    elevation: 10
    padding: 25
    spacing: 25
    orientation: "vertical"
    
    MDToolbar:
        title: '[size=17]Classificador de Lesões de Pele[/size]'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        right_action_items: [['close', lambda x: app.fechar()]]
        md_bg_color: app.theme_cls.primary_dark
    
    Image:
        id: img
        source: "vazia.png"
        #allow_stretch: True
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        size_hint: 1.75, 1.75
    
    MDRoundFlatButton:
        text: "Classificar" # Texto do botão
        font_size: 12  # Tamanho da letra
        pos_hint: {"center_x": .5, "center_y": .25} # Posição na página 
        on_release: app.file_chooser() # Função quando apertar botão
            
    MDLabel:
        id: result
        text: ""
        font_size: 35
        pos_hint: {"center_x": .5, "center_y": .10}
        halign: "center"
        
"""

class FileChoosser(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        self.title = 'Skin Lesion Detector'
        return Builder.load_string(kv)

    def file_chooser(self):
        filechooser.open_file(on_selection=self.selected)


    def selected(self, selection):
        if selection:
            path = selection[0]
            self.root.ids.img.source = selection[0]
            resultado = cnn.abrir_img(path)
            self.root.ids.result.text = resultado



if __name__ == "__main__":
    FileChoosser().run()