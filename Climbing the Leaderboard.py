class Score_board:
    def climbingLeaderboard(self, scores, alice):
        self.boardScores = sorted(set(scores), reverse=True)
        alice_rank = list(map(self.rankBoard,alice))
        return alice_rank

    def rankBoard(self, current):
        score_bank = self.boardScores
        midIndex = len(score_bank)//2
        while midIndex > 0:
            if current in score_bank:
                return(self.boardScores.index(current)+1)
            elif current < score_bank[midIndex]:
                score_bank = score_bank[midIndex:]
                midIndex = len(score_bank)//2
            elif current > score_bank[midIndex]:
                score_bank = score_bank[:midIndex]
                midIndex = len(score_bank)//2
        else:
            boardIndex = self.boardScores.index(score_bank[0])
            if current in score_bank:
                return(self.boardScores.index(current)+1)
            elif current > score_bank[0] and boardIndex == 0:
                return(1)
            elif current < score_bank[0] and boardIndex == (len(self.boardScores)-1):
                return(boardIndex + 2)
            elif current > score_bank[0]:
                return(boardIndex)
            elif current < score_bank[0]:
                return(boardIndex + 2)

if __name__ == '__main__':
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    coord = Score_board()
    result = coord.climbingLeaderboard(scores, alice)
    print('\n'.join(map(str, result)))
    print('\n')
