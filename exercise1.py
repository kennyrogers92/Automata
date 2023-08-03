from finstatemach import DFA

# Initialize a DFA that accepts nonempty strings with alternating symbols
T1a = DFA(states={"q", "q0", "q1", "q01", "q10", "qx"}, alphabet={"0", "1"}, 
            transition={
                "q"   : {"0" : "q0", "1" : "q1"},
                "q0"  : {"0" : "qx", "1" : "q01"},
                "q1"  : {"0" : "q10", "1" : "qx"},
                "q01" : {"0" : "q10", "1" : "qx"},
                "q10" : {"0" : "qx", "1" : "q01"},
                "qx"  : {"0" : "qx", "1" : "qx"}
            }, 
            start_state="q", accept_states={"q01","q10"})

# Initialize a DFA that accepts strings starting and ending with 101
T1b = DFA(states={'q', 'qx', 'q1', 'q10', 'q101','q1011', 'q1010', 'q10100'}, alphabet={'0', '1'},
            transition={
                'q' : {'0' : 'qx', '1': 'q1'},
                'qx' : {'0' : 'qx', '1': 'qx'},
                'q1' : {'0' : 'q10', '1': 'qx'},
                'q10' : {'0' : 'qx', '1': 'q101'},
                'q101' : {'0' : 'q1010', '1': 'q1011'},
                'q1011' : {'0' : 'q1010', '1': 'q1011'},
                'q1010' : {'0' : 'q10100', '1': 'q101'},
                'q10100' : {'0' : 'q10100', '1': 'q1011'}
            },
            start_state='q', accept_states={'q101'})


# Initialize a DFA that accepts strings with 01 or 10 as substring
T2a = DFA(states={"q", "q0", "q1", "qx"}, alphabet={"0", "1"}, 
            transition={
                "q" : {"0" : "q0", "1" : "q1"},
                "q0" : {"0" : "q0", "1" : "qx"},
                "q1" : {"0" : "qx", "1" : "q1"},
                "qx" : {"0" : "qx", "1" : "qx"}
            }, 
            start_state="q", accept_states={"qx"})

# Initialize a DFA that accepts strings with exactly two 0s
T2b = DFA(states={"q", "q0", "q00", "qx"}, alphabet={"0", "1"}, 
            transition={
                "q"  : {"0" : "q0", "1" : "q"},
                "q0" : {"0": "q00", "1" : "q0"},
                "q00" : {"0" : "qx", "1" : "q00"},
                "qx" : {"0" : "qx", "1" : "qx"}
            }, 
            start_state="q", accept_states={"q00"})

# Initialize a DFA that accepts nonempty strings starting with 0
T3a1 = DFA(states={"q", "q0", "q1"}, alphabet={"0", "1"}, 
            transition={
                "q"  : {"0" : "q0", "1" : "q1"},
                "q0" : {"0" : "q0", "1" : "q0"},
                "q1" : {"0" : "q1", "1" : "q1"}
            }, 
            start_state="q", accept_states={"q0"})

# Initialize a DFA that accepts nonempty strings having at most one 1
T3a2 = DFA(states={"r0", "r1", "rx"}, alphabet={"0", "1"}, 
            transition={
                "r0" : {"0" : "r0", "1" : "r1"},
                "rx" : {"0" : "rx", "1" : "rx"},
                "r1" : {"0" : "r1", "1" : "rx"}
            }, 
            start_state="r0", accept_states={"r0", "r1"})

# Initialize a DFA that accepts strings with even length
T3b1 = DFA(states={"q_odd", "q_even"}, alphabet={"0", "1"}, 
            transition={
                "q_odd" : {"0" : "q_even", "1" : "q_even"},
                "q_even": {"0" : "q_odd", "1" : "q_odd"}
            }, 
            start_state="q_even", accept_states={"q_even"})

# Initialize a DFA that accepts strings with an odd number of 1s
T3b2 = DFA(states={"r_odd", "r_even"}, alphabet={"0", "1"}, 
            transition={
                "r_odd" : {"0" : "r_odd", "1" : "r_even"},
                "r_even": {"0" : "r_even", "1" : "r_odd"},
            }, 
            start_state="r_even", accept_states={"r_odd"})

T1a.state_diagram().render(view=True)