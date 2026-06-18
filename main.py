import os
import random
from datetime import datetime
from io import BytesIO
from urllib.parse import quote

import requests
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from PIL import Image


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("GROQ_API_KEY not found. Please add it inside your .env file.")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


STYLE_PRESETS = {
    "Realistic": "realistic, highly detailed, natural lighting",
    "Cyberpunk": "cyberpunk, neon lighting, futuristic atmosphere, cinematic",
    "Anime": "anime style, vibrant colors, clean line art, detailed background",
    "Minimalist": "minimalist, clean composition, soft colors, modern design",
    "Oil Painting": "oil painting, visible brush strokes, artistic texture",
    "3D Render": "3D render, cinematic lighting, ultra detailed, sharp focus"
}


SIZE_MAP = {
    "Square (1:1)": (1024, 1024),
    "Landscape (16:9)": (1344, 768),
    "Portrait (9:16)": (768, 1344)
}


def improve_prompt(user_prompt, style):
    system_prompt = """
You are an expert AI image prompt engineer.
Rewrite the user's basic idea into a detailed text-to-image prompt.
Keep it clear, visual, and suitable for digital artwork generation.
Do not add unsafe, violent, adult, or copyrighted character content.
Return only the improved prompt.
"""

    style_text = STYLE_PRESETS[style]

    user_message = f"""
User idea: {user_prompt}

Required style: {style_text}

Create one final high-quality image generation prompt.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7,
        max_tokens=250
    )

    return response.choices[0].message.content.strip()


def generate_image(prompt, width, height, seed):
    encoded_prompt = quote(prompt)

    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

    params = {
        "width": width,
        "height": height,
        "seed": seed,
        "model": "flux",
        "enhance": "false"
    }

    response = requests.get(
        url,
        params=params,
        timeout=(3.05, 120),
        stream=True
    )

    response.raise_for_status()

    image_bytes = BytesIO()

    for chunk in response.iter_content(chunk_size=65536):
        if chunk:
            image_bytes.write(chunk)

    image_bytes.seek(0)

    image = Image.open(image_bytes)
    image.load()

    image_bytes.seek(0)
    return image_bytes.read()


def save_image(image_bytes):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"generated_{timestamp}.png"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "wb") as file:
        file.write(image_bytes)

    return filepath


st.set_page_config(
    page_title="Multimodal Image Generation Studio",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 Multimodal Image Generation Studio")
st.write("Generate digital artwork from text using Groq prompt enhancement + image generation API.")

with st.sidebar:
    st.header("Generation Settings")

    style = st.selectbox(
        "Choose Art Style",
        list(STYLE_PRESETS.keys())
    )

    size_label = st.selectbox(
        "Choose Aspect Ratio",
        list(SIZE_MAP.keys())
    )

    generation_count = st.slider(
        "Number of Images",
        min_value=1,
        max_value=3,
        value=1
    )

    use_groq_enhancement = st.checkbox(
        "Enhance prompt using Groq",
        value=True
    )

user_prompt = st.text_area(
    "Enter your image description",
    placeholder="Example: A futuristic AI robot standing in a neon city...",
    height=150
)

if st.button("Generate Images"):
    if not user_prompt.strip():
        st.error("Please enter an image description.")
    else:
        width, height = SIZE_MAP[size_label]

        try:
            if use_groq_enhancement:
                with st.spinner("Improving prompt using Groq..."):
                    final_prompt = improve_prompt(user_prompt, style)
            else:
                final_prompt = f"{user_prompt}. Style: {STYLE_PRESETS[style]}"

            st.subheader("Final Prompt")
            st.info(final_prompt)

            st.subheader("Generated Images")

            cols = st.columns(generation_count)

            for i in range(generation_count):
                seed = random.randint(1, 999999)

                with st.spinner(f"Generating image {i + 1}..."):
                    image_bytes = generate_image(final_prompt, width, height, seed)
                    filepath = save_image(image_bytes)

                image = Image.open(BytesIO(image_bytes))

                with cols[i]:
                    st.image(
                        image,
                        caption=f"Image {i + 1} | Seed: {seed}",
                        use_container_width=True
                    )

                    st.download_button(
                        label="Download Image",
                        data=image_bytes,
                        file_name=os.path.basename(filepath),
                        mime="image/png"
                    )

                    st.success(f"Saved: {filepath}")

        except Exception as error:
            st.error(f"Generation failed: {error}")