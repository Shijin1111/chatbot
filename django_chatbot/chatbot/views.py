from django.shortcuts import render
from django.http import JsonResponse

import os
import google.generativeai as genai

def ask_openai(message):
    genai.configure(api_key="AIzaSyAjr1v-NGJb8qix3HXgQABxQViwMgdSCkI")

    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    chat_session = model.start_chat(
    history=[
    ]
    )
    
    res = chat_session.send_message(f"{message}reduce the time complexity of this code using any method")
    print(res)
    return res.text






def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message':message,'response':response})
    return render(request,'chatbot.html')
