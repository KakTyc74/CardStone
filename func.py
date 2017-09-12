def cdestr(card):
    cardhp = card.hp
    if cardhp <= 0:
        #del card
        print ('\n\nКарта', card.name, 'уничтожена')

def fight(ccard, pcard):
    ccard.attack(pcard)
    print ('\nКарта компьютера',ccard.name,', наносит урон',ccard.atk,'твоей карте', pcard.name)
    print ('Карта', pcard.name,'отвечает', ccard.name,'и наносит урон ',pcard.atk,'\n')
    print ("Твоя карта: ", pcard)
    print ("Моя карта: ", ccard,'\n')
    #    cdestr(card)

def chkdead(hand):
  #  while not d <= len(hand):
    for card in hand:
        if card.dead():
            hand.remove(card)
    return len(hand) == 0

def chkwin(pcard,ccard,h):
    if chkdead(pcard) and chkdead(ccard):
        print ('\nВсе карты на столе погибли. Ничья')
        q = 1
    elif chkdead(pcard) and not chkdead(ccard):
        print ('\nА карта',ccard[h].name,'жива. Я выиграл')
        q = 1
    elif not chkdead(pcard) and chkdead(ccard):
        print ('\nА карта',pcard[h].name,'жива. Ты выиграл')
        q = 1
    else:
        q = 0
    return q

    
