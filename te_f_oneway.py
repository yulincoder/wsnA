def get_total_mean(*args):
    """ obtaining the mean value of total data.
    """
    tmp_sum, item_number = 0.0, 0.0
    for e in args:
        tmp_sum += sum(e)
        item_number += len(e)

    return tmp_sum/item_number


def get_group_mean(group):
    """ obtaining the mean value of a group.
    """
    return float(sum(group))/len(group)



def te_f_oneway(*args):
    """ ANOVA
    """
    total_mean = get_total_mean(*args)

    QA = sum([len(e)*((get_group_mean(e) - total_mean)**2) for e in args])
    S2A = QA/(len(args) - 1)

    QE = sum([(i - get_group_mean(e))**2 for e in args for i in e])
    S2E = QE / (sum([len(e) for e in args]) - len(args))

    # QT can be use to check the correct : QT = QA + QE
    QT = sum([(i - total_mean)**2 for e in args for i in e])

    F = S2A / S2E
    return F

if __name__ == '__main__':
    a1 = [1600, 1610, 1650, 1680, 1700, 1720, 1800] # mean = 2
    a2 = [1580, 1640, 1640, 1700, 1750] # mean = 3
    a3 = [1460, 1550, 1600, 1620, 1640, 1660, 1740, 1820] # mean = 3
    a4 = [1510, 1520, 1530, 1570, 1600, 1680]
    te_f_oneway(a1, a2, a3, a4)

    from scipy.stats import f_oneway
    print f_oneway(a1, a2, a3, a4)
