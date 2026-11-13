
import os
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing")

client = genai.Client(api_key=api_key)

prompt = """
اكتب سكريبت فيديو علمي باللغة العربية الفصحى.
الموضوع: لماذا لا نشعر بدوران الأرض؟
المدة: حوالي 3 دقائق.
اجعل المعلومات دقيقة ومشوقة، مع مقدمة وخاتمة.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

os.makedirs("output", exist_ok=True)

with open("output/script.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("تم إنشاء السكريبت بنجاح!")
