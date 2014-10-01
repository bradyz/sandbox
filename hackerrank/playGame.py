# HACKERRANK PLAY GAME DYNAMIC PROGRAMMING

def best_score(brickList, isTurn, score):
    if len(brickList) <= 3:
        if isTurn:
            if len(brickList) == 0:
                return score
            elif len(brickList) == 1:
                return brickList[0] + score
            elif len(brickList) == 2:
                oneScore = best_score(brickList[1:], not isTurn, score + brickList[0])
                twoScore = best_score(brickList[2:], not isTurn, score + brickList[0] + brickList[1]) 
                return max(oneScore, twoScore)
            else:
                oneScore = best_score(brickList[1:], not isTurn, score + brickList[0])
                twoScore = best_score(brickList[2:], not isTurn, score + brickList[0] + brickList[1]) 
                threeScore = best_score(brickList[2:], not isTurn, score + brickList[0] + brickList[1] + brickList[2]) 
                return max(oneScore, twoScore, threeScore)
        else:
            if len(brickList) == 0:
                return score
            elif len(brickList) == 1:
                return score
            elif len(brickList) == 2:
                oneScore = best_score(brickList[1:], not isTurn, score)
                twoScore = best_score(brickList[2:], not isTurn, score) 
                return min(oneScore, twoScore)
            else:
                oneScore = best_score(brickList[1:], not isTurn, score)
                twoScore = best_score(brickList[2:], not isTurn, score) 
                threeScore = best_score(brickList[3:], not isTurn, score)
                return min(oneScore, twoScore, threeScore)
    else:
        if isTurn:
            oneScore = best_score(brickList[1:], not isTurn, score + brickList[0])
            twoScore = best_score(brickList[2:], not isTurn, score + brickList[0] + brickList[1]) 
            threeScore = best_score(brickList[3:], not isTurn, score + brickList[0] + brickList[1] + brickList[3])
            return max(threeScore, oneScore, twoScore)
        else:
            oneScore = best_score(brickList[1:], not isTurn, score)
            twoScore = best_score(brickList[2:], not isTurn, score)
            threeScore = best_score(brickList[3:], not isTurn, score)
            return min(threeScore, oneScore, twoScore)

asdf = [999, 1, 1 ,1, 0]
print asdf
print best_score(asdf, True, 0)
asdf = [0, 1, 1, 1, 999]
print asdf
print best_score(asdf, True, 0)

