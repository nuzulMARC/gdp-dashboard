
# GDP Dashboard with Streamlit

This project is a **dynamic dashboard** built with **Streamlit** to visualize GDP data. It allows users to filter GDP information by sector, year, and value range. The dashboard provides visualizations such as line plots, heatmaps, and pie charts for better insights. The app is **Dockerized** for easy setup and deployment.

---

## Features

- Filter GDP by **sectors** and **categories** with multi-select checkboxes.
- **Range sliders** to fine-tune year and value selection.
- **"Unselect All" button** to reset sector selections quickly.
- Visualizations:
  - **Line Chart** for GDP values over time.
![image](https://github.com/user-attachments/assets/4ac88f13-0f56-4cc3-9227-64adf27662a0)

  - **Heatmap** for sector-wise GDP values.
![image](https://github.com/user-attachments/assets/3570759a-b8f6-4f1d-85b8-d5066c35dfa9)

  - **Pie Chart** for sector proportions.
![image](https://github.com/user-attachments/assets/ea961a3b-087d-48f6-b1b0-55ca2a41220e)

- **Dockerized** for easy deployment.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Docker Deployment](#docker-deployment)
- [Running the Docker Container](#running-the-docker-container)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

### Prerequisites
- **Python** 3.9 or higher
- **Docker** installed ([Download Docker](https://www.docker.com/get-started))

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/gdp-dashboard.git
cd gdp-dashboard
```

### Step 2: Create a Virtual Environment and Install Dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # For Linux/Mac
# On Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

### Step 3: Run the Streamlit App Locally

```bash
streamlit run app.py
```

Access the app in your browser at **[http://localhost:8501](http://localhost:8501)**.

---

## Docker Deployment

If you prefer to run the app in a **Docker container**, follow these steps:

### Step 1: Build the Docker Image

In the root of the project folder (`gdp_dashboard`), run:

```bash
docker build -t gdp-dashboard .
```

### Step 2: Run the Docker Container

```bash
docker run -p 8501:8501 gdp-dashboard
```

### Step 3: Access the App

Open your browser and visit **[http://localhost:8501](http://localhost:8501)**.

---

## Running the Docker Container with Docker Hub Image

If you’ve pushed the Docker image to **Docker Hub**, you can pull and run it easily:

### Step 1: Pull the Image from Docker Hub

```bash
docker pull nuzul890/gdp-dashboard:latest
```

### Step 2: Run the Container from Docker Hub

```bash
docker run -p 8501:8501 nuzul890/gdp-dashboard:latest
```

---

## Usage

1. **Select a category** from the dropdown to filter sectors.
2. **Multi-select sectors** using checkboxes.
3. Use **range sliders** to adjust the year and value ranges.
4. Explore the visualizations:
   - **Line chart** to see GDP trends over time.
   - **Heatmap** for sector-wise comparisons.
   - **Pie chart** to view sector proportions.

---

## Screenshots

### Line Chart
_A screenshot of the line chart showing GDP trends over time._

### Heatmap
_A screenshot of the heatmap visualizing sector-wise GDP values._

---

## Contributing

Contributions are welcome! Please follow these steps:
Wpository.
2. Create a new branch:
   ```bash
   git checkout -b feature-new-feature
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-new-feature
   ```
5. Submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

---

### How to Use This

1. Save this content as **`README.md`** in the root of your project (`gdp_dashboard`).
2. Add and commit the changes:

   ```bash
   git add README.md
   git commit -m "Add README.md with Docker instructions"
   git push origin main
   ```

This version of the README includes clear instructions for both **local** and **Docker-based deployment**, making it easy for anyone to run and contribute to your project.
