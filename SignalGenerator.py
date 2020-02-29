from Instrument import Instrument


class Anritsu_Synthesizer(Instrument):
    def __init__(self, resource_name):
        # call parent instrument constructor to set resource_name
        super().__init__(resource_name)
        self.set_output_at_reset_off()

    def set_frequency(self, freqinhz):
        self.instr.write('CF0 ' + str(freqinhz) + ' HZ')

    def set_power(self, power):
        self.instr.write('L0 ' + str(power) + ' DM')

    def set_output_off(self):
        self.instr.write('RF0')

    def set_output_on(self):
        self.instr.write('RF1')

    def set_output_at_reset_off(self):
        self.instr.write('RO1')
