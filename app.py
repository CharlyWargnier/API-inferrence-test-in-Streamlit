import streamlit as st
import requests
import pandas as pd


st.title("SIMPLE TEST FROM HF site")

import requests

API_KEY = st.secrets["API_KEY"]

API_URL = "https://api-inference.huggingface.co/models/valhalla/distilbart-mnli-12-3"

headers = {"Authorization": f"Bearer {API_KEY}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query(
    {
        "inputs": "I want to order clothes from jumia",
        "parameters": {"candidate_labels": ["refund", "legal", "faq"]},
    }
)

output
