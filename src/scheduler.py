from collections import deque
from process import Process
from process_state import ProcessState

class Scheduler:
    def __init__(self, time_quantum: int):
        self.high_priority_queue = deque()  # Fila de alta prioridade
        self.low_priority_queue = deque()   # Fila de baixa prioridade
        self.time_quantum = time_quantum
        self.current_process = None
        self.current_time = 0

    def add_process(self, process: Process, high_priority: bool = False):
        process.state = ProcessState.READY
        if high_priority:
            self.high_priority_queue.append(process)
        else:
            self.low_priority_queue.append(process)

    def get_next_process(self) -> Process:
        # Se houver processos na fila de alta prioridade, execute até o fim (FCFS)
        if self.high_priority_queue:
            self.current_process = self.high_priority_queue.popleft()
            self.current_process.state = ProcessState.RUNNING
            self.current_time = 0
            return self.current_process
        
        # Se não houver processos de alta prioridade, pega da fila de baixa prioridade (Round Robin)
        if self.low_priority_queue:
            if self.current_process and self.current_process.state != ProcessState.TERMINATED:
                # Reinsere o processo na fila de baixa prioridade
                self.low_priority_queue.append(self.current_process)
            self.current_process = self.low_priority_queue.popleft()
            self.current_process.state = ProcessState.RUNNING
            self.current_time = 0
            return self.current_process

        return None

    def tick(self):
        self.current_time += 1
        if self.current_process:
            if self.current_process.program_counter >= len(self.current_process.instructions):
                # Processo atual completou sua execução
                self.current_process.state = ProcessState.TERMINATED
                self.current_process = None
                self.current_time = 0  # Resetar o tempo atual
                return
            
            if self.current_time >= self.time_quantum:
                if self.current_process.state == ProcessState.RUNNING:
                    # Coloca o processo atual como pronto
                    self.current_process.state = ProcessState.READY
                    if self.high_priority_queue: 
                        # Coloca de volta apenas se há processos de alta prioridade
                        self.high_priority_queue.append(self.current_process)
                    else:
                        # Se não, coloca de volta na fila de baixa prioridade
                        self.low_priority_queue.append(self.current_process)
                # Obter próximo processo para executar
                self.get_next_process()

    def is_current_process_complete(self) -> bool:
        return (self.current_process.program_counter >= len(self.current_process.instructions))
