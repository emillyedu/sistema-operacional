import itertools
from enum import Enum
from typing import List, Dict
from process_state import ProcessState

#Classe que representa um processo
class Process:
    pid_generator = itertools.count()  # Gerador de PID único

    def __init__(self, instructions: List[str]):
        self.pid = next(self.pid_generator)  # PID único para cada processo
        self.state = ProcessState.READY  # Estado inicial do processo
        self.program_counter = 0  # Contador de programa (inicia em 0)
        self.registers = [0] * 8  # Simulação de 8 registros
        self.memory = []  # Memória alocada para o processo
        self.instructions = instructions  # Lista de instruções do processo
        self.tasks = []

    def __repr__(self):
        return f"Process(pid={self.pid}, state={self.state}, pc={self.program_counter})"
