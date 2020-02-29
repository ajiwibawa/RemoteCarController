from Instrument import Instrument


class Agilent_33220x(Instrument):
    def __init__(self, resource_name):
        # call parent instrument constructor to set resource_name
        super().__init__(resource_name)

    # Override close method implementation to send 'SYSTem:LOCal' to put instrument in local mode
    def close(self):
        self.instr.write('SYSTem:LOCal')
        self.instr.close()

    def set_frequency(self, freqinhz):
        self.instr.write('FREQuency ' + str(freqinhz) + ' HZ')

    def set_output_off(self):
        self.instr.write('OUTPut OFF')

    def set_output_on(self):
        self.instr.write('OUTPut ON')

    def set_vpp(self, vppinvolt):
        self.instr.write('VOLTage ' + str(vppinvolt))

    def set_voltage_high(self, highvoltageinvolt):
        self.instr.write('VOLTage:HIGH ' + str(highvoltageinvolt))

    def set_voltage_low(self, lowvoltageinvolt):
        self.instr.write('VOLTage:LOW ' + str(lowvoltageinvolt))

    def set_waveform_shape(self, waveformshape):
        # waveformshape: {SINusoid|SQUare|RAMP|PULSe|NOISe|DC|USER}
        self.instr.write('FUNCtion ' + str(waveformshape))

    def set_arbitrary_waveform_shape(self):
        self.instr.write('FUNCtion:USER VOLATILE')
        self.instr.write('FUNCtion:SHAPe USER')

    def set_AM_depth(self, depthinpercent):
        self.instr.write('AM:DEPTh ' + str(depthinpercent))

    def set_AM_internal_mod_frequency(self, freqinhz):
        self.instr.write('AM:INTernal:FREQuency ' + str(freqinhz))

    def set_AM_internal_mod_waveform_shape(self, waveformshape):
        # waveformshape: {SINusoid|SQUare|RAMP|NRAMp|TRIangle|NOISe|USER}
        self.instr.write('AM:INTernal:FUNCtion ' + str(waveformshape))

    def set_AM_source_external(self):
        self.instr.write('AM:SOURce EXTernal')

    def set_AM_source_internal(self):
        self.instr.write('AM:SOURce INTernal')

    def set_AM_state_off(self):
        self.instr.write('AM:STATe OFF')

    def set_AM_state_on(self):
        self.instr.write('AM:STATe ON')

    def set_burst_mode(self, burstmode):
        # burstmode: {TRIGgered|GATed}
        self.instr.write('BURS:MODE ' + str(burstmode))

    def set_burst_count(self, burstcount):
        self.instr.write('BURS:NCYC ' + str(burstcount))

    def set_burst_period(self, burstperiod):
        self.instr.write('BURS:INT:PER ' + str(burstperiod))

    def set_burst_mode_on(self):
        self.instr.write('BURS:STAT ON')

    def set_burst_mode_off(self):
        self.instr.write('BURS:STAT OFF')

    def set_pulse_period(self, periodinsec):
        self.instr.write('PULSe:PERiod ' + str(periodinsec))

    def set_pulse_width(self, pulsewidthinsec):
        self.instr.write('FUNCtion:PULSe:WIDTh ' + str(pulsewidthinsec))

    def set_trigger_source(self, triggersource):
        # triggersource: {IMMediate|EXTernal|BUS}
        self.instr.write('TRIG:SOUR ' + str(triggersource))

    def trigger(self):
        self.instr.write('TRIGger')

    def download_arb_waveform_data_to_volatile(self, data):
        self.instr.write('DATA VOLATILE, ' + data)
