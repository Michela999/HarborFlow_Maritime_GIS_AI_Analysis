# Phase 0 – Initial Setup & GIS Base Layers

**Date:** 2026-01-17

## Overview
Phase 0 focuses on initializing the HarborFlow project environment, defining the repository structure, and preparing the base GIS layers required for subsequent maritime spatial analysis.

This phase establishes the spatial foundation on which AIS, weather, and maintenance data will later be integrated.

---

## Repository & Environment Setup

- Git repository structure finalized
- Data folders (`raw`, `cleaned`, `processed`) created and tracked using `.gitkeep`
- ArcGIS Pro project initialized
- Project geodatabase created for spatial operations

---

## Base GIS Layers (Phase 0)

The following **Natural Earth 10m resolution shapefiles** were loaded into ArcGIS Pro as base layers:

- `ne_10m_ports.shp`
- `ne_10m_coastline.shp`
- `ne_10m_land_scale_rank.shp`

**Source:** Natural Earth – Quick Start Dataset  
**Scale:** 1:10m  
**Geometry types:** Point (Ports), Line (Coastline), Polygon (Land)

These layers provide:
- Global port reference points
- High-resolution coastline geometry
- Landmass polygons for spatial context and masking

---

## GIS Operations Performed

- Shapefiles imported into the ArcGIS Pro project
- Coordinate reference systems verified
- Layer visibility and ordering configured
- Initial symbology applied for visual clarity
- Attribute tables inspected for structure and consistency

No editing or feature modification was performed during this phase.

---

## Outputs

- ArcGIS Pro map with base layers successfully loaded
- Screenshots documenting setup and layer inspection

**Screenshots location:**  
`docs/screens/phase0/`

---

## Notes

- The ArcGIS Pro project file (`.aprx`) is intentionally **not versioned** in this repository due to file size and platform-specific locks.
- The project file can be shared via cloud storage (OneDrive / Google Drive) upon request.
- Phase 0 is complete and serves as the spatial baseline for all subsequent phases.
