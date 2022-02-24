

def compSeq ():
    seq1 = "(((((...((.....)))))))"
    seq11 = "GGGCAAAUCCUCUUCGGUGCCC"
    liss11 = list(seq11.strip())
    seq2 = "(((<<...((.....))>>)))"
    seq22 = "GGGAAAAUCCUCUUCGGUUCCC"
    liss22 = list(seq22.strip())
    BpNbrInBoth = 0
    message1 = "Nombres de bases similaires:"
    ErrorMessage = "Les deux séquences sont de taille différentes!"

    if len(seq1) == len(seq2) and seq1.count('(') == seq1.count(')') and seq1.count('<') == seq1.count('>') and seq2.count('(') == seq2.count(')') and seq2.count('<') == seq2.count('>'):
        nbr1 = seq1.count('(') + seq1.count('<')
        nbr2 = seq2.count('(') + seq2.count('<')
        x = -1
        y = -1

        for i in range(len(liss11)):
            for j in range(len(liss22)):
                if (liss11[i] == liss22[j]) and (liss11[x] == liss22[y]):

                    x -= -1
                    y -= -1
                    BpNbrInBoth += 1
                    break








    return message1 + " " + str(BpNbrInBoth)




print(compSeq())