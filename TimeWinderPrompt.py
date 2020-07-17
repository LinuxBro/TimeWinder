from cmd import Cmd
import datetime

class TimeWinderPrompt(Cmd):
    claim = ""
    def do_exit(self, inp):
        print("Bye")
        return True
    def do_newclaim(self, inp):
        'Create a new claim and switch the context to that claim'
        goodname = False
        while not goodname:
            name = input("Enter Claim Name")
            goodname = verify(name)
        claimdate = datetime.datetime.now().date()
        claimname = str(claimdate) + "_" +  name
        print(claimname)


        
    def verifyname(self, name):
        # < > : " / \ | ? * are all no-no's in windows file names
        if "#" in name:
            return False
        elif "<" in name:
            return False
        elif ">" in name:
            return False
        elif ":" in name:
            return False
        elif "" in name:
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

