file = open("/private/var/log/wifi.log")
phrase = input("Enter a Search phrase:")

for line in file:
    if phrase in line:
        print(line)
    else:
        continue