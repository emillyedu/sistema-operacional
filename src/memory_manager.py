import time
from collections import OrderedDict
from process import *

class MemoryManager:
    def __init__(self, physical_memory_size: int, virtual_memory_size: int):
        self.physical_memory = OrderedDict()  # Manter a ordem de uso
        self.virtual_memory = {} 
        self.physical_memory_size = physical_memory_size
        self.virtual_memory_size = virtual_memory_size

    def allocate(self, process: Process):
        print(f"Alocando processo {process.pid}.")
        if len(self.physical_memory) >= self.physical_memory_size:
            print("Memória física cheia, movendo processo para a memória virtual.")
            self.move_to_virtual_memory()
        self.physical_memory[process.pid] = process

    def move_to_virtual_memory(self):
        # Movendo o processo menos utilizado para a memória virtual
        if self.physical_memory:
            pid, process = self.physical_memory.popitem(last=False)  # Remove o primeiro (menos utilizado)
            self.virtual_memory[pid] = process
            print(f"Processo {pid} movido para a memória virtual.")

    def copy_from_virtual_memory(self, pid: int):
        if pid in self.virtual_memory:
            process = self.virtual_memory.pop(pid)
            time.sleep(1)  # Atraso artificial
            self.physical_memory[pid] = process
            print(f"Processo {pid} copiado para memória principal após atraso.")

