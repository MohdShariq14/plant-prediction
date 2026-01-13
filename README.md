# 🌿 Leaf Disease Detection System

[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-009688.svg?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg?style=flat&logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776ab.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/Groq-AI%20Powered-orange.svg?style=flat)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat)](LICENSE)

An enterprise-grade AI-powered leaf disease detection system featuring a dual-interface architecture: a FastAPI backend service and an interactive Streamlit web application. Built with Meta's Llama Vision models via Groq API, this system provides accurate disease identification, severity assessment, and actionable treatment recommendations for agricultural and horticultural applications.

## System Demo

![Leaf Disease Detection Demo]

*Experience the power of AI-driven plant health analysis in action*

## 🎯 Key Features

### 🎯 Core Capabilities
- **🔍 Advanced Disease Detection**: Identifies 500+ plant diseases across multiple categories (fungal, bacterial, viral, pest-related, nutrient deficiencies)
- **📊 Precision Severity Assessment**: AI-powered classification of disease severity levels (mild, moderate, severe)
- ** High-Confidence Scoring**: Provides confidence percentages (0-100%) with advanced uncertainty quantification
- **💡 Expert Treatment Recommendations**: Evidence-based, actionable treatment protocols tailored to specific diseases
- **📋 Comprehensive Symptom Analysis**: Detailed visual symptom identification with causal relationship mapping
- **⚡ Real-time Processing**: Optimized inference pipeline with sub-5-second response times

### 🏗️ Architecture Components
- **FastAPI Backend (app.py)**: RESTful API service with automatic OpenAPI documentation
- **Streamlit Frontend (main.py)**: Interactive web interface with modern UI/UX design
- **Core AI Engine (Leaf Disease/main.py)**: Advanced disease detection engine powered by Meta Llama Vision
- **Utility Layer (utils.py)**: Image processing and data transformation utilities
- **Cloud Deployment**: Production-ready with Vercel integration and scalable architecture

## 🏗️ Project Architecture

### Directory Structure

**Main Application Components:**
- **🚀 main.py** - Streamlit Web Application with interactive UI components, real-time image preview, results visualization, and modern CSS styling
- **🔧 app.py** - FastAPI Backend Service with RESTful API endpoints, file upload handling, error management, and JSON response formatting
- **🧠 Leaf Disease/main.py** - Core AI Detection Engine containing the LeafDiseaseDetector class, DiseaseAnalysisResult dataclass, Groq API integration, base64 image processing, response parsing and comprehensive error handling

**Supporting Files:**
- **🛠️ utils.py** - Image processing utilities and helper functions
- **🧪 test_api.py** - Comprehensive API testing suite
- **📋 requirements.txt** - Python dependencies and package versions
- **⚙️ vercel.json** - Deployment configuration for cloud platforms
- **📁 Media/** - Sample test images for development and testing

### Core Module: Leaf Disease/main.py

The heart of the system, featuring the **LeafDiseaseDetector Class** which provides advanced AI-powered leaf disease detection using Groq's Llama Vision models. This class supports multi-format image input (JPEG, PNG, WebP, BMP, TIFF), automatic base64 encoding, structured JSON output with comprehensive disease information, robust error handling and response validation, plus configurable AI model parameters.

The **DiseaseAnalysisResult DataClass** serves as a structured container for disease analysis results, including boolean detection status, specific disease identification, category classification, severity assessment levels, AI confidence scores (0-100%), observable symptom lists, environmental and biological factors, evidence-based treatment recommendations, and ISO 8601 timestamps.

## 🚀 Quick Start Guide

### Prerequisites
- **Python 3.8+** (3.9+ recommended for optimal performance)
- **Groq API Key** ([Get your free key here](https://console.groq.com/))
- **Git** for repository cloning

### 1. Repository Setup
**Clone the repository:**
- Run: git clone https://github.com/Divy-Gupta/Plant-leaf-Disease-Detection.git
- Navigate to: cd leaf-diseases-detect/Front

**Create and activate virtual environment (recommended):**
- Windows PowerShell: python -m venv venv then .\venv\Scripts\Activate.ps1
- Linux/macOS: python -m venv venv then source venv/bin/activate

### 2. Dependencies Installation
**Install all required packages:**
- Run: pip install -r requirements.txt
- Verify: python -c "import streamlit, fastapi, groq; print('All dependencies installed successfully!')"

### 3. Environment Configuration
Create a .env file in the project root with the following variables:
- **Required: Groq API Key** - GROQ_API_KEY=your_groq_api_key_here
- **Optional: Model Configuration** - MODEL_NAME=meta-llama/llama-4-scout-17b-16e-instruct
- **Optional: Temperature** - DEFAULT_TEMPERATURE=0.3
- **Optional: Max Tokens** - DEFAULT_MAX_TOKENS=1024

### 4. Application Launch

#### Option A: Streamlit Web Interface (Recommended for Users)
**Launch the interactive web application:**
- Command: streamlit run main.py --server.port 8501 --server.address 0.0.0.0
- Access at: http://localhost:8501

#### Option B: FastAPI Backend Service (Recommended for Developers)
**Launch the API server:**
- Command: uvicorn app:app --reload --host 0.0.0.0 --port 8000
- API Documentation: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc

#### Option C: Both Services (Full Stack)
**Terminal 1: Launch FastAPI** - uvicorn app:app --reload --port 8000
**Terminal 2: Launch Streamlit** - streamlit run main.py --server.port 8501

## 📡 API Reference

### Streamlit Web Interface (main.py)

The Streamlit application provides an intuitive web interface for leaf disease detection:

#### Key Features:
- **Drag-and-drop image upload** with instant preview
- **Real-time disease analysis** with progress indicators
- **Professional result display** with modern CSS styling
- **Comprehensive disease information** including symptoms, causes, and treatments
- **Responsive design** optimized for desktop and mobile devices

#### Usage Flow:
1. Access the web interface at http://localhost:8501
2. Upload a leaf image (JPG, PNG supported)
3. Click "🔍 Detect Disease" to analyze
4. View detailed results with professional formatting

### FastAPI Backend Service (app.py)

#### POST /disease-detection-file
Upload an image file for comprehensive disease analysis.

**Request:**
- **Content-Type**: multipart/form-data
- **Body**: Image file (JPEG, PNG, WebP, BMP, TIFF)
- **Max Size**: 10MB per image

**Response Example:**
A JSON object containing:
- disease_detected: true/false
- disease_name: "Brown Spot Disease"
- disease_type: "fungal"
- severity: "moderate"
- confidence: 87.3
- symptoms: Array of observed symptoms like "Circular brown spots with yellow halos"
- possible_causes: Array of environmental factors like "High humidity levels"
- treatment: Array of recommendations like "Apply copper-based fungicide spray"
- analysis_timestamp: ISO timestamp

#### GET /
Root endpoint providing API information and status.

**Response:**
- message: "Leaf Disease Detection API"
- version: "1.0.0"
- endpoints: Available endpoint descriptions

### Core Detection Engine (Leaf Disease/main.py)

#### LeafDiseaseDetector.analyze_leaf_image_base64()
Core analysis method for base64 encoded images.

**Parameters:**
- base64_image (string): Base64 encoded image data
- temperature (float, optional): AI model creativity (0.0-2.0, default: 0.3)
- max_tokens (integer, optional): Response length limit (default: 1024)

**Returns:**
- Dictionary: Structured disease analysis results

**Example Usage:**
Initialize detector with LeafDiseaseDetector(), then call analyze_leaf_image_base64(base64_image_data) to get results including disease name, confidence percentage, and treatment recommendations.


### Comprehensive Disease Detection Capabilities

#### Fungal Diseases (40+ varieties):
- Leaf spot diseases, blights, rusts, mildews, anthracnose
- Early/late blight, powdery mildew, downy mildew
- Septoria leaf spot, cercospora leaf spot, black spot

#### Bacterial Diseases (15+ varieties):
- Bacterial leaf spot, fire blight, bacterial wilt
- Xanthomonas infections, pseudomonas diseases
- Crown gall, bacterial canker

#### Viral Diseases (20+ varieties):
- Mosaic viruses, yellowing diseases, leaf curl viruses
- Tobacco mosaic virus, cucumber mosaic virus
- Tomato spotted wilt virus, potato virus Y

#### Pest-Related Damage (25+ types):
- Insect feeding damage, mite infestations
- Aphid damage, thrips damage, scale insects
- Caterpillar feeding, leaf miner trails

#### Nutrient Deficiencies (10+ types):
- Nitrogen, phosphorus, potassium deficiencies
- Micronutrient deficiencies (iron, magnesium, calcium)
- pH-related nutrient lockout symptoms

#### Abiotic Stress Factors:
- Heat stress, cold damage, drought stress
- Chemical burn, sun scald, wind damage
- Over/under-watering symptoms

## 🤝 Contributing & Development

### Development Setup
**Fork and clone the repository:**
- Commands: git clone https://github.com/your-username/leaf-diseases-detect.git, cd leaf-diseases-detect/Front

**Create development environment:**
- Commands: python -m venv dev-env, .\dev-env\Scripts\Activate.ps1

**Install development dependencies:**
- Commands: pip install -r requirements.txt, pip install pytest black isort mypy

### Code Quality Standards
- **Style Guide**: PEP 8 compliance with Black formatter
- **Type Hints**: Full type annotation using mypy
- **Documentation**: Comprehensive docstrings for all classes and methods
- **Testing**: Unit tests for core functionality with pytest
- **Error Handling**: Robust exception handling and logging

### Development Workflow
1. **Create Feature Branch**: git checkout -b feature/amazing-feature
2. **Implement Changes**: Follow coding standards and add tests
3. **Run Quality Checks**:
   - Code formatting: black . --check
   - Import sorting: isort . --check-only
   - Type checking: mypy .
   - Run test suite: pytest tests/
4. **Commit Changes**: git commit -m 'feat: Add amazing feature'
5. **Push Branch**: git push origin feature/amazing-feature
6. **Create Pull Request**: Submit PR with detailed description

### Project Structure Guidelines
**Front/ directory contains:**
- main.py (Streamlit frontend with UI/UX focus)
- app.py (FastAPI backend with API endpoints)
- utils.py (Shared utilities and helpers)
- test_api.py (Integration tests)
- Leaf Disease/ (Core AI detection engine and configuration)
- tests/ (Unit test directory for all components)
- docs/ (Additional documentation)

### Contributing Guidelines
- **Bug Reports**: Use GitHub Issues with detailed reproduction steps
- **Feature Requests**: Propose new features with use case descriptions
- **Code Contributions**: Follow the development workflow above
- **Documentation**: Update README.md and docstrings for any changes
- **Security**: Report security vulnerabilities privately via GitHub Security

### Areas for Contribution
- **🔬 Model Improvement**: Experiment with new AI models and techniques
- **🎨 UI Enhancement**: Improve Streamlit interface design and usability
- **⚡ Performance**: Optimize image processing and API response times
- **🧪 Testing**: Expand test coverage and add integration tests
- **📱 Mobile Support**: Enhance mobile device compatibility
- **🌍 Internationalization**: Add support for multiple languages
- **📊 Analytics**: Implement usage analytics and performance monitoring

## 📝 License & Legal

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for complete terms and conditions.

### Third-Party Acknowledgments
- **Groq API**: AI inference platform
- **Meta Llama Models**: Vision-language models
- **FastAPI**: Modern web framework for APIs
- **Streamlit**: Interactive web application framework
- **Python Ecosystem**: NumPy, Pillow, and other supporting libraries


---

<div align="center">

**Star ⭐ this repository if it helped you protect your plants!**

</div>
