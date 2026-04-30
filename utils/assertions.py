from utils.logger import get_logger

logger = get_logger()


class SoftAssertions:
    """Soft assertions - continue testing even if assertion fails"""

    def __init__(self):
        self.failures = []

    def assert_true(self, condition, message):
        """Assert condition is True"""
        if not condition:
            self.failures.append(f"FAILED: {message}")
            logger.warning(f"Assertion failed: {message}")
        else:
            logger.info(f"Assertion passed: {message}")

    def assert_false(self, condition, message):
        """Assert condition is False"""
        if condition:
            self.failures.append(f"FAILED: {message}")
            logger.warning(f"Assertion failed: {message}")
        else:
            logger.info(f"Assertion passed: {message}")

    def assert_equal(self, actual, expected, message):
        """Assert actual equals expected"""
        if actual != expected:
            self.failures.append(f"FAILED: {message} | Expected: {expected}, Got: {actual}")
            logger.warning(f"Assertion failed: {message} | Expected: {expected}, Got: {actual}")
        else:
            logger.info(f"Assertion passed: {message}")

    def assert_not_equal(self, actual, expected, message):
        """Assert actual does not equal expected"""
        if actual == expected:
            self.failures.append(f"FAILED: {message} | Should not be: {expected}")
            logger.warning(f"Assertion failed: {message}")
        else:
            logger.info(f"Assertion passed: {message}")

    def assert_in(self, item, collection, message):
        """Assert item is in collection"""
        if item not in collection:
            self.failures.append(f"FAILED: {message} | '{item}' not found in collection")
            logger.warning(f"Assertion failed: {message}")
        else:
            logger.info(f"Assertion passed: {message}")

    def assert_not_empty(self, value, message):
        """Assert value is not empty"""
        if not value:
            self.failures.append(f"FAILED: {message} | Value is empty")
            logger.warning(f"Assertion failed: {message}")
        else:
            logger.info(f"Assertion passed: {message}")

    def assert_contains(self, text, substring, message):
        """Assert text contains substring"""
        if substring not in text:
            self.failures.append(f"FAILED: {message} | '{substring}' not found in '{text}'")
            logger.warning(f"Assertion failed: {message}")
        else:
            logger.info(f"Assertion passed: {message}")

    def get_failures(self):
        """Get all failures"""
        return self.failures

    def has_failures(self):
        """Check if there are any failures"""
        return len(self.failures) > 0

    def print_failures(self):
        """Print all failures"""
        if self.failures:
            logger.error(f"\n========== SOFT ASSERTION FAILURES ({len(self.failures)}) ==========")
            for idx, failure in enumerate(self.failures, 1):
                logger.error(f"{idx}. {failure}")
            logger.error("=" * 60)
        else:
            logger.info("No soft assertion failures!")

    def clear_failures(self):
        """Clear all failures"""
        self.failures.clear()
