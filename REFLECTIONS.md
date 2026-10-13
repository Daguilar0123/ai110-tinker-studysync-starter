# Tinker 1B: Split the Logic

## Part 1: Test First

📍 **Checkpoint:** Why test a function that already works?

I am not sure why you would test a function that already works, other than not being completely sure that it actually does work in all cases. In that case (no pun intended), it is important to test a working function for edge cases, or cases that are on the periphery. The uncommon cases. The things that don't always or typically occur, but they do occur once in a while nonetheless. Rather than have your app crash with no explanation, testing helps preempt that.

## Part 2: Split It

📍 **Checkpoint:** What would break if the import in scoring.py pointed to the wrong file?

    boosted = apply_streak_bonus(combined, streak)

First, if it pointed at an invalid file, there would be an immediate error alerting us to the fact that the file does not exist. If it pointed to an existing file but not the correct file, it would appear as if everything was fine. Nothing would change on the surface, until `apply_streak_bonus` were called. `apply_streak_bonus` appears in `render_session_scorer_tab()`. It is the function that returns the value for the variable called `boosted`. So depending on which file the `import` in `scoring.py` pointed to, the main change would be the value of `boosted`. As a result, `boosted` would change the value of `session_score` and `rating` themselves.

## Part 3: Break It on Purpose

```
Decide: real bug, or an input the function was never meant to receive? Either answer is fine — the point is deciding on purpose.
```

📍 **Checkpoint:** You have 2-3 breaker inputs, each with a one-line decision: fix it, or flag it out of scope.

```
(ai110-tinker-studysync-starter) danielaguilar@Mac-mini ai110-tinker-studysync-starter % python -c '
from scoring import session_rating
for x in [-5, 150, 87.5]:
    try:
        print(f"session_rating({x!r}) -> {session_rating(x)!r}")
    except Exception as e:
        print(f"session_rating({x!r}) raised {type(e).__name__}: {e}")
'

session_rating(-5) -> 'Skip'
session_rating(150) -> 'Great'
session_rating(87.5) -> 'Good'
(ai110-tinker-studysync-starter) danielaguilar@Mac-mini ai110-tinker-studysync-starter % 
```

OR

```
(ai110-tinker-studysync-starter) danielaguilar@Mac-mini ai110-tinker-studysync-starter % python
Python 3.13.13 (main, May 10 2026, 19:20:37) [Clang 22.1.3 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Cmd click to launch VS Code Native REPL (https://aka.ms/python-native-repl)
>>> from scoring import session_rating
>>> session_rating(-5)
'Skip'
>>> session_rating(150)
'Great'
>>> session_rating(87.5)
'Good'
>>> 
```

The point is that these inputs mistakenly ran and gave output that seems correct, when in fact the output is incorrect. In my opinion, giving false answers confidently is worse than giving false answers obviously. That means this is more problematic than the program just crashing, because not only is it wrong, but it presents as if it is correct.

It's input the function was never meant to receive, but it is not a bug because the program works just fine in the sense that it runs with no errors.

**Which breaker input surprised you most, and why?**

I was most surprised by all of the inputs not being bugs, but once I traced the flow of information, from the user input via the sliders to the path those inputs took to get to the `session_rating(...)` function, it became clear why this was the case.


# Tinker 2B: Wire it Up
## Part 1: 
📍Checkpoint: The broken counter still resets. The fixed counter climbs with each click.Explain the difference in one sentence using "rerun."
Before you move on, answer: In your own words, what does "rerun" mean here? Then tighten it into one sentence.

Rerun is Streamlit running the whole script from top to bottom each time, so the broken counter's count = 0 executes on every rerun, while the fixed counter's fixed_count = 0 executes only when the key is missing from session state, which happens once per session on the first load only.

## Part 2: Validate before you store
📍 Checkpoint: An empty subject or a zero/negative duration shows an error and adds nothing. A valid session still adds correctly.
Before you move on, have one navigator answer:
What's one input a user might type that you haven't tested yet?
non-alphanumeric symbols, all numbers no alphas. These get accepted with no error, despite being nonsensical.

## Part 3: Plain Class vs. Dataclass
📍Checkpoint: SessionDC works, its output matches PlainSession's, and you can name one thing @dataclass generated for you.
```
@dataclass
class SessionDC:
    subject: str
    minutes: int
    priority: str = "medium"

From those lines, @dataclass generates:

- __init__, which takes subject, minutes, and priority="medium", the same signature as PlainSession.__init__.
- __repr__, which prints the class name and each field. Running both classes with the same values printed the same text, so the output matches.
- __eq__, which compares fields. Two SessionDC objects with the same values are equal. PlainSession has no __eq__, so two with the same values are not equal.
```
What did @dataclass generate that you didn't write yourself?
As described above, @dataclass generates the constructor, the __repr__ and the __eq__ methods, which are responsible for initializing the class instance, printing the class instance fields, and comparing those fields. This is seen by the fact that SessionDC even prints at all, let alone prints identically to PlainSession.

## Part 4: Recurrence and Conflicts
📍Checkpoint: next_occurrence is correct for both frequencies. find_conflicts flags the duplicate slot and handles an empty list safely — try the "Check for time conflicts" button in the Session Log tab to see it wired into the app.

Before you move on, answer: Why does find_conflicts need to handle an empty list without crashing? Then name a real scenario where that matters.

An empty list is a normal input, not an edge case, because it's what the function receives whenever no sessions have been logged or no clashes exist, so a crash there would be a common failure. The loops never index into the list, so an empty input simply runs zero iterations and returns the empty result, but code that indexed directly (such as sessions[0]) would raise an IndexError on this same input.