def spy_game(arr):
    """
    This functions searches for the sequence 0, 0, 7 in an integer array.

    Utilizes a table and is expected to work with other state machines,
    if a transition table for that particular state machine is made.

    The transition table is considered a list of dictionaries, where
    each dictionary represents the transitions of every state that
    represents the list index.
    """

    # This table is supposed to find if the list has the sequence '007' in it
    transitionTable = [{0:1}, {0:2}, {7:3}, {0:3, 1:3, 2:3, 3:3, 4:3, 5:3, 6:3, 7:3, 8:3, 9:3, 0:3}]
    finalStates = [3]

    state = 0
    for num in arr:
        if num in transitionTable[state]:
            state = transitionTable[state][num]
        else:
            state = 0
    return state in finalStates

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))