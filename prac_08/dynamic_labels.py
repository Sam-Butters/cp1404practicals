"""
Kivy program to create labels
Sam Butters
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelApp(App):
    """Kivy app to create dynamic labels."""
    def __init__(self, **kwargs):
        """Initiate main program with a list of names."""
        super().__init__(**kwargs)
        self.names = ["George", "Kevin", "Adrian", "Thomas"]

    def build(self):
        """Construct the main app."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from a list and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.name_label.add_widget(temp_label)


DynamicLabelApp().run()
