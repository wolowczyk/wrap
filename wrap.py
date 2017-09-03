def wrap(t, n):
    w = ''
    rest = ''
    t = t.split()
    index = 0
    for word in t:
        # managing the "rest" of the long word
        while rest != '':

            # if rest is short
            if len(rest) <= n:
                w += '\n' + rest
                index = len(rest) + 1
                rest = ''

            # if rest is long
            else:

                # adding rest to the previous verse (checking how long is previous verse)
                if n - index - len(rest) >= 0:
                    w += rest[:n - 1] + '-'
                    rest = rest[n - 1:]
                    index = len(rest) + 1

                # adding rest to the next verse
                else:
                    w += '\n' + rest[:n - 1] + '-'
                    rest = rest[n - 1:]
                    index = len(rest) + 1

        # if the word is long and possible to split
        if len(word) > n:

            # if it's the first word
            if word == t[0]:
                w += word[:n-1] + '-'
                rest = word[n-1:]
                index = len(word[n-1:])

            # checking if can add whole word to previous verse
            elif n - index - len(word) >= 0:
                w += word
                index += 1 + len(word)

            # checking how many letters of word to be split, can be added to previous verse
            elif index < n:
                y = n - index

                # if can put just 1 character, do not add '-'
                if y == 1:
                    w += ''

                # checking how many characters can put into verses
                else:
                    w += ' ' + word[:y - 1] + '-'
                rest = word[y - 1:]
                index += 1 + len(word[:y])
            # adding rest to next verse
            else:
                w += '\n' + word[:n-1] + '-'
                rest = word[n-1:]
                index = len(word[:n-1]) + 1

        # if the word is short and impossible to split
        elif len(word) < n:

            # checking if first word
            if word == t[0]:
                w += word
                index += 1 + len(word)

            # adding word to previous verse
            elif n - index - len(word) >= 0:
                w += ' ' + word
                index += len(word) + 1

            # adding word to next verse
            else:
                w += '\n' + word
                index = len(word) + 1

        # if the word is exactly n long
        else:

            # if first word
            if word == t[0]:
                w += word
                index = len(word)

            # if not the first one
            else:
                w += '\n' + word
                index = len(word)
    return w