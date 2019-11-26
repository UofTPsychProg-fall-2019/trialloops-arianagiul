#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 

import numpy as np
import pandas as pd
import os, sys
import ctypes
from psychopy import visual, core, event, gui, logging

#experiment
expName = 'WeirdImages'
fileName = ''
while True:
    expInfo = {'subjNum':''}
    dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    if dlg.OK == False: core.quit()
    fileName = expName + '_' + expInfo['subjNum']+'.csv'
    break

#create data frame
variables = ['trial', 'condition', 'scene', 'rt']
outputs = pd.DataFrame(columns=variables)

#create a window
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height')

#unchanging information
instruct_begin = visual.TextStim(win, pos=(0,0), height=None, color='black', alignHoriz='center', text="""You will be asked to decide whether or not a scene is likely or unlikely.

Respond as quickly and as accurately as possible.

If you think the scene is likely, press the right arrow key. If you think the scene is unlikely, press the left arrow key.

Press the left or right arrow key to begin.""")
instruct_trialtop = visual.TextStim(win, pos=(0,0.75), height=None, color='black', text='Is this scene likely or unlikely?')
instruct_trialbottomright = visual.TextStim(win, pos=(0.5,-0.75), height=None, color='black', text='Right Key = likely')
instruct_trialbottomleft = visual.TextStim(win, pos=(-0.5,-0.75), height=None, color='black', text='Left Key = unlikely')
thanks = visual.TextStim(win, text='Thank you for your participation.', height=None, pos=(0,0), color='black')
ntrials = 8

#clock stuff
trialClock = core.Clock()
eventClock = core.Clock()

#make a list or a pd.DataFrame that contains trial-specific info (stimulus, etc)
conditions = pd.read_csv('conditions.csv')

#randomizing
conditions = conditions.sample(frac=1)
conditions = conditions.reset_index()

#%% your loop here
# start by copying your one trial here, then identify what needs to be
# changed on every trial.  Likely your stimuli, but you might want to change a few things

#beginning instructions display until a key is pressed
instruct_begin.draw()
win.flip()
event.waitKeys()

for t in np.arange(0, ntrials):
    
    event.clearEvents()
    eventClock.reset()
    
    # include your trial code in your loop but replace anything that should 
    # change on each trial with a variable that uses your iterater
    # e.g. thisStimName = stim[t]
    #      thisStim = visual.ImageStim(win, image=thisStimName ...)
    
    outputs.loc[t,'trial'] = t + 1
    outputs.loc[t,'condition'] = conditions.loc[t,'condition']
    outputs.loc[t,'scene'] = conditions.loc[t,'object']

    yesno = visual.ImageStim(win, size=(1,1), pos=(0,0), image='pics/'+conditions.loc[t,'object'])
    
    #recording parameters
    
    trialClock.reset()
    yesno.draw()
    win.flip()
    keys = event.waitkeys(maxWait = 4, keylist = ['left','right'])
    
    # if you're recording responses, be sure to store your responses in a list
    # or DataFrame which also uses your iterater!
    outputs.loc[t,'rt'] = trialClock.getTime()
    
    

#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

outputs.to_csv(fileName, index=False)

thanks.draw()
win.flip()

core.wait(2)
win.close()
