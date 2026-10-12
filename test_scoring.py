"""
Tinker 1B, Part 1: write an assert-based pytest test for session_rating()
BEFORE you touch anything else. One test is started for you -- add at least
one more.
"""

from scoring import session_rating


def test_session_rating_boundary_90_is_great():
    assert session_rating(90) == "Great"

def test_session_rating_boundary_85_is_good():
    assert session_rating(85) == "Good"

def test_session_rating_boundary_72_is_OK():
    assert session_rating(72) == "OK"

def test_session_rating_boundary_63_is_meh():
    assert session_rating(63) == "Meh"

def test_session_rating_boundary_59_is_skip():
    assert session_rating(59) == "Skip"