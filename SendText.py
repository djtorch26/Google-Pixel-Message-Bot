# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:03:31 2020

Sends The Bee movie Script word by word in seperate message strings to any phone number in your contacts list.

FAILSAFE: MOVE MOUSE TO TOP LEFT CORNER TO STOP PROGRAM
FAILSAFE: MOVE MOUSE TO TOP LEFT CORNER TO STOP PROGRAM
FAILSAFE: MOVE MOUSE TO TOP LEFT CORNER TO STOP PROGRAM
FAILSAFE: MOVE MOUSE TO TOP LEFT CORNER TO STOP PROGRAM
FAILSAFE: MOVE MOUSE TO TOP LEFT CORNER TO STOP PROGRAM

"""


from selenium import webdriver
import pyautogui as control
import sys

control.FAILSAFE = True #failsafe in case messaging wrong person, MOVE MOUSE TO TOP LEFT CORNER TO STOP PROGRAM
from time import sleep

control.PAUSE = .2  #amount of time in between each 'control.action'

Chatname = 'INPUT CHAT NAME HERE' #input text chat name, individual or Group Chat, doesn't matter

def main():
    driver = webdriver.Firefox()
    driver.get("https://messages.google.com/web/authentication")
    sleep(5)
    convobox = driver.find_element_by_partial_link_text(Chatname) 
    convobox.click()
    textbox = driver.find_element_by_class_name('input')
    SendMessages(textbox)


def SendMessages(clickable):
    script = open('no_line_script.txt')
    for i in range(count_lines()):
        line = script.readline().rstrip('\n').split(" ")
        for word in line:
            print(f'Sending the word {word}')
            try:
                control.typewrite(word)
                control.press('enter')
            except:
                sys.exit()
                print("Error in sending last message")
    
def count_lines(file='no_line_script.txt'):
    with open(file, 'r') as file:
        for index, line in enumerate(file):
            pass
    file.close()
    return index + 1

def remove_lines(original='BeeMovieScript.txt', empty='no_line_script.txt'):
    script = open(original, 'r')
    empty_script = open(empty, 'w')

    script_length = count_lines(original)
    for i in range(script_length):
        line = script.readline()
        if line.replace(" ","") not in ['\n','\r\n']:
            empty_script.write(line)
            
if __name__ == "__main__":
    main()
