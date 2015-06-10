# Three of a crime - python program
# We will take input from users to enter number of players and display the same
import random
#num_players = raw_input("Enter number of players:")
num_players = input("Enter number of players:")
num_players=int(num_players)
print "Players are :" , num_players



#perform a check for num of players to be either 2 or 3
while(num_players<2 or num_players>3):
    num_players = input("Please enter either 2 or 3 number of players:")
    num_players=int(num_players)
    print "Players are :" , num_players

if num_players==2:
    players=['P1','P2']
else:
    players=['P1','P2','P3']

count =0
criminals =['A','B','C','D','E','F','G']
preparators = random.sample(criminals,3)
#print "preparators are:"
for p in preparators : print (p)
def criminals_match() :
    global count
    global match
    global m_index
    match=list()
    count=0
    m_index=0
    while count==0 or count>=3:
        criminals_players =random.sample(criminals,3)
        #print "Criminals shown to players"
        #for c in criminals_players :
        #    print c
        for i in range(0,len(preparators)):
      
            	
            for j in range(0,len(criminals_players)):
                
                
                if preparators[i]==criminals_players[j]:
                    count=count+1
                    match.insert(m_index,preparators[i])
                    m_index=m_index+1
                    #print "Value is:" ,preparators[i]
    #print "No. of preparators in the criminals displayed :" ,count    
    return criminals_players;

print "Welcome to Three of a crime"
global count_no
count_no=0
num_player = num_players
def playthegame():
    global count_no
    global num_player
    global guess_list
    guess_list=list()
    count1=0
    #flag_while=flag_break=flag_for=0
    count_match=0
    criminals_players =criminals_match();
    print "Criminals on card are:"
    for p in criminals_players:print p
    print "No. of preparators in the criminals displayed :" ,count 
    
   
    
    
    for m in range(0,num_player):
        player = players[num_player-1]
        #print player
        #print "Num player value:" , num_player
        
        
        
        while num_player>0:
        #or num_player<num_players:
            player = players[num_player-1]
            print player , "is playing"
            guess=raw_input("Do you want to guess ? yes or no:")
            
            if guess.upper()=="NO":
                count_no=count_no+1
                if count_no==4:
                    print "Sorry!! your chances to guess are finished"
                    #print "Next player - num player value",num_player
                    num_player=num_player-1
                    count_no=0
                    break;
                print "You have another chance to play"
                playthegame()
                
                
            else :
                print "Please enter your criminals"
                #guess_criminal=raw_input("Please enter your options")
                for m in range(0,3):
                    guess_criminal = raw_input()
                    guess_list.insert(m,guess_criminal)
                    
                            
                for n in range(0,3)  :
                    
                    #print "n value:" , n
                    for q in range(0,len(preparators)):
                        #print "q value:",q
                        if guess_list[n].upper()==preparators[q]:
                            count_match=count_match+1
                if count_match==3:
                    print "Wow!! You won the game"
                    num_player=0
                    count_no=0
                    break;
                else:
                    print "Sorry !! You are out of game"
                    num_player=num_player-1
                    count_no=0
                    break;
                         
    return ;

playthegame();


