# Please note that this is just a temporary, proof of concept, script

numbers     = open("fonts/numbers", "r")
alphabet    = open("fonts/alphabet", "r")

for i in alphabet:
    print(i, end = '')
    c = i[4:11]
    if c[0] == '1':
        print(" #### ")
    else:
        print(" .... ")
    for x in range(3):
        if c[5] == '1':
            print("#    ", end = '')
        else:
            print(".    ", end = '')
        if c[1] == '1':
            print("#")
        else:
            print(".")
    if c[6] == '1':
        print(" #### ")
    else:
        print(" .... ")
    for x in range(3):
        if c[4] == '1':
            print("#    ", end = '')
        else:
            print(".    ", end = '')
        if c[2] == '1':
            print("#")
        else:
            print(".")
    if c[3] == '1':
        print(" #### ")
    else:
        print(" .... ")
