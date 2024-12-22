from abc import ABC, abstractmethod
class NinjaTurtle(ABC):
    pass
    @abstractmethod
    def aliasOF(self):
        pass
class leonardo(NinjaTurtle):
    def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.alias = __alias
    @property
    def aliasOF(self):
        return f"His alias is {self.__alias} "
class Michelangelo(NinjaTurtle):
    def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.alias = __alias
    @property
    def aliasOF(self):
        return f"His alias is {self.__alias} "
class Donatello(NinjaTurtle):
    def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.alias = __alias
    @property
    def aliasOF(self):
        return f"His alias is {self.__alias} "
class Raphael(NinjaTurtle):
    def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.alias = __alias
    @property
    def aliasOF(self):
        return f"His alias is {self.__alias} "