def process_input(inputs):
    output = []

    for input in inputs:
        x = int(input[0])
        y = int(input[1])
        string = input[2]

        # thoughts... when evaluating whether to fill in ????, you always want to fill in with the same thing
        # more thoughts... if front and back are the same, you just fill in with the same
        # further thoughts... if not the same, then you select the obviously best one

        # this section of code basically splits the string by the ? character
        # since all we need to do is identify blocks of ????, and review the remaining strings
        string = string.split('?')
        string = list(filter(lambda x: len(x) != 0, string))

        cost = 0
        prev_sub_char = ''
        for substring in string:
            if prev_sub_char == "C":
                if substring[0] == "J":
                    cost += x # you basically select the min cost each time, so i don't care what you actually fill in
                prev_char = ''
                for char in substring:
                    if prev_char == '':
                        prev_char = char
                        continue
                    elif prev_char == 'C' and char == 'J':
                        cost += x
                    elif prev_char == 'J' and char == 'C':
                        cost += y
                    prev_char = char
                    continue
                prev_sub_char = substring[-1]
            elif prev_sub_char == "J":
                if substring[0] == "C":
                    cost += y # you basically select the min cost each time, so i don't care what you actually fill in
                prev_char = ''
                for char in substring:
                    if prev_char == '':
                        prev_char = char
                        continue
                    elif prev_char == 'C' and char == 'J':
                        cost += x
                    elif prev_char == 'J' and char == 'C':
                        cost += y
                    prev_char = char
                    continue
                prev_sub_char = substring[-1]
            elif prev_sub_char == "":
                prev_char = ''
                for char in substring:
                    if prev_char == '':
                        prev_char = char
                        continue
                    elif prev_char == 'C' and char == 'J':
                        cost += x
                    elif prev_char == 'J' and char == 'C':
                        cost += y
                    prev_char = char
                    continue
                prev_sub_char = substring[-1]
        output.append(cost)

    return output


if __name__ == "__main__":
    n = int(input())
    inputs = []
    for _ in range(n):
        str = input()
        inputs.append(str.split(" "))

    output_lines = process_input(inputs)

    i = 1
    for l in output_lines:
        print("Case #{}: {}".format(i, l))
        i += 1
