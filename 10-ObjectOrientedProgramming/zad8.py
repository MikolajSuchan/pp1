class TV:
    def __init__(self,is_on,):
        self.is_on=is_on
        self.channel_no=1
        self.channels=[]

    def turn_on(self):
        self.is_on=True

    def turn_off(self):
        self.is_on=False

    def set_channel(self,num):
        self.channel_no=num

    def show_channels(self):
        print(self.channels)

    def set_channels(self):
        self.channels=["TVP1","TVP2","Polsat","TVN","Filmbox","Discovery"]

    def show_status(self):
        if self.is_on:
            print(f"TV is  on,channel:{self.channel_no}({self.channels[self.channel_no-1]})")
        else:
            print("TV is off")

p=TV(False)
p.show_status()
p.turn_on()
p.show_status()
p.show_channels()
p.set_channels()
p.show_channels()
p.show_status()
p.show_status()