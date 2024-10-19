class Schedule:
    def __init__(self, day, time):
        self.day = day
        self.time = time

    def __str__(self):
        return f"{self.day} at {self.time}"
