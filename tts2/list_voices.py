'''
List all supported voices in Azure Speech Service
'''

import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
import os

load_dotenv()

# Load configuration
speech_key = os.getenv("AZURE_API_KEY")
service_region = os.getenv("AZURE_SPEECH_REGION", "eastus2")

# Initialize speech config
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Get synthesis voices
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)

print(f"Fetching supported voices for region: {service_region}\n")
print("=" * 80)

result = synthesizer.get_voices_async().get()

if result.reason == speechsdk.ResultReason.VoicesListRetrieved:
    print(f"{'Locale':<15} {'Short Name':<30} {'Gender':<10} {'Name':<40}")
    print("-" * 80)
    
    voices_by_locale = {}
    
    for voice in result.voices:
        locale = voice.locale
        if locale not in voices_by_locale:
            voices_by_locale[locale] = []
        voices_by_locale[locale].append(voice)
    
    # Sort by locale
    for locale in sorted(voices_by_locale.keys()):
        for voice in voices_by_locale[locale]:
            print(f"{locale:<15} {voice.short_name:<30} {voice.gender:<10} {voice.name:<40}")

elif result.reason == speechsdk.ResultReason.Canceled:
    print(f"Error: {result.error_details}")
    print("\nMake sure:")
    print("  1. AZURE_API_KEY is set correctly in .env")
    print("  2. AZURE_SPEECH_REGION is valid (default: eastus2)")

print("\n" + "=" * 80)
