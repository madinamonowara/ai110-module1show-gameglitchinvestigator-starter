# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, the feedback system was incorrect and confusing. The hint logic didn’t match my guesses, and it always told me to “go lower” no matter what number I entered. The game also didn’t properly reset between rounds, which broke the flow completely. Overall, the state management felt inconsistent and unreliable.

Bugs I noticed
- hint logic always says “go lower”; even for very low guesses (like 1)
- new game didn’t reset input or attempts correctly
- attempts count was incorrect (8 instead of 7)
- Game sometimes stopped accepting input unless refreshed
- Game ended early with attempts still remaining

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | |
| | | | |
| | | | |

1. First Try
   - Input: Multiple guesses (including 1)
   - Expected: if the guess is too high or too low.
   - Actual: Every guess was told to "go lower," even when I entered 1. The correct answer was 96.
   - Console Output/Error: none

2. Second Try
   - Input: "New Game"
   - Expected: input field should clear and the game should reset to 7 attempts.
   - Actual: The input field kept the previous number, the game gave 8 attempts instead of 7, and it stopped accepting guesses until I refreshed the page.
   - Console Output/Error: none

3. Third Try
   - Input: Multiple guesses 
   - Expected: hints and tries being read correctly. 
   - Actual: The hints seemed random and unhelpful. The game ended even though there was still 1 attempt remaining.
   - Console Output/Error: None

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project? ChatGPT and mostly Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result): 
      The hint logic is backwards in apps.py. In the `check_guess()` function, when a guess is higher than the secret number, the game correctly labels it as "Too High" but displays the message "Go HIGHER!" instead of telling the player to go lower. When a guess is lower than the secret number, the game displays "Go LOWER!" instead of "Go HIGHER." This is why the hints are so misleading. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result):
      brought up the scoring more than once. didn't implement; ignored that suggestion.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? 
      Testing it myself.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
      Recreated the exact steps I did the first 3 times I played this game and noted if I experienced those bugs again.

- Did AI help you design or understand any tests? How?
    Yes, it did. Helped me write regression tests to make sure the "go lower" and "too high" hints were working correctly.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    Reruns are the word that describes how Streamlit runs the entire script from top to bottom every time you make a change. Compare this to when coding something front-end related: if you change a button's look, then only that button is affected. However, because the entire script is run from top to bottom each time, memory of the output of each rerun also resets. That's why session_state is so helpful, it's where you put the things you want remembered, no matter how many times the script is run.  

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
    This could be a testing habit, a prompting strategy, or a way you used Git.
    In future labs, I'll continue to enforce that I only want to focus on a specific bug and keep sessions smaller and contained.

- What is one thing you would do differently next time you work with AI on a coding task?
    Start with even more context.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
    As long as you're overseeing what kind of changes its making and making sure its not making any assuptins you dont agree with, its a very helpful tool.
