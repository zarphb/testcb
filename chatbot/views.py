from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from django.views.decorators.csrf import csrf_exempt


model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('message', '')  

        
        inputs = tokenizer.encode(user_input, return_tensors='pt')
        outputs = model.generate(inputs, max_length=150, do_sample=True, top_p=0.95, top_k=50)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return JsonResponse({"response": response})
    else:
        return JsonResponse({"error": "Only POST requests are allowed."}, status=405)



def chat_page(request):
    return render(request, 'chatbot/chat.html')



