def Strongest_Extension(class_name, extensions):
    strength = []
    for ext in extensions:
        CAP = len([x for x in ext if x.isalpha() and x.isupper()])
        SM = len([x for x in ext if x.isalpha() and x.islower()])
        strength.append(CAP - SM)
    max_strength = max(strength)
    for i in range(len(strength)):
        if strength[i] == max_strength:
            return class_name + "." + extensions[i]
