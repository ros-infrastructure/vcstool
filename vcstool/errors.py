"""Custom exceptions for the vcstool package."""
import sys


class VcsToolError(Exception):
    """Base exception for vcstool-specific errors."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class UnsupportedPythonVersionError(VcsToolError):
    """Raised when the Python version is too old for vcstool."""

    def __init__(self, min_version: str = "3.7"):
        current_version = f"{sys.version_info.major}.{sys.version_info.minor}"
        message = (
            f"Unsupported Python version ({current_version}). "
            f"vcstool requires Python {min_version} or higher."
        )
        super().__init__(message)
