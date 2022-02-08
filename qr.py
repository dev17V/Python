# May Show Error "Import "qrcode" could not be resolved" Just Leave It! It Will Work
# pip install qrcode

import qrcode 
import os 

def clear():
    os.system('clear')
def main():
    url = input("Please Type The URL You Want To Turn Into A QR Code: ")
    img = qrcode.make(url)
    img.show()
    print("Complete!")
    #clear()
    main()
clear()
main()