# Feedback Log

## Joss Raine, 07/08/2025

### Feedback 1. Ethical Issue

The project requires the user to install third party packages without acknowledging any potential security risks, or detailing how and why they are used in the project.

*Actions*:
- REQUIREMENT_README.md : updated clarity by adding more info on each libary used and any ethical concerns with any external libaries (colorama)
- Added system requirements

### Feedback 2

Installation documentation references external system requirements, but does not include them directly.

Depencies documentation does not account for any future usability of this project, as the version of packages being included is not mentioned or controlled through listed steps.

*Actions*:
- REQUIREMENT_README.md: Added system requirements
- INSTALLATION_README.md: Added step for installation of dependencies

### Feedback 3. Readability

I might be unfamiliar with how the Monte Carlo Tree search functions, but to me it was a little difficult to understand how exactly it makes decisions. There is also no explanation on the different difficulties of AI that are included in the project and how this affects gameplay and fairness.

*Actions*:
- REQUIREMENT_README.md: Improved the general readablity
- README.md:
  - Rewrote the entirety of Monte carlo description to make it much more understandable and simple (hopefully)
  - Added an explination of each of the Monte Carlo agent diffrent difficulties 
  - Adding very basic images to help with this
  - Actually added explaination on why the Agent decides the node it plays


## Cat Brandt, 08/08/2025

### Feedback 1. Ethical Focus Ethical Focus- Transparency

Principle 1.5 of ACM's Code of Ethics 'Respect the work required to produce new ideas, inventions, creative works, and computing artifacts' states computing professionals should credit the creators or ideas. Since Monte Carlo agents leverage Monte Carlo methods, such as the tree search you explain in detail in your readme.md, you could potentially mention the creator/s of this method to cover this ethical issue.

*Actions*:
- README.md: Added ethics to the AI section (Credit to the original algorithm inspirations)

### Feedback 2. Industry Relevant - Fairness
  I might have just missed this, but it could be an idea to include a brief explanation of how to play the game and the main objective (how to win). This is a widely known game, but not all users may be familiar with the rules. Adding a description or in-game visual example would be a great use of user-centred design (Human-centred Values Principle)

*Actions*:
- README.md: Add "How to Play" section with visual description of the game to give more visual instruction

### Feedback 3. Ethical Focus - Human-Centred Values
  Utilising the Monte Carlo agent is a great way for players to experiment with game strategies and an opportunity for learning, as the user observes and reacts to how the AI 'thinks'. It is great that you have provided three difficulty levels that range from beginner to advanced play, however I think further explanation of the three difficulty levels could make the distinction clearer to the user (e.g. what the numbers against each level represent - "Normal AI: 250").


*Actions*:
- GENERAL_README.md: Added clarity to difficulty levels (ie 250 means 250 simulations of the agent)

## External review from friend, 09/08/2025
### Feedback 1. 
Play - What are the minimal amount of instructions the player needs to understand the concept
 
While other information can be useful depending on each individual users need, specifications and knowledge of inner workings is unnecessary.
Instead of having extra information most users won't need in teh main readme, the extra knowledge should be attached to the end of the README pointing to other relevant files with that extra information.

*Actions:*
- Create a seperate markdown file (MONTE_CARLO_EXPLANATION.md) for explanation of Monte Carlo agent
- README.md: Add a reference to this file in Extra Information section

### Feedback 2.
In REQUIREMENT_README.md, the current order of the documentation is confusing and mixed. There are mentions of how to run the program before instructions on how to install the required dependancies.

*Actions:*
- REQUIREMENT_README.md: Remove "How to Run" section, as this was already mentioned in INSTALLATION_README.md, to eliminate the confusion

## Max Acosta, 09/08/2025
### Feedback 1. Privacy & Data Handling
Add a clear Privacy Statement that emphasizes that no personal information is collected, stored, or shared. No network calls are made, and AI decisions are made locally without user profiling. This aligns with the Australian Privacy Principles.

*Action:*

  - Add Privacy Statement in README.md

### Feedback 2. Code Comments and Docstrings:

Docstrings that explains what the ‘player’ class represents and what the methods do, missing in the “player.py” file.

*Actions:*
- player.py:
 Add doctrings to explain what 'player' class does on top of the class