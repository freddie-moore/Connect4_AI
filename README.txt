THE GAME:

Connect 4 is a classic game where two players take turns dropping colored discs into a vertical grid. The objective is to connect four of one's own discs of the same color next to each other vertically, horizontally, or diagonally. In this program, you can play against a computer controlled AI that uses the minimax algorithm to make its moves.

MINIMAX:

The hardest part of implementing the minimax algorithm was deciding on an effective, yet computationally efficient way to evaluate the state of the board. In the end I decided the best way to do this was by counting every row of pieces, that had the possibility (i.e. within bounds) to be developed into a row of 4. I then raised this count to the power of 10 and added it to a total. Raising to such a high power ensures that the AI will favour moves that build 3 or 4 pieces in a line, as opposed to lots of lines of 2 pieces. Overall, the AI works very well with this current evaluation function.

ALPHA BETA PRUNING:

The algorithm is currently set to a depth of 5, I found this to be the limit at which the game becomes unenjoyable due to the AI taking too long to respond with a move. With a tree depth of 5 and a branching depth of 5, at each call of the minimax algorithm the programme considers 3125 different possible game states (5^5). This would take too long to compute. By utilizing alpha beta pruning we are able to make our programme run 2.913x quicker.

I also ran tests for other depth factors, both with and without alpha beta pruning, to see the effect. I simulated the same move in each test-case, I simulated each test case 100 times and took the quickest result from each. As evidenced by the table below, the algorithm becomes dramatically more efficient at higher depths; as expected.

Depth  |   With Alpha Beta Pruning   |  Without Alpha Beta Pruning
-------|-----------------------------|-----------------------------
1      | 0.0006853000                | 0.0006918000
2      | 0.0048283000                | 0.0053734000
3      | 0.0304384000                | 0.0391731000
4      | 0.1454915000                | 0.2858988000
5      | 0.7056615000                | 2.0556612000
6      | 3.0236077000                | 14.6718049000


CREDITS:
More information on the minimax algorithm and alpha-beta pruning can be found here : https://www.youtube.com/watch?v=l-hh51ncgDI&t=545s