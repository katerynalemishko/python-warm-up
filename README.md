Here I present my solutions on collection of Python excersizes that I found the most fun and interesting to work on.

Let me explain how the code from each particular excersize works.


SPIRAL MATRIX

In the 'spiral-matrix' excercise I wrote a code that  takes as an input a number, n,  and builds a matrix of a size of nxn, filled with numbers from 1 to n^2 in a spiral-like manner, i.e., the spiral starts at the top left corner of the matrix and then turns clockwise every time it reaches a new corner.

Here is an example of how this code works:

Sample Input:
5
Sample Output:
1  2  3  4  5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

For more examples, check the Jupyter notebook file in the 'spiral-matrix' folder.


DICE ROLLING

In the dice-rolling exercise I simulate a game that involves throwing dice. 
A player starts the game at the bottom the stairs and moves up or down the stairs according to the roll of a single die:

-if the die roll is 3,4 or 5, the player makes one step up the stairs;
-if the die roll is 1 or 2, the player needs to make one step down (if he is currently at the step 0, he does not make any move);
-if the die roll is 6, the player needs to roll the die again and make as many steps forward as the new roll of the die shows.

In the code I wrote I simulate this game to answers the question about the most probable outcome of the game after making a certain number of steps.
The results provided by the code can be used to increase the probability of one’s success in betting. 

Check the Jupiter notebook file containing the explanatory notes, the code and all the visualizations.






