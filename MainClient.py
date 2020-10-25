def Connect(self):
    import socket

    Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Client.connect(("192.168.1.4", 2108))
    return Client


def ReceiveTextToSpeak(self):
    Text = Connect(self).recv(1024).decode('utf-8')
    if Text is not None:
        return Text
