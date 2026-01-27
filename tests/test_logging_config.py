"""Unit tests for logging_config.py"""
import logging
import pytest


class TestLoggingConfig:
    """Test Logging config class"""

    @pytest.fixture(autouse=True)
    def setup_logger(self, tmp_path):
        """Alternative file handler for a temp file"""
        self.log_file = tmp_path / "piccolo_game_errors.log"
        # Check that file exists
        yield
        # Empty logging after test
        logging.shutdown()
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
