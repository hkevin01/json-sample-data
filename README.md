# json-sample-data

## Project Overview
This project provides sample JSON data for graph and chart visualization, organized by difficulty level: beginner, intermediate, and advanced. The datasets are designed for use in data visualization tools, libraries, and educational settings, supporting users from basic to complex scenarios.

## Data Levels
- **Beginner:** Simple node-link or bar chart data
- **Intermediate:** Multi-series, grouped, or hierarchical data
- **Advanced:** Complex, nested, or real-world datasets for advanced visualizations

## Installation
No installation is required for data usage. For code and scripts, clone the repository:

```bash
git clone https://github.com/hkevin01/json-sample-data.git
```

## Usage Examples
- Use the sample JSON files in the `data/` directory for your visualization projects.
- Example (Python):
  ```python
  import json
  with open('data/beginner-sample.json') as f:
      data = json.load(f)
  # Use `data` with your visualization library
  ```
- Example (JavaScript):
  ```js
  fetch('data/intermediate-sample.json')
    .then(res => res.json())
    .then(data => {
      // Use data for chart rendering
    });
  ```

## Contribution Guidelines
- Fork the repository and create a feature branch.
- Submit pull requests with clear descriptions.
- Follow the coding standards outlined in `.editorconfig` and `.prettierrc`.
- Add tests for new scripts or code.
- See `CONTRIBUTING.md` for more details.

## License
MIT License. See `LICENSE` file for details.