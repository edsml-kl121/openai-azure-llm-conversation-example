from pathlib import Path
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

endpoint = os.getenv("AZURE_ENDPOINT")
deployment_name = "gpt-4o-mini-tts"
api_key = os.getenv("AZURE_API_KEY")

# example_input ="""สวัสดีค่ะ ยินดีต้อนรับนะคะ ที่เน็กซ์โทเปียตอนนี้มีหลายอย่างน่ากินเลยค่ะ ทั้งโซนคาเฟ่ที่มีเครื่องดื่มพิเศษกับเบเกอรี่อบใหม่ทุกวัน แล้วก็โซนฟู้ดคอร์ตก็มีทั้งอาหารไทย ฟิวชัน และของทานเล่นจากหลายร้านเด็ด ถ้าชอบอะไรแนวไหนเป็นพิเศษ แอมช่วยแนะนำเมนูให้ได้เลยนะคะ จะได้เลือกง่ายขึ้นหน่อย"""
example_input ="""สวัสดีค่ะ ยินดีต้อนรับสู่ NEXTOPIA นะคะ ที่นี่เหมือนเมืองแห่งอนาคตที่รวมทุกอย่างไว้ครบเลยค่ะ ทั้งโซนเทคโนโลยีล้ำๆ โซนนวัตกรรมเพื่อความยั่งยืน พื้นที่สำหรับทำงานร่วมกันของคนเก่งๆ จากหลายวงการ ไปจนถึงโซนไลฟ์สไตล์ที่มีทั้งคาเฟ่ ร้านอาหาร และพื้นที่สร้างแรงบันดาลใจอีกเยอะเลย สิ่งที่ทำให้ NEXTOPIA พิเศษคือมันไม่ได้เป็นแค่ “เมือง” ธรรมดา แต่เป็นเหมือนพื้นที่ที่ทุกคนสามารถเข้ามามีส่วนร่วมในการสร้างอนาคตร่วมกัน ไม่ว่าจะเป็นองค์กร พาร์ตเนอร์ หรือคนทั่วไปที่อยากแชร์ไอเดียดีๆ ก็ร่วมเป็น Friends of NEXTOPIA ได้หมดเลยค่ะ อยากให้แอมช่วยเล่าโซนไหนก่อนดีคะ ระหว่างโซนเทคโนโลยี โซนไลฟ์สไตล์ หรือโซนนวัตกรรมยั่งยืนดี?"""

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2025-03-01-preview"
)
speech_file_path = Path(__file__).parent / "speech_azure_bad2.mp3"

with client.audio.speech.with_streaming_response.create(
    model=deployment_name,
    voice="alloy",
    input=example_input,
#     instructions="""Please generate Thai speech that sounds natural and human-like.
# Use clear Thai pronunciation, correct tones, and smooth sentence flow.
# Avoid robotic rhythm, avoid karaoke-style pronunciation, and avoid over-emphasizing each syllable.

# Speak with:
# • a warm, friendly tone
# • natural pacing (not too fast, not too slow)
# • connected syllables instead of splitting every sound
# • subtle intonation variation like a real Thai speaker

# If the sentence contains English words, pronounce them in a natural Thai accent.
# Make the delivery sound like a real person, not a text-to-speech engine.

# เน็กซ์โทเปีย is pronounced as Nextopia""",
    # instructions="""Speak in a cheerful and positive tone.""",
) as response:
    response.stream_to_file(speech_file_path)