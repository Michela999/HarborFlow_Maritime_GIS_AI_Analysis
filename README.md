\# HarborFlow – Maritime GIS \& AI Analysis



HarborFlow is a \*\*Maritime GIS \& AI project\*\* designed to analyze vessel movements, port activity, weather conditions, and maintenance patterns.  

The project integrates \*\*GIS mapping, Python analytics, SQL, and AI/ML\*\* to deliver operational insights and portfolio-ready outputs for the maritime industry.



---



\## \*\*Project Objectives\*\*



\- Analyze maritime traffic and port activity using \*\*AIS data\*\*

\- Study \*\*weather impacts\*\* on vessel behavior

\- Simulate \*\*vessel maintenance data\*\* for predictive analysis

\- Visualize routes, density, and hotspots using \*\*GIS\*\*

\- Clean, preprocess, and merge datasets using \*\*Python \& SQL\*\*

\- Build foundations for \*\*predictive maintenance and route optimization\*\*

\- Document the full workflow for \*\*GitHub \& portfolio presentation\*\*



---



\## \*\*Repository Structure\*\*



HarborFlow\_Maritime\_GIS\_AI\_Analysis/

│

├─ data/

│ ├─ raw/

│ │ ├─ ais/

│ │ ├─ weather/

│ │ └─ maintenance/

│ ├─ cleaned/

│ └─ processed/

│

├─ docs/

│ └─ screens/

│ ├─ phase0/

│ ├─ phase1/

│ ├─ phase2/

│ ├─ phase3/

│ ├─ phase4/

│ ├─ phase5/

│ ├─ phase6/

│ └─ phase7/

│

├─ maps/ # ArcGIS Pro projects and geodatabases

├─ notebooks/ # Jupyter notebooks (EDA, cleaning, ML)

├─ tableau/ # Tableau dashboards

└─ README.md





---



\## \*\*Tools \& Technologies\*\*



\*\*GIS\*\*

\- ArcGIS Pro

\- Shapefiles \& Geodatabases (.gdb)



\*\*Analytics \& Data\*\*

\- Python (Pandas, NumPy)

\- SQL (SQLite / PostgreSQL)

\- Jupyter Notebooks



\*\*Visualization\*\*

\- Matplotlib

\- Seaborn

\- Plotly

\- Tableau



\*\*Machine Learning\*\*

\- Scikit-learn

\- Random Forest

\- XGBoost



\*\*Documentation\*\*

\- GitHub

\- Markdown

\- Screenshots \& logs



---



\## \*\*Phase Workflow Overview\*\*



\### \*\*PHASE 0 – Initial Setup\*\*

\*\*Date:\*\* 2026-01-17



\*\*Tasks Completed\*\*

\- Folder structure verified

\- ArcGIS Pro project and geodatabase created

\- Base layers loaded (Ports, Coastline, Land)

\- Initial attribute tables reviewed



\*\*Outputs\*\*

\- Screenshots saved in `docs/screens/phase0/`



---



\### \*\*PHASE 1 – Data Import \& Exploratory Analysis\*\*

\*\*Date:\*\* 2026-01-23  

\*\*Status:\*\* ✅ Completed



---



\## \*\*Phase 1 – Detailed Log\*\*



\### \*\*AIS Data\*\*

\- Imported AIS vessel traffic data for \*\*Port of Livorno\*\*

\- File:

data/raw/ais/ais\_ports\_global\_oct2023/Livorno.csv



\- Records: ~19,700

\- No missing values or duplicates detected



\*\*EDA Outputs\*\*

\- Vessel count over time

\- Speed distribution

\- Vessel type frequency

\- Spatial position plots



\*\*Screenshots\*\*

\- `ais\_ship\_count\_time.png`

\- `ais\_speed\_distribution.png`

\- `ais\_vessel\_type\_frequency.png`

\- `ais\_positions.png`

\- `ais\_summary\_statistics\_before\_cleaning.csv`



---



\### \*\*Weather Data\*\*

\- Downloaded historical weather data (Oct 2023) using \*\*Open-Meteo API\*\*

\- Location: \*\*Livorno\*\*



\*\*File\*\*



data/raw/weather/weather\_openmeteo\_livorno\_oct2023.csv





\*\*Weather EDA Completed\*\*

\- Verified structure and datatypes

\- No missing values detected

\- Stable latitude/longitude (fixed location)

\- Key variables analyzed:

&nbsp; - Temperature

&nbsp; - Wind speed \& direction

&nbsp; - Surface pressure

&nbsp; - Precipitation

&nbsp; - Weather codes



\*\*Screenshots\*\*

\- `01\_weather\_download\_livorno.png`

\- `02\_weather\_download\_livorno.png`



---



\### \*\*Maintenance Data (Proxy Dataset)\*\*



Because real maintenance data is rarely public, a \*\*maintenance proxy dataset\*\* was created to simulate realistic scenarios.



\*\*File\*\*



data/raw/maintenance/maintenance\_proxy.csv





\*\*Columns\*\*

\- vessel\_id

\- vessel\_type

\- last\_maintenance

\- maintenance\_type

\- hours\_since\_last

\- next\_due\_hours

\- port



---



\### \*\*Maintenance EDA Results\*\*

\- No missing values

\- Vessel types: Cargo, Tanker, Passenger

\- Maintenance types: Engine, Hull, Navigation

\- Hours since last maintenance: \*\*50–300\*\*

\- Next maintenance due: \*\*400–600 hours\*\*



✅ Phase 1 Maintenance EDA completed successfully



---



\## \*\*Phase Status\*\*

🟢 \*\*Phase 1 completed\*\*



---



\## \*\*Next Steps\*\*



\### \*\*PHASE 2 – Cleaning \& Preprocessing\*\*

\- Remove outliers

\- Standardize formats

\- Merge AIS, weather, and maintenance datasets

\- Save cleaned data in `data/processed/`



\### \*\*PHASE 3 – SQL Analysis \& KPIs\*\*

\- Build SQL database

\- Aggregate KPIs (traffic, speed, weather impact)

\- Prepare data for Tableau \& ArcGIS



\### \*\*PHASE 4 – Visualizations \& Dashboards\*\*

\- GIS heatmaps

\- Tableau dashboards

\- Python visualizations



\### \*\*PHASE 5 – Cybersecurity \& Risk Alerts\*\*

\- Anomaly detection

\- Risk simulations

\- GIS-based alert mapping



\### \*\*PHASE 6 – AI / ML Modeling\*\*

\- Feature engineering

\- Predictive maintenance models

\- Route optimization



\### \*\*PHASE 7 – Portfolio Integration\*\*

\- Repository polishing

\- Final documentation

\- Portfolio website integration



---



\## \*\*Future Improvements\*\*

\- Live AIS streaming

\- Automated ETL pipelines

\- Cloud deployment (AWS / GCP / Azure)

\- Real-time dashboards

\- Advanced predictive models





