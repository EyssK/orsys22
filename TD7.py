"""
Créez une fonction `to_list` qui prend en argument une `str` et qui retourne une liste composée de chaque caractère de cette chaîne.
"""

def to_list(l):
    res = list()
    for c in l:
        res.append(c)
    return res

def main():
    l = to_list("abcdefg")
    print(l)

if __name__ == '__main__' :
    main()