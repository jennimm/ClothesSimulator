from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout

class Clothes(Button):
    source = StringProperty("")
    pass 

class ClothesList(GridLayout):
    pass

class MyApp(App):

    def onClick(self, instance):
        return Image(source = "top.jpg")

    def build(self):
        #return Label(text='Hello world')
        # return Image(source = "mannequin.jpg")
        self.layout = ClothesList()
        self.root = ScrollView(
                        size_hint=(None, None), 
                        size=Window.size,
                        scroll_type=['bars', 'content']
                    )
        self.root.add_widget(self.layout)
        foo = Clothes(source="top.jpg")
        self.layout.add_widget(foo)
        return self.root

    





if __name__ == '__main__':
    MyApp().run()


