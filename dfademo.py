from finstatemach import DFA

def DFASamples(num):
    """
    Function that returns a DFA as a function of index
    """
    # Initialize a DFA that accepts string that ends with 10^k where k is even
    if num == 0:
        M = DFA(states={"q1", "q2", "q3"}, alphabet={"0", "1"},
            transition={
                "q1": {"0" : "q1", "1" : "q2"},
                "q2": {"0" : "q3", "1" : "q2"},
                "q3": {"0" : "q2", "1" : "q2"}
            },
            start_state="q1", accept_states={"q2"})
    
    # Initialize a DFA that accepts strings with even number of 1s
    if num == 1:
        M = DFA(states={"q0", "q1"}, alphabet={"0", "1"},
            transition={
                "q0": {"0" : "q0", "1" : "q1"},
                "q1": {"0" : "q1", "1" : "q0"},
            },
            start_state="q0", accept_states={"q0"})

    # Initialize a DFA that accepts string with 100 or 101 as substring
    if num == 2:
        M = DFA(states={"q", "q1", "q10", "q100", "q101"}, alphabet={"0", "1"},
            transition={
                "q"     : {"0" : "q", "1" : "q1"},
                "q1"    : {"0" : "q10", "1" : "q1"},
                "q10"   : {"0" : "q100", "1" : "q101"},
                "q100"  : {"0" : "q100", "1" : "q100"},
                "q101"  : {"0" : "q101", "1" : "q101"},
            },
            start_state="q", accept_states={"q100", "q101"})
        
    # Initialize a DFA that accepts strings with same first and last symbol
    if num == 3:
        M = DFA(states={"q", "q00", "q01", "q10", "q11"}, alphabet={"0", "1"},
            transition={
                "q"    : {"0" : "q00", "1" : "q11"},
                "q00"  : {"0" : "q00", "1" : "q01"},
                "q01"  : {"0" : "q00", "1" : "q01"},
                "q10"  : {"0" : "q10", "1" : "q11"},
                "q11"  : {"0" : "q10", "1" : "q11"},
            },
            start_state="q", accept_states={"q00", "q11"})
        
    # Initialize a DFA that accepts string that starts with 0
    if num == 4:
        M = DFA(states={"q", "q0", "q1"}, alphabet={"0", "1"},
            transition={
                "q": {"0" : "q0", "1" : "q1"},
                "q0": {"0" : "q0", "1" : "q0"},
                "q1": {"0" : "q1", "1" : "q1"}
            },
            start_state="q", accept_states={"q0"})
        
    # Initialize a DFA that accepts string that ends with 0
    if num == 5:
        M = DFA(states={"r", "r0"}, alphabet={"0", "1", "x"},
            transition={
                "r": {"0" : "r0", "1" : "r", "x" : "r"},
                "r0": {"0" : "r0", "1" : "r", "x" : "r"}
            },
            start_state="r", accept_states={"r0"})

    # Initialize a DFA that accepts strings that has 1 in its third or second to the last string, equivalent to NFASamples(1)
    if num == 6:
        M = DFA(states={"q000", "q001", "q011", "q111", "q110", "q100", "q101", "q010"}, alphabet={"0", "1"},
            transition={
                "q000": {"0" : "q000", "1" : "q001"},
                "q001": {"0" : "q010", "1" : "q011"},
                "q011": {"0" : "q110", "1" : "q111"},
                "q111": {"0" : "q110", "1" : "q111"},
                "q110": {"0" : "q100", "1" : "q101"},
                "q100": {"0" : "q000", "1" : "q001"},
                "q101": {"0" : "q010", "1" : "q011"},
                "q010": {"0" : "q100", "1" : "q101"},
            },
            start_state="q000", accept_states={"q010", "q011", "q100", "q101", "q111", "q110"})
        
    # Initialize a DFA with 0s divisible by 2 or 3, equivalent to NFASamples(2)
    if num == 7:
        M = DFA(states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}, alphabet={'0'},
            transition={
                'q0': {'0' : 'q1'},
                'q1': {'0' : 'q2'},
                'q2': {'0' : 'q3'},
                'q3': {'0' : 'q4'},
                'q4': {'0' : 'q5'},
                'q5': {'0' : 'q0'}
            },
            start_state='q0', accept_states={'q0', 'q2', 'q3', 'q4'})
    
    # Initialize a DFA that accepts sum of strings from 0, 1, 2, r equivalent to 0 mod 3
    if num == 8:
        M = DFA(states={'q0', 'q1', 'q2'}, alphabet={'0', '1', '2', 'r'},
            transition={
                'q0': {'0' : 'q0', '1' : 'q1', '2' : 'q2', 'r' : 'q0'},
                'q1': {'0' : 'q1', '1' : 'q2', '2' : 'q0', 'r' : 'q0'},
                'q2': {'0' : 'q2', '1' : 'q0', '2' : 'q1', 'r' : 'q0'}
            },
            start_state='q0', accept_states={'q0'}) 
    
    # Initialize DFA that accepts strings with the same first and last symbol
    if num == 9:
        M = DFA(states={'q', 'q0x', 'q00', 'q1x', 'q11'}, alphabet={'0', '1'},
            transition={
                'q': {'0' : 'q00', '1' : 'q11'},
                'q00': {'0' : 'q00', '1' : 'q0x'},
                'q0x': {'0' : 'q00', '1' : 'q0x'},
                'q11': {'0' : 'q1x', '1' : 'q11'},
                'q1x': {'0' : 'q1x', '1' : 'q11'},
            },
            start_state='q', accept_states={'q00', 'q11'})
    
    # Initialize a DFA
    if num == 10:
        M = DFA(states={frozenset(set()), frozenset({'q1'}), frozenset({'q2'}), frozenset({'q3'}), 
                        frozenset({'q1', 'q2'}), frozenset({'q1', 'q3'}), frozenset({'q2', 'q3'}),
                        frozenset({'q1', 'q2', 'q3'})}, alphabet={'0', '1'},
                transition={
                    frozenset(set()) : {'0' : frozenset(set()), '1' : frozenset(set())},
                    frozenset({'q1'}) : {'0' : frozenset({'q1', 'q2', 'q3'}), '1' : frozenset(set())},
                    frozenset({'q2'}) : {'0' : frozenset(set()), '1' : frozenset(set())},
                    frozenset({'q3'}) : {'0' : frozenset({'q2', 'q3'}), '1' : frozenset({'q1', 'q2', 'q3'})},
                    frozenset({'q1', 'q2'}) : {'0' : frozenset({'q1', 'q2', 'q3'}), '1' : frozenset(set())},
                    frozenset({'q1', 'q3'}) : {'0' : frozenset({'q1', 'q2', 'q3'}), '1' : frozenset({'q1', 'q2', 'q3'})},
                    frozenset({'q2', 'q3'}) : {'0' : frozenset({'q1', 'q2'}), '1' : frozenset({'q1', 'q2', 'q3'})},
                    frozenset({'q1', 'q2', 'q3'}) : {'0' : frozenset({'q1', 'q2', 'q3'}), '1' : frozenset({'q1', 'q2', 'q3'})}
                },
                start_state=frozenset({'q1'}), accept_states={frozenset({'q3'}), frozenset({'q1', 'q3'}), 
                                                              frozenset({'q2', 'q3'}), frozenset({'q1', 'q2', 'q3'})})
    # Return DFA
    return M
        
if __name__ == "__main__":
    M1, M2 = DFASamples(4), DFASamples(5)
    M = (M1 & M2).to_NFA()
    M.state_diagram().render(view=True)
    
    # Print string representation of the DFA
    print(f"{M}")
    # Check if the input string is accepted by the DFA
    for input_string in ["000101000", "0001010101", "1001001011"]:
        is_input_string_accepted = M.accepts(input_string)
        print(M.__repr__() + " accepts " + input_string + "? "
              + str(is_input_string_accepted))