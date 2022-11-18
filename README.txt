Author: Samuel Lehman
        18/11/2022
        Last modified: 1:07PM 11/18/2022

Project Title: Metadata Management
This project is project assignment 2 for CS457 Database Management Systems at the University of Nevada, Reno
This program allows for the creation of databases and tables similar to SQLite

Getting Started:
This document will help you get this program running on your local environment 

Prerequisites:
Python version 3.9.2
A unix operating system such as ubuntu or the linux subsystem for windows

System Design:
This program uses linux directories as databases and files as database tables

Built with/Implementation:
This program was written in Python
Its functionalities are creating, altering, and viewing databases and tables
This program uses if an for loops to achieve this 
This program also allows a user to preform joins on tables
Modules used in the program are:
os: to get file paths
sys: to get program arguments
subprocess: to run linux commands from the program
This program uses a custom made class called "SamQLTable" that provides
functionality to create and manipulate tables

How to run/test:
1) Open a linux virtual machine or use the linux subsystem for windows
2) change directory to where the files are installed
3) run the command "python3 samuellehman_pa3.py" to run the program without a test file
if you have a test file run the command "python3 samuellehman_pa3.py [test file]"
a test file has been provided so you can just run "python3 samuellehman_pa3.py test.sql"