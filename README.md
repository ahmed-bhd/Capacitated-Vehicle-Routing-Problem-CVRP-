
```markdown
# CVRP Optimization Project

A professional-grade **Capacitated Vehicle Routing Problem (CVRP)** solver designed for logistics and supply chain management. 

This tool uses real-world road network data via OSRM to provide accurate, actionable routing plans that minimize fleet operational costs.

## Features
- **Real-World Routing:** Utilizes OSRM for accurate distance and time matrices.
- **Advanced Optimization:** Powered by Google OR-Tools with metaheuristic search (Guided Local Search).
- **Logistics Extensions:** Supports heterogeneous fleets, route duration limits, and custom start/end points.
- **Visualization:** Generates interactive Folium maps to display optimized routes.
- **Extensible:** Configurable via YAML files for different logistics scenarios.

## Quick Start
1. **Clone the repository.**
2. **Install dependencies:**
   ```bash
   make install

```

3. **Configure the solver:** Edit `config/base.yaml` to define your depot, customer demands, and fleet size.
4. **Run the optimization:**
```bash
cvrp-solve --config config/base.yaml

```



## Documentation

See the `docs/` folder for a detailed breakdown of the mathematical model, problem constraints, and data specifications.
