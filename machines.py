from collections import defaultdict
from typing import Optional


class TuringMachine:
    def __init__(self,
                 states: set[str],
                 symbols: set[str],
                 blank_symbol: str,
                 input_symbols: set[str],
                 initial_state: str,
                 accepting_states: set[str],
                 transitions: dict[tuple[str, str], tuple[str, str, int]],
                 ) -> None:
        self.states = states
        self.symbols = symbols
        self.blank_symbol = blank_symbol
        self.input_symbols = input_symbols
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.transitions = transitions

        self.__head: Optional[int] = None
        self.__halted: Optional[bool] = None
        self.__current_state: Optional[str] = None
        self.__tape: Optional[defaultdict[int, str]] = None

    def initialize(self, input_symbols: dict[int, str]) -> None:
        self.__head = 0
        self.__halted = False
        self.__current_state = self.initial_state
        self.__tape = defaultdict(lambda: self.blank_symbol, input_symbols)

    def step(self) -> None:
        if self.__halted:
            raise RuntimeError('Cannot step halted machine')

        try:
            state, symbol, direction = self.transitions[(self.__current_state, self.__tape[self.__head])]
        except KeyError:
            self.__halted = True
            return
        self.__tape[self.__head] = symbol
        self.__current_state = state
        self.__head += direction

    def is_input_accepted(self) -> bool:
        if not self.__halted:
            raise RuntimeError('Machine still running')
        return self.__current_state in self.accepting_states

    def print(self, window=10) -> None:
        print('... ', end='')
        print(' '.join(self.__tape[i] for i in range(self.__head - window, self.__head + window + 1)), end='')
        print(f' ... state = {self.__current_state}')
        print(f'{" " * (2 * window + 4)}^')

    def simulate(self) -> bool:
        while not self.__halted:
            self.print()
            self.step()
        return self.is_input_accepted()
