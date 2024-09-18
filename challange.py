
def somme_recursive(liste):
    total = 0
    for element in liste:
        if isinstance(element, list):  
            total += somme_recursive(element)
        else:
            total += element  
    return total

print(somme_recursive([15, 2, 8, [5, [99, 5], 6, 10], 5, 9, [9, [5, []]]]))