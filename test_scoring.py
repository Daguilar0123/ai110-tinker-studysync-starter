"""
Tinker 1B, Part 1: write an assert-based pytest test for session_rating()
BEFORE you touch anything else. One test is started for you -- add at least
one more.
"""

import pytest

from scoring import session_rating


def test_session_rating_boundary_90_is_great():
    assert session_rating(90) == "Great"

def test_session_rating_boundary_60_is_meh():
    assert session_rating(60) == "Meh"

def test_session_rating_rejects_negative_score():
    with pytest.raises(ValueError):
        session_rating(-10)

def test_session_rating_rejects_score_over_100():
    with pytest.raises(ValueError):
        session_rating(120)

def test_session_rating_rejects_decimal_score():
    with pytest.raises(TypeError):
        session_rating(2.3)
