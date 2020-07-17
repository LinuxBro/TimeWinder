import time

import datetime
import TimeWinderPrompt
def main():
    prompt = TimeWinderPrompt.TimeWinderPrompt()
    prompt.cmdloop()


def newClaim():
    time.sleep(1)
    data = input("enter input")
    currentmenu = "newclaim"
    claimdate = datetime.date(datetime.datetime.now())
    print(claimdate)
    print("New Claim Path")
    time.sleep(3)


def oldClaim():
    print("Old Claim Path")
    time.sleep(1)


def startup():
    # DO NOT TOUCH THIS, THE ESCAPE CHARACTERS ARE FINE
    # DO NOT TOUCH THIS, THE ESCAPE CHARACTERS ARE FINE
    # DO NOT TOUCH THIS, THE ESCAPE CHARACTERS ARE FINE
    print('''
                               ________  __                                            
              (()             /        |/  |                                           
              (()             $$$$$$$$/ $$/  _____  ____    ______                     
              (()                $$ |   /  |/     \/    \  /      \                    
              (()                $$ |   $$ |$$$$$$ $$$$  |/$$$$$$  |                   
              (()                $$ |   $$ |$$ | $$ | $$ |$$    $$ |                   
              .+.                $$ |   $$ |$$ | $$ | $$ |$$$$$$$$/                    
          _.-//_\\-._             $$ |   $$ |$$ | $$ | $$ |$$       |                   
        .'.-' XII '-.'.          $$/    $$/ $$/  $$/  $$/  $$$$$$$/                    
      /`.'*         *'.`\\        __       __  __                  __                       
     / /*        /    *\ \\      /  |  _  /  |/  |                /  |                     
    | ;        _/       ; |     $$ | / \ $$ |$$/  _______    ____$$ |  ______    ______   
    | |IX     (_)    III| |     $$ |/$  \$$ |/  |/       \  /    $$ | /      \  /      \ 
    | ;         \       ; |     $$ /$$$  $$ |$$ |$$$$$$$  |/$$$$$$$ |/$$$$$$  |/$$$$$$  |
     \ \*        \    */ /      $$ $$/$$ $$ |$$ |$$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
      \ '.*       \ *.'./       $$$$/  $$$$ |$$ |$$ |  $$ |$$ \__$$ |$$$$$$$$/ $$ |      
       '._'-.__VI_.-'_.'        $$$/    $$$ |$$ |$$ |  $$ |$$    $$ |$$       |$$ |      
          '-.,___,.-'           $$/      $$/ $$/ $$/   $$/  $$$$$$$/  $$$$$$$/ $$/       
                               
''')
    # DO NOT TOUCH THIS, THE ESCAPE CHARACTERS ARE FINE
    # DO NOT TOUCH THIS, THE ESCAPE CHARACTERS ARE FINE
    # DO NOT TOUCH THIS, THE ESCAPE CHARACTERS ARE FINE
    time.sleep(.5)
if __name__ == "__main__":
    startup()
    main()