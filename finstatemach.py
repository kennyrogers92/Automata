"""
Module for Finite State Machines
"""

from graphviz import Digraph
from itertools import chain, combinations

# Preliminaries
class _frozenset(frozenset):
    """
    User-defined class for frozenset to modify class representation
    
    Attributes
    ----------
        frozenset : frozenset
            collection of set of strings
    """
    def __repr__(self):
        return replace_last_closeparen((frozenset.__repr__(self)).replace("_frozenset(", "", 1))
    
class equivalence_class(_frozenset):
    """
    User-defined class for representation of equivalence class notation
    
    Attributes
    ----------
        _frozenset : _frozenset
            collection of set of strings
    """
    def __repr__(self):
        return equivalence_class_repr(_frozenset(self).__repr__())

def set_product(A, B):
    """
    Returns the Cartesian Product of two sets
    
    Attributes
    ----------
        A, B : set
            any collection of strings
    """
    Prod = {(a, b) for a in A for b in B}
    return Prod

def powerset(A):
    """
    Returns the powerset of a set
    """
    temp = chain.from_iterable(combinations(A, n) for n in range(len(A)+1))
    Powerset = set()
    for subset in temp:
        subset = _frozenset(subset)
        Powerset.add(subset)
    return Powerset

def replace_last_closeparen(string):
    """
        Replace the last parenthesis of a frozenset by ""
    """
    index = string.rfind(")")
    return string[:index] + ""

def delete_apostrophe(string):
    """
    Deletes the apostrophe strings in a given string
    """
    return string.replace("\"", "").replace("\'", "")

def equivalence_class_repr(string):
    """
    Returns a frozenset to the equivalence class notation
    """
    return string.replace("{", "[", 1).replace("}", "]", 1)

def get_keys_from_value(dict, value):
    """
    Returns a list of keys that has the corresponding value 'value'
    """
    return [key for key, val in dict.items() if val == value]

"Empty string representation"
eps = "\u03B5"
"Empty set representation"
phi = "\u03A6"

def parse_expression(string):
    """
    Returns the parsed expression of a string in a list
    """
    n = len(string)
    partition = []
    for i in range(n):
        pass

class DFA():
    """
    Class for Deterministic Finite Automata (DFA)
    
    Attributes
    ----------
        states : set
            collection of states
        alphabet : set
            collection of symbols
        transition : dict
            transition function of the form transition[state][symbol] = [state]
        start_state : str
            the starting state
        accept_states : set
            the accepting or final states
    """
    
    def __init__(self, states=set(), alphabet=set(), transition=dict,
            start_state=None, accept_states=set()):
        "Class initialization"
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transition = transition
        self.start_state = start_state
        self.accept_states = set(accept_states)
    
    def __repr__(self):
        """
        Class representation
        """
        return "Deterministic Finite Automaton (DFA) at " + f"{hex(id(self))}"
    
    def __str__(self):
        """
        String representation
        """
        str_self = (
            self.__repr__() + "\n"
            + "States           : " + f"{self.states}" + "\n"
            + "Alphabet         : " + f"{self.alphabet}" + "\n"
            + "Start State      : " + f"{self.start_state}" + "\n"
            + "Accept States    : " + f"{self.accept_states}" + "\n"
            +  self.str_transition()
        )
        return delete_apostrophe(str_self)    
    
    def str_transition(self):
        """
        String representation of the transition function
        """
        string  = "Transitions: state, symbol -> state"
        for state in self.transition:
            state_transitions = self.transition[state]
            for symbol in self.alphabet:
                state_str = f"{state}"
                next_state_str = f"{state_transitions[symbol]}"
                if state == set():
                    state_str = phi
                if state_transitions[symbol] == set():
                    next_state_str = phi
                string += "\n\t" + state_str + " , " + symbol + " -> "+ next_state_str
        return string
    
    def state_diagram(self):
        """
        Converts the DFA class to a graphviz Digraph class
        """
        graph = Digraph()
        graph.attr(rankdir = "LR", center="True", label=self.__repr__(), labelloc="t", fontsize="11pt")
        graph.node("entry", "", shape="none")
        for state in self.states - self.accept_states:
            state_str = delete_apostrophe(str(state))
            if state == set():
                state_str = phi
            graph.node(str(state), state_str, fixedsize="False", shape="circle",
                       fontname="Helvetica,Arial,sans-serif", fontsize="9pt")
        for state in self.accept_states:
            state_str = delete_apostrophe(str(state))
            if state == set():
                state_str = phi
            graph.node(str(state), state_str, fixedsize="False", shape="doublecircle",
                       fontname="Helvetica,Arial,sans-serif", fontsize="9pt")
        graph.edge("entry", str(self.start_state), arrowhead="vee", arrowsize="0.25")
        for state in self.states:
            for other_state in self.states:
                label = ",".join(get_keys_from_value(self.transition[state], other_state))
                if label:
                    graph.edge(str(state), str(other_state), label, arrowhead="vee", arrowsize="0.25",
                           fontname="Helvetica,Arial,sans-serif", fontsize="9pt")
        return graph
    
    def relabel(self):
        """
        Returns the relabeled states of DFA in natural numbers 
            starting at 0
        """
    
    def print_stats(self):
        """
        Prints the statistics of DFA
        """
                       
    def accepts(self, input_string=""):
        """
        Returns True if the DFA accepts the DFA accepts the input string,
            default as the empty string, otherwise False
        """
        current_state = self.start_state
        for idx in range(len(input_string)):
            current_symbol = input_string[idx]
            current_state = self.transition[current_state][current_symbol]
        if current_state in self.accept_states:
            return True
        else: 
            return False

    def transition_ext(self, alphabet=set()):
        """
        Returns the extension of transition of a DFA to larger alphabet
        """
        transition = self.transition.copy()
        for state in self.states:
            state_transitions = transition[state]
            for symbol in alphabet - self.alphabet:
                state_transitions.update({symbol: state})
        return transition
    
    def to_NFA(self):
        """
        Converts DFA to NFA
        """
        transition = {}
        for state in self.states:
            transition[state] = {}
            state_transitions = transition[state]
            state_transitions.update({'' : set()})
            for symbol in self.alphabet:
                state_transitions.update({symbol : {self.transition[state][symbol]}})
        return NFA(self.states, self.alphabet, transition, self.start_state, self.accept_states)
    
    # Regular Operations of DFAs
    def __neg__(self):
        """
        Returns the complement of a given DFA
        """
        return DFA(self.states, self.alphabet, self.transition, self.start_state,
               self.states - self.accept_states)
    
    def __and__(self, other):
        """
        Returns the intersection of two DFAs
        """
        states = set_product(self.states, other.states)
        alphabet = self.alphabet & other.alphabet
        transition = {}
        for state in states:
            transition[state] = {}
            state_transitions = transition[state]
            for symbol in alphabet:
                state_transitions.update({symbol : (self.transition[state[0]][symbol],
                                                    other.transition[state[1]][symbol])})
        start_state = (self.start_state, other.start_state)
        accept_states = set_product(self.accept_states, other.accept_states)
        return DFA(states, alphabet, transition, start_state, accept_states)
    
    def __or__(self, other):
        """
        Returns the union of two DFAs
        """
        states = set_product(self.states, other.states)
        alphabet = self.alphabet | other.alphabet
        transition = {}
        self.transition = self.transition_ext(alphabet)
        other.transition = other.transition_ext(alphabet)
        for state in states:
            transition[state] = {}
            state_transitions = transition[state]
            for symbol in alphabet:
                state_transitions.update({symbol : (self.transition[state[0]][symbol],
                                                    other.transition[state[1]][symbol])})
        start_state = (self.start_state, other.start_state)
        accept_states = set_product(self.accept_states, other.states) | set_product(self.states, other.accept_states)
        return DFA(states, alphabet, transition, start_state, accept_states)
    
    def __sub__(self, other):
        """
        Returns the relative complement of a DFA from other DFA
        """
        return self & -other
    
    # Concatenation and Star
    
    # DFA Minimization
    def strip(self):
        """
        Returns an equivalent DFA with unreachable states removed
        """
        ReachableStates = {self.start_state}
        NewStates = {self.start_state}
        while NewStates:
            TempState = set()
            for state in NewStates:
                for symbol in self.alphabet:
                    TempState = TempState | {self.transition[state][symbol]}
            NewStates = TempState - ReachableStates
            ReachableStates = ReachableStates | NewStates
        states = ReachableStates
        accept_states = ReachableStates & self.accept_states
        transition = self.transition.copy()
        for state in self.states - states:
            transition.pop(state)
        return DFA(states, self.alphabet, transition, self.start_state, accept_states)

    def minimize(self):
        """
        Returns the minimal equivalent DFA
        """
        self = self.strip()
        # Denote adjacency matrix G as AdjMat
        AdjMat = {}
        for (state, other_state) in set_product(self.states, self.states):
            AdjMat.update({(state, other_state): 0})
        for (state, other_state) in set_product(self.accept_states, self.states - self.accept_states):
            AdjMat[(state, other_state)] = 1
            AdjMat[(other_state, state)] = 1
        while True:
            AdjMat_old = AdjMat.copy()
            for (state, other_state) in set_product(self.states, self.states - {state}):
                    for symbol in self.alphabet:
                        if AdjMat[(self.transition[state][symbol], self.transition[other_state][symbol])] == 1:
                            AdjMat[(state, other_state)] = 1
                            AdjMat[(other_state, state)] = 1
            if AdjMat_old == AdjMat:
                break
        states = set()
        accept_states = set()
        transition = {}
        for state in self.states:
            equiv_states = {state}
            for other_state in self.states - equiv_states:
                if AdjMat[(state, other_state)] == 0:
                    equiv_states = equiv_states | {other_state}
            equiv_states = equivalence_class(equiv_states)
            states = states | {equiv_states}
            if state == self.start_state:
                start_state = equiv_states
            if state in self.accept_states:
                accept_states = accept_states | {equiv_states}
        for equiv_states in states:
            transition[equiv_states] = {}
            state_transitions = transition[equiv_states]
            for symbol in self.alphabet:
                for state in equiv_states:
                    current_state = self.transition[state][symbol]
                    for other_equiv_state in states:
                        if current_state in other_equiv_state:
                            equiv_states_transition = other_equiv_state
                    break
                state_transitions.update({symbol: equiv_states_transition})
        return DFA(states, self.alphabet, transition, start_state, accept_states)


class NFA():
    """
    Class for Nondeterministic Finite Automata (DFA)
    
    Attributes
    ----------
        states : set
            collection of states
        alphabet : set with the empty string ''
            collection of symbols and empty string
        transition : dict
            transition function of the form transition[state][symbol] = [set of states]
        start_state : str
            the starting state
        accept_states : set
            the accepting or final states
    """
    
    def __init__(self, states=set(), alphabet=set(), transition=dict,
                 start_state=None, accept_states=set()):
        "Class initialization"
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transition = transition
        self.start_state = start_state
        self.accept_states = set(accept_states)
    
    def __repr__(self):
        """
        Class representation
        """
        return "Nondeterministic Finite Automaton (NFA) at " + f"{hex(id(self))}"
    
    def __str__(self):
        """
        String representation
        """
        str_self = (
            self.__repr__() + "\n"
            + "States           : " + f"{self.states}" + "\n"
            + "Alphabet         : " + f"{self.alphabet}" + "\n"
            + "Start State      : " + f"{self.start_state}" + "\n"
            + "Accept States    : " + f"{self.accept_states}" + "\n"
            +  self.str_transition()
        )
        return delete_apostrophe(str_self)  
        
    def str_transition(self):
        """
        String representation of the transition function
        """
        string  = "Transitions: state, symbol -> set of states"
        for state in self.transition:
            state_transitions = self.transition[state]
            for symbol in self.alphabet | {''}:
                symbol_str = symbol
                state_str = f"{state}"
                next_state_str = f"{state_transitions[symbol]}"
                if symbol == '':
                    symbol_str = eps
                if state == set():
                    state_str = phi
                if state_transitions[symbol] == set():
                    next_state_str = phi
                string += "\n\t" + state_str + " , " + symbol_str + " -> "+ next_state_str
        return string
    
    def state_diagram(self):
        """
        Converts the NFA class to a graphviz Digraph class
        """
        graph = Digraph()
        graph.attr(rankdir = "LR", center="True", label=self.__repr__(), labelloc="t", fontsize="11pt")
        graph.node("entry", "", shape="none")
        for state in self.states - self.accept_states:
            graph.node(str(state), delete_apostrophe(str(state)), fixedsize="False", shape="circle",
                       fontname="Helvetica,Arial,sans-serif", fontsize="9pt")
        for state in self.accept_states:
            graph.node(str(state), delete_apostrophe(str(state)), fixedsize="False", shape="doublecircle",
                       fontname="Helvetica,Arial,sans-serif", fontsize="9pt")
        graph.edge("entry", str(self.start_state), arrowhead="vee", arrowsize="0.25")
        for state in self.states:
            for other_state in self.states:
                label = ",".join(get_keys_from_value(self.transition[state], {other_state}))
                if label:
                    graph.edge(str(state), str(other_state), label, arrowhead="vee", arrowsize="0.25",
                           fontname="Helvetica,Arial,sans-serif", fontsize="9pt")
            symbol = ''
            other_states = self.transition[state][symbol]
            if other_state:
                for other_state in other_states:
                    graph.edge(str(state), str(other_state), eps, arrowhead="vee", arrowsize="0.25",
                        fontname="Helvetica,Arial,sans-serif", fontsize="9pt")
        return graph
    
    # def relabel
    
    # def print_stats
    
    def accepts_via_DFA(self, input_string=""):
        """
        Returns True if input string is accepted by converting to DFA then checking by DFA.accept()
        """
        M = self.to_DFA()
        return M.accepts(input_string)
        
    def accepts(self, input_string=""):
        """
        Returns True if the NFA accepts the NFA accepts the input string,
            default as the empty string, otherwise False
        """
        k = len(input_string) 
        J = range(1, k)
        empty_string = ''
        if self.transition[self.start_state][empty_string]:
            input_string = empty_string + input_string
            J = range(k)
        CurrentStates = {self.start_state}
        for idx in J:
            NewStates = set()
            for state in CurrentStates:
                currentsymbol = input_string[idx]
                NewStates = NewStates | self.transition[state][currentsymbol]
            ReachableStates = set()
            for other_state in NewStates:
                ReachableStates = ReachableStates | self.reach(other_state)
            CurrentStates = NewStates | ReachableStates
        if (CurrentStates & self.accept_states):
            return True
        else:
            return False
        
    def reach(self, state):
        """
        Returns the reachable states of a state by following at least 0 empty string transition
        """
        Reach = {state}
        NewStates = {state}
        while NewStates:
            TempStates = set()
            for somestate in NewStates:
                empty_string = ''
                reached_states = set(self.transition[somestate][empty_string])
                TempStates = TempStates | reached_states
            NewStates = TempStates - Reach
            Reach = Reach | NewStates
        return _frozenset(Reach)
        
    def to_DFA(self):
        """
        Converts NFA to DFA
        """
        states = powerset(self.states)
        start_state = self.reach(self.start_state)
        transition = {}
        accept_states = set()
        for substates in states:
            transition[substates] = {}
            for symbol in self.alphabet:
                Reach = set()
                for state in substates:
                    reached_states = set(self.transition[state][symbol])
                    for reached_state in reached_states:
                        Reach = Reach | self.reach(reached_state)
                transition[substates].update({symbol : Reach})
            if (substates & self.accept_states):
                accept_states = accept_states | {substates}
        return DFA(states, self.alphabet, transition, start_state, accept_states)
        
    # Regular Operations of NFAs
    def __or__(self, other):
        """
        Returns the union of two NFAs
        """
        start_state = 'start'
        states = self.states | other.states | {start_state}
        alphabet = self.alphabet | other.alphabet
        transition = self.transition.copy()
        for state in self.states:
            for symbol in other.alphabet - self.alphabet:
                transition[state].update({symbol : set()})
        for state in other.states:
            transition[state] = {}
            for symbol in alphabet | {''}:
                if symbol in (other.alphabet | ''):
                    transition[state].update({symbol : other.transition[state][symbol]})
                else:
                    transition[state].update({symbol : set()})
        transition[start_state] = {}
        transition[start_state].update({'' : {self.start_state, other.start_state}})
        for symbol in alphabet:
            transition[start_state].update({symbol : set()})
        accept_states = self.accept_states | other.accept_states
        return NFA(states, alphabet, transition, start_state, accept_states)
    
    def __add__(self, other):
        """
        Returns the concatenation of two NFAs
        """
        states = self.states | other.states
        alphabet = self.alphabet | other.alphabet
        transition = self.transition.copy()
        for state in self.states:
            transition[state] = {}
            for symbol in other.alphabet - self.alphabet:
                transition[state].update({symbol : set()})
        for state in self.accept_states:
            transition[state] = {}
            transition[state].update({'' : transition[state][''] | {other.start_state}})
        for state in other.states:
            transition[state] = {}
            for symbol in alphabet | {''}:
                if symbol in (other.alphabet | ''):
                    transition[state].update({symbol : other.transition[state][symbol]})
                else:
                    transition[state].update({symbol : set()})
        return NFA(states, alphabet, transition, self.start_state, other.accept_states)
        
    def __mul__(self):
        """
        Returns the star of NFA
        """
        start_state = 'q0`'
        empty_string = ''
        states = self.states | {start_state}
        accept_states = self.accept_states | self.start_state
        transition = {}
        transition[start_state] = {}
        transition[start_state].update({empty_string : {self.start_state}})
        for symbol in self.alphabet:
            transition[start_state].update({symbol : set()})
        for state in self.state:
            transition[symbol] = {}
            if state in self.states - self.accept_states:
                for symbol in (self.alphabet | empty_string):
                    transition[state].update({symbol : self.transition[state][symbol]})
            else:
                for symbol in self.alphabet:
                    transition[state].update({symbol : self.transition[state][symbol]})
        for state in self.accept_states:
            transition[state] = {}
            transition[state].update({empty_string : self.transition[state][empty_string]} | {self.start_state})
        return NFA(states, self.alphabet, transition, start_state, accept_states)
                
    
class RegEx():
    """
    Class for Regular Expression
    
    Attributes
    ----------
        string : str
            input string to be verified as RegEx over the alphabet
        alphabet : set
            collection of symbols, default is binary
    """
    def __init__(self, string=str(), alphabet={'0', '1'}):
        "Class Initialization"
        self.string = string
        self.alphabet = alphabet
    
    def __repr__(self):
        "Class representation"
        return "Regular Expression (RegEx) at " + f"{hex(id(self))}"\
            + " over " + f"{self.alphabet}"
    
    def __str__(self):
        "String representation"
        return self.string
    
    def parse_expression(self):
        """
        """
        partitions = []
        for symbol in self:
            pass
        
class GNFA():
    """
    Class for Generalized Nondeterministic Finite Automata
    
    Attributes
    ----------
        states : set
            collection of states
        alphabet : set with the empty string ''
            collection of symbols and empty string
        transition : dict
            transition function of the form transition[state][states] = [RegEx]
        start_state : str
            the starting state
        accept_states : set
            the accepting or final states
    """