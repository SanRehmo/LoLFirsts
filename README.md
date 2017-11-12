# LoLFirsts

This is a classifier we wrote for the Predicitve Data Analysis Hackathon in Hannover, 11.11.2017. The goal was to extract something useful from a League of Legends dataset. 

We trained a Binary Decision Tree on the big "firsts" of each match:

* firstBlood
* firstTower
* firstInhibitor
* firstBaron
* firstDragon
* firstRiftHerald

Using these, we predict if a team will win the match. The classifier gets to around 87% accuracy on our test split. If we take out the Inhibitor, which appears late into the game, we still get over 70%. Still enough to justify rage quitting, I'd say.