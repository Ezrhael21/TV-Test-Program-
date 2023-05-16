# Ezrhael R. Sicat
# BSCpE 1-5 
# 05/15/2023
# TV Test Program

from TV import TVTest

tv = TVTest()

print (tv.channel)
print (tv.volumelevel)
print (tv.on)

tv.set_channel(5)
tv.set_volumelevel(3)

print (tv.turn_on())
print (tv.turn_off())
print (tv.get_channel())
print (tv.set_channel)
print (tv.get_volumelevel())
print (tv.set_volumelevel)
# Create a seperate file class for the following:
# Method to turn on the tv
# Method to turn of the tv
# Method to get channel from the user
# Method to set channel
# Method to get volume from the user
# Method to set volume
# Method to increase channel by 1
# Method to decrease channel by 1
# Method to increase volume by 1 
# Method to decrease volume by 1 
# Method to print the output
# Call the class from the main file
# Display the output