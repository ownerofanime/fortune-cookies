import random

random_cookies = 'abcdefghijklmnop'
x = 1
while x > 0: 
    answer = int(input('please pick a fortune cookie that you would want to have 1/2/3: '))
    if answer == 1:
        new_cookies = random.choice(random_cookies).upper()
    elif answer == 2:
        new_cookies = random.choice(random_cookies).upper()
    elif answer == 3:
        new_cookies = random.choice(random_cookies).upper()

    fortune_cookies = {
    'A': "Your kindness will lead you to unexpected blessings.",
    'B': "Adventure is on the horizon—prepare to take a leap.",
    'C': "A small act of courage will spark great change.",
    'D': "The opportunity you've been waiting for is coming soon.",
    'E': "You will bring joy to someones life today.",
    'F': "Hard work will soon pay off in surprising ways.",
    'G': "Trust your instincts—they will lead you to success.",
    'H': "New friendships will enrich your journey.",
    'I': "A calm mind brings inner strength and clarity.",
    'J': "Something lost will soon return to you.",
    'K': "Your dreams are closer than they appear."
    }
    
    if new_cookies in fortune_cookies: 
        print(f'fortune: {fortune_cookies[new_cookies]}')
    else:
        print('error')
