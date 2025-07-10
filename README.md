# AI Web Scraper

An intelligent web scraping tool that combines dynamic content extraction with AI-powered data parsing. This application uses Selenium for dynamic content loading and Ollama's LLaMA model for intelligent information extraction based on natural language descriptions.

## Features

- **Dynamic Content Scraping**: Handles JavaScript-heavy websites with automatic scrolling
- **AI-Powered Parsing**: Uses LLaMA 3.2 model to extract specific information based on natural language queries
- **Intelligent Content Cleaning**: Removes scripts, styles, and unnecessary elements
- **Chunked Processing**: Handles large web pages by splitting content into manageable chunks

## Prerequisites

- Python 3.8 or higher
- Chrome browser installed
- ChromeDriver executable
- Ollama with LLaMA 3.2 model installed

## Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/ai-web-scraper.git
cd ai-web-scraper
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Download ChromeDriver**:
   - Download ChromeDriver from [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)
   - Place the `chromedriver` executable in the project root directory
   - Make sure it's executable: `chmod +x chromedriver` (Linux/Mac)

4. **Install Ollama and LLaMA model**:
   - Install Ollama from [https://ollama.ai/](https://ollama.ai/)
   - Pull the LLaMA 3.2 model: `ollama pull llama3.2`

## Usage

1. **Start the application**:
```bash
streamlit run main.py
```

2. **Access the web interface**:
   - Open your browser and go to `http://localhost:8501`

3. **Scrape a website**:
   - Enter the website URL in the input field
   - Click "Scrape Site" to extract the content
   - View the raw DOM content in the expandable section

4. **Extract specific information**:
   - Describe what information you're looking for in natural language
   - Click "See content" to get AI-parsed results

## Example Usage

1. **URL**: `https://example-news-site.com`
2. **Description**: "Extract all article titles and their publication dates"
3. **Result**: The AI will identify and return only the article titles and dates from the scraped content

## Project Structure

```
ai-web-scraper/
├── main.py              # Streamlit application entry point
├── scrape.py            # Web scraping functions with Selenium
├── parse.py             # AI parsing logic with Ollama
├── requirements.txt     # Python dependencies
├── chromedriver         # ChromeDriver executable (you need to download this)
└── README.md           # This file
```

## File Descriptions

- **`main.py`**: Main Streamlit application that provides the web interface
- **`scrape.py`**: Contains functions for dynamic content scraping, content cleaning, and DOM processing
- **`parse.py`**: Handles AI-powered content parsing using Ollama's LLaMA model
- **`requirements.txt`**: Lists all Python package dependencies

