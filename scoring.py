from scoring_helpers import apply_streak_bonus
"""
StudySync -- Session Scorer (Ticket 1, Tinker 1B).

TICKET: apply_streak_bonus() works but shouldn't live here -- it belongs in
the shared scoring_helpers module. session_rating() has no test coverage,
and neither function has been checked against bad input.

1. Write a pytest test for session_rating() BEFORE touching anything broken.
2. Move apply_streak_bonus() into scoring_helpers.py and fix the import here.
3. Find 2-3 "breaker" inputs for session_rating() and decide if they need handling.
"""


def session_rating(combined_score: int) -> str:
    """Rate a study session from its combined minutes+focus score (0-100)."""
    if not isinstance(combined_score, int):
        raise TypeError(f"combined_score must be an int, got {type(combined_score).__name__}")
    if not 0 <= combined_score <= 100:
        raise ValueError(f"combined_score must be between 0 and 100, got {combined_score}")
    if combined_score >= 90:
        return "Great"
    if combined_score >= 80:
        return "Good"
    if combined_score >= 70:
        return "OK"
    if combined_score >= 60:
        return "Meh"
    return "Skip"

def render_session_scorer_tab():
    import streamlit as st

    st.subheader("Score a Session")
    minutes = st.slider("Minutes studied", 0, 60, 30)
    focus = st.slider("Focus (0-60)", 0, 60, 30)
    streak = st.number_input("Current streak (days)", min_value=0, value=0, step=1)

    combined = minutes + focus
    boosted = apply_streak_bonus(combined, streak)
    rating = session_rating(boosted)
    st.metric("Rating", rating, help=f"Combined {combined} -> boosted {boosted}")


def run_demo():
    sessions = [-10, 120, 2.3, 55, 68, 82, 91, 77]
    streak = 3
    for raw in sessions:
        boosted = apply_streak_bonus(raw, streak)
        try:
            rating = session_rating(boosted)
        except (TypeError, ValueError) as exc:
            print(f"Raw: {raw} -> Boosted: {boosted} -> Rejected: {exc}")
            continue
        print(f"Raw: {raw} -> Boosted: {boosted} -> Rating: {rating}")


if __name__ == "__main__":
    run_demo()
