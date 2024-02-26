class Strategy:
    """
    Class representing a trading strategy.

    This class provides methods for defining trading strategies
    and executing trading actions such as opening and closing positions.

    Attributes:
        None
    """

    @staticmethod
    def __params_to_string(**kwargs):
        """
        Convert parameters to a string representation.

        Args:
            kwargs (dict): Dictionary containing parameters.

        Returns:
            str: String representation of parameters.
        """
        return ", ".join([f"{key}={repr(value)}" for key, value in kwargs.items() if value is not None])

    @staticmethod
    def indicator():
        return f"BUY"

    @staticmethod
    def strategy():
        return f"BUY"
