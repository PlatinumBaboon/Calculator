def spacer(str1):
    str6 = str1.replace("-", " - ")
    str2 = str6.replace("+", " + ")
    str3 = str2.replace("*", " * ")
    str4 = str3.replace("/", " / ")
    str5 = str4.replace("^", " ^ ")
    str7 = str5.replace(" . ", ".")
    return str7


def bracket_pair_finder(calculation):
    start_bracket_index_array = []
    end_bracket_index_array = []
    bracket_pairs = {}

    for i in range(len(calculation)):
        if calculation[i] == '(':
            start_bracket_index_array.append(i)
        elif calculation[i] == ')':
            end_bracket_index_array.append(i)

    for i in range(len(start_bracket_index_array) - 1, -1, -1):
        for x in range(len(end_bracket_index_array)):
            if end_bracket_index_array[x] < start_bracket_index_array[i] or end_bracket_index_array[
                x] in bracket_pairs.values():
                continue
            else:
                bracket_pairs[start_bracket_index_array[i]] = end_bracket_index_array[x]
                break
        break
    if len(bracket_pairs) != 0:
        return bracket_pairs


def equation(eq):
    eq = spacer(eq)
    eq = eq.split()
    while len(eq) > 2:
        for e in eq:
            if e == '-' and eq[eq.index(e) - 1] == '^':
                firstnum = eq.index(e) - 1
                secondnum = eq.index(e) + 1
                thirdnum = eq.index(e) - 2
                num1 = eq[firstnum]
                num2 = eq[secondnum]
                num3 = eq[thirdnum]
                just = pow(float(num3), float(-(int(num2))))
                answer = spacer(str(just))
                eq.pop(thirdnum)
                eq.pop(thirdnum)
                eq.pop(thirdnum)
                eq.pop(thirdnum)
                eq.insert(thirdnum, answer)
                eq = ' '.join(eq)
                eq = spacer(eq)
                eq = eq.split()
            else:
                continue
        for e in eq:
            if e == "^":
                firstnum = eq.index(e) - 1
                secondnum = eq.index(e) + 1
                num1 = eq[firstnum]
                num2 = eq[secondnum]
                answer = str(pow(float(num1), float(num2)))
                eq.pop(firstnum)
                secondnum = eq.index(e) + 1
                eq.pop(secondnum)
                eq.insert(eq.index(e), answer)
                eq.remove(e)
            else:
                continue
        for e in eq:
            if e == "/":
                try:
                    if eq[eq.index(e) + 1] == '-':
                        firstnum = eq.index(e) - 1
                        secondnum = eq.index(e) + 1
                        thirdnum = eq.index(e) + 2
                        num1 = eq[firstnum]
                        num2 = eq[secondnum]
                        num3 = eq[thirdnum]
                        sum = [str(num1), str(e), str(num2), str(num3), ]
                        just = ' '.join(sum)
                        answer = spacer(str(eval(just)))
                        eq.pop(firstnum)
                        eq.pop(firstnum)
                        eq.pop(firstnum)
                        eq.pop(firstnum)
                        eq.insert(firstnum, answer)
                        eq = ' '.join(eq)
                        eq = spacer(eq)
                        eq = eq.split()
                        if len(eq) == 2:
                            return ''.join(eq)
                except:
                    continue
            if e == "/":
                try:
                    firstnum = eq.index(e) - 1
                    secondnum = eq.index(e) + 1
                    num1 = eq[firstnum]
                    num2 = eq[secondnum]
                    sum = [num1, e, num2]
                    just = ' '.join(sum)
                    answer = str(eval(just))
                    eq.pop(firstnum)
                    secondnum = eq.index(e) + 1
                    eq.pop(secondnum)
                    eq.insert(eq.index(e), answer)
                    eq.remove(e)
                except:
                    continue
            else:
                continue
        for e in eq:
            if e == "*":
                try:
                    if eq[eq.index(e) + 1] == '-':
                        firstnum = eq.index(e) - 1
                        secondnum = eq.index(e) + 1
                        thirdnum = eq.index(e) + 2
                        num1 = eq[firstnum]
                        num2 = eq[secondnum]
                        num3 = eq[thirdnum]
                        sum = [str(num1), str(e), str(num2), str(num3), ]
                        just = ' '.join(sum)
                        answer = spacer(str(eval(just)))
                        eq.pop(firstnum)
                        eq.pop(firstnum)
                        eq.pop(firstnum)
                        eq.pop(firstnum)
                        eq.insert(firstnum, answer)
                        eq = ' '.join(eq)
                        eq = spacer(eq)
                        eq = eq.split()
                        if len(eq) == 2:
                            return ''.join(eq)
                except:
                    continue
                try:
                    firstnum = eq.index(e) - 1
                    secondnum = eq.index(e) + 1
                    num1 = eq[firstnum]
                    num2 = eq[secondnum]
                    sum = [num1, e, num2]
                    just = ' '.join(sum)
                    answer = str(eval(just))
                    eq.pop(firstnum)
                    secondnum = eq.index(e) + 1
                    eq.pop(secondnum)
                    eq.insert(eq.index(e), answer)
                    eq.remove(e)
                except:
                    continue
            else:
                continue
        for e in eq:
            if e == "+":
                try:
                    if eq[eq.index(e) - 1] == '-':
                        eq.remove(str(eq[eq.index(e)]))
                        eq = ''.join(eq)
                        eq = spacer(eq)
                        eq = eq.split()
                    if eq[eq.index(e) + 1] == '-':
                        eq.remove(str(eq[eq.index(e)]))
                        eq = ''.join(eq)
                        eq = spacer(eq)
                        eq = eq.split()
                    if eq[eq.index(e) - 2] == '-':
                        firstnum = eq.index(e) - 1
                        secondnum = eq.index(e) + 1
                        thirdnum = eq.index(e) - 2
                        num1 = eq[firstnum]
                        num2 = eq[secondnum]
                        num3 = eq[thirdnum]
                        sum = [str(num3), str(num1), str(e), str(num2), ]
                        just = ' '.join(sum)
                        answer = spacer(str(eval(just)))
                        eq.pop(thirdnum)
                        eq.pop(thirdnum)
                        eq.pop(thirdnum)
                        eq.pop(thirdnum)
                        eq.insert(firstnum, answer)
                        eq = ''.join(eq)
                        eq = spacer(eq)
                        eq = eq.split()
                        if len(eq) == 2:
                            return ''.join(eq)
                except:
                    continue
                try:
                    firstnum = eq.index(e) - 1
                    secondnum = eq.index(e) + 1
                    num1 = eq[firstnum]
                    num2 = eq[secondnum]
                    sum = [num1, e, num2]
                    just = ' '.join(sum)
                    answer = str(eval(just))
                    eq.pop(firstnum)
                    secondnum = eq.index(e) + 1
                    eq.pop(secondnum)
                    eq.insert(eq.index(e), answer)
                    eq.remove(e)
                except:
                    continue
            else:
                continue
        for e in eq:
            try:
                if e == '-':
                    try:
                        if eq[eq.index(e) + 1] == '-':
                            eq.insert(eq.index(e), '+')
                            eq.pop(eq.index(e))
                            eq.pop(eq.index(e))
                            eq = ''.join(eq)
                            eq = spacer(eq)
                            eq = eq.split()
                    except:
                        continue
                    if eq[eq.index(e) + 2] == '-':
                        if eq[eq.index(e) + 3] == '-':
                            eq.insert((eq.index(e) + 2), '+')
                            eq.pop(eq.index(e) + 3)
                            eq.pop(eq.index(e) + 3)
                            eq = ''.join(eq)
                            eq = spacer(eq)
                            eq = eq.split()
                            if len(eq) == 2:
                                return ''.join(eq)
                    if eq[eq.index(e) + 2] == '-':
                        try:
                            firstnum = eq.index(e) + 1
                            secondnum = eq.index(e) + 2
                            thirdnum = eq.index(e) + 3
                            num1 = eq[firstnum]
                            num2 = eq[secondnum]
                            num3 = eq[thirdnum]
                            sum = [str(e), str(num1), str(num2), str(num3), ]
                            just = ' '.join(sum)
                            answer = spacer(str(eval(just)))
                            eq.remove(str(num1))
                            eq.remove(str(num2))
                            eq.remove(str(num3))
                            eq.insert(eq.index(e), answer)
                            eq.remove(str(e))
                            eq = ' '.join(eq)
                            eq = eq.split()
                            if len(eq) == 2:
                                return ''.join(eq)
                        except:
                            continue
            except:
                continue
                if len(eq) == 2:
                    return ''.join(eq)
        for e in eq:
            try:
                if e == "-":
                    try:
                        firstnum = eq.index(e) - 1
                        secondnum = eq.index(e) + 1
                        num1 = eq[firstnum]
                        num2 = eq[secondnum]
                        sum = [str(num1), str(e), str(num2)]
                        just = ' '.join(sum)
                        answer = spacer(str(eval(just)))
                        eq.remove(str(num1))
                        eq.remove(str(num2))
                        eq.insert(eq.index(e), answer)
                        eq.remove(str(e))
                        eq = ' '.join(eq)
                        eq = eq.split()
                    except:
                        continue
                    if len(eq) == 2:
                        return ''.join(eq)
            except:
                continue
        else:
            try:
                if eq[0] == '+':
                    eq.pop(0)
            except:
                continue
            return str(' '.join(eq))


def remove_brackets(puz):
    for e in puz:
        if e == '(':
            bracket_pair_finder(puz)
            startbracket = list(bracket_pair_finder(puz).keys())[0]
            endbracket = list(bracket_pair_finder(puz).values())[0]
            bracket_pair = puz[(startbracket + 1):endbracket]
            x = range(endbracket, (startbracket - 1), -1)
            list_pop = list(puz)
            for i in x:
                list_pop.pop(i)
            list_pop.insert(startbracket, str(equation(bracket_pair)))
            just = ''.join(list_pop)
            puz = puz.replace(puz, just)
            puz = spacer(puz)
            puz = puz.split()
            puz = ' '.join(puz)
    return puz


def Default():
    dice = input("error incorrect Format try again?(y/n)")
    if dice.lower() == "y":
        math(input("input sum( e.g. 4 + 6) :"))
    elif dice.lower() == "n":
        print("Goodbye")
    else:
        Default2()


def Default2():
    dice = input("error incorrect Format try again?(y/n)")
    if dice.lower() == "y":
        math(input("input sum( e.g. 4 + 6) :"))
    elif dice.lower() == "n":
        print("Goodbye")
    else:
        Default()


def math(equat):
    equat = spacer(equat)
    count = 0
    try:
        while len(equat.split()) > 2 and count < 10:
            nobrackets = remove_brackets(equat)
            equat = equation(nobrackets)
            count += 1

        else:
            try:
                for e in equat.split():
                    if e =='/':
                        if equat.split().index(e + 1) == '0':
                            return ''
                if isinstance(int(''.join(equat)), int) == True:
                    return ''.join(equat)

            except:
                try:
                    if isinstance(float(''.join(equat)), float) == True:
                        return ''.join(equat)
                except:
                    if isinstance(''.join(equat), int) == False:
                        return ''
    except:
        return ''

def math2(answer):
    if answer == '':
        Default()
    else:
        return answer
    
#Can add these back in if not using GUI
#Sum = input("input sum( e.g. 4 + 6) :")
#print(math2(math(spacer(Sum))))

