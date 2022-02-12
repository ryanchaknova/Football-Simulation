import pandas as pd
#from pandas.core.arrays.sparse import dtype
import numpy as np
import time

#always take higher of 2 overalls
def getMaxPlayer(team,cat): #helper function for all plays 
    #check=team[cat].to_list()
    max=team[cat].max()
    #print(max)
    
    check=team.loc[team[cat]==max]
    #print(check)# print(type(cat))
    check2=check.loc[check["Overall"]==check["Overall"].max()]
    
    return(check2)# print(team)
def getMaxPositionPlayer(team,position,size):
    players=team.loc[team["Position"]==position]
    if(len(players)==1):
        return(players)
    else:
        playersReturn=list()
        
        while(len(playersReturn)<=size):
            temp=list()
  
            players=temp
def readTeam(name):
    #need to delete frist row
      
    name=name+".xlsx"
    #	Team	Position	Archetype	Jersey #	First Name	Last Name	Age	Height	Weight	Overall	Speed	Acceleration	Agility	Change of Dir	Strength	Jumping	Awareness	Carrying	Break Tackle	Juke Move	Spin Move	Trucking	Stiff Arm	BC Vision	Catching	Catch In Traffic	Spec Catch	Release	Short RR	Medium RR	Deep RR	Throw Power	Throw Acc Short	Throw Acc Mid	Throw Acc Deep	Throw Under Pressure	Throw On The Run	Play Action	Break Sack	Run Block	Run Block Power	Run Block Finesse	Pass Block	Pass Block Power	Pass Block Finesse	Impact Blocking	Lead Blocking	Tackle	Hit Power	Pursuit	Man Coverage	Zone Coverage	Press	Play Recognition	Power Moves	Finesse Moves	Block Shedding	Kick Power	Kick Accuracy	Kick Return	Stamina	Injury	Toughness	Total Salary	Signing Bonus	Run Style	Birthdate	Years Pro	Handedness	College	Portrait ID	Team ID	Primary Key	Full Name	Player Asset	Iteration	Status	BLANK


    check=pd.read_excel(name)
    check.columns=["#","Team","Position","Archetype","Jersey #","First Name","Last Name","Age","Height","Weight","Overall","Speed","Acceleration","Agility","Change of Dir","Strength","Jumping","Awareness","Carrying","Break Tackle","Juke Move","Spin Move","Trucking","Stiff Arm","BC Vision","Catching","Catch In Traffic","Spec Catch","Release","Short RR","Medium RR","Deep RR","Throw Power","Throw Acc Short","Throw Acc Mid","Thrrow Acc Deep","Thorw Under Pressure","Throw on The Run","PLay Action","Break Sack","Run Block","Power Run Block","Run Block Finesse","Pass Block","Pass Block Power","Pass Block Finesse","Impact Blocking","Lead Blocking","Tackle","Hit Power","Pursuit","Man Coverage","Zone Coverage","Press","Play Recognition","Power Moves","Finesse Moves","Block Shedding","Kick Power","Kick Accuracy","Kick Return","Stamina","Injury","Toughness","Total Salary","Signing Bonus","Run Style","Birthdate","Years Pro","Handedness","College","Portrait ID","Team ID","Primiary Key","Full Name","Player Asset","Iteration","Status","BLANK"]
    i=0
    #for col in check.columns:
        #print(i)
        #i+=1
        #print(col)
    
    colnamesINT=["Height","Weight","Overall","Speed","Acceleration","Agility","Change of Dir","Strength","Jumping","Awareness","Carrying","Break Tackle","Juke Move","Spin Move","Trucking","Stiff Arm","BC Vision","Catching","Catch In Traffic","Spec Catch","Release","Short RR","Medium RR","Deep RR","Throw Power","Throw Acc Short","Throw Acc Mid","Thrrow Acc Deep","Thorw Under Pressure","Throw on The Run","PLay Action","Break Sack","Run Block","Power Run Block","Run Block Finesse","Pass Block","Pass Block Power","Pass Block Finesse","Impact Blocking","Lead Blocking","Tackle","Hit Power","Pursuit","Man Coverage","Zone Coverage","Press","Play Recognition","Power Moves","Finesse Moves","Block Shedding","Kick Power","Kick Accuracy","Kick Return","Stamina","Injury","Toughness"]
    for i in range(len(colnamesINT)):
        for j in range(0,len(check[colnamesINT[i]])):
            #print(j)
            #print(check[colnamesINT[i]][j])
            if(j==0):
                check[colnamesINT[i]][j]=-1
            check[colnamesINT[i]][j]=int(check[colnamesINT[i]][j])
           # print(type(check[colnamesINT[i]][j]))
    #print(check["Kick Return"])
    
    #for i in range(len(check["Kick Return"])):
        #print(type(check["Kick Return"][i]))
    
    #print(np.where(max(check["Kick Return"]))[1])
    
    #print(check["First Name"][np.where(max(check["Kick Return"]))])
    
    
   # print()
    
    return check


#broncos=readTeam("Broncos")
#getMaxPositionPlayer(broncos,"QB")



#simply use name strings in order away,home,control away is bool set to true is user controlls away,sim true if no-one is controlled by user
#returns 1 for away team kick, 0 for home team kick
def CoinToss(team1,team2,sim,home,away):
    np.random.seed(int(time.time())+np.random.randint(0,9999,dtype=int))
    coin = np.array(["1", "0"])
    result=np.random.choice(coin)
    if(sim==0):
        awayChoice=np.random.choice(coin)
        if(awayChoice==result):
            #away sim win
            print(away," have won the coin toss")
            #below should be remade to inflict real team tendicies which will be created at a later date
            # 1 for defer, 0 for receive
            kick=np.random.choice(coin,p=[.90,.10]) #defer 90% of the time, this will change to real world %
            if(kick=="1"):
                print(away," have elected to defer")
                return(kick)
            else:
                print(away," have elected to receive")
                return(kick)
        else:
            print(home," have won the coin toss") 
            kick=np.random.choice(coin,p=[.90,.10])
            if(kick=="1"):
                print(home," have elected to defer")
                return(0)
            else:
                print(home," have elected to receive")
                return(1)
    elif(sim=="1"):
        #prompt user for tails or heads
        print("Please choose Tails or Heads\n1: Heads\n0: Tails")
        choice=input()
        
        if(result==choice):
            #user have won coin toss
            print("You have won the coin toss!\n1: Defer\n0: Receive\n")
            return input()
        else:
            print("You have lost the coin toss!")
            kick=np.random.choice(coin,p=[.90,.10]) #defer 90% of the time, this will change to real world %
            print(kick)
            if(kick=="1"):
                print(away," have elected to defer")
                return(0)
            else:
                print(away," have elected to recieve test")
                return(1)
                
    else: #home is controlled
        print("home")
        awayChoice=np.random.choice(coin) 
        if(awayChoice=="1"):
            print(away," have chosen Heads\n")
        else:
            print(away," have chosen Tails\n")


        if(result==awayChoice):
            print("no win")
            if(awayChoice=="1"):
                print("The coin is heads ",away," have won the coin toss\n")
            else:
                print("The coin is tails ",away," have won the coin toss\n")
            
            
            
            
            kick=np.random.choice(coin,p=[.90,.10]) #defer 90% of the time, this will change to real world %
            if(kick=="1"):
                print(away," have elected to defer")
            else:
                print(away," have elected to receive")
            return(kick)
        else:
            print("win")
            if(awayChoice=="1"):
                print("The coin is tails ",home," have won the coin toss\n")
            else:
                print("The coin is heads ",home," have won the coin toss\n")
            
            
            print("You have won the coin toss!\n1: Defer\n0: Receive\n")
            choice=input()
            if(choice=="1"):
                return(0)
            else:
                return(1)

#1 for awaykcick,0 for home,take team ratings and names, diff is home-away
def Kickoff(awayKick,home,away,homeName,awayName,sim,Quater,diff,tendies):
    turnover=False
    np.random.seed(int(time.time())+np.random.randint(0,9999,dtype=int))
    kickType=np.array(["Onside","Squib","SkyKick","Normal"])
    KickStyle=np.array(["Left","Right","Short","Deep"])
    kickStart=np.array(["Touchback","Out of Bounds","In Play","Success"])
    #if home/away change to one value
    if(awayKick=="0"):
        #print("abron kick")
        Tend=tendies.loc[tendies["Team"]==awayName]
        returner=getMaxPlayer(home,"Kick Return")
        kicker=getMaxPositionPlayer(away,"K",1)
        power=float(kicker["Kick Power"].to_list()[0])
        Acc=float(kicker["Kick Accuracy"].to_list()[0])
        Return=float(returner["Kick Return"].to_list()[0])
        Speed=float(returner["Speed"].to_list()[0])
        Stiff=float(returner["Stiff Arm"].to_list()[0])
        Truck=float(returner["Trucking"].to_list()[0])
        Spin=float(returner["Spin Move"].to_list()[0])
        Juke=float(returner["Juke Move"].to_list()[0])
        breakTakle=float(returner["Break Tackle"].to_list()[0])
        Carry=float(returner["Carrying"].to_list()[0])
        if(Quater>=4 and diff>3):
            kickTypeResult=np.random.choice(kickType,p=[.8,.01,.02,.17])
            KickStyleResult=np.random.choice(KickStyle,p=[.3,.3,.1,.3])
        else:
            kickTypeResult=np.random.choice(kickType,p=[.005,.0075,.0075,.98])
            KickStyleResult=np.random.choice(KickStyle,p=[.1,.1,.1,.7])
    else:
        Tend=tendies.loc[tendies["Team"]==homeName]
        returner=getMaxPlayer(away,"Kick Return")
        kicker=getMaxPositionPlayer(home,"K",1)
        power=float(kicker["Kick Power"].to_list()[0])
        Acc=float(kicker["Kick Accuracy"].to_list()[0])
        Return=float(returner["Kick Return"].to_list()[0])
        Speed=float(returner["Speed"].to_list()[0])
        Stiff=float(returner["Stiff Arm"].to_list()[0])
        Truck=float(returner["Trucking"].to_list()[0])
        Spin=float(returner["Spin Move"].to_list()[0])
        Juke=float(returner["Juke Move"].to_list()[0])
        breakTakle=float(returner["Break Tackle"].to_list()[0])
        Carry=float(returner["Carrying"].to_list()[0])
        if(Quater>=4 and diff<3):
            kickTypeResult=np.random.choice(kickType,p=[.8,.01,.02,.17])
            KickStyleResult=np.random.choice(KickStyle,p=[.3,.3,.1,.3])
        else:
            kickTypeResult=np.random.choice(kickType,p=[.01,.01,.08,.9])
            KickStyleResult=np.random.choice(KickStyle,p=[.1,.1,.1,.7])
    #print(returner)
    #print(awayKick)
    
    
    
    if(sim==0 or (sim==1 and awayKick=="0")):
        #print(sim)
        #print(awayKick)
        #print("check")
        np.random.seed(int(time.time()+np.random.randint(0,9999,dtype=int)))
        check=np.random.randint(0, 100,dtype=int)
        if(Acc<check):
            KickStyleResult=np.random.choice(KickStyle,p=[.01,.33,.33,.33])
        tbBaseProb=Tend["Touchback"]
        onBaseProb=Tend["Onside"]
        tbMultProb=float(tbBaseProb)*1.2*float(Tend["Touchback"])
        if(tbMultProb>.99):
            tbMultProb=.99
        if(kickTypeResult=="Onside"):
            if(KickStyleResult=="Left" or KickStyleResult=="Right"):
                kickStartResult=np.random.choice(kickStart,p=[0,(1-onBaseProb)/4,3*(1-onBaseProb)/4,onBaseProb])
            elif(KickStyleResult=="Short"):
                kickStartResult=np.random.choice(kickStart,p=[0,(1-onBaseProb)/8,7*(1-onBaseProb)/8,onBaseProb])
            else:
                kickStartResult=np.random.choice(kickStart,p=[0,(1-onBaseProb/2)/8,7*(1-onBaseProb/2)/8,onBaseProb/2])
#kickStart=np.array(["Touchback","Out of Bounds","In Play","Success"])
        elif(kickTypeResult=="Squib"):
            if(KickStyleResult=="Left" or KickStyleResult=="Right"):
                tbMultProbTemp=tbMultProb/3
                tbPlace=1-tbMultProbTemp
                kickStartResult=np.random.choice(kickStart,p=[tbMultProbTemp,24*tbPlace/64,39*tbPlace/64,tbPlace/64])
            elif(KickStyleResult=="Short"):
                tbMultProbTemp=tbMultProb/4
                tbPlace=1-tbMultProbTemp
                kickStartResult=np.random.choice(kickStart,p=[tbMultProbTemp,2*tbPlace/64,61*tbPlace/64,tbPlace/64])
            else:
                tbMultProbTemp=tbMultProb/2
                tbPlace=1-tbMultProbTemp
                kickStartResult=np.random.choice(kickStart,p=[tbMultProbTemp,2*tbPlace/64,61*tbPlace/64,tbPlace/64])
        elif(kickTypeResult=="SkyKick"):#maybe have a hangtime stat
            if(KickStyleResult=="Left" or KickStyleResult=="Right"):
                tbMultProbTemp=tbMultProb/3
                tbPlace=1-tbMultProbTemp
                kickStartResult=np.random.choice(kickStart,p=[tbMultProbTemp,24*tbPlace/64,39*tbPlace/64,tbPlace/64])
            elif(KickStyleResult=="Short"):
                tbMultProbTemp=tbMultProb/4
                tbPlace=1-tbMultProbTemp
                kickStartResult=np.random.choice(kickStart,p=[tbMultProbTemp,2*tbPlace/64,61*tbPlace/64,tbPlace/64])
            else:
                tbMultProbTemp=tbMultProb/2
                tbPlace=1-tbMultProbTemp
                kickStartResult=np.random.choice(kickStart,p=[tbMultProbTemp,2*tbPlace/64,61*tbPlace/64,tbPlace/64])
        else:
            if(KickStyleResult=="Left" or KickStyleResult=="Right"):
                tbMultProbTemp=tbMultProb/2
                tbPlace=1-tbMultProbTemp
                kickStartResult=np.random.choice(kickStart,p=[tbMultProbTemp,24*tbPlace/64,39*tbPlace/64,tbPlace/64])
            elif(KickStyleResult=="Short"):
                tbMultProbTemp=tbMultProb/4
                tbPlace=1-tbMultProbTemp
                kickStartResult=np.random.choice(kickStart,p=[tbMultProbTemp,2*tbPlace/64,61*tbPlace/64,tbPlace/64])
            else:
                tbMultProbTemp=tbMultProb
                tbPlace=1-tbMultProbTemp
                kickStartResult=np.random.choice(kickStart,p=[tbMultProbTemp,2*tbPlace/64,61*tbPlace/64,tbPlace/64])
    elif(sim!=0): #control away
        #print("check2")
       # print(awayKick)
        #print(type(awayKick))
        if(awayKick=="1"):
            print("Please Select A Kick Type\n1: Onside\n2: Squib\n3: Skykick\n4: Normal")
            choice=input()
            if(choice=="1"):
                kickTypeResult="Onside"
            elif(choice=="2"):
                kickTypeResult="Squib"
            elif(choice=="3"):
                kickTypeResult="Skykick"
            else:
                kickTypeResult="Normal"
            print("Please Select A Kick Style\n1: Left\n2: Right\n3: Short\n4: Deep")
            choice=input()
            #print("style choice: ",choice) 
            if(choice=="1"):
                #print("burger")
                KickStyleResult="Left"
            elif(choice=="2"):
                KickStyleResult="Right"
                #print("burger1")

            elif(choice=="3"):
                KickStyleResult="Short"
                #print("burger2")

            else:
                KickStyleResult="Deep"
                #print("burger3")

        np.random.seed(int(time.time())+np.random.randint(0,9999,dtype=int))
        check=np.random.randint(0, 100)
        # print(Acc)
        # print(type(Acc))
        # print(check)
        # print(type(check)) 
        # print("ksr: ",KickStyleResult)
        if(Acc<check):
            #print("cheese")
            KickStyleResult=np.random.choice(KickStyle,p=[.01,.33,.33,.33])
        tbBaseProb=Tend["Touchback"]
        onBaseProb=Tend["Onside"]  
        tbMultProb=float(tbBaseProb)*1.2*float(Tend["Touchback"])
        if(tbMultProb>.99):
            tbMultProb=.99
        if(kickTypeResult=="Onside"):
            if(KickStyleResult=="Left" or KickStyleResult=="Right"):
                kickStartResult=np.random.choice(kickStart,p=[0,(1-onBaseProb)/4,3*(1-onBaseProb)/4,onBaseProb])
            elif(KickStyleResult=="Short"):
                kickStartResult=np.random.choice(kickStart,p=[0,(1-onBaseProb)/8,7*(1-onBaseProb)/8,onBaseProb])
            else:
                kickStartResult=np.random.choice(kickStart,p=[0,(1-onBaseProb/2)/8,7*(1-onBaseProb/2)/8,onBaseProb/2])
            if(kickStartResult=="Success"):
                turnover=True
#kickStart=np.array(["Touchback","Out of Bounds","In Play","Success"])
        elif(kickTypeResult=="Squib"):
            if(KickStyleResult=="Left" or KickStyleResult=="Right"):
                tbMultProbTemp=tbMultProb/3
                tbPlace=1-tbMultProbTemp
                kickStartResult=np.random.choice(kickStart,p=[tbMultProbTemp,24*tbPlace/64,39*tbPlace/64,tbPlace/64])
            elif(KickStyleResult=="Short"):
                tbMultProbTemp=tbMultProb/4
                tbPlace=1-tbMultProbTemp
                kickStartResult=np.random.choice(kickStart,p=[tbMultProbTemp,2*tbPlace/64,61*tbPlace/64,tbPlace/64])
            else:
                tbMultProbTemp=tbMultProb/2
                tbPlace=1-tbMultProbTemp
                kickStartResult=np.random.choice(kickStart,p=[tbMultProbTemp,2*tbPlace/64,61*tbPlace/64,tbPlace/64])
        elif(kickTypeResult=="SkyKick"):#maybe have a hangtime stat
            if(KickStyleResult=="Left" or KickStyleResult=="Right"):
                tbMultProbTemp=tbMultProb/3
                tbPlace=1-tbMultProbTemp
                kickStartResult=np.random.choice(kickStart,p=[tbMultProbTemp,24*tbPlace/64,39*tbPlace/64,tbPlace/64])
            elif(KickStyleResult=="Short"):
                tbMultProbTemp=tbMultProb/4
                tbPlace=1-tbMultProbTemp
                kickStartResult=np.random.choice(kickStart,p=[tbMultProbTemp,2*tbPlace/64,61*tbPlace/64,tbPlace/64])
            else:
                tbMultProbTemp=tbMultProb/2
                tbPlace=1-tbMultProbTemp
                kickStartResult=np.random.choice(kickStart,p=[tbMultProbTemp,2*tbPlace/64,61*tbPlace/64,tbPlace/64])
        else:
            if(KickStyleResult=="Left" or KickStyleResult=="Right"):
                tbMultProbTemp=tbMultProb/2
                tbPlace=1-tbMultProbTemp
                kickStartResult=np.random.choice(kickStart,p=[tbMultProbTemp,24*tbPlace/64,39*tbPlace/64,tbPlace/64])
            elif(KickStyleResult=="Short"):
                tbMultProbTemp=tbMultProb/4
                tbPlace=1-tbMultProbTemp
                kickStartResult=np.random.choice(kickStart,p=[tbMultProbTemp,2*tbPlace/64,61*tbPlace/64,tbPlace/64])
            else:
                tbMultProbTemp=tbMultProb
                tbPlace=1-tbMultProbTemp
                kickStartResult=np.random.choice(kickStart,p=[tbMultProbTemp,2*tbPlace/64,61*tbPlace/64,tbPlace/64])
    #else:


    print(kickTypeResult)
    print(KickStyleResult)
    print(kickStartResult)

    if(kickStartResult=="In Play"):
        starting=np.random.normal(100-float(power),(100-float(Acc))**(1/2))
        if(starting<=0):
            starting=0
            print("Ball is Caught on the goal line")
        else:
            print("Ball is Caught on the ",starting," yard line")
    elif(kickStartResult=="Out of Bounds"):
        starting=np.random.normal(100-power,(100-Acc)**(1/2))+8
        if(starting>40):
            print("Ball is placed on the", starting ," yard line")
            return(starting)
        else:
            return(40)
            print("Ball is placed on the", starting ," yard line")
    elif(kickStartResult=="Touchback"):
        print("Ball is placed at the 25 yard line")
        return(25)
    
    
    if(kickStartResult=="In Play"):
        print("Ball is being returned by ",returner["Full Name"].to_list()[0])
        meanReturn=(Return+Carry+Juke+Speed+Spin+Truck+Stiff)/7
        
        #print(meanReturn)
        
        returnYards=np.random.lognormal(meanReturn/85,14/meanReturn**(1/2))*5
        if(returnYards<=10):
            returnYards*=3
            if(returnYards<=1.5):
                returnYards*=2.5
        if(returnYards+starting<100):
            print("Return of ",returnYards," to the ",returnYards+starting," yard line")
        else:
            print("20...15...10...5...Touchdown!")
    #kickType=np.array(["Onside","Squib","SkyKick","Normal"])
    #KickStyle=np.array(["Left","Right","Short","Deep"])
        if(returnYards+starting<100):
            return(str(returnYards+starting))
        elif(turnover==1):
            returnStart=returnYards+starting
        #TO DO
        #get a list of defense players
        #pick one to pick up the fumble
        #simulate return
        #add a check for a fumble occuring to also make turnover set to true AS WELL AS SAFTEIES
        #return a negative value if the team lost possession
        return(returnYards+starting)
# in order of away,home,user is INT! 0 for sim,1 for away,2 for home
def StartGame(team1,team2,user):
    home=readTeam(team2)
    away=readTeam(team1)
    tendies=pd.read_csv("Tendincies.csv")

    if(user==0): #sim
        coin=CoinToss(away,home,0,team1,team2)
        #print("coin=",coin)
        check=Kickoff(coin,home,away,team2,team1,0,1,0,tendies)
    elif(user==1): #away
        coin=CoinToss(away,home,1,team1,team2)
        #print("coin= ",coin)
        check=Kickoff(coin,home,away,team2,team1,1,1,0,tendies)
    else: #home 
        coin=CoinToss(away,home,2,team1,team2)
        #print("coin=", coin)
        check=Kickoff(coin,home,away,team2,team1,2,1,0,tendies)
        
    print(check)

#StartGame("Broncos","Raiders",2 )




#def Run():

#def ShortPass():
  
#def MedPass():

#def LongPass():

#def Punt():

#def Fumble():

#def Interception():

#def FeildGoal()

#def Conversion():

#def Turnover():

def startDrive(offense,defense,sim,ball,starting,time,quater):
    down=1
    QB=getMaxPositionPlayer(offense,"QB",1)
    print(QB)
    WR=getMaxPositionPlayer(offense,"WR",6)

    # while(down<5):
    #     blah
startDrive(readTeam("Broncos"),readTeam("Raiders"),0,0,25,15,1)