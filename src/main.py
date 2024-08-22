from process_manager import ProcessManager
from scheduler import Scheduler
from virtual_machine import VirtualMachine

# Criando o gerenciador de processos e o escalonador
process_manager = ProcessManager()
scheduler = Scheduler(time_quantum=3)  # Quantum de tempo de 3

# Criando processos
process1 = process_manager.create_process(["LOAD R1, 5", "ADD R1, R2", "STORE R1, 100"])
process2 = process_manager.create_process(["LOAD R3, 10", "SUB R3, R1", "STORE R3, 200"])

# Adicionando processos ao escalonador
scheduler.add_process(process1)
scheduler.add_process(process2)

# Criando a máquina virtual e executando os processos
vm = VirtualMachine(scheduler, process_manager)
vm.run()
