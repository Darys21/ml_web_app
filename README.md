# ML Model Training Web Application

This project is a web application for managing and training machine learning models, developed by ANGUILET Joan-yves Darys.

## Project Overview

The application provides a user-friendly interface for:
- Uploading machine learning datasets
- Training ML models on the uploaded data
- Visualizing training results and model performance

## Technical Stack

- **Backend**: Python (Flask)
- **Version Control**: Git & GitHub
- **ML Data/Model Versioning**: DVC
- **CI/CD**: Jenkins
- **Storage**: Google Cloud Platform

## Features

1. **Data Management**
   - Upload ML datasets (CSV format supported)
   - Data version control using DVC
   - Remote storage integration with Google Drive

2. **Model Training**
   - Support for multiple ML algorithms:
     - Linear Regression
     - SVM
     - Random Forest
   - Model versioning with DVC
   - Performance metrics visualization using Flask templates

3. **CI/CD Pipeline**
   - Automated testing with Jenkins
   - Model training validation
   - Test reporting and monitoring

## Project Structure

The project follows a Flask application structure:
- `/app` - Main application directory
  - `/templates` - Flask HTML templates
  - `/static` - CSS, JavaScript, and static files
  - `/models` - ML model implementations
  - `/utils` - Helper functions and utilities
- Data and models tracked with DVC
- Continuous Integration through Jenkins pipelines

## Getting Started

[Installation and setup instructions will be added]

## Documentation

[Detailed documentation will be added]

## Contributing

[Contribution guidelines will be added]
