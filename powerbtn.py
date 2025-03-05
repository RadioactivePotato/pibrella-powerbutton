import time
import os
import pibrella

# sequence() is currently unused
def sequence():
    pibrella.light.red.on()
    time.sleep(1)
    pibrella.light.red.off()
    pibrella.light.yellow.on()
    time.sleep(1)
    pibrella.light.yellow.off()
    pibrella.light.green.on()
    time.sleep(1)
    pibrella.light.green.off()

def lighton():
    pibrella.light.red.on()
    pibrella.light.yellow.on()
    pibrella.light.green.on()

def lightoff():
    pibrella.light.red.off()
    pibrella.light.yellow.off()
    pibrella.light.green.off()

def poweroff():
    print("""
    ############
    POWERING OFF
    ############
    """)
    os.system("sudo poweroff")

def finalseq():
    print("Shutting down in 3 seconds") # it's actually 2.5 seconds
    lighton()
    time.sleep(0.5)
    lightoff()
    time.sleep(0.5)
    lighton()
    time.sleep(0.5)
    lightoff()
    time.sleep(0.5)
    lighton()
    time.sleep(0.5)
    lightoff()
    poweroff()

def check_button_hold():
    hold_time = 0
    while True:
        print("Button UP")
        if pibrella.button.read() == 1:
            print("Button DOWN")
            start_time = time.time()
            while pibrella.button.read() == 1:
                if time.time() - start_time >= 3: # hold button for 3 seconds
                    finalseq()
                    break
                time.sleep(0.1) # time in seconds to check for button status
        time.sleep(0.1)

if __name__ == "__main__":
    check_button_hold()
