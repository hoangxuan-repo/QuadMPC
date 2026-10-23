"""Generate stance/swing contact schedules."""


class GaitScheduler:
    def __init__(self, frequency=2.0, duty_factor=0.6):
        self.frequency = frequency
        self.duty_factor = duty_factor

    def get_contacts(self, time):
        raise NotImplementedError
