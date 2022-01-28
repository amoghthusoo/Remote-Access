import socket as s
from kivy.app import App
from kivy.lang import Builder


client_socket = s.socket()
client_socket.connect(('192.168.228.36', 9999))
print()
print(client_socket.recv(1024).decode())




ui = '''
Button:
    text : 'Play/Pause'
    size_hint_x : None
    size_hint_y : None
    width : '120dp'
    height : '55dp'
    pos_hint : {'center_x' : 0.5, 'center_y' : 0.5}
    on_press : app.trigger_start()
    on_release : app.trigger_stop()
    always_release : True
'''

class Remote(App):

    def build(self):
        self._ui = Builder.load_string(ui)
        return self._ui

    def trigger_start(self):
        client_socket.send(bytes('True', 'utf-8'))

    def trigger_stop(self):
        client_socket.send(bytes('False', 'utf-8'))

root = Remote()

if __name__ == '__main__':
   root.run()
