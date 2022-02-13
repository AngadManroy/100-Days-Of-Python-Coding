from email import message
from ipaddress import ip_network
from random import choice
import enc_dec

if __name__=="__main__":
    x = True
    while x:
        mode = input("Encode or Decode?")
        if mode.lower() == 'encode' or mode.lower() == 'decode':
            message_= input("Enter your message: ")
            print(f"Your final message is {enc_dec.caeser(message_=message_,mode_=mode)}")
        else:
            print("Not an appropriate option")
        choice_ = input("Would you like to continue(y/n): ")
        if choice_.lower() == 'n':
            x = False
            print("GoodBye!!")