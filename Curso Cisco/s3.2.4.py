x = 777
y=1

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
while y!=x:
    y = int(input())
    print("Ha ha! You're stuck in my loop!")
print("Well done, muggle! You are free now.")