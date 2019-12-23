# Please note that this is just a temporary, proof of concept, script

numbers  = open("fonts/numbers", "r")
alphabet = open("fonts/alphabet", "r")

fonts = [numbers, alphabet]

id = 0
for f in fonts:
    for l in f:
        c = 0
        done  = False
        first = True
        while not done:
            if c > len(l):
                done = True
            else:
                if l[c] is not '\n' and l[c] is not '/':
                    if l[c] is not ' ':
                        if first:
                            # TODO Set label
                            # label = l[c]
                            print('label = ' + l[c])
                            first = False
                            c += 1
                        else:
                            # TODO Set value
                            # value = l[c:c + 7]
                            print('value = ' + l[c:c + 7])
                            c += 7
                    else:
                        c += 1
                else:
                    done = True

#for i in alphabet:
#    print(i, end = '')
#    c = i[4:11]
#    if c[0] == '1':
#        print(" #### ")
#    else:
#        print(" .... ")
#    for x in range(3):
#        if c[5] == '1':
#            print("#    ", end = '')
#        else:
#            print(".    ", end = '')
#        if c[1] == '1':
#            print("#")
#        else:
#            print(".")
#    if c[6] == '1':
#        print(" #### ")
#    else:
#        print(" .... ")
#    for x in range(3):
#        if c[4] == '1':
#            print("#    ", end = '')
#        else:
#            print(".    ", end = '')
#        if c[2] == '1':
#            print("#")
#        else:
#            print(".")
#    if c[3] == '1':
#        print(" #### ")
#    else:
#        print(" .... ")
