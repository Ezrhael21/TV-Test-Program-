# Ezrhael R. Sicat
# BSCpE 1-5 
# 05/15/2023
# TV Test Program

import pyfiglet
font = pyfiglet.figlet_format("TV Test Program", font = "slant", justify = "center")
print (font)

from TV import TVTest

# Create two seperate instances of the TVTest Class
tv_one = TVTest()
tv_two = TVTest()

# Ask the user for TV1 details
channel_one = int(input("Enter TV1's channel: "))
volume_level_one = int(input("Enter TV1's volume level: "))
status_one = input("Is TV1 on? (yes/no): ")

# Set TV1 Details
tv_one.set_channel(channel_one)
tv_one.set_volumelevel(volume_level_one)

# Turn on/off TV1 based on user input
if status_one.lower() == "yes":
    tv_one.turn_on()
else:
    tv_one.turn_off()

# Ask the user for TV2 details
channel_two = int(input("Enter TV2's channel: "))
volume_level_two = int(input("Enter TV2's volume level: "))
status_two = input("Is TV2 on? (yes/no): ")

# Set TV2 Details
tv_two.set_channel(channel_two)
tv_two.set_volumelevel(volume_level_two)

# Turn on/off TV1 based on user input
if status_two.lower() == "yes":
    tv_two.turn_on()
else:
    tv_two.turn_off()

# Display the output
print("TV1's channel is " + str(tv_one.get_channel()) + " and volume level is " + str(tv_one.get_volumelevel()))
print("TV2's channel is " + str(tv_two.get_channel()) + " and volume level is " + str(tv_two.get_volumelevel()))
