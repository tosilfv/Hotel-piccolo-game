"""Unit tests for logging_config.py"""
import logging
import pytest


class TestLoggingConfig:
    """Test Logging config class"""

    @pytest.fixture(autouse=True)
    def setup_logger(self, tmp_path):
        """Setup a temporary log file for testing and cleanup after test"""
        # Create a temporary path for the log file
        self.log_file = tmp_path / "piccolo_game_errors.log"

        # Yield control back to the test; everything before this is setup
        yield

        # Shut down all loggers and flush any remaining log messages
        logging.shutdown()

        # Remove all existing handlers from the root logger to prevent interference with other tests
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

    def test_configure_logging_writes_error(self):
        """Test configure logging writes an error"""
        logger = logging.getLogger("piccolo")
        logger.setLevel(logging.ERROR)
        fh = logging.FileHandler(self.log_file, encoding="utf-8")
        formatter = logging.Formatter("%(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        # Write a test error
        test_message = "This is a test error"
        logger.error(test_message)

        # Flush and close
        fh.flush()
        fh.close()

        # Check that file was created and contains message
        assert self.log_file.exists()
        content = self.log_file.read_text(encoding="utf-8")
        assert test_message in content
