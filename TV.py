class TVTest:
    # Initialize the TV object
    def __init__(self):
        self.channel = 0
        self.volumelevel = 0
        self.on = False
    
    # Method to turn on the tv
    def turn_on(self):
        self.on = True

    # Method to turn off the tv
    def turn_off(self):
        self.on = False

    # Method to get the current channel of the tv
    def get_channel(self):
        return self.channel 
    
    # Method to set the channel of the tv
    def set_channel(self, channel):
        self.channel = channel

    # Method to get the current volume level of the tv
    def get_volumelevel(self):
        return self.volumelevel
    
    # Method to set the volume level of the tv
    def set_volumelevel(self, volumelevel):
        self.volumelevel = volumelevel
    

        
    


    
    


    
