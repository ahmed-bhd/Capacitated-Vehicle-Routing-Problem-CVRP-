# Data Dictionary & Sources

| Field | Type | Description | Source |
|-------|------|-------------|--------|
| `lat` | Float | Latitude coordinate | OSM / GPS |
| `lon` | Float | Longitude coordinate | OSM / GPS |
| `demand` | Int | Item count/kg per stop | WMS/OMS |
| `capacity`| Int | Max load capacity | Fleet Specs |

All distances are calculated using the [OSRM API](https://project-osrm.org/).