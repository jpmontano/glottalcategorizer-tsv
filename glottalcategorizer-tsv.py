#!/usr/bin/python3.4 -tt

# Disregarding carons (ǧ, ȟ and ǩ), these are all of the Nishnaabe
# graphemes in sorted order:
# - ' a aa b ch d e g h i ii j k
# m mb n nd ng nh nj ns ny nz nzh
# o oo p s sh shk sk t w y z zh
#
#
# Including carons (ǧ, ȟ and ǩ), these are all of the Nishnaabe
# graphemes in sorted order:
# - ' a aa b ch cȟ d e g ǧ h ȟ i ii j k ǩ
# m mb n nd ng nǧ nh nȟ nj ns ny nz nzh nzȟ
# o oo p s sh sȟ shk shǩ sk sǩ t w y z zh zȟ


import csv
import re


#
GLOTTALFILENAME = "glottals.tsv"

# Read the .tsv file into a list of lists (i.e., a 2d list)
with open(GLOTTALFILENAME, newline='') as fin:
    lines = list(csv.reader(fin, delimiter='\t'))


# 
lhs = [ "'", "([^a]|^)a", "aa", "([^m]|^)b", "ch", "cȟ", "([^n]|^)d", "e",
    "([^n]|^)g", "([^n]|^)ǧ", "[^c|n|s|z]h", "[^c|n|s|z]ȟ", "([^i]|^)i",
    "ii", "([^n]|^)j", "([^s|sh]|^)k", "([^s|sh]|^)ǩ", "m", "mb", "nd",
    "ng", "nǧ", "nh", "nȟ", "nj", "ns", "ny", "nzh", "nzȟ", "([^o]|^)o",
    "oo", "p", "sh", "sȟ", "shk", "shǩ", "sk", "sǩ", "t", "w", "([^n]|^)y",
    "([^n]|^)zh", "([^n]|^)zȟ" ]

rhs = [ "-", "'", "a([^a]|$)", "aa", "b", "ch", "cȟ", "d", "e", "g",
    "ǧ", "h", "ȟ", "i([^i]|$)", "ii", "j", "k", "ǩ", "m([^b]|$)", "mb",
    "n([^d|g|ǧ|h|ȟ|j|s|y|z|zh|zȟ]|$)", "nd", "ng", "nǧ", "nh", "nȟ",
    "nj", "ns", "ny", "nz([^h|ȟ]|$)", "nzh", "nzȟ", "o([^o]|$)", "oo",
    "p", "s([^h|ȟ|k|ǩ]|$)", "sh([^k|ǩ]|$)", "sȟ", "shk", "shǩ", "sk",
    "sǩ", "t", "w", "y", "z([^h|ȟ]|$)", "zh", "zȟ" ]

glottals = [ "h", "ȟ" ]


# Initialize.
numofcats = 0
obscats = []

#
for i in range( len(lhs) ):

    #
    for j in range( len(rhs) ):

        #
        for glottal in glottals:

            #
            glotpatcat = lhs[i] + glottal + rhs[j]
            alreadyprintedheading = "False"

            #
            for line in lines:
                currentobs = re.search(glotpatcat, line[0])
                if (currentobs):
                    if (alreadyprintedheading == "False"):
                        print("\n------" + glotpatcat + "------")
                        alreadyprintedheading = "True"
                        numofcats += 1
                        obscats.append(glotpatcat) 

                    # Element 0 is the current Nishnaabe term
                    # Element 1 is the current Nishnaabe part of speech
                    # Element 2 is the current English gloss
                    print(line[0] + "\t" + line[1] + "\t" + line[2])


# Display for the user a final summary of the computed results.
print("\nThe number of hypothetically possible glottal pattern " +
    "categories is: " + str( len(lhs) * len(rhs) * len(glottals) ) )
print("\nThe number of observed glottal pattern " +
    "categories is: " + str( numofcats ) )
print("\nThe observed glottal pattern categories are, as regexen, ")
print(obscats)
