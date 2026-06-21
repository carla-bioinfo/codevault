"""Tests for codevault package initialization and version."""

from codevault import __version__, __author__, __email__


def test_version_is_string():
    """Test that __version__ is a string."""
    assert isinstance(__version__, str)


def test_version_matches_expected():
    """Test that __version__ matches project version."""
    assert __version__ == "0.1.0-alpha1"


def test_author_is_set():
    """Test that __author__ is defined."""
    assert __author__ == "Carla Rodrigues"


def test_email_is_set():
    """Test that __email__ is defined."""
    assert __email__ == "carlabio.biomol@gmail.com"
