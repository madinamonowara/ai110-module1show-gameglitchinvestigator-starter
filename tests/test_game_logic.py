#FIX:Tuple-unpacking fixes and regression tests added using Claude
from logic_utils import check_guess


def test_winning_guess():
    # check_guess returns (outcome, message)
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# FIX: Regression tests for the hint-direction bug: outcome alone wasn't broken,
# the message direction was, so these assert on the direction.

def test_too_high_hint_tells_you_to_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()


def test_too_low_hint_tells_you_to_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()