#%%
 
import random
def choose():
    words=['rainbow','computer','science','programming','mathematics','player','condition','reverse','water','board','geeks']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thanks(p1n,p2n,p1,p2):
    print(p1n,'your score is :',p1)
    print(p2n,'your score is :',p2)
    print('thanks for playing')
    print('have a nice day')

def play():
    p1name=input('player 1 ,please enter your name')
    p2name=input ('player 2,please enter your name')
    pp1=0
    pp2=0
    turn =0
    while(1):
        #computer task
        picked_word=choose()
        #create question 
        qn=jumble(picked_word)
        print (qn)

        #player1
        if turn %2==0:
            print(p1name,'your turn ')
            ans=input ('what is on my mind ')
            if ans==picked_word:
                pp1=pp1+1
                print('your score is :',pp1)
            else:
                print ('better luck nest time .i thought :',picked_word)
            c=input('press 1 to continue and 0 to quit')
            if c==0:
                print('thanks ',p1name,p2name,pp1,pp2)
                break

        #player2
        else:
            print(p2name, 'your turn ')
            ans=input ('what is on my mind ')
            if ans==picked_word:
                pp2=pp2+1
                print('your score is :',pp2)
            else:
                print ('better luck nest time .i thought :',picked_word)
            c=input('press 1 to continue and 0 to quit')
            if c==0:
                thanks(p1name,p2name,pp1,pp2)
                break
        turn=turn+1
play()