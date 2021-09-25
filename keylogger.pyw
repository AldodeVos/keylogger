from pynput.keyboard import Key, Listener, KeyCode
import csv
from pynput import keyboard


csvfile = open('keystrokes.csv', 'a', newline='')
writer = csv.writer(csvfile)

last_press = Key.shift               #shift is often held, which creates a long list of inputs like any other key. while that shouldn't be the case.
key_names = [Key.esc, Key.f1, Key.f2, Key.f3, Key.f4, Key.f5, Key.f6, Key.f7, Key.f8, Key.f9, Key.f10, Key.f11, Key.f12, Key.f13, Key.f14, Key.f15,
             ['`'], '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', Key.backspace, Key.home, Key.page_up, Key.tab,
             'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', Key.enter, Key.delete, Key.end, Key.page_down, Key.caps_lock,
             'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", '\\', Key.shift,
             'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', Key.shift_r,
             Key.ctrl_l, Key.alt_l, Key.cmd, Key.space, Key.cmd_r, Key.alt_gr, Key.ctrl_r, Key.left, Key.down, Key.right, Key.up,
             '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
             'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', '|',
             'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?']                   #names of keys
writer.writerow(key_names)           #upon start of program, write the keys on top of csv file in order to see what counting number fits to what key

key_press_count = []                 #initialize list of counting numbers. Makes it the same length as the name list
for _ in range(len(key_names)):
    key_press_count.append(0)

def on_press(key):
    global last_press
    global key_names
    global key_press_count

    #write to csv when 50 keys have been pressed
    if sum(key_press_count) > 50:
        writer.writerow(key_press_count)
        csvfile.flush()

        #reset the count list
        key_press_count = []
        for _ in range(len(key_names)):
            key_press_count.append(0)

    if key == Key.shift and last_press == Key.shift:
        pass
    else:
        array_count = -1
        match = 0
        for i in key_names:
            array_count += 1
            try:
                if i == key.char:
                    match = 1
                    break
            except AttributeError:
                if i == key:
                    match = 1
                    break
        if match == 0:
            try:
                key_names.append(key.char)
                key_press_count.append(1)
            except AttributeError:
                key_names.append(key)
                key_press_count.append(1)
        else:
            key_press_count[array_count] += 1
        last_press = key
    
##quit on esc
def on_release(key):
    pass
#    if key == keyboard.Key.esc:
#        # Stop listener
#        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()