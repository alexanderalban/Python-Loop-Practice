# Loooooops

# For loops have a specific length
# Using range() returns an iterator.
# It helps to think of the variables we're using as having the word "every" in front of them

for x in range(0, 5):
    print("hello")

print(list(range(10, 20)))

for x in range(0, 5):
    print('hello %s' % x)

wizard_list = ['spider legs', 'toe of frog',
               'snail tongue', 'bat wing', 'slug butter', 'bear burp']
for i in wizard_list:
    print(i)

# Loops in the same block
hugehairypants = ["huge", "hairy", "pants"]
for i in hugehairypants:
    print(i)
    print(i)

# Loops in different blocks
ironmanmoney = ["iron", "man", "money"]
for i in ironmanmoney:
    print(i)
    for j in ironmanmoney:
        print(j)

# Let's get more practical. The duplicating coins trick from before: 20 found coins plus 10 magic coins multiplied by 365 days
# in the year, minus the 3 coins a week stolen by the raven

total = 20 + 10 * 365 - 3 * 52
print(total)

# How will our pile of gold increase each week?

found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = found_coins

for week in range(1, 53):
    coins = coins + magic_coins - stolen_coins
    print('Week %s = %s' % (week, coins))


# While Loops
# While loops is used when you don't know ahead of time when it needs to stop looping

# imagine a staircase with 20 steps
for step in range(0, 20):
    print(step)

x = 45
y = 80
while x < 50 and y < 100:
    x = x + 1
    y = y + 1
    print(x, y)

# More Practice!

# Break the loop
for x in range(0, 20):
    print('hello %s' % x)
    if x < 9:
        break

# Check for even numbers
for even in range(0, 33):
    if (even % 2) == 0:
        print("%s is even" % even)

# Make a loop that prints out the ingredient of a nice sandwich

ingredients = ["bread", "ham", "cheddar", "mayo",
               "mustard", "lettuce", "banana peppers"]

for i in ingredients:
    print(i)

# If you were standing on the moon, your weight would be 16.5 percent of what it is on Earth. You can calculate that by
# multiplying your Earth weight by 0.165. If you gained a kilo in weight every year for the next 15 years, what would your
# weight be when you visited the moon each year and at the end of the 15 years?

weight = 91

for i in range(0, 15):
    weight = weight + 1
    moon_weight = weight * 0.165
    print(moon_weight)
