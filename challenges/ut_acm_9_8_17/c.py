start = len('I went to ')
end = len('and all I got was this shirt.')

for _ in range(int(input())):
    print(input()[start:-end])
