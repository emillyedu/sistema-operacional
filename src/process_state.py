from enum import Enum

# Possíveis estados de um processo
class ProcessState(Enum):
    READY = "ready"
    RUNNING = "running"
    BLOCKED = "blocked"
    TERMINATED = "terminated"