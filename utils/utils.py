
import time

from selenium.common.exceptions import TimeoutException


def wait_for(callback, expected_result=True, timeout=10, poll_frequency=0.5):
    end_time = time.monotonic() + timeout

    while time.monotonic() < end_time:
        result = callback()

        if result == expected_result:
            return result

        time.sleep(poll_frequency)

    raise TimeoutException(
        f"Condition was not met within {timeout} seconds. "
        f"Expected: {expected_result!r}"
    )