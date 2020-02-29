import visa


class Instrument:
    def __init__(self, resource_name):
        self.resourceName = resource_name
        rm = visa.ResourceManager()
        self.instr = rm.open_resource(self.resourceName)

    def instr(self):
        return self.instr

    def clear(self):
        self.instr.clear()

    def close(self):
        self.instr.close()

    def identity_query(self):
        return self.instr.query('*IDN?')

    def reset(self):
        self.instr.write('*RST')
