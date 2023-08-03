from finstatemach import NFA, DFA

def NFASamples(num):
    """
    Function that returns a DFA as a function of index
    """
    # Initialize an NFA that accepts string with 101 or 11 as a substring
    if num == 0:
        N = NFA(states={'q1', 'q2', 'q3', 'q4'}, alphabet={'0', '1'},
            transition={
                'q1' : {'0' : {'q1'}, '1' : {'q1', 'q2'}, '' : {}},
                'q2' : {'0' : {'q3'}, '1' : {}, '' : {'q3'}},
                'q3' : {'0' : {}, '1' : {'q4'}, '' : {}},
                'q4' : {'0' : {'q4'}, '1' : {'q4'}, '' : {}},
            },
            start_state='q1', accept_states={'q4'})
    
    # Initialize an NFA that accepts strings that has 1 in its third or second to the last string, equivalent to DFASamples(6)
    if num == 1:
        N = NFA(states={'q1', 'q2', 'q3', 'q4'}, alphabet={'0', '1'},
            transition={
                'q1' : {'0' : {'q1'}, '1' : {'q1', 'q2'}, '' : {}},
                'q2' : {'0' : {'q3'}, '1' : {'q3'}, '' : {'q3'}},
                'q3' : {'0' : {'q4'}, '1' : {'q4'}, '' : {}},
                'q4' : {'0' : {}, '1' : {}, '' : {}},
            },
            start_state='q1', accept_states={'q4'})
        
    # Initialize an NFA with 0s divisible by 2 or 3, equivalent to DFASamples(7)
    if num == 2:
        N = NFA(states={'s', 'q0', 'q1', 'r0', 'r1', 'r2'}, alphabet={'0'},
            transition={
                's' : {'0' : {}, '' : {'q0', 'r0'}},
                'q0' : {'0' : {'q1'}, '' : {}},
                'q1' : {'0' : {'q0'}, '' : {}},
                'r0' : {'0' : {'r1'}, '' : {}},
                'r1' : {'0' : {'r2'}, '' : {}},
                'r2' : {'0' : {'r0'}, '' : {}}
            },
            start_state='s', accept_states={'q0', 'r0'})
        
    # Initialize an NFA that accepts empty string, string of zeros,
    #   string ending with 1 followed by at least two 0,
    #   or string ending with two 1 followed at least one zero
    if num == 3:
        N = NFA(states={'q', 'r', 's'}, alphabet={'0', '1'},
            transition={
                'q' : {'0' : {}, '1' : {'r'}, '' : {'s'}},
                'r' : {'0' : {'r', 's'}, '1' : {'s'}, '' : {}},
                's' : {'0' : {'q'}, '1' : {}, '' : {}},
            },
            start_state='q', accept_states={'q'})
    
    # Return NFA
    return N


if __name__ == "__main__":
    N = NFASamples(3)
    M = N.to_DFA()
    M.state_diagram().render(view=True)
    #M.state_diagram().render(view=True)
    # Print string representation of the DFA
    print(f"{M}")