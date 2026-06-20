# Mathematical Formulation

The project implements a three-index vehicle flow model. 

## Decision Variables
- \( x_{ijv} \in \{0, 1\} \): Binary variable, 1 if vehicle \(v\) traverses arc \((i, j)\).

## Objective Function
Minimize total distance: 
$$\min \sum_{v \in V} \sum_{i \in N} \sum_{j \in N} c_{ij} x_{ijv}$$

## Subtour Elimination
We utilize the Miller-Tucker-Zemlin (MTZ) formulation to ensure connectivity and capacity tracking.