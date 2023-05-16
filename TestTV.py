# Ezrhael R. Sicat
# BSCpE 1-5 
# 05/15/2023
# TV Test Program

from TV import TVTest

# Create two seperate instances of the TVTest Class
tv_one = TVTest()
tv_two = TVTest()

# Ask the user for TV1 details
channel_one = int(input("Enter TV1's channel: "))
volume_level_one = int(input("Enter TV1's volume level: "))

# Set TV1 Details
tv_one.set_channel(channel_one)
tv_one.set_volumelevel(volume_level_one)

# Set TV2 Details
tv_two.set_channel(4)
tv_two.set_volumelevel(9)

# Display the output
print("TV1's channel is " + str(tv_one.get_channel()) + " and volume level is " + str(tv_one.get_volumelevel()))
print("TV2's channel is " + str(tv_two.get_channel()) + " and volume level is " + str(tv_two.get_volumelevel()))
