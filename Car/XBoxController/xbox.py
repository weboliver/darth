import evdev


def ConnectXboxBT():
    print('----------------')
    print('Attempting to connect to your xbox contoller...')

    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

    print('-------------------')
    print('These devices were found on your Robot...')

    for device in devices:
        print(device.path, device.name, device.phys)

    print('-------------------')
    print('-------------------')
    print('Now connecting to your Xbox controller....')
    print('-------------------')

    for device in devices:
        print('Path: ',device.path,', Device Name: ',device.name,', Device address: ',device.phys)
        print('-------------------')
        #print(type(device.name))
        #print('find a text 1;',device.name.__contains__('box'))
        #print('find a text 2;',device.name.__contains__('Cons'))
        if (device.name.__contains__('box') == True) and (device.name.__contains__('Cons') == False):
            print('-------------------')
            print('This device is compatible.')
            print('The Xbox controller was FOUND!!!')
            print('-------------------')
            #device = device.path
            print(device)
            #print(device)
            print('-------------------')
            print(dir(device))
            print('----------')
            print(device.capabilities())
            print('----------')
            print(device.capabilities(verbose=True))
            print('----------')
            print(device.info)
            print('----------')
            print(device.leds)
            print('----------')
            print(device.name)
            print('----------')
            print(device.path)
            print('----------')
            print(device.phys)
            print('----------')
            break
        else:
            print('This device was not compatible.')
            print('-------------------')

    print('-------------------')

    return device

def ReadXboxBT(device):
    
    print('dev is ',device)
    
    if device == 'False':
        device = ConnectXboxBT()

    print('Press any button on Xbox. Y to EXIT.')

    while 1:
        try:
            xkey = device.read_one()
            #print('key :', xkey)
            if xkey is not None:
                print('new command-----------------------------------------------')
                print('new command-----------------------------------------------')
                print('key :', xkey)
                print('key code :', xkey.code)
                print('key type :', xkey.type)
                print('key value :', xkey.value)
                if xkey.code == 304 and xkey.value == 1:
                    print('A button was pressed')
                elif xkey.code == 304 and xkey.value == 0:
                    print('A button was released')
                elif xkey.code == 305 and xkey.value == 1:
                    print('B button was pressed')
                elif xkey.code == 305 and xkey.value == 0:
                    print('B button was released')
                elif xkey.code == 307 and xkey.value == 1:
                    print('X button was pressed')
                elif xkey.code == 307 and xkey.value == 0:
                    print('X button was released')
                elif xkey.code == 308 and xkey.value == 1:
                    print('Y button was pressed')
                elif xkey.code == 308 and xkey.value == 0:
                    print('Y button was released')
                    break
                elif xkey.code == 311 and xkey.value == 1:
                    print('Right Trigger upper was pressed')
                elif xkey.code == 311 and xkey.value == 0:
                    print('Right Trigger upper was released')
                elif xkey.code == 313 and xkey.value == 1:
                    print('Right Trigger lower was pressed')
                elif xkey.code == 313 and xkey.value == 0:
                    print('Right Trigger lower was released')
                elif xkey.code == 310 and xkey.value == 1:
                    print('Left Trigger upper was pressed')
                elif xkey.code == 310 and xkey.value == 0:
                    print('Left Trigger upper was released')
                elif xkey.code == 0 and xkey.type == 3:  # Left joystick, left and right.
                    print('----------')
                    print('Left joystick - X axis')
                    print('value', xkey.value)
                    print('----------')
                elif xkey.code == 1 and xkey.type == 3:  # Left joystick, up and down.
                    print('----------')
                    print('Left joystick - Y axis')
                    print('value', xkey.value)
                    print('----------')
                elif xkey.code == 2 and xkey.type == 3:  # Right joystick, left and right.
                    print('----------')
                    print('Right joystick - X axis')
                    print('value', xkey.value)
                    print('----------')
                elif xkey.code == 5 and xkey.type == 3:  # Right joystick, left and right.
                    print('----------')
                    print('Right joystick - Y axis')
                    print('value', xkey.value)
                    print('----------')
                elif xkey.code == 9 and xkey.type == 3:  #
                    print('----------')
                    print('Right Trigger Lower.')
                    print('value', xkey.value)
                    print('----------')
                elif xkey.code == 10 and xkey.type == 3:  #
                    print('----------')
                    print('Left Trigger Lower.')
                    print('value', xkey.value)
                    print('----------')
                elif xkey.code == 17 and xkey.value == 0:
                    print('Select was released')
        except:
            print('----------------')
            print('The xbox controller was not detected. Is it turned on?')
            print('----------------')
            break

if __name__ == "__main__":

    print('''
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##*###%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%##*####%%%*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@                                             @@@@@@@@@@@@@@####*##%@##*%@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@  This program was brought to you by the:    @@@@@@@@@@@@@%%#%@@@@@@@@*#%#*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%
    @@                                             @@@@@@@@@@@@@@%######%*+**+#%%%#*#**%@@@@@@@@@%@@@@@@@@@@@@@#
    @@    _.~"~._.~"~._.~"~._.~"~._.~"~._.~"~._    @@@@@@@@@@@@@@@@@%###%##***+*++*%###***@@@@@@@@#%*=+*++==*+*#
    @@    _.~"~._.~"~._.~"~._.~"~._.~"~._.~"~._    @@@@@@@@@@@@@@@@@@@@%%#*******++%+%##+#@@@@@@@@%#*=-***=-++@%
    @@    _.~"                             "~._    @@@%%%%@@@@@@@@@@@@@@@%##*******%+###*%@@@@@@@@%#%##*#**++%@%
    @@    _.~"   Brisbane Robotics Club.   "~._    @@%####%@@@@@@@@@@@@@@%##****###%+####@@@@@@@@@%######:-:+=@%
    @@    _.~"                             "~._    @@#***##@@@@@@@@@@@%##%%%%######%*#%%%%##**#%@@@%####**+++#@%
    @@    _.~"~._.~"~._.~"~._.~"~._.~"~._.~"~._    @@#*****@@%%%####%%%%%%%%%%%%%%%%%%##%%######@@@@@%%%####%@@%
    @@    _.~"~._.~"~._.~"~._.~"~._.~"~._.~"~._    @@@####*#########%%######%#%%%%%#***#@@%%%##**#@@@@@%@%%@@@@%
    @@                                             @@@#**###%%%%@%@@@%#########%%###%%@@@@@@%##***#@@@@@@@@@@@@%
    @@ website: http://brisbaneroboticsclub.id.au/ @@@@@%%@@@@@@@@@@@%*****+*###**########%@@@%%%#%%@@@@@######*
    @@                                             @@@@@@@@@@@@@@@@@@%#******#***@@@@@@@@@@@@@@#******%@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*****#**#@@@@@@@@@@@@@@#*#*#%*#@%%@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%######%@@@@@@@@@@@@@@@@%%@%##%%@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@                                                                                                        @@
    @@    For instructions : http://brisbaneroboticsclub.id.au/connect-xbox-controller-to-nvidia-nano-raspberry-pi/  @@
    @@                                                                                                        @@
    @@    To run code      : python3 xbox.py                                                                  @@
    @@                                                                                                        @@
    @@    NOTE             : Humans were NOT harmed making this robot. This is free and open-source software  @@
    @@                       distributed under the terms of the GNU General Public License version 2.         @@
    @@                                                                                                        @@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ''')

    print('-------------------')
    print('Turn on Xbox controller now.')
    print('-------------------')

    print('-------------------')
    print('Starting Main Menu loop.')
    print('-------------------')

    device = 'False'

    while 1:

        inp = int(input('1. Read Xbox via Bluetooth.\
        \n2. Exit. \
        \n>>> '))

        if inp == 1:
            ReadXboxBT(device)
        elif inp == 2:
            break

    print('----------------')
    print('Program End.')
    print('----------------')
