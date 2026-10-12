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
