# Monty Hall
**Simulation of the Monty Hall Problem**

**Introduction**</br>
The Monte Hall problem, a brain teaser question, is loosely based on the American television game show Let's Make a Deal and named after its original host, Monty Hall.
</br>(Source: Wikipedia)

**The Monte Hall Problem**</br>
Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?</br>
(Source: Wikipedia)

**Hypothesis**</br>
A simple solution proposed by Vos Savant saying that your chances of winning the car is 0.67 or 2/3 if you switch, while it is 0.33 or 1/3 if you stick to your initial choice. Also, it is not fifty-fifty.</br>
Say if you initially pick door 1:

| Behind door 1 | Behind door 2 | Behind door 3 | Result if staying at door 1 |	Result if switching to the door offered |
| ------------- | ------------- | --------------| --------------------------- | --------------------------------------- |
| Car           | Goat          | Goat          | Wins car                    | Wins goat                               |
| Goat          | Car           | Goat          | Wins goat                   | Wins car                                |
| Goat          | Goat          | Car           | Wins goat                   | Wins car                                |

(Source: Wikipedia)

**Simulation**</br>
The code montyhall.py simulates the real-time event at the game show, and calculate the chances or probability of the guest winning the car if he/she switch or stick to the initial choice.

**Result**</br>
No switch after door opened: 33 wins over 100 times</br>
Probability = 0.33</br>
Switch after door opened: 67 wins over 100 times</br>
Probability = 0.67</br>
Random guess after door opened: 54 wins over 100 times</br>
Probability = 0.54

**Conclusion**</br>
The result is obvious that if you switch, your chances of winning the car is close to 2/3, while it is close to 1/3 if you don't.
If make a random guess between the two unopened doors, your chances of winning the car is 0.5.
So you know what to do next time if you happen to be invited to the game show.
