# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

{The first time I ran the game, all inputs seemed okay. The game created was to show
a number guessing game. The output tells you whether or not your guess is higher or lower
than the actual number. However, during the guessing process, there were issues occuring.

- (1) One of my guesses was '27', which then the output prompted me that the number was "Higher".
  I then set my next guess to '28', to which the outputed prompted me that the number was "Lower."
  This indicates that the output decisions were not accurate.
- (2) Another issue I ran into was restarting the game. After I finished my first round,
  I wanted to continue playing more games. Upon clicking the button, the game would
  not reset even if I tried switching to another level of difficulty, the game would not reset.
- (3) Input numbers are not within bounds. By conducting tests without following instructions,
  I decided to test if an input that is out of bounds from the range would be allowed.
  With an input such as '422', the output given was "Go Higher!". This proves that the
  checking for an input within range was not properly working.}

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

{
For the duration of this project, I utilized GPT-5.3-Codex within Copilot to help create resolutions. I first did my own playthrough of the game and found errors through my experience. I wrote these errors in detail to Copilot's Ask Mode.

The AI suggested creating bounds to the code and error handling that would fix the bugs and issues I was facing. For instance, one of the bugs I ran into was the game was letting inputs that were out-of-range be taken and still giving wrongful hints. The AI suggested adding a check after parsing the numbers and have inputs within scope of the difficulty. I verified the results by impelmenting them and running another playthrough to make sure the fixes were done appropriately.

Additionally, there were cases where the AI was misleading. Although the code and logic was correct, doing another playthrough showcased an experience that still needed work. While AI can handle the error, it lacks in also compensating for the user experience -- especially for something like a game.

I treated the AI as a teammate who has another pair of eyes for me. It was able to identify errors in the logic and I was able to test the outcome and make sure everything runs smoothly. It was a thinker that brought out the issues and created quick fixes.
}

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

{
In order for me to decide whether a bug was really fixed, I ran multiple playthroughs that would help me determine if the logic was correct. After the fixes were implemented, I was able to see through different test cases that the code was now running as inteded. The AI was able to to run me through the logic and help me understand what the code is doing in the background as I run my test such as helping me understand the behavior when I try to restart a game or run inputs that were out-of-range.
}

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

{
When Streamlit "reruns" it essentially runs the entire script all over again from top to bottom. For instance, every time you interact with the app such as clicking a button, the entire script runs again to execute this (rerun). Session state allows the program to store values are refer back to them during the rerun. Then, the data can be persisten to the current user.
}

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

{
One strategy that this project has taught me is using the Ask Mode first before using the Agent. This allows me to actually understand my error rather than just having it fixed right away. Not only does this allow me to learn, but lets me debug on my own as well if the AI gets it's corrections wrong in Agent mode. One thing I would do diffrently next time is to ask the AI to give me a run down of the code on it's own before I introduce my issues. That way, I can confirm with the AI about my findings and also see the thought process behind how the code works logically in case there is no coding error but a methodical error instead. This project changed the way I think about how AI generates code by learning how useful context is from my perspective. It allows the AI to develop a more curated and accurate code to satisfy my needs.
}
