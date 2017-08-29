import pygame
from allclasses import Card
from func import fight, cdestr, chkdead, chkwin


def game_loop():
    # Card(name, mana, hp, atk)
    card1 = Card("card1", "2", "5" , "2")  
    card2 = Card("card2", "6", "10", "2")
    card3 = Card("card3", "2", "6" , "1")  
    card4 = Card("card4", "1", "2", "3")
    a=0
    q=0
    c=0
    n=0
    pcard = []
    ccard = []
    cardlist = [card1, card2, card3, card4]
    l = len(cardlist)


    for n in range(0,2):
        try:
            a = input('\t\tВыбери 1 карту из 4\n\n')
            a = int(a)
        except:
            print('Ошибка. Выбери 1 карту из 4')
            game_loop()
        pcard.append(cardlist[a-1])
    #    print ('всего карт', len(cardlist))
    #    print ('у меня карт', len(pcard))
    cardlist = list(set(cardlist).difference(pcard))
    ccard += cardlist
    cardlist += pcard
#    print ('у компа карт',len(ccard))
#    print ('не выбранных карт осталось', len(cardlist))
        
    print ("Ваши карты: ",'\n', pcard[0],'\n', pcard[1])
    print ("My turn, and my card is: ",'\n', ccard[0],'\n', ccard[1])
    print ("Now is your turn! Fight with m e bastard!")
    t=0
    while not q:
        t+=1
        if t%2 != 0:
            offh = ccard
            defh = pcard
        else:
            offh = pcard
            defh = ccard
        input('Для продолжения нажмите любую клавишу')
        print ('\n---------------------------------FIGHT TURN',t,'----------------------------------')
        for h in range(0,min(len(offh),len(defh))):
            fight(offh[h-2+len(offh)], defh[h-2+len(defh)])
            q = chkwin(pcard,ccard,h) # удалить h, когда вынесем комменатрии о смерти карты в отдельну функцию
    input ('\n\nНажмите любую клавишу, чтобы выйти')
game_loop()
quit()
