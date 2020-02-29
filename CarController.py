import FunctionGenerator
import time
from time import sleep


class CarController:
    CONTROL_PULSE_PATTERN = ['1', '1', '1', '0']
    DIRECTION_PULSE_PATTERN = ['1', '0']

    HIGH_VOLTAGE_LEVEL = 3.3
    LOW_VOLTAGE_LEVEL = 0
    LONG_PULSE_WIDTH_MS = 2.1
    SHORT_PULSE_PERIOD_MS = 1.4
    CONTROL_PULSE_PERIOD_MS = 2.8
    CONTROL_PULSE_COUNT = 4

    # direction pulse counts
    FORWARD_PULSE_COUNT = 10
    FORWARD_RIGHT_PULSE_COUNT = 28
    FORWARD_LEFT_PULSE_COUNT = 34
    BACKWARD_PULSE_COUNT = 40
    BACKWARD_RIGHT_PULSE_COUNT = 52
    BACKWARD_LEFT_PULSE_COUNT = 46
    STOP_PULSE_COUNT = 4

    INVALID_CODE_DESCRIPTION = 'Invalid Code'

    def __init__(self, function_generator_resource_name):
        self.fg = FunctionGenerator.Agilent_33220x(function_generator_resource_name)
        self.__init_fg()

    def __init_fg(self):
        self.fg.clear()
        self.fg.reset()
        sleep(0.5)
        print(self.fg.identity_query())
        self.fg.set_output_off()
        self.fg.set_arbitrary_waveform_shape()
        self.fg.set_voltage_high(self.HIGH_VOLTAGE_LEVEL)
        self.fg.set_voltage_low(self.LOW_VOLTAGE_LEVEL)

    def lookup_code_description(self, code_number):
        code_description = {
            self.FORWARD_PULSE_COUNT: 'Forward',
            self.FORWARD_RIGHT_PULSE_COUNT: 'Forward/Right',
            self.FORWARD_LEFT_PULSE_COUNT: 'Forward/Left',
            self.BACKWARD_PULSE_COUNT: 'Backward',
            self.BACKWARD_LEFT_PULSE_COUNT: 'Backward/Left',
            self.BACKWARD_RIGHT_PULSE_COUNT: 'Backward/Right',
            self.STOP_PULSE_COUNT: 'Stop'
        }
        if self.__is_number(code_number):
            return code_description.get(int(code_number), self.INVALID_CODE_DESCRIPTION)
        else:
            return self.INVALID_CODE_DESCRIPTION

    def forward(self):
        print('f')
        self.__create_waveform_pattern(self.FORWARD_PULSE_COUNT)
        self.fg.set_output_on()

    def forward_right(self):
        print('fr')
        self.__create_waveform_pattern(self.FORWARD_RIGHT_PULSE_COUNT)
        self.fg.set_output_on()

    def forward_left(self):
        print('fl')
        self.__create_waveform_pattern(self.FORWARD_LEFT_PULSE_COUNT)
        self.fg.set_output_on()

    def backward(self):
        print('b')
        self.__create_waveform_pattern(self.BACKWARD_PULSE_COUNT)
        self.fg.set_output_on()

    def backward_left(self):
        print('bl')
        self.__create_waveform_pattern(self.BACKWARD_LEFT_PULSE_COUNT)
        self.fg.set_output_on()

    def backward_right(self):
        print('br')
        self.__create_waveform_pattern(self.BACKWARD_RIGHT_PULSE_COUNT)
        self.fg.set_output_on()

    def stop(self):
        print('stop')
        # self.__create_waveform_pattern(self.STOP_PULSE_COUNT)
        # self.fg.set_output_on()
        self.fg.set_output_off()

    def close(self):
        print('close')
        self.fg.close()

    def move(self, direction_pulse_count, duration=None):
        self.__create_waveform_pattern(direction_pulse_count)
        self.fg.set_output_on()

        if duration is not None:
            # keep sending the pulses for the specified duration
            t_end = time.time() + duration
            while time.time() < t_end:
                sleep(0.01)

            self.fg.set_output_off()

    def __create_waveform_pattern(self, directionpulsecount):
        # Calculate total waveform period and frequency
        period = (self.CONTROL_PULSE_COUNT * self.CONTROL_PULSE_PERIOD_MS) + \
                 (directionpulsecount * self.SHORT_PULSE_PERIOD_MS)
        self.fg.set_frequency((1 / period) * 1000)  # period is defined in milli sec

        # Build control pulses waveform
        control_pulse_list = self.CONTROL_PULSE_PATTERN
        for i in range(1, self.CONTROL_PULSE_COUNT):
            control_pulse_list = control_pulse_list + self.CONTROL_PULSE_PATTERN

        # Build direction pulses waveform
        direction_pulse_list = self.DIRECTION_PULSE_PATTERN
        for i in range(1, directionpulsecount):
            direction_pulse_list = direction_pulse_list + self.DIRECTION_PULSE_PATTERN

        control_waveform = ','.join(control_pulse_list)
        direction_waveform = ','.join(direction_pulse_list)
        final_waveform = control_waveform + ',' + direction_waveform
        print('Final waveform: ' + final_waveform)

        self.fg.download_arb_waveform_data_to_volatile(final_waveform)

    def __is_number(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False
