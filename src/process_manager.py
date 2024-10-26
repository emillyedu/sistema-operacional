from typing import List, Dict
from process import Process
from process_state import ProcessState
from memory_manager import *


# Classe que gerencia os processos
class ProcessManager:
    def __init__(self, memory_manager: MemoryManager):
        self.process_table: Dict[int, Process] = {}  # Tabela de processos
        self.memory_manager = memory_manager

    def create_process(self, instructions: List[str]) -> Process:
        process = Process(instructions)
        self.process_table[process.pid] = process  # Adiciona o processo à tabela
        self.memory_manager.allocate(process) # Aloca o processo na memória
        return process

    def terminate_process(self, pid: int) -> bool:
        process = self.process_table.get(pid)
        if process:
            process.state = ProcessState.TERMINATED  # Define o estado do processo como TERMINATED
            return True
        return False

    def get_process(self, pid: int) -> Process:
        return self.process_table.get(pid)