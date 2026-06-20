# Capacitated-Vehicle-Routing-Problem-CVRP-


# German-CVRP-Optimizer

A specialized logistics optimization tool designed to solve the **Capacitated Vehicle Routing Problem (CVRP)** for major German cities. This tool helps businesses minimize travel distance and optimize fleet utilization by calculating the most efficient routes between a central depot and various delivery locations.

---

### 1. Introduction

The Capacitated Vehicle Routing Problem (CVRP) is a classic optimization challenge where the goal is to service a set of customers with a fleet of vehicles of limited capacity. This project automates this process for German logistics scenarios, enabling users to generate routes that respect both geographic reality and capacity constraints.

### 2. Technologies Used

* **Language:** Python 3.x
* **Solver Engine:** Google OR-Tools (Routing library)
* **Visualization:** Folium (for interactive Leaflet.js maps)
* **Data Handling:** Pandas & NumPy
* **CLI Interface:** Click (for a user-friendly command-line experience)
* **Distance Calculation:** Haversine formula (with support for OSRM integration)

### 3. Features

* **Automated Route Optimization:** Solves CVRP using OR-Tools to minimize total travel distance.
* **Interactive Visualization:** Generates a browser-based, color-coded map (`route_map.html`) to visualize vehicle paths.
* **Fleet Analytics:** Provides a summary report on fleet utilization, average load, and total distance.
* **Extensible Data Generation:** Includes a dynamic script to generate custom city datasets across Germany.

### 4. The Process of Solution

The solution follows a structured pipeline to convert raw location data into actionable routes:

1. **Data Preparation:** Loads latitude, longitude, and demand data.
2. **Distance Matrix Building:** Computes the distance between all pairs of nodes.
3. **Optimization:** The OR-Tools solver assigns routes by balancing the distance cost against vehicle capacity constraints.
4. **Extraction:** Decodes the solver's internal indexes back into human-readable routes.
5. **Visualization:** Renders the solution as an interactive map and terminal report.

### 5. What I Learned

* **Constraint Programming:** Gained deep insights into how OR-Tools handles complex constraints like vehicle capacity and depot return rules.
* **Geospatial Logic:** Learned to handle geographic data and the distinction between "as-the-crow-flies" distances versus real-world road-network distances.
* **Project Architecture:** Developed a clean, modular structure that separates logic (solvers) from presentation (visualization) and data management.

### 6. How It Could Be Improved

* **OSRM Integration:** Setup a local OSRM (Open Source Routing Machine) server to move from Haversine distances to real-road distances.
* **Time Windows:** Add "Time Window" constraints to ensure deliveries happen within specific hours.
* **Dynamic Capacity:** Allow the solver to pick the optimal number of vehicles required for a specific demand, rather than setting it manually.

### 7. How to Run the Project

1. **Install dependencies:**
```bash
pip install -r requirements.txt

```


2. **Generate the location data:**
```bash
python src/cvrp/data/generate_sample.py

```


3. **Run the solver:**
```bash
python -m cvrp.cli

```


4. **View results:** Open `output/route_map.html` in any web browser.

### 8. Project Structure

```text
CVRP/
├── src/
│   ├── cvrp/
│   │   ├── data/              # Input CSV files
│   │   ├── distance/          # Matrix building logic
│   │   ├── routing/           # Solver & statistics logic
│   │   └── visualization/     # Map generation
│   └── cli.py                 # Main entry point
├── output/                    # Generated maps and reports
└── README.md

```
