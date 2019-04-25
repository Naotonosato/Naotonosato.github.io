import os,sys
sys.path.append('./')
from kivy.core.window import Window
from kivy.app import App
from kivy.resources import resource_add_path
from kivy.core.text import LabelBase,DEFAULT_FONT
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.utils import platform
from kivy.properties import StringProperty
from multi_language_textinput import MultiLanguageTextInput


if platform == 'win':

    resource_add_path('c:/Windows/Fonts')
    LabelBase.register(DEFAULT_FONT, 'YuGothR.ttc')
    Factory.register('MultiLanguageTextInput', MultiLanguageTextInput)


class IO(object):

    def new(self,filename):

        with open(filename,'w+'):
            pass

    def save(self,filename,text):

        with open(filename,'w') as f:
            f.write(text)


class Editor(App):

    text = StringProperty()
    filename = StringProperty()

    def __init__(self,**kwargs):

        super().__init__(**kwargs) 
        self.io = IO()
        self.keyboard = Window.request_keyboard(lambda *_: _,self)
        self.keyboard.bind(on_key_down=self.on_key)

    def convert(self,text):

        with open('__','w+') as f:
            pass
        result = os.system('echo | pandoc -f rst -t markdown __')
        print(result)

    def on_key(self,_,code,text,modifiers):

        if 'ctrl' in modifiers and text == 's':
            if not self.filename:
                self.popup = Popup(content=Factory.FileNamePopup())
                self.popup.bind(on_dismiss=lambda *_:self.io.save(self.filename,self.text))
                self.popup.open()
                return
            self.io.save(self.filename,self.root.ids['rst_code'].textinput.text)

Editor().run()