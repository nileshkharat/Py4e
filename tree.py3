"""
Christmas Tree
Chirag is a pure Desi boy. And his one and only dream is to meet Santa Claus. He decided to decorate a Christmas tree for Santa on coming Christmas. Chirag made an interesting Christmas tree that grows day by day.

The Christmas tree is comprised of the following Parts:

Stand 
Each Part is further comprised of Branches. 
Branches are comprised of Leaves.
How the tree appears as a function of days should be understood. Basis that print the tree as it appears on the given day. Below are the rules that govern how the tree appears on a given day. Write a program to generate such a Christmas tree whose input is number of days.

Rules:

If tree is one day old you cannot grow. Print a message “You cannot generate christmas tree” 
Tree will die after 20 days; it should give a message “Tree is no more” 
Tree will have one part less than the number of days. E.g. On 2nd day tree will have 1 part and one stand., On 3rd day tree will have 2 parts and one stand On 4th day tree will have 3 parts and one stand and so on. 
Top-most part will be the widest and bottom-most part will be the narrowest. 
Difference in number of branches between top-most and second from top will be 2 
Difference in number of branches between second from top and bottom-most part will be 1.
Input Format:

First line of input contains number of days denoted by N

Output Format:

Print Christmas Tree for given N

OR

Print “You cannot generate christmas tree” if N <= 1

OR

Print “Tree is no more” if N > 20

Constraints:

0<= N <=20
"""
l = 0
space = 0
N = int(input())

def christmas_tree(a, N):
    global space
    for row in range(a, N + 1):
        # Blank Space
        for sp in range(1, N + space - row + 1):
            print(" ", end='')
        # Star Printing
        for Stars in range(1, 2 * row):
            print("*", end='')
        print()
    space += 1

if (N <= 1):
    print("You cannot generate Christmas tree")
elif (N > 20):
    print("The Tree is no More")
else:
    # First One pyramid
    christmas_tree(1, N + 1)
    # Others pyramid (Branches)
    for i in range(2, N ):
        christmas_tree(2, N - l)
        l += 1

    # Stand of the Tree
    print(' ' * N + '*')
    print(' ' * N + '*')