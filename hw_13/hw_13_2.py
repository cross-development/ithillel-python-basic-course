class Counter:
    """
    A digital counter class that maintains a value within specified bounds.

    Attributes:
        current (int): Current value of the counter
        min_value (int): Minimum allowed value
        max_value (int): Maximum allowed value
    """

    def __init__(self, current: int = 1, min_value: int = 0, max_value: int = 10) -> None:
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start: int) -> None:
        """
        Set the current value of the counter.

        Args:
            start (int): New current value
        """
        self.current = start

    def set_max(self, max_max: int) -> None:
        """
        Set the maximum allowed value.

        Args:
            max_max (int): New maximum value
        """
        self.max_value = max_max

    def set_min(self, min_min: int) -> None:
        """
        Set the minimum allowed value.

        Args:
            min_min (int): New minimum value
        """
        self.min_value = min_min

    def step_up(self) -> None:
        """
        Increment the counter by 1.

        Raises:
            ValueError: If the counter has reached its maximum value
        """
        if self.current >= self.max_value:
            raise ValueError("Досягнуто максимуму")

        self.current += 1

    def step_down(self) -> None:
        """
        Decrement the counter by 1.

        Raises:
            ValueError: If the counter has reached its minimum value
        """
        if self.current <= self.min_value:
            raise ValueError("Досягнуто мінімуму")

        self.current -= 1

    def get_current(self) -> int:
        """
        Get the current value of the counter.

        Returns:
            int: Current value
        """
        return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()

assert counter.get_current() == 10, 'Test1'

try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнут максимум

assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()

assert counter.get_current() == 7, 'Test3'

try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнут минимум

assert counter.get_current() == 7, 'Test4'
