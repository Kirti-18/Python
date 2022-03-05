"""
1.You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
Input Format

The first line contains the integer, .
The next  lines each contain a word.

Output Format

Output  lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1

"""

from collections import OrderedDict

total_words = int(input())

words_dict = OrderedDict()
for i in range(total_words):
    word = input()
    if word in words_dict:
        words_dict[word] = words_dict[word] + 1
    else:
        words_dict[word] = 1
 
print(len(words_dict))        
print(*words_dict.values())

"""
2. A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

GOOGLE would have it's logo with the letters G,O,E.

Input Format

A single line of input containing the string .

Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0

aabbbccde
Sample Output 0

b 3
a 2
c 2
"""

from collections import Counter
from operator import itemgetter


if __name__ == '__main__':
    s = input()
    counter = Counter(s)
    letter_list = []
    for key,value in counter.items():
        letter_list.append((key,-value))
  
    # -ve values help in sorting with 2 values
    letter_list_sorted = sorted(letter_list, key=itemgetter(1,0))
    for i in letter_list_sorted[0:3]:
        print(f"{i[0]} {-i[1]}")
    
    # OR sol2: sort the vlaues before applying Counter
    #[print(*c) for c in Counter(sorted(input())).most_common(3)]
    

"""
3.There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if
cube[i] is on top of cube[j] then sideLength[j]>=sideLength[i].

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

Example
blocks=[1,2,3,8,7]
Result: No

After choosing the rightmost element,7 , choose the leftmost element,1 . After than, the choices are 2 and 8. These are both larger than the top block of size 1.

blocks=[1,2,3,7,8]
Result: Yes

Choose blocks from right to left in order to successfully stack the blocks.

Input Format

The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains n, the number of cubes.
The second line contains n space separated integers, denoting the sideLengths of each cube in that order.

Output Format

For each test case, output a single line containing either Yes or No.

Sample Input

STDIN        Function
-----        --------
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]
Sample Output

Yes
No
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

test_cases = int(input())

for _ in range(test_cases):
    size = int(input())
    d = deque()
    d.extend(list(map(int,(input().split()))))
    temp = d.copy()
    stack = []
    while(len(temp) != 0):        
        right = temp.pop()
        if len(temp) >= 1:
            left = temp.popleft()
        else:
            left = 0
        # first 2 elements insertion in stack 
        if len(stack) == 0:
            if right == left:
                stack.extend([left,right])
            elif right < left:
                stack.extend([left,right])
            elif left < right:
                stack.extend([right,left])
        else:
            # when both left and right are equal
            if left == right:
                if stack[-1] >= left:
                    stack.extend([left,right])
            # when left < right, compare with last stack element
            elif left < right:
                    if stack[-1] > right:
                        stack.extend([right,left])
                    else:
                        print("No")
                        break
            # when right < left, compare with last element
            elif right < left:
                    if stack[-1] > left:
                        stack.extend([left, right])
                    else:
                        print("No")
                        break

            if len(stack) == len(d):
                print("Yes")
                break
            
            
            
    
