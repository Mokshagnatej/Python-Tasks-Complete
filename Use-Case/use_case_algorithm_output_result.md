# Use Case: Simulating Random Coin Flips and Dice Rolls Using NumPy

## Aim

To design a Python application using NumPy that simulates random coin flips and dice rolls, analyzes the outcomes, and displays the probabilities of each event.

## Algorithm

1. Start the program.
2. Import the required library — numpy.
3. Input the number of simulations (number of flips/rolls).
4. For coin flip simulation:
   - Use `numpy.random.choice(['Heads', 'Tails'], size=n)` to generate random results.
   - Count the occurrences of "Heads" and "Tails".
5. For dice roll simulation:
   - Use `numpy.random.randint(1, 7, size=n)` to simulate dice outcomes (1 to 6).
   - Count the frequency of each face.
6. Display the outcomes and probabilities for both simulations.
7. End the program.

## Sample Output

```
Enter number of simulations: 10

Coin Flip Simulation:
Total Flips: 10
Heads: 6 (60.00%)
Tails: 4 (40.00%)

Dice Roll Simulation:
Total Rolls: 10
Face 1: 1 (10.00%)
Face 2: 3 (30.00%)
Face 3: 2 (20.00%)
Face 4: 1 (10.00%)
Face 5: 2 (20.00%)
Face 6: 1 (10.00%)
```

## Result

The Python application successfully simulates random coin flips and dice rolls using NumPy. It displays the frequency and probability of each possible outcome, demonstrating the concept of randomness and probability distribution effectively.
