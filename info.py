"""
----------Introduction to Bash Scripting:------------------
What is Bash?
    A shell language
    Bourne Again Shell
    Easy commands
Why learn Bash?
    Most used shell
    Stands the test of time
    Comes with Linux and other OS
Why not Bash?
    Lacks features
    No OOP
    Difficult syntax compared to Python
    Newer tools like Ansible
Still useful
    Lightweight and always available
    Is not mutually exclusive
    Basic Knowledge makes big difference

Will use WSL (Windows Subsystem for Linux)
(Write every command in terminal from ubuntu)

Basic commands-----------------------------------------
echo: displays text you pass as an argument
    echo hello
cat: displays content of a file
        But first we need to create a file:
    vim: text editor
        vim textfile.txt
            press i to enter insert mode
            type whatever you want
            pres esc to go back to command mode
            :w
                to write the file and save changes
                :q
                    to exit file
                    or just do :wq
                    :q! to exit without saving changes
    cat textfile.txt
ls: list files in cur dir
    ls -l: long format (-l is called a flag)
pwd: print working directory
bash: run shell script
    bash name_of_file
echo $SHELL:
    veryfy in which shell you are running (bash in this case)
chmod u+x name_of_file:
    give user executable permission for a specific file

Writing your first bash script------------------------------
vim shelltest.sh
    press a to enter append mode (just to show another way rather than i)
        (this will append your text rather than insert it)
        insert mode: write character before the cursor
        append mode: write character after the cursor
    write:
        echo Hello World!
    esc
    :wq
bash shelltest.sh
    run our bash script
echo $SHELL
    to veryfy that we are running in a bash shell, so teretically we shouldnt
    have to specify it, but is a best practice to do so
    But good news is that we can enter this info inside our shell script
    (type it at top of script)
    In order to do that you have to provide the full path to the shell
    interpreter. So copy the output path of the command echo $SHELL
    and paste it in shel script
vim shelltest.sh
    the first line should be:
    #!copied_path (#!/bin/bash)
    (this is called the shebang: #!
    which is basically telling shell script which interpreter to use)
    save and go back to terminal (:wq)
./shelltest.sh
    to now run the file in a better way
    permission will be denied, so you have to grant permissions:
        chmod u+x shelltest.sh
            grant permission to execute file only to user
./shelltest.sh

Variables--------------------------------------------------------------
vim shelltest.sh


"""
