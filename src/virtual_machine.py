from process_manager import ProcessManager
from scheduler import Scheduler
from process import Process
from process_state import ProcessState

# Classe que representa a máquina virtual
class VirtualMachine:
    def __init__(self, scheduler: Scheduler, process_manager: ProcessManager):
        self.scheduler = scheduler
        self.process_manager = process_manager

    def run(self):
        # Executa enquanto houver processos não terminados
        while True:
            process = self.scheduler.get_next_process()
            if not process:
                break
            self.execute_process(process)
    
            if process.state == ProcessState.TERMINATED:
                continue  
            self.scheduler.tick()



    def execute_process(self, process: Process):
        if process.pid in self.process_manager.memory_manager.virtual_memory:
            self.process_manager.memory_manager.copy_from_virtual_memory(process.pid)

        if process.program_counter < len(process.instructions):
            instruction = process.instructions[process.program_counter]
            self.execute_instruction(process, instruction)
            process.program_counter += 1

            if process.program_counter == len(process.instructions):
                process.state = ProcessState.TERMINATED  # Termina o processo se todas as instruções foram executadas
                print(f"Processo {process.pid} completou todas as instruções e está finalizado.")

    def execute_instruction(self, process: Process, instruction: str):
        # Simulação de execução de instruções
        print(f"Processo {process.pid} executando instrução: {instruction}")