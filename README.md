# AiCore Project
## Hangman 

## Table of Contents
### 1. Overview
### 2. Installation instructions
### 3. Usage instructions
### 4. File structure 
### 5. License information 


Not sure what this is or why it was pasted off my cursor but it might be important: 
https://portal.theaicore.com/project/ccec2912-b0c5-4798-bcfd-21add0e658af 

## 1. Overview

Basically I'm creating a game of Hangman by following instructions on AiCore's teaching platform. The project aim is to combine and 
consolidate what I've learned so far on AiCore into a functional activity.
I have used file manipulation in GitBash, Python coding (in VSCode, despite Spyder being \**chef's kiss*\*), and git and GitHub to submit this project online. 
So far I haven't learned anything new by completing this project, but I have revised quite a few little things. For instance:
 - mv is the git bash command for moving a file from one directory 
 - README.txt is a markdown file so I can use the same formatting codes as in RMarkdown (with which I am more familiar) 
 - string.lower() will turn every letter in string to lowercase 

Within this repo are the following files: 

 - README.md (this file)
 - README.txt (an older version of README that you can ignore)
 - milestone\_2.py (an initial piece of code named according to AiCore's instructions) 
 - milestone\_3.py (a more developed piece of code on which you can run a single turn of Hangman) 
 - milestone\_4.py (an encapsulation of the work so far, folded into a class called Hangman) 
 - milestone\_5.py (should be the final iteration of the game, which includes the winning/losing logic of it.) 

### Learned and yet to learn: 

Two major bugs have shaped my learning experience on this project. 
The first was solved by a friend who is a full-time coder. 
When initiating self.attributes I should NOT include the self prefix in their definitions; this I knew. However, when I kept getting NameErrors in my attempts to execute a function defined in the class, it was consistently because somewhere in the definition of the *function* I was **not** including the self prefix for a called attribute. In short:
 - Defining attributes within a class doesn't require the self prefix
 - Defining functions within a class *does*. 

The second major bug is yet to be solved.
I've tried various iterations of positioning the play\_game function\- instructions dictate that it be on its own (outside the class), but that consistently left it seemingly not adjusting the number of lives *within the specific instance of game* whenever I left print checks in the function definition. 
So you'll see in my latest iteration of milestone\_5.py, I attempted to turn the play\_game function into a class function. 
The same issue persists. smh 

However, as I have done more than was asked of me for this assignment, and I don't have all week to work on this, I'm calling it... a project, complete. :/ 

## 2. Installation instructions

To install this game of Hangman, pull this repo or simply copy and paste milestone\_3.py into your own file. 


## 3. Usage instructions

Run milestone\_\?.py to play a game of Hangman. If you don't know how that game works, here's the general idea: https://www.wikihow.com/Play-Hangman


## 4. File structure

At this stage there is no directory hierarchy. There is simply the Hangman folder which contains all relevant documents. 

The structure of milestone\_3.py is as follows:

 - import random 
 - select a random word from a list 
 - define check\_guess function 
 - define ask\_for\_input function
 - call ask\_for\_input function. 


## 5. License information

This code is following step-by-step instructions from AiCore, so credit for code development goes to them. Anyone is welcome to use this code to help their learning. 
 
