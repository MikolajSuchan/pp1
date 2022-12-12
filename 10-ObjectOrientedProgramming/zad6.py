class University():
    def __init__(self):
        self.name="UEK"

    def print_name(self):
        print(self.name)

    def set_name(self,name):
        self.name=name
    

u1=University()
u1.print_name()
u1.set_name("MIT")
u1.print_name()
