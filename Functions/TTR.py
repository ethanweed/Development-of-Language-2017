#TTR

# Takes all text files in a folder, calculates type-to-token ratio, and plots a bar plot
# Usage: TTR(pathin)
# example:
# 	pathin = 'users/ethan/Desktop/data'
#	TTR(pathin)

def TTRplot (pathin):
    import os
    import glob
    import string
    import numpy as np
    import matplotlib.pyplot as plt
    
    os.chdir(pathin)

    punct = set(string.punctuation)

    titles = []
    ttratio = []

    for file in glob.glob('*.txt'):
        with open(file,'r') as f:

            text = f.read()
            text = text.lower()
            text = ''.join(x for x in text if x not in punct)
            text = text.split(' ')


            t = file[:-4]
            titles.append(t)

            ttr = (len(set(text))/len(text))
            ttratio.append(ttr)
    xpos = range(len(titles))
    plt.bar(xpos, ttratio, align = 'center')
    plt.xticks(xpos, titles, rotation = 80)
    plt.title('Type to token ratio')
    plt.show
    return(ttratio)
