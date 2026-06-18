# Multimodal Image Generation Studio

A Streamlit-based Generative AI application that converts natural language text descriptions into high-quality digital artwork.
This project uses the Groq API to improve user prompts and an image generation API to create visual artwork from the final prompt.

## Project Objective

The goal of this project is to build a visual application that allows users to enter a text description and generate digital artwork based on that description.

The application supports style selection, aspect ratio selection, multiple image generation, image preview, local saving, and image download.

## Features

* Text-to-image generation
* Prompt enhancement using Groq API
* Multiple art style presets
* Aspect ratio and resolution selection
* Generation count control
* Image preview inside the web app
* Download generated images
* Save generated images locally
* Error handling for failed API requests
* Clean Streamlit user interface

## Tech Stack

* Python
* Streamlit
* Groq API
* Pollinations Image API
* Requests
* Pillow
* python-dotenv

## How the Project Works

1. The user enters a natural language image description.
2. The user selects an art style, aspect ratio, and number of images.
3. The Groq API improves the raw user prompt into a detailed image-generation prompt.
4. The final prompt is sent to the image generation API.
5. The API returns generated image data.
6. The application displays the generated images in the Streamlit interface.
7. The generated images are saved locally inside the `outputs` folder.
8. The user can download the generated images.

## Project Structure

```text
DecodeLabs-GenAI-Project3/
│
├── main.py
├── requirements.txt
├── .env
├── README.md
│
└── outputs/
    └── generated_images.png
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/DecodeLabs-GenAI-Project3.git
```

```bash
cd DecodeLabs-GenAI-Project3
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

For Windows PowerShell:

```bash
.venv\Scripts\activate
```

For Mac/Linux:

```bash
source .venv/bin/activate
```

### 4. Install Required Packages

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Important: Do not upload your `.env` file to GitHub because it contains your private API key.

## requirements.txt

```txt
streamlit
groq
python-dotenv
requests
Pillow
```

## How to Run the Project

Run the Streamlit app using:

```bash
streamlit run main.py
```

After running the command, the application will open in your browser.

## Usage

1. Open the application in your browser.
2. Enter an image description.
3. Select an art style.
4. Select an aspect ratio.
5. Choose the number of images to generate.
6. Click the **Generate Images** button.
7. View the generated images.
8. Download or use the saved images from the `outputs` folder.

## Example Prompts

```text
A futuristic AI robot standing in a neon cyberpunk city
```

```text
A peaceful mountain village during sunset in oil painting style
```

```text
A 3D render of a smart home controlled by artificial intelligence
```

```text
A minimalist poster showing the relationship between humans and AI
```

## Supported Styles

* Realistic
* Cyberpunk
* Anime
* Minimalist
* Oil Painting
* 3D Render

## Supported Aspect Ratios

| Aspect Ratio | Resolution  |
| ------------ | ----------- |
| Square       | 1024 x 1024 |
| Landscape    | 1344 x 768  |
| Portrait     | 768 x 1344  |

## Output

Generated images are saved inside the `outputs` folder with unique filenames.

Example:

```text
outputs/generated_20260618_153045_123456.png
```

## Important Note

Groq API is used for prompt enhancement, not direct image generation.
The final image is generated using an image generation API after Groq improves the user prompt.

## Learning Outcomes

Through this project, I learned:

* How to integrate APIs in a Python application
* How to use Groq API for prompt enhancement
* How to send text prompts to an image generation API
* How to handle image URLs and binary image data
* How to save generated images locally
* How to display generated images in a Streamlit web application
* How to create a simple visual Generative AI application

## Future Improvements

* Add user login system
* Store image generation history
* Add advanced prompt controls
* Add negative prompt support
* Add image editing features
* Add gallery view for generated images
* Add more image generation models

## Conclusion

The Multimodal Image Generation Studio demonstrates how Generative AI can convert human language into visual artwork.
This project combines prompt engineering, API integration, image handling, and web application development to create a practical AI-powered visual generation tool.
