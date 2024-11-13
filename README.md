<!-- PROJECT SHIELDS -->
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">VADISKG Timeline Visualization</h3>

  <p align="center">
    A system for visualizing citation counts over time for selected variables.
    <br />
    <br />
    <a href="https://github.com/vadis-project/vadiskg/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/vadis-project/vadiskg/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#contact">Citation</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
![vadis_summarization_api](https://github.com/user-attachments/assets/1ca65ec0-156a-4381-a691-93da7dd64f76)

VADISKG Timeline Visualization is a system demonstration that shows how citation counts for selected variables change over time. It provides an interactive visualization, allowing users to explore trends and patterns in the citation data.

<!-- GETTING STARTED -->
## Getting Started

Follow these steps to get a local copy of the VADISKG Timeline Visualization up and running.

### Prerequisites

Before you begin, ensure that you have the following installed:

* **uv** (a package manager for Python projects)
  - Install **uv** by following the instructions in the [official documentation](https://docs.astral.sh/uv/getting-started/installation/).

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/vadis-project/vadiskg.git
   ```
2. Navigate into the project directory:
   ```sh
   cd vadiskg
   ```
3. Sync and install dependencies using **uv**:
   ```sh
   uv sync
   ```

4. Run the Streamlit application:
   ```sh
   uv run streamlit run src/vadiskg/demo.py
   ```

Once the command is executed, the application will be activated. You can view the timeline visualization by opening [http://localhost:8501](http://localhost:8501) in your web browser.

<!-- USAGE EXAMPLES -->
## Usage

Once the application is running, you will see a web interface that allows you to visualize citation counts over time for various selected variables. Use the interactive controls to adjust the settings and explore different data points. If the web page does not automatically open for you, you click [this](http://localhost:8501) to open it yourself.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

For any questions or inquiries, please feel free to raise an issue in this repository or contact me:

Sotaro Takeshita - sotaro.takeshita@uni-mannheim.de

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[issues-shield]: https://img.shields.io/github/issues/vadis-project/vadiskg.svg?style=for-the-badge
[issues-url]: https://github.com/vadis-project/vadiskg/issues
[license-shield]: https://img.shields.io/github/license/vadis-project/vadiskg.svg?style=for-the-badge
[license-url]: https://github.com/vadis-project/vadiskg/blob/master/LICENSE
[product-screenshot]: images/screenshot.png
