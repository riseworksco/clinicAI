# Copyright 2024 Yuan Chen
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
import time

from django.shortcuts import render
from Music_Therapy_API.settings import genai

model = genai.GenerativeModel('gemini-pro')


# Create your views here.
def index(request):
    context = {"header": "Chat"}
    return render(request, "chat/index.html", context)


def generate_response(request):
    response = model.generate_content("What is the meaning of life?")
    time.sleep(10)
    logging.INFO(response.text)
    logging.INFO(response.prompt_feedback)
    context = {"response": response}
    return render(request, "chat/index.html", context)
