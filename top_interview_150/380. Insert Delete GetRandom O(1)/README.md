Problem:
Create an object htat fulfills the requirements

Thought:
I was very confused by the original ask of the question as I thoguht that randomizedSet meant to generate a random set and perform operations.

    I had to look at example solutions to see what the ask really was about and then realized that its simply asking me to create a empty set that can be tested.

Sol1:
Opted to use a brute force method but pretty sure it won't meet the O(1) runtime requirement.

Sol2:
Realized what you can do is switch the deleted val with the last item and simply do a flip on the hash map as well. Perfect solution
