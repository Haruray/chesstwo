# Chess Two
Creating basic mechanic of a modified chess. Inspired by Heroes Might and Magic. For learning purpose.
For real, this is just for learning.

Creating basic mechanic like pawn movement, input validation, and random generator for attack/defense. This project also my first use OOP in python.

## Vanilla Version
Each player choose between 3 classes: Gladiator, Guardian, and Ninja. Gladiator has higher chance to kill enemies, Guardian has higher chance of defending themself, and Ninja can move 2 blocks at a time. This version has bot with 3 difficulty available : Easy, Normal, and Unfair.
## Battle Tendency Version
Each player now have pawns with different class: Gladiator, Defender, and Ninja (note: in this version, Defender is alternate name of Guardian). 
* Gladiator has higher chance to kill enemies, and if a Gladiator kills an enemy, he will enter "Berserk" mode for one next turn.
* Defender has higher chance of surviving from enemy attacks and also higher chance to perform counter-attack. If a Defender holding ground, then his defense and counter attack chance will be increased (max 5 turns).
* Ninja can move 2 blocks at a time and also it can't be counter-attacked.

This version has bot with 2 difficulty available : Easy and Normal.

### How to play
Choose which version to play, and run "main_program.py"

### Upcoming updates
* New difficulty on both version : hard, and adding "unfair" difficulty to battle tendency version.
* Unfair difficulty fix to make it better.
* Pawns limit increase (from 10 to 12).
* Random drops to increase attack/defense/counter-attack chance.
* New pawn class : Saint. More info later.
* New game mode : King's Bounty. More info later.
