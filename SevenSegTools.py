# Please note that this is just a temporary, proof of concept, script

numbers  = open("fonts/numbers", "r")
alphabet = open("fonts/alphabet", "r")

fonts = [numbers, alphabet]
chars = {}

for f in fonts:
    for l in f:
        c = 0
        done  = False
        first = True
        label = None
        while not done:
            value = None
            if c > len(l):
                done = True
            else:
                if l[c] is not '\n' and l[c] is not '/':
                    if l[c] is not ' ':
                        if first:
                            label = l[c]
                            chars[label] = []
                            print('label = ' + label)
                            first = False
                            c += 1
                        else:
                            value = int(l[c:c + 7], 2)
                            chars[label].append(value)
                            print('value = {0:07b}'.format(value))
                            c += 7
                    else:
                        c += 1
                else:
                    done = True

print(chars)

for c in chars:
    for v in range(len(chars[c])):
        r = chars[c][v]
        d = [False] * 7
        print(r)
        for s in range(len(d)):
            if ((r >> s) & 1):
                d[s] = True
        if d[6]: print(" #### ")
        else: print(" .... ")
        for x in range(3):
            if d[1]: print("#    ", end = '')
            else: print(".    ", end = '')
            if d[5]: print("#")
            else: print(".")
        if d[0]: print(" #### ")
        else: print(" .... ")
        for x in range(3):
            if d[2]: print("#    ", end = '')
            else: print(".    ", end = '')
            if d[4]: print("#")
            else: print(".")
        if d[3]: print(" #### ")
        else: print(" .... ")
