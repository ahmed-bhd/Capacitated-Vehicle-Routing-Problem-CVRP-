# Problem Definition

The Capacitated Vehicle Routing Problem (CVRP) is the core of this project. 
- **Objective:** Minimize the total fleet travel distance.
- **Key Constraints:** - Each customer must be visited exactly once.
  - Total vehicle load must not exceed capacity `Q`.
  - All routes must start and end at the depot.
- **Assumptions:** Single depot, deterministic customer demands, and static travel costs derived from OSRM.