
'''
  For more samples please visit https://github.com/Azure-Samples/cognitive-services-speech-sdk
'''

import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
from pathlib import Path
import os
import time

start = time.time()

load_dotenv()

# Load configuration from environment
speech_key = os.getenv("AZURE_API_KEY")
service_region = os.getenv("AZURE_SPEECH_REGION", "eastus2")

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
# Use Thai voice - now with correct full name
# speech_config.speech_synthesis_voice_name = "th-TH-PremwadeeNeural" # (Female)
# speech_config.speech_synthesis_voice_name = "th-TH-NiwatNeural" # (Male)
# speech_config.speech_synthesis_voice_name = "th-TH-AcharaNeural" # (Female)

# Set up audio output to WAV file
output_file = Path(__file__).parent / "output_nextopia_AcharaNeural.wav"
audio_config = speechsdk.audio.AudioOutputConfig(filename=str(output_file))

text = """สวัสดีค่ะ ยินดีต้อนรับสู่ NEXTOPIA นะคะ ที่นี่เหมือนเมืองแห่งอนาคตที่รวมทุกอย่างไว้ครบเลยค่ะ ทั้งโซนเทคโนโลยีล้ำๆ โซนนวัตกรรมเพื่อความยั่งยืน พื้นที่สำหรับทำงานร่วมกันของคนเก่งๆ จากหลายวงการ ไปจนถึงโซนไลฟ์สไตล์ที่มีทั้งคาเฟ่ ร้านอาหาร และพื้นที่สร้างแรงบันดาลใจอีกเยอะเลย สิ่งที่ทำให้ NEXTOPIA พิเศษคือมันไม่ได้เป็นแค่ "เมือง" ธรรมดา แต่เป็นเหมือนพื้นที่ที่ทุกคนสามารถเข้ามามีส่วนร่วมในการสร้างอนาคตร่วมกัน ไม่ว่าจะเป็นองค์กร พาร์ตเนอร์ หรือคนทั่วไปที่อยากแชร์ไอเดียดีๆ ก็ร่วมเป็น Friends of NEXTOPIA ได้หมดเลยค่ะ อยากให้แอมช่วยเล่าโซนไหนก่อนดีคะ ระหว่างโซนเทคโนโลยี โซนไลฟ์สไตล์ หรือโซนนวัตกรรมยั่งยืนดี?"""

# Use SSML for slower speech rate (0.7 = 70% speed)
# ssml_text = f'<speak version="1.0" xml:lang="th-TH"><voice xml:lang="th-TH" name="th-TH-PremwadeeNeural"><prosody rate="0.7">{text}</prosody></voice></speak>'
# ssml_text = f'<speak version="1.0" xml:lang="th-TH"><voice xml:lang="th-TH" name="th-TH-NiwatNeural"><prosody rate="0.7">{text}</prosody></voice></speak>'
ssml_text = f'<speak version="1.0" xml:lang="th-TH"><voice xml:lang="th-TH" name="th-TH-AcharaNeural"><prosody rate="0.7">{text}</prosody></voice></speak>'

# Create synthesizer with file output
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

result = speech_synthesizer.speak_ssml_async(ssml_text).get()
# Check result
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print(f"✓ Speech synthesized successfully!")
    print(f"  Saved to: {output_file}")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print(f"✗ Speech synthesis canceled: {cancellation_details.reason}")
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print(f"  Error details: {cancellation_details.error_details}")

end= time.time()
print(f"Time taken: {end - start} seconds")