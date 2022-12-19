class Music():
    
    def __init__(self, name,song,album,year):
        self.name = name
        self.song = song
        self.album = album
        self.year = year
    
    def __str__(self):
        data=f"Performer:{self.name}\n"+f"Song:{self.song}\n"+f"Album:{self.album}\n"+f"Year:{self.year}"
        return data
        
    
my_music1 = Music("Ed Sheeran","Hearts Don't Break Around Here","Divide",2017)
my_music2=Music("data2","data2","data",2222)
my_music3=Music("data2","data3","data",3333)
print(my_music1)
print(my_music2)
print(my_music3)