from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


class HomeScreen(Screen):
    pass

class GraveyardsScreen(Screen):
    pass

class GraveyardOfMind(App):
    def build(self):
        Builder.load_file("styles.kv")
        return Builder.load_file("screens.kv")

if __name__ == '__main__':
    GraveyardOfMind().run()