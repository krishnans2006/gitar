class Note:
    def __init__(self, name: str, pin: int):
        self.name = name
        self.pin = pin

    def press(self):
        print(f"{self.name} pressed")

    def release(self):
        print(f"{self.name} released")
