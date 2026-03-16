from pathlib import Path
import sys

# Ensure tests can import modules from the project root regardless of pytest CWD.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # Updated: check_guess now returns (outcome, message), so assert the outcome.
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # Updated: assert outcome from tuple return contract.
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # Updated: assert outcome from tuple return contract.
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_guess_comparison_uses_numeric_values_not_string_ordering():
    # Regression check for number guessing fix: avoid lexicographic string comparison.
    outcome, _ = check_guess("9", "10")
    assert outcome == "Too Low"


def test_parse_guess_rejects_non_numeric_input():
    # Regression check for input validation fix: non-numeric values should fail cleanly.
    ok, guess_int, error = parse_guess("abc")
    assert ok is False
    assert guess_int is None
    assert error == "That is not a number."


def test_restart_fix_clears_guess_input_key_in_app_code():
    # Regression guard for the restart fix: input must be cleared on new game.
    app_py = Path(__file__).resolve().parents[1] / "app.py"
    source = app_py.read_text(encoding="utf-8")
    assert 'st.session_state[f"guess_input_{difficulty}"] = ""' in source
