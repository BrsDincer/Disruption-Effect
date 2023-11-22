# Disruption Effect

## Overview

This project simulates a universe in a 2D grid environment using Python, with the primary focus on understanding the occurrence of anomalies or disruptions over a vast timescale. The simulation is designed to provide insights into how rare events might occur in the universe and their relationship to the density of objects within a simulated space.

## Concepts

### Simulation Hypothesis
The project is partly inspired by the Simulation Hypothesis, which posits that our reality might be a simulated environment created by a more advanced civilization. In this context, the simulation explores the idea of 'anomalies' or 'glitches' as rare but significant events within the universe.

## Perspective

### Understanding Rarity of Events

By setting a probability that reflects rare events over a long timescale, the simulation helps conceptualize how infrequent yet significant events occur in the vast timeline of the universe. It puts into perspective the rarity and impact of certain cosmic phenomena in the grand scheme of things.

### Scale and Human Perception

The simulation underscores the difference between human-scale time (decades to centuries) and cosmic time scales (millions to billions of years). It highlights how events that seem incredibly rare or almost impossible in a human lifetime are more probable over longer durations.

### Simulation Hypothesis Insights

If one were to entertain the Simulation Hypothesis, this approach offers a way to consider how a simulated universe might be programmed. It raises questions about the nature of anomalies or 'glitches' in such a simulation—could rare but significant events in our universe (like quantum anomalies or unexplained cosmic phenomena) be akin to these programmed disruptions?

### Reflecting on Randomness and Determinism

The simulation, with its blend of deterministic rules (the movement of objects) and random disruptions, mirrors philosophical and scientific discussions about determinism and randomness in the universe. It can prompt contemplation about the balance of predictable laws of physics and random or unexplained events in shaping the history of the universe.

### Modeling and Predictive Tools

On a more practical level, this approach demonstrates how modeling and simulations can be used as tools to study complex systems. It shows how adjusting parameters (like error_probability) can significantly change outcomes, reflecting the sensitivity of complex systems to initial conditions and random events.

### Philosophical and Existential Reflection

The idea of life as a simulation, with built-in errors or anomalies, opens up existential and philosophical discussions. It encourages thinking about the nature of reality, our place in the universe, and how much we can truly know or predict about the world around us.

## Density-Dependent Error Probability
The simulation introduces the concept of density-dependent error probability, where the likelihood of anomalies is influenced by the density of objects in the universe. This approach draws from ideas of proportionality and normalization in mathematics, reflecting scenarios where denser areas might have a higher likelihood of experiencing significant events.

## Representation of Time
The simulation also plays with the concept of representing the vast timescale of the universe (13.7 billion years) in a compressed format, correlating it with real-time execution in seconds for practical demonstration purposes.

## Technologies

- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- ![Pygame](https://img.shields.io/badge/Pygame-3776AB?style=for-the-badge&logo=pygame&logoColor=white)
- ![NumPy](https://img.shields.io/badge/NumPy-3776AB?style=for-the-badge&logo=numpy&logoColor=white)

## Features

- **2D Grid Universe**: The universe is represented as a 2D grid, where each cell can either contain an object or be empty.
- **Object Movement**: Basic rules govern the movement and interaction of objects within the grid.
- **Anomaly Simulation**: Anomalies (or disruptions) occur randomly, with their probability being influenced by the current state of the universe.
- **Time Representation**: The simulation runs in real-time but represents the extensive timeline of the universe.

## Mathematical Formulas

### Current Error Probability Calculation

The probability of an error (anomaly) occurring in each iteration is calculated as follows:

Error Probability = min(Number of Occupied Cells/Total Number of Cells × Maximum Error Probability,Maximum Error Probability)

Where:

- Number of Occupied Cells: The count of cells currently containing an object (value = 1).
- Total Number of Cells: The total cells in the grid, calculated as size^2
- Maximum Error Probability: A predefined upper limit to the error probability.

This formula adjusts the error probability in proportion to the object density, with a cap to prevent it from exceeding a realistic threshold.

## How to Run

1. Ensure Python is installed on your system.
2. Install Pygame and NumPy.
3. Run the script to start the simulation.
4. Observe the occurrence of anomalies and their frequency over the simulated period.

## Installation and Running the Simulation
To run the simulation, ensure you have Python, Pygame, and NumPy installed in your environment. Clone the repository and run the main simulation script.

```bash
git clone https://github.com/Memoriae-Technology/Disruption-Effect.git
cd /Disruption-Effect/src
python simulation_base.py
```

## Future Enhancements

- Enhance the complexity of the rules governing object interactions.
- Introduce different types of objects or entities within the universe.
- Implement more sophisticated algorithms for anomaly generation.
