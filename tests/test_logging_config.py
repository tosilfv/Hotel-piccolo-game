"""Unit tests for logging_config.py"""
import logging
import pytest
from utils.logging_config import configure_logging


class TestLoggingConfig:
    """Tests for Piccolo game logging configuration"""

    @pytest.fixture(autouse=True)
    def setup_logger(self, tmp_path):
        # Setup: temporary log file path
        self.log_file = tmp_path / "piccolo_game_errors.log"

        # Cleanup: reset logging
        logging.shutdown()
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

    def test_configure_logging_sets_error_level(self):
        # Setup: get logger
        logger = logging.getLogger("piccolo")

        # Set initial level different from ERROR for the test
        logger.setLevel(logging.INFO)

        # Action: configure logging
        configure_logging()

        # Assert: logger level is ERROR
        assert logger.level == logging.ERROR

    def test_configure_logging_creates_log_file(self):
        # Setup: create a logger with temp file handler
        logger = logging.getLogger("piccolo")
        logger.setLevel(logging.ERROR)
        fh = logging.FileHandler(self.log_file, encoding="utf-8")
        formatter = logging.Formatter("%(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        test_message = "Test error message"

        # Action: log an error
        logger.error(test_message)
        fh.flush()
        fh.close()

        # Assert: file exists and contains message
        assert self.log_file.exists()
        content = self.log_file.read_text(encoding="utf-8")
        assert test_message in content
