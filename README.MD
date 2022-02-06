# Keylogger using shell

> This is a simple keylogger which logs the keystrokes by usr till the program is running.  
> Mostly used language is Python but initialization can be done only with shell script.  
> I'll upload one more simple keylogger but it's main disadvantage is the output file can't be deleted as the output file is not being closed by program.  
> Before using this keylogger, you need to modify the program with various data which I'll be explaining later.  

# Tools used to run

1. If you're using Linux destro (Kali Linux, Ubuntu, Parrot etc), you just need to clone this repo using ```git clone https://github.com/nitinkumar30/keylogger```  
2. If you're using Windows OS, you need to run it inside VS Code (I've tried in VS Code).
   1. Visual Studio Code
   2. Try [this](https://stackoverflow.com/a/50527994) solution to run
   3. If above solution doesn't work, try [this](https://stackoverflow.com/questions/42606837/how-do-i-use-bash-on-windows-from-the-visual-studio-code-integrated-terminal)

# Code to run this keylogger

1. For Linux OS
   1. Open terminal in **sudo** mode and type ```git clone https://github.com/nitinkumar30/keylogger```  
   2. It'll create a local directory of it. Now type ```ls```. You'll see the directory ___keylogger___.  
   3. Type ```cd keylogger```
   4. Now again type ```ls -l``` to see all files with their file permissions
   5. Now type ```chmod +x setup.sh``` to give executable permission to shell\bash file  
   6. Now type ```pip3 install -r requirements.txt``` [ btw, my code will install required libraries automatically but just to make sure everything works fine]
   7. Now run the script as ```./setup.sh OPTION``` ; OPTION is the options chosen by user how he need the output file generated of the log file. There are 2 options: ```file``` and ```email```.  
   8. The output file will be generated and filename will be in format ___keylog_starttime_endtime___.  
   9. In case you need to mail the output, you need to do some changes in code as well as Google Account itself. For more info, kindly visit **Google Account customisation and File changes to be done** below.  
   10. To stop the program simply type ```CTRL + C``` in terminal.
2. For Windows OS
   1. Extract the downloaded repo and open the folder in Visual Studio Code.  
   2. Follow [this](https://stackoverflow.com/a/50527994) process or go up to **Tools used to run**  
   3. Change the file [keylogger.py](https://github.com/nitinkumar30/keylogger/blob/main/keylogger.py) as per the instructions.  
   4. Run the file [setup.sh](https://github.com/nitinkumar30/keylogger/blob/main/setup.sh) using the code ```./setup.sh OPTION``` ;OPTION is the options chosen by user how he need the output file generated of the log file. There are 2 options: ```file``` and ```email```.  
   5. File will run and the output file will be mailed or saved in local directory as per the above files.  
   6. In the end, you need to stop the program. To do so, simple type ```CTRL + C``` in terminal.  

# Google Account customisation

1. The very first thing you need to do is customise your google gmail account.
2. Visit [here](https://support.google.com/mail/answer/7126229?p=WantAuthError&visit_id=637796421626626182-1497188236&rd=2#cantsignin&zippy=%2Ci-cant-sign-in-to-my-email-client%2Cstep-change-smtp-other-settings-in-your-email-client%2Cstep-check-that-imap-is-turned-on) and check IMAP is turned ON.
3. Now try to run code. If you're getting an error related to OAuth or authentication, you need to provide App Password. So, go to next step.
4. Turn ON less secured apps by navigating [here](https://support.google.com/accounts/answer/6010255)
5. Now, create a new App Password by navigating [here](https://support.google.com/accounts/answer/185833)
6. Copy the 16-character code in yellow bar and paste in [keylogger.py](https://github.com/nitinkumar30/keylogger/blob/main/keylogger.py)
7. Now, run the code.!

# File changes to be done

1. Firstly you need to pass your gmail id in 9th line inside [keylogger.py](). Following is the code:
      EMAIL_ADDRESS = "yourgmailid@gmail.com"
2. Now, you need to pass your google account password(of course you need to give and it can't be hacked as it's in your local file) in next line. 
      EMAIL_PASSWORD = "yourgmailpass@123"
3. If google account password doesn't work, delete the google account password and put App Password(that 16 digit code you got) in the same place.
      EMAIL_PASSWORD = "abcdefghijklmnop"

# Disclaimer

**Kindly don't use this to harm anyone or perform any unethical activities. I strongly support ethical hacking and my intension is just to let my fellow githubers know how to make a simple keylogger.**  
**Also this repo is PUBLIC and you may use the code for free but make sure to give me due credits for my work, dedication and whole weekend.**  

# Author

[Nitin Kumar](https://linkedin.com/in/nitin30kumar/)
