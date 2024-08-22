from collections import deque
from process import Process
from process_state import ProcessState

class Scheduler:
    def __init__(self, time_quantum: int):
        self.ready_queue = deque()  # Fila de processos prontos
        self.time_quantum = time_quantum  # Quantum de tempo para execução
        self.current_process = None
        self.current_time = 0

    def add_process(self, process: Process):
        process.state = ProcessState.READY
        self.ready_queue.append(process)  # Adiciona o processo à fila de prontos

    def get_next_process(self) -> Process:
        if self.current_process and self.current_process.state != ProcessState.TERMINATED:
            self.ready_queue.append(self.current_process)  # Reinsere o processo na fila se não terminado
        if self.ready_queue:
            self.current_process = self.ready_queue.popleft()  # Pega o próximo processo da fila
            self.current_process.state = ProcessState.RUNNING  # Define como o processo em execução
            self.current_time = 0
            return self.current_process
        return None

    def tick(self):
        self.current_time += 1
        if self.current_time >= self.time_quantum:
            self.current_process.state = ProcessState.READY  # Define como pronto após o quantum
            self.get_next_process()  # Pega o próximo processo da fila
