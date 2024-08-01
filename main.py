import kivy
from kivy.app import App
from kivy.utils import platform
from window_manager import WindowManager
from first_window import FirstWindow
from second_window import SecondWindow
from third_window import ThirdWindow

if platform == 'android':
    from android.permissions import request_permissions, Permission

class MobileApp(App):
    def build(self):
        if platform == 'android':
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
        sm = WindowManager()
        sm.add_widget(FirstWindow(name='first'))
        sm.add_widget(SecondWindow(name='second'))
        sm.add_widget(ThirdWindow(name='third'))
        return sm

if __name__ == '__main__':
    MobileApp().run()
