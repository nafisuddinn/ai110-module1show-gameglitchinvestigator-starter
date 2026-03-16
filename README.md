# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

{
The purpose of the game is create a number guessing game with a hint and scoring system.
Across my playthrough of the game, I was able to identify three bugs that made the game's
mechanics unplayable. One bug that I found was the wrongful comparisons of numbers. When an input of '27' was given, the output would be to "Go Higher!", but an input of '28' would prompt the user to "Go Lower!" As the correct number isn't a float, this output decision was not accurate. Another bug I found was the inability to restart the game. Upon completing one game, the logic behind restarting did not allow another game to start. This bug spread across all the difficulties, making it a difficulty in itself to play. Lastly, input numbers were not defined within the scope of the rules. The game calls for guesses between 1-100, however, when numbers above this range or below were inputted, the output would give inaccurate judgements.

To help debug the program, I utilized the GPT-5.3-Codex model within Copilot to identify the root source of the problems and create solutions for them. In separate chats, I introduced each bug in the Ask Model. This allowed me to consult with the AI to pinpoint exactly where the code as pushing wrongful outputs. I was able to identify the causes and also have a proposed plan by the AI on how to debug the code. After each consideration, I updated the codebase with # FIXME comments to mark where the appropriate fixes should be mandated. Then, with the Agent Mode, I guided the AI on how to approach the solution and create a fix that would improve the game and take out the bugs while preserving a user experience.
}

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
      ![Screenshot of winning game](../Screenshot%202026-03-15%20at%2011.35.05%E2%80%AFPM.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
