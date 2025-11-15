#!/bin/bash

# Load environment variables from .env file
if [ -f ../.env ]; then
  export $(cat ../.env | grep -v '^#' | xargs)
fi

curl -X POST "https://kandanail-0150-resource.openai.azure.com/openai/deployments/gpt-4o-mini-tts/audio/speech?api-version=2025-03-01-preview" \
  -H "Content-Type: application/json" \
  -H "api-key: $AZURE_API_KEY" \
  -d '{
      "model": "gpt-4o-mini-tts",
      "input": "The quick brown fox jumped over the lazy dog",
      "voice": "alloy"
    }' --output speech.mp3