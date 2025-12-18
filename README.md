# Reinforcement Learning Snake AI

This project implements an **autonomous Snake game agent** using **Deep Reinforcement Learning**.  
The agent learns to play the game by interacting with the environment and improving its decisions over time using a **Deep Q-Network (DQN)**.

---

## Project Goal

Build an AI agent that can:
- Play Snake without human input
- Improve performance over time
- Maximize score by learning optimal movement strategies
- Avoid collisions and survive longer

---

## Core Concepts Used

- Reinforcement Learning
- Deep Q-Learning
- State Representation
- Action Selection
- Reward Engineering
- Exploration vs Exploitation
- Experience Replay
- Neural Network Function Approximation

---

## State Representation

The agent observes the environment using a structured state vector that includes:
- Immediate danger in all directions
- Current movement direction
- Relative position of food

This compact representation allows efficient learning and faster convergence.

---

## Action Space

The agent can perform one of the following actions at each step:
- Move Straight
- Turn Left
- Turn Right

Actions are encoded using one-hot vectors for compatibility with neural network outputs.

---

## Reward System

The reward mechanism guides the learning process:
- Positive reward for eating food
- Negative reward for collisions
- Neutral reward for valid movement

This encourages safe navigation and goal-oriented behavior.

---

## Exploration Strategy

The agent uses an **epsilon-greedy strategy**:
- Random actions are taken during early training
- Gradual shift towards model-predicted actions
- Ensures proper environment exploration and prevents premature convergence

---

## Neural Network Model

- Fully connected feedforward network
- ReLU activation functions
- Output layer predicts action values
- Trained using gradient-based optimization

Framework used: **PyTorch**

---

## Training Pipeline

- Continuous interaction with environment
- Online training after every step
- Experience replay buffer for stability
- Environment reset on terminal states

---

## Technology Stack

- Python
- PyTorch
- NumPy
- Pygame


