from process_manager import ProcessManager
from scheduler import Scheduler
from virtual_machine import VirtualMachine
from memory_manager import MemoryManager

def main():
    print("~SISTEMA OPERACIONAL~")
    # Solicitar o tamanho da memória física e virtual
    physical_memory_size = int(input("Tamanho da memória física em unidades: "))
    virtual_memory_size = int(input("Tamanho da memória virtual em unidades: "))

    # Criando o gerenciador de memória
    memory_manager = MemoryManager(physical_memory_size, virtual_memory_size)

    # Criando o gerenciador de processos e o escalonador
    process_manager = ProcessManager(memory_manager)
    scheduler = Scheduler(time_quantum=3)  # Quantum de tempo de 3

    # Adicionando processos através da linha de comando
    while True:
        print("Adicionando processos:")
        instructions = input("Insira as instruções do processo (ou 'sair' para executar): ")
        if instructions.lower() == 'sair':
            break

        # Criando um novo processo com as instruções inseridas
        process = process_manager.create_process(instructions.split(";"))
        
        # Perguntando ao usuário se o processo deve ser de alta prioridade
        priority = input("Este processo é de alta prioridade? (s/n): ").strip().lower()
        is_high_priority = priority == 's'
        
        # Adicionando o processo ao escalonador
        scheduler.add_process(process, high_priority=is_high_priority)

    # Criando a máquina virtual e executando os processos
    vm = VirtualMachine(scheduler, process_manager)
    vm.run()

if __name__ == "__main__":
    main()
