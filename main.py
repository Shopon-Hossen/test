from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp

# Kivy Layout using KivyMD 2.0.1 syntax
KV = '''
MDScreen:
    # Set the background color to match the theme
    md_bg_color: self.theme_cls.backgroundColor

    MDBoxLayout:
        orientation: "vertical"

        # KivyMD 2.0+ App Bar syntax
        MDTopAppBar:
            type: "small"
            
            MDTopAppBarTitle:
                text: "KivyMD 2.0.1 Phone Test"
            
            MDTopAppBarTrailingButtonContainer:
                MDActionTopAppBarButton:
                    icon: "theme-light-dark"
                    on_release: app.switch_theme()

        # Main content area
        MDFloatLayout:
            MDBoxLayout:
                orientation: "vertical"
                spacing: "24dp"
                adaptive_height: True
                pos_hint: {"center_x": .5, "center_y": .5}

                MDLabel:
                    text: app.status_text
                    halign: "center"
                    # KivyMD 2.0+ typography syntax
                    font_style: "Headline"
                    role: "small"

                # KivyMD 2.0+ Button syntax requires MDButtonText
                MDButton:
                    style: "elevated"
                    pos_hint: {"center_x": .5}
                    on_release: app.button_pressed()
                    
                    MDButtonText:
                        text: "Tap to Test Touch"
'''

class TestApp(MDApp):
    # This property updates the UI automatically when changed
    status_text = StringProperty("App is running!")
    click_count = 0

    def build(self):
        # Set initial theme settings
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Olive"
        
        return Builder.load_string(KV)

    def button_pressed(self):
        # Test screen touch / interactions
        self.click_count += 1
        self.status_text = f"Button tapped {self.click_count} times!"

    def switch_theme(self):
        # Test performance of dynamic UI updates
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )


if __name__ == '__main__':
    TestApp().run()