#!/usr/bin/python3
# _ _ _ _ _ TOTAL OF ALL THE ELEMENTS FOUND ONLY IN ONE SET ________
def only_diff_elements(set_1, set_2):
    diff_1 = list(set_1 ^ set_2)
    return(diff_1)
