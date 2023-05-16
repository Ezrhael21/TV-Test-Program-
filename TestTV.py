# Ezrhael R. Sicat
# BSCpE 1-5 
# 05/15/2023
# TV Test Program

from TV import TVTest

# Create two seperate instances of the TVTest Class
tv_one = TVTest()
tv_two = TVTest()

# Set TV1 Details
tv_one.set_channel(3)
tv_one.set_volumelevel(5)


# Display the output
print("TV1's channel is " + str(tv_one.get_channel()) + " and volume level is " + str(tv_one.get_volumelevel()))
