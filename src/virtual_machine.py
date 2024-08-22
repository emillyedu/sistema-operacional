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
        while any(p.state != ProcessState.TERMINATED for p in self.process_manager.process_table.values()):
            process = self.scheduler.get_next_process()
            if process:
                self.execute_process(process)
                self.scheduler.tick()

    def execute_process(self, process: Process):
        if process.program_counter < len(process.instructions):
            instruction = process.instructions[process.program_counter]
            self.execute_instruction(process, instruction)
            process.program_counter += 1

            if process.program_counter == len(process.instructions):
                process.state = ProcessState.TERMINATED  # Termina o processo se todas as instruções foram executadas
                print(f"Process {process.pid} has completed all instructions and is now terminated.")

    def execute_instruction(self, process: Process, instruction: str):
        # Simulação de execução de instruções
        print(f"Process {process.pid} executing instruction: {instruction}")