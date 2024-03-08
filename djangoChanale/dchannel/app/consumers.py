# Topic

from channels.consumer import SyncConsumer,AsyncConsumer

class MySyncConsumer(SyncConsumer):
    
    def websocket_connect(self,event):
        print("connected")
    
    def websocket_receive(self,event):
        print("received data")
    
    def websocket_disconnect(self,event):
        print("websocket disconnect")

class MyAsyncConsumer(AsyncConsumer):
    
   async def websocket_connect(self,event):
        print("connected")
    
   async def websocket_receive(self,event):
        print("received data")
    
   async def websocket_disconnect(self,event):
        print("websocket disconnect")