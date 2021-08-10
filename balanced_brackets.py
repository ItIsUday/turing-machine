"""Turing machine that accepts set of all strings of balanced parentheses consisting of (, {, } and )"""

from machines import TuringMachine


def main():
    machine = TuringMachine(states={"q0", "q1", "q2", "q3", "q4"},
                            symbols={"(", ")", "{", "}", "B", "X"},
                            blank_symbol="B",
                            input_symbols={"(", ")", "{", "}", "B"},
                            initial_state="q0",
                            accepting_states={"q4"},
                            transitions={
                                ("q0", ")"): ("q1", "X", -1),
                                ("q0", "}"): ("q2", "X", -1),
                                ("q0", "B"): ("q3", "B", -1),
                                ("q0", "X"): ("q0", "X", 1),
                                ("q0", "("): ("q0", "(", 1),
                                ("q0", "{"): ("q0", "{", 1),
                                ("q1", "X"): ("q1", "X", -1),
                                ("q2", "X"): ("q2", "X", -1),
                                ("q1", "("): ("q0", "X", 1),
                                ("q2", "{"): ("q0", "X", 1),
                                ("q3", "X"): ("q3", "X", -1),
                                ("q3", "B"): ("q4", "B", 1),
                            })

    machine.initialize(get_input())

    if machine.simulate():
        print("Balanced")
    else:
        print("Not balanced")


def get_input():
    acceptable_inputs = {"(", ")", "{", "}"}
    print("Enter a string consisting of characters", acceptable_inputs, " only: ", end="")
    expr = input()

    for symbol in expr:
        if symbol not in acceptable_inputs:
            print("Invalid input: ", symbol)
            exit(1)
    return dict(enumerate(expr))


if __name__ == "__main__":
    main()
