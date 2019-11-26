#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 1
Use this template script to present one trial with your desired structure
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging

# open a white full screen window (making a second window for the beginning instructions)
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height') 

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
#trialClock = core.Clock()

#%% up to you!
# this is where you build a trial that you might actually use one day!
# just try to make one trial ordering your lines of code according to the 
# sequence of events that happen on one trial
# if you're stuck you can use the responseExercise.py answer as a starting point 

#importing trial information
conditions = pd.read_csv('conditions.csv')

# maybe start by making stimulus objects (e.g. myPic = visual.ImageStim(...))

#trial prompt
instruct_trialtop = visual.TextStim(win, pos=(0,0.75), height=None, color='black', text='Is this scene likely or unlikely?')
#trial response keys
instruct_trialbottomright = visual.TextStim(win, pos=(0.5,-0.75), height=None, color='black', text='Right Key = likely')
instruct_trialbottomleft = visual.TextStim(win, pos=(-0.5,-0.75), height=None, color='black', text='Left Key = unlikely')
#trial image stimulus
yesno = visual.ImageStim(win, size=(1,1), pos=(0,0), image='pics/yes1.png')

#draw all trial stimuli
instruct_trialtop.draw()
instruct_trialbottomright.draw()
instruct_trialbottomleft.draw()
yesno.draw()

# then flip your window
win.flip()

# then record your responses
leys = event.waitKeys(keyList=['right','left'])
print(keys)

#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

core.wait(2)
win.close()
