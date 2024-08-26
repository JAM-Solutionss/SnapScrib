import time
import threading
from collections import deque
from typing import Optional, Deque, Tuple


class FunctionTracker:
    _local: threading.local = threading.local()

    @classmethod
    def current_function(self) -> Optional[str]:
        """
        Returns the name of the current function being tracked, 
        or `None` if no function is currently being tracked.

        This method is part of the `FunctionTracker` class, which is used 
        to track the execution of functions in the application. 
        It provides a way to retrieve the name of the function that is currently 
        being tracked, which can be useful for logging, debugging, or other purposes.

        Returns:
            Optional[str]: The name of the current function being tracked, 
            or `None` if no function is currently being tracked.
        """
        return getattr(self._local, "current_function", None)

    @classmethod
    def set_current_function(self, func_name: str) -> None:
        """
        Sets the current function being tracked and adds it to the function call stack.
        
        This method is part of the `FunctionTracker` class, which is used to track the
        execution of functions in the application. It provides a way to set the current
        function being tracked and add it to the function call stack, which can be
        useful for logging, debugging, or other purposes.
        
        Args:
            func_name (str): The name of the function to be tracked.
        
        Returns:
            None
        """
        self._local.current_function = func_name
        if not hasattr(self._local, "function_stack"):
            self._local.function_stack = deque()
        self._local.function_stack.append((func_name, time.time()))

    @classmethod
    def clear_current_function(self) -> None:
        """
        Clears the current function being tracked and removes the most recent
        function from the function call stack.

        This method is part of the `FunctionTracker` class, which is used to track
        the execution of functions in the application. It provides a way to clear
        the current function being tracked and remove the most recent function from
        the function call stack, which can be useful for resetting the state of
        the function tracking system.
        """
        self._local.current_function = None
        if hasattr(self._local, "function_stack"):
            self._local.function_stack.pop()

    @classmethod
    def get_function_stack(self) -> Deque[Tuple[str, float]]:
        """
        Returns the function call stack maintained by the `FunctionTracker` class.
        
        This method retrieves the `function_stack` attribute from the thread-local 
        storage of the `FunctionTracker` class. The `function_stack` is a deque (double-ended queue) 
        that stores the names of the functions that have been entered and the times at 
        which they were entered.
        
        If the `function_stack` attribute does not exist in the thread-local storage, 
        this method returns an empty deque.
        
        Returns:
            Deque[Tuple[str, float]]: The function call stack, where each element 
            is a tuple containing the name of the function and the time at which it was entered.
        """
        return getattr(self._local, "function_stack", deque())

    @classmethod
    def get_execution_time(self) -> int | float:
        """
        Returns the execution time of the most recent function call tracked by
        the `FunctionTracker` class.

        This method retrieves the function call stack maintained by the `FunctionTracker`
        class and calculates the execution time of the most recent function call.
        If there are no function calls in the stack, it returns 0.

        Returns:
            int | float: The execution time of the most recent function call, in seconds.
        """
        stack = self.get_function_stack()
        if stack:
            start_time = stack[-1][1]
            return time.time() - start_time
        return 0

    @classmethod
    def reset(self) -> None:
        """
        Resets the current function being tracked and clears the function
        call stack maintained by the `FunctionTracker` class.

        This method is part of the `FunctionTracker` class, which is used
        to track the execution of functions in the application. It provides a way
        to reset the state of the function tracking system by clearing the current
        function being tracked and the function call stack.
        """
        self._local.current_function = None
        self._local.function_stack = deque()


function_tracker = FunctionTracker()


class track_function:
    def __init__(self, func):
        """
        Initializes a new instance of the `track_function` context manager.

        The `track_function` context manager is used to track the execution 
        of a function. When the context manager is entered, it sets the current 
        function being tracked in the `FunctionTracker` class. When the context 
        manager is exited, it clears the current function being tracked.

        The `func` parameter is the function that will be tracked when the context manager is used.
        """
        self.func = func

    def __enter__(self):
        """
        Sets the current function being tracked in the `FunctionTracker` 
        class to the qualified name of the decorated function.

        This method is called when the context manager is entered, 
        and it records the start time of the function call and adds it to 
        the function call stack maintained by the `FunctionTracker` class.
        """
        function_tracker.set_current_function(self.func.__qualname__)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Clears the current function being tracked when the `track_function` context manager
        is exited. This is called automatically when the `with` block is left, either
        normally or due to an exception being raised.
        """
        function_tracker.clear_current_function()


def track(func):
    """
    Decorator that tracks the execution of the decorated function.

    When the decorated function is called, it is wrapped in a context manager that
    records the start time of the function call and adds it to the function call
    stack maintained by the `FunctionTracker` class. When the function returns, the
    context manager clears the current function from the stack.

    This decorator can be used to measure the execution time of functions and
    provide insights into the call flow of an application.
    """

    def wrapper(*args, **kwargs):
        with track_function(func):
            return func(*args, **kwargs)

    return wrapper
