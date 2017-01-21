### Televsion control emulation
##
#
# 2. Write a program that simulates a television by creating it as an object.
#   The user should be able to enter a channel number and raise or lower the volume.
#   Make sure that the channel number and volume level stay within valid ranges.
#
##
###


class Television(object):
    def __init__(self, channel_number = None, channel_name = "", volume = 10):
        self.channel_number = channel_number
        self.channel_name = channel_name
        self.volume = volume

    def __str__(self):
        string = """
        You are watching now: {}
        Your current volume value is: {}
        """.format(str(self.channel_name), str(self.volume))
        return string

    def volume_up(self):
        self.volume += 1
        if self.volume > 99:
            print("MAX!!!1")
            self.volume = 99
        else:
            print("Volume: {}".format(self.volume))

    def volume_down(self):
        self.volume -= 1
        if self.volume <= 0:
            print("Volume: MUTE")
            self.volume = 0
        else:
            print("Volume: {}".format(self.volume))

    def change_channel(self):
        # The try/except block could be moved to Object instantiating step
        try:
            self.channel_number = int(input("Channel number: "))
        except ValueError:
            print("Please enter a channel number (1-4)")
        else:
            if self.channel_number == 1:
                self.channel_name = "2x2"
            elif self.channel_number == 2:
                self.channel_name =  "Euronews"
            elif self.channel_number == 3:
                self.channel_name = "MTV"
            elif self.channel_number == 4:
                self.channel_name = "18+"
            else:
                print("Sorry, no such channel.")

def main():
    # Object instantiating
    tv = Television()
    while True:
        print("""
            1 - Change Channel
            2 - Turn up Volume
            3 - Turn down Volume
        """)
        choice = input("> ")

        if choice == "1":
            print("Choice a TV channel from 1 to 4")
            tv.change_channel()
            print(tv)
        elif choice == "2":
            print("You can turn up volume to 99.")
            tv.volume_up()
        elif choice == "3":
            print("You can turn down a volume to 0 to mute it off.")
            tv.volume_down()
        else:
            print("{} isn't a valid options.".format(choice))

main()


