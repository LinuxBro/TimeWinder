from cmd import Cmd
import datetime
import os
from os import path
import Claim
import Line
from prettytable import PrettyTable


class TimeWinderPrompt(Cmd):
    claim: Claim.Claim = ""
    prompt = "TW>"

    def startup(self):
        if not self.home_check():
            os.mkdir("Claims")
            print("Claims directory not found, one was created for you at: " + os.getcwd() + "\Claims")

    @staticmethod
    def do_exit(inp):
        print("Bye")
        return True

    def do_setPerDiem(self,inputdiem):
        try:
            diem = float(inputdiem)
        except Exception as e:
            print("failed to input a float.  usage is 'setPerDiem XX.XX'")
            return
        "Sets per diem for every day in the claim, automatically calculating the 75/25 split for first/last day"
        for day in self.claim.days:
            day.lines.append(Line.Line(diem,"Per Diem", "Y", "Per Diem"))
    def do_newclaim(self, inp):
        'Create a new claim and switch the context to that claim'
        self.prompt = "New Claim> "

        "Ask for the name of the claim, as well as verify it."
        "When the name is verified create a folder for it."
        goodname = False
        name = ""
        while not goodname:
            name: str = input("Enter Claim Name: ")
            goodname = self.verifyname(name)
        claimdate = datetime.datetime.now().date()
        claimname = str(claimdate) + "_" + name
        self.prompt = claimname + "> "
        claimdir = "Claims\\"+claimname
        imagesdir = "Claims\\"+claimname+"\\Images"
        os.mkdir(claimdir)
        os.mkdir(imagesdir)
        #TODO properly validate date
        daterange = input("Provide the start-end dates in the format MM/DD/YYYY-MM/DD/YYYY (currently does not check, be careful): ")
        startdate,enddate = self.verifydate(daterange)
        newclaim = Claim.Claim(claimdir, claimname,startdate,enddate)
        self.claim = newclaim
        self.prompt = claimname + "> "


    def do_print(self):
        "Prints current status of claim"








    @staticmethod
    def verifydate(daterange):
        start = daterange[:10]
        end = daterange[11:22]
        startdate = datetime.datetime.strptime(start,'%m/%d/%Y')
        enddate = datetime.datetime.strptime(end, '%m/%d/%Y')
        return startdate, enddate

    @staticmethod
    def verifyname(name):
        # < > : " / \ | ? * are all no-no's in windows file names
        if "#" in name:
            return False
        elif "<" in name:
            return False
        elif ">" in name:
            return False
        elif ":" in name:
            return False
        elif "\"" in name:
            return False
        elif "/" in name:
            return False
        elif "\\" in name:
            return False
        elif "|" in name:
            return False
        elif "?" in name:
            return False
        elif "*" in name:
            return False
        else:
            return True

    @staticmethod
    def home_check():
        if path.exists("Claims"):
            return True
        else:
            return False

