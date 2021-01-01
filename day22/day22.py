from collections import deque
import copy

def main():
    decks = open("input22.txt", "r").read().strip().split('\n\n')
    player1 = deque([int(card) for card in decks[0].split('\n')[1:]])
    player2 = deque([int(card) for card in decks[1].split('\n')[1:]])
    memo = {} #Deck -> Result           Used for memoization

    winnerCombat, winningDeck = playCombat(copy.copy(player1),copy.copy(player2))
    ans1 = countScore(winningDeck)

    winnerRecursiveCombat, winningDeck = playRecursiveCombat(player1, player2, memo)
    ans2 = countScore(winningDeck)

    print('Answer Part1:', ans1)
    print('Answer Part2:', ans2)

def playCombat(player1, player2):            #Takes two decks and return (numberOfWinningPlayers, deck)
    while player1 and player2:
        card1 = player1.popleft()
        card2 = player2.popleft()
        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)
    if player1:         #If player1 has cards left -> player one is the winner
        return (1, player1)
    else: 
        return (2, player2)

def playRecursiveCombat(player1, player2, memo):            
    previousDecks = set()
    while player1 and player2:   
        thisDeck = (tuple(player1), tuple(player2))        
        if thisDeck in previousDecks:               #Check if exactly the same decks have been played before in this game. If so player one wins. 
            memo[thisDeck] = (1, player1)
            return (1, player1)
        
        if thisDeck in memo.keys():                 #If the exact decks have been played before return result. 
            return memo[thisDeck]
        
        previousDecks.add(thisDeck)
        card1 = player1.popleft()
        card2 = player2.popleft()
       
        if card1 <= len(player1) and card2 <= len(player2):     #If True play sub-game!
            p1 = list(player1)
            p2 = list(player2)
            result = playRecursiveCombat(deque(p1[:card1]), deque(p2[:card2]), memo)  #Play sub-game
            if result[0] == 1:      #If player1 wins sub-game:
                player1.append(card1)
                player1.append(card2)
            else:                   #If player2 wins sub-game:
                player2.append(card2)
                player2.append(card1)
        else:                               #Else highest card wins
            if card1 > card2:
                player1.append(card1)
                player1.append(card2)
            else: 
                player2.append(card2)
                player2.append(card1)
    if player1:
        memo[thisDeck] = (1, player1)       #Save result to memo and return it
        return (1, player1)
    else:
        memo[thisDeck] = (2, player2)       #Save result to memo and return it
        return (2, player2)

def countScore(deck):
    score = 0
    i = 1
    while deck:
        score += deck.pop() * i
        i += 1
    return score

main()