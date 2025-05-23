---
layout: page
title: "Bang!: The Dice Game"
description: Object Oriented Programming Course @ TTU
img: assets/img/research/academic/oop_thumbnail.png
importance: 7
category: classes
giscus_comments: true
toc:
  sidebar: left
---


This [project repository](https://github.com/shanto268/BangTheDiceGame) is for an OOP project that we had for our OOP course. We had to recreate a GUI Bang! the Dice Game using JAVA. This repository contains our attempt.

**Rules:** [Game rules](http://www.dvgiochi.net/bang_the_dice_game/BANG!_dice_game-rules.pdf)

## Current Status
The program allows the user to play the game on the command line against the AI.

## Assignments

Meghan Engert: UML Use Case Diagrams, UML Class Diagrams, CRC Cards, Arrow Pile Class and BangDiceGame class

Cierra Ditmore: Character, Dice,  and Game Functions Classes

**Sadman Ahmed Shanto:** Development of AI logic and gameplay simulation. 

## Project Presentation Slide

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <iframe src="../../assets/img/research/academic/oop_bang.pdf" width="100%" height="600px" class="rounded z-depth-1">
        </iframe>
    </div>
</div>

## Project Presentation Video

<div class="row mt-3">
    <div class="col-sm mt-3">
        {% include video.liquid path="https://www.youtube.com/embed/AS29JGoWais" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

## Gameplay Video

<div class="row mt-3">
    <div class="col-sm mt-3">
        {% include video.liquid path="https://www.youtube.com/embed/NP2MkpuRWxs" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

### AI logic

<div class="row mt-3">
    <div class="col-sm mt-3">
        {% include video.liquid path="https://www.youtube.com/embed/oewrBJD0vEs" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Each AI upon construction is allocated certain behavior parameters that dictate their playing style.

```java
//Behavior defining parameters
private double willingToTrick;
private double Aggressiveness;
private double Safetiness;
private double Niceness;
private double willingToKeepDice;
private double willingToKeepHealth;
private double willingToKeepShots;
private double willingToKeepArrow;
private double willingToKeepGatling;
private double SkepticProbability;
private double Stubbornness;
```
When it is not the AI's turn, it observes the game and records the following in its memory.

* Players who shot sheriff
* Players who gave beers to sheriff

Using, the initial distribution of roles and number of players and such information the AI assigns proabilities for certain roles to each player in the form of a probability vector. 
```java
ArrayList<Double> ProbabilityVector;
```

P Vector has form [P(sheriff), P(renegade), P(outlaw), P(deputy)]
for example if the game started out with 5 players, the P Vector for any given player before. Role is revealed would be as follows:
```java
[1./5, 1./5, 2./5, 1./5]
```
After role information is revealed, e.g. player is sheriff, the vector is updated
```java
[1.0, 0.0, 0.0, 0.0]
```
The probability vector is always stays normalized. In general, depending on a certain player's interaction with the sheriff the AI updates the `ProbabilityVector` by an amount corresponding to its `SkepticProbability` value. this approach encapsulates the skeptic nature of a player and their attentiveness to the events in the gameplay.

When it is the AI's turn, it rolls the 5 dices and keeps each die with a certain willing to keep probability and a payoff matrix that determines the AI's strategy and the effectiveness of a certain dice roll. The number of reroll's is also determined stochastically with some strategy.

To resolve the die, the AI employs the following algorithm.

* based on its role determine target roles (i.e. whether to shoot or help sheriff) 
* based on the probability vector, assign all other players a guessed role (i.e. the role corresponding to the element in the vector with the highest number (always normalized))
* always resolve any arrows first
* see if there is three dynamite's in which case the turn ends and no reroll is allowed
* based on current life points and target roles evaluate whether to keep beer for itself or pass to someone who would help the AI in is objective
* using a similar approach for the bull's eyes 1 and 2
* depending on the number of Gatling adjust the probability of keeping the gatling (i.e. the willingness to keep gatling increases if there is 2 or more gatlings (constrained to 3))

The AI Logic is discussed in greater details in the AILogic.txt file.

## To Do List
- [x] Successful debugging of command line version of the game
- [ ] GUI implementation
- [x] Project Video/Presentation 
- [x] Integration of Expansion Pack

## Active Issues
- [x] Chief arrow handling in AI logic 
- [x] NullPointer Exceptions
- [x] AI playing with negative lifePoints
- [x] AI could keep more than 5 dices in some cases with more than one dynamite rolls

**Note:** All bugs have been taken care of!

# Documentation

## JavaDoc Html File
[javaDoc file](https://github.com/shanto268/BangTheDiceGame/blob/master/BangDiceJavaDoc.html)

## UML Use Case Diagrams
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="https://raw.githubusercontent.com/shanto268/BangTheDiceGame/master/BangClassDiagram.PNG" title="Use Case Diagram" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

## UML Class Diagrams
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="https://raw.githubusercontent.com/shanto268/BangTheDiceGame/master/UML_class_diagrams_2.png" title="Class Diagram 2" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="https://raw.githubusercontent.com/shanto268/BangTheDiceGame/master/UML_class_diagrams_1.png" title="Class Diagram 1" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="https://raw.githubusercontent.com/shanto268/BangTheDiceGame/master/UML_class_diagrams_3.png" title="Class Diagram 3" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="https://raw.githubusercontent.com/shanto268/BangTheDiceGame/master/UML_class_diagrams_4.png" title="Class Diagram 4" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

## CRC Cards
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="https://raw.githubusercontent.com/shanto268/BangTheDiceGame/master/CRC_Cards_1-3_1.png" title="CRC Card 1" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="https://raw.githubusercontent.com/shanto268/BangTheDiceGame/master/CRC_Cards_1-3_2.png" title="CRC Card 2" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="https://raw.githubusercontent.com/shanto268/BangTheDiceGame/master/CRC_Cards_1-3_3.png" title="CRC Card 3" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

## GUI Plan
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="https://raw.githubusercontent.com/shanto268/BangTheDiceGame/master/gui.png" title="GUI Plan" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
