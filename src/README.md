# Máquina Virtual (VM) - Projeto

## Objetivo do Projeto

Desenvolver uma Máquina Virtual (VM) que simule a execução de processos em um sistema operacional de propósito específico. O projeto deve incluir a implementação de componentes essenciais como gerenciamento de processos, memória, entrada/saída (E/S), escalonamento de processos, um sistema de arquivos simples, uma linguagem de instruções e uma Interface de Linha de Comando (CLI).

## Componentes Implementados

### 1. Gerenciador de Processos

**Requisitos Atendidos:**
- **Estrutura de dados para representar um processo:** Implementado na classe `Process` (`process.py`).
- **Funcionalidades para criar, gerenciar e terminar processos:** Implementado na classe `ProcessManager` (`process_manager.py`).
- **Atributos do processo:**
  - **PID:** Implementado.
  - **Estado do Processo:** Implementado usando `ProcessState`.
  - **Contador de Programa (PC):** Implementado como `program_counter`.
  - **Registros:** Implementado como uma lista de registros (`registers`).
  - **Memória Alocada:** Implementado como uma lista (`memory`), embora não haja alocação real.
  - **Instruções:** Implementado como uma lista de instruções (`instructions`).
  - **Tarefas:** Campo `tasks` está presente, mas não é utilizado.

**Tarefas Implementadas:**
- **Classe para representar um processo:** Implementado como `Process`.
- **Classe para gerenciar processos:** Implementado como `ProcessManager`.
- **Métodos para criar e terminar processos:** Implementados em `ProcessManager` (`create_process` e `terminate_process`).
- **Manter e atualizar o estado dos processos:** Implementado em `ProcessManager`.

### 2. Escalonador de Processos

**Requisitos Atendidos:**
- **Escalonador de processos:** Implementado na classe `Scheduler` (`scheduler.py`).
- **Algoritmos de escalonamento:** Implementado Round Robin, com base no quantum de tempo.

**Tarefas Implementadas:**
- **Classe para gerenciar o escalonamento de processos:** Implementado como `Scheduler`.
- **Métodos para adicionar processos e selecionar o próximo processo:** Implementados em `Scheduler` (`add_process` e `get_next_process`).
- **Alternância entre processos:** Implementado em `Scheduler` com o método `tick`.

### 3. Simulação da Execução de Processos

**Requisitos Atendidos:**
- **Ciclo de execução (busca, decodificação, execução, atualização):** Implementado na classe `VirtualMachine` (`virtual_machine.py`).
- **Conjunto de instruções:** Simulação de execução de instruções é implementada, mas o conjunto real de instruções é limitado a mensagens de impressão.

**Tarefas Implementadas:**
- **Classe principal para a VM:** Implementado como `VirtualMachine`.
- **Ciclo de execução dos processos:** Implementado em `run` e `execute_process` na `VirtualMachine`.
- **Conjunto de instruções:** Presente como uma simulação de execução, mas as instruções reais e sua lógica precisam ser detalhadas e implementadas.
- **Alternância e gerenciamento do estado de cada processo:** Implementado.


## Execução

Para executar o projeto, siga o passo abaixo:

- Navegue até o diretório onde os arquivos foram salvos.
- Execute o arquivo `.\src\main.py` usando o comando:
  ```
  python .\src\main.py
  ```

## Funcionamento do arquivo Main:

**Inicialização:**

- O ProcessManager e o Scheduler (com quantum de tempo 3) são criados.
- Dois processos de exemplo são definidos com instruções de manipulação de memória e operações aritméticas junto com o tempo de execução de cada instrução.
- Os processos são adicionados ao escalonador.

**Execução da Máquina Virtual:**

- A VirtualMachine é iniciada, utilizando o gerenciador de processos e o escalonador.
- A máquina virtual executa em loop até que todos os processos estejam terminados.
- Em cada iteração:
  - O escalonador seleciona o próximo processo a ser executado.
  - A máquina virtual simula a execução das instruções do processo durante o quantum de tempo.
  - O escalonador é notificado sobre o tempo decorrido.
  - Se um processo termina, o gerenciador de processos é informado para marcá-lo como terminado.
  - 
**Simulação de Instruções:**

- A execução de instruções é atualmente com foco em simulação simplificada que imprime as instruções sendo executadas e os processos que terminam no terminal para demonstrar conceitos de gerenciadores de processo, escalonadores e execução de instruções.
- Em uma implementação completa real, a máquina virtual pode ser expandida com novos conceitos para interpretar e executar as instruções em um ambiente virtualizado, manipulando registradores, alocando memória e outros recursos como um SO.