import math
from collections import Counter
import numpy as np
"""
judge A says N: P(A, N) = 0.9
judge A says R: P(A, R) = 0.1
judge B says N: P(B, N) = 0.8
judge B says R: P(B, R) = 0.2
both judges say N: P(A, N) × P(B, N) = 0.72
both judges say R: P(A, R) × P(B, R) = 0.02
judges agree: 0.74

Calculation Example
Most statistical software has the ability to calculate k. For simple data sets (i.e. two raters, two items) calculating k by hand is fairly straightforward. For larger data sets, you’ll probably want to use software like SPSS.

The following formula is used for agreement between two raters. If you have more than two raters, you’ll need to use a formula variation. For example, in SAS the procedure for Kappa is PROC FREQ, while you’ll need to use the SAS macro MAGREE for multiple raters.

The formula to calculate Cohen’s kappa for two raters is:
cohen's kappa statistic


where:
Po = the relative observed agreement among raters.
Pe = the hypothetical probability of chance agreement

Example Question: The following hypothetical data comes from a medical test where two radiographers rated 50 images for needing further study. The researchers (A and B) either said Yes (for further study) or No (No further study needed).

20 images were rated Yes by both.
15 images were rated No by both.
Overall, rater A said Yes to 25 images and No to 25.
Overall, Rater B said Yes to 30 images and No to 20.
Calculate Cohen’s kappa for this data set.

Step 1: Calculate po (the observed proportional agreement):
20 images were rated Yes by both.
15 images were rated No by both.
So,
Po = number in agreement / total = (20 + 15) / 50 = 0.70.

Step 2: Find the probability that the raters would randomly both say Yes.
Rater A said Yes to 25/50 images, or 50%(0.5).
Rater B said Yes to 30/50 images, or 60%(0.6).
The total probability of the raters both saying Yes randomly is:
0.5 * 0.6 = 0.30.

Step 3: Calculate the probability that the raters would randomly both say No.
Rater A said No to 25/50 images, or 50%(0.5).
Rater B said No to 20/50 images, or 40%(0.6).
The total probability of the raters both saying No randomly is:
0.5 * 0.4 = 0.20.

Step 4: Calculate Pe. Add your answers from Step 2 and 3 to get the overall probability that the raters would randomly agree.
Pe = 0.30 + 0.20 = 0.50.

Step 5: Insert your calculations into the formula and solve:

k = (Po – pe) / (1 – pe = (0.70 – 0.50) / (1 – 0.50) = 0.40.

k = 0.40, which indicates fair agreement.

"""


def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


def input_list():
    jo = []
    a_list = []
    b_list = []
    r = []
    l = []
    same = []
    ones = []
    twos = []
    with open('w.txt') as f:
        for line in f:
            line = line.rstrip()
            line = line.split()
            for item in line:
                r.append(item)
            one = line[0]
            two = line[1]
            l.append((one, two))
            ones.append(one)
            twos.append(two)

        ones = Counter(ones)
        twos = Counter(twos)

        unique = set(r)
        lc = Counter(l)
        for k, v in lc.items():
            if k[0] == k[1]:
                same.append(v)

        all_same = sum(same)
        len_l = len(l)

        # (80, 26) ones

        po =  all_same / len_l


        for v1, v2 in zip(ones.values(), twos.values()):
            vv = v1 / len_l
            vv2 = v2 / len_l
            a_list.append(vv)
            b_list.append(vv2)
        # (0.7777777777777778, 0.6507936507936508, 0.2222222222222222, 0.3492063492063492) 0.07760141093474426, 0.5061728395061729]

        for i, j in zip(a_list, b_list):
            c = i * j
            jo.append(c)


        s_jo = sum(jo)

        kk = (po - s_jo) / (1 - s_jo)



        return kk











def dict():


 "def unique():\n"
 "    #l = []\n"
 "    full_list = []\n"
 "    with open('w.txt') as f:\n"
 "        for line in f:\n"
 "            line = line.strip()\n"
 "            line = line.split()\n"
 "            for item in line:\n"
 "                full_list.append(item)\n"
 "    return set(full_list)\n"
 "\n"
 "def ip():\n"
 "    l = input_list()\n"
 "    numl = []\n"
 "    un = unique()\n"
 "    for i in range(len(un)):\n"
 "        numl.append(i)\n"
 "\n"
 "\n"
 "\n"
 "\n"
 "def amount_of_input():\n"
 "    l = input_list()\n"
 "    count_input = set(l)\n"
 "    return(count_input)"


"""def po():
    l = input_list()
    for item in 

            if item[0] == amount_of_input()[i] and item[1] == amount_of_input()[i]:
                yes += 1
            if item[0] == 0 and item[1] == 0:
                no += 1
        p_o = (yes + no) / len_l
    return p_o

def pe():
    l = input_list()
    len_l = len(l)

    na = 0
    nb = 0
    ya  = 0
    yb  = 0

    for item in l:
        if item[0] == 0:
            na = na + 1
        if item[1] == 0:
            nb = nb + 1
        if item[0] == 1:
            ya = ya + 1
        if item[1] == 1:
            yb = yb + 1


    random_yes_a = ya/len_l
    random_yes_b = yb/len_l

    random_yes = random_yes_a * random_yes_b

    random_no_a = na/len_l
    random_no_b = nb/len_l

    random_no = random_no_a * random_no_b

    prob_yes = random_yes + random_no

    return prob_yes


def k():
    Po = po()
    Pe = pe()
    kk = (Po - Pe) / (1 - Pe)
    return kk"""



def main():
    print(input_list())



if __name__ == '__main__':
    main()
