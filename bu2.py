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


def input_list():
    l = []
    with open('tk.txt') as f:
        for line in f:
            line = line.rstrip()
            line = line.split()
            one = int(line[0])
            two = int(line[1])
            l.append((one, two))
    return l

def po():
    yes = 0
    no = 0
    l = input_list()
    len_l = len(input_list())
    for item in l:
        if item[0] == 1 and item[1] == 1:
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

    return (ya,yb,na,nb)

    # (Counter({'1': 98, '0': 28}), Counter({'1': 82, '0': 44}))


def k():
    Po = po()
    Pe = pe()
    kk = (Po - Pe) / (1 - Pe)
    return kk



def main():
    print(k())



if __name__ == '__main__':
    main()
