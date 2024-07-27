"""
CP1404 - Programming II
Kivy GUI to convert Miles to Km
Sam Butters
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class ConvertMilesApp(App):
    """Kivy app to convert miles to kilometers."""
    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle calculation, output result to label widget."""
        print("calculate button test")
        miles = self.format_miles()
        kilometers = miles * MILES_TO_KM
        self.root.ids.output_label.text = str(kilometers)

    def format_miles(self):
        """Get miles from input, convert to a float."""
        try:
            miles = float(self.root.ids.input_miles.text)
            return miles
        except ValueError:
            return 0.0

    def handle_increment(self, change):
        """Handle up/down button press, changing text input by 1."""
        miles = self.format_miles()
        miles += change
        self.root.ids.input_miles.text = str(miles)


ConvertMilesApp().run()
