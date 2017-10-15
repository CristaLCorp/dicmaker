#!/usr/bin/env python

import itertools
import sys
import getopt

wordlist = ""
write_file = "none"

def usage():
    print("")
    print("DicMaker : ")
    print("\" It Just Makes Dics ! \"")
    print("")
    print("Usage : dicmaker.py -l coma,separated,words/digits -w path/to/write/file.txt")
    print("")
    print("-l --list        - list of words/digits to use (coma separated values)")
    print("-w --write       - output file name (i.e. wordlist.txt). Default stdout")
    print("-h --help        - display this message")
    print("")
    print("examples :")
    print(" ./dicmaker.py -l hmmmm,le,caca,c,est,delicieux -w /home/datguy/stupidlist.txt")
    print("")
    sys.exit(0)


def generetaliste(list, operator, write_file, ow):

    file_to_write = open(write_file, "a")
    compteur = 0

    for x in range(1, len(list) + 1):
        for i in itertools.permutations(list, x):
            compteur +=1
            if write_file != "none":
                file_to_write.write(operator.join(i)+"\n")
            else:
                print(operator.join(i))

    file_to_write.close()
    return compteur


def main():

    global write_file
    global wordlist

    if not len(sys.argv[1:]):
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:l:w:", ['help', 'list', 'write'])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o,a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--list"):
            wordlist = a
        elif o in ("-w", "--write"):
            f = open(a, "w")
            f.write("")
            f.close()
            write_file = a
        else:
            assert False, "Unhandled Option"



    transformations = 0

    wordlist = wordlist.split(",")

    listcap = []
    for x in wordlist:
        if x.isalpha :
            listcap.append(str.capitalize(x))

    operators = ['-', ' ', '.', ' ', '']

    for op in operators:
        transformations += generetaliste(wordlist, op, write_file, ow=True)
    for op in operators:
        transformations += generetaliste(listcap, op, write_file, ow=False)

    print("\n" + str(transformations) + " transformations")


main()


# regex inutile mais c t long a trouver du coup...
#p = re.compile('^([a-z]|[0-9])(([a-z]|[0-9])+.?)+([a-z]|[0-9])$')
