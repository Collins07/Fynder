from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



def ussd_home(request):
    return HttpResponse("Welcome to the Fynder USSD Service")

@csrf_exempt
def ussd_callback(request):
    session_id = request.POST.get('sessionId')
    service_code = request.POST.get('serviceCode')
    phone_number = request.POST.get('phoneNumber')
    text = request.POST.get('text', '')

    response = ""

    # Start of USSD flow
    if text == "":
        # Initial USSD menu
        response = "CON Hello, Welcome to Fynder. Let's help you report or find your lost child or pet.\n"
        response += "1. Report Lost Child\n"
        response += "2. Report Lost Pet\n"

    elif text == "1":
        response = "CON Are you reporting a missing child or a lost but found child?\n"
        response += "1. Missing Child\n"
        response += "2. Lost but Found Child\n"

    elif text == "1*1":
        response = "CON Was the child wearing a Fynder wristband?\n"
        response += "1. Yes\n"
        response += "2. No\n"

    elif text == "1*1*1":
        response = "CON Please enter the ID on the wristband:\n"

    elif text.startswith("1*1*1*"):
        child_id = text.split('*')[-1]
        response = f"END Thank you. We will reach out to you once we find your child (ID: {child_id})."

    elif text == "1*1*2":
        response = "END We are calling you in a few seconds via 0718074023. Thank you."

    # Other cases for reporting lost pets
    elif text == "2":
        response = "CON Are you reporting a missing pet or a lost but found pet?\n"
        response += "1. Missing Pet\n"
        response += "2. Lost but Found Pet\n"

    elif text == "2*1":
        response = "CON Was the pet wearing a Fynder collar?\n"
        response += "1. Yes\n"
        response += "2. No\n"

    elif text == "2*1*1":
        response = "CON Please enter the ID on the collar:\n"

    elif text.startswith("2*1*1*"):
        pet_id = text.split('*')[-1]
        response = f"END Thank you. We will reach out to you once we find your pet (ID: {pet_id})."

    elif text == "2*1*2":
        response = "END We are calling you in a few seconds via 0718074023. Thank you."

    else:
        response = "END Invalid input. Please try again."

    return HttpResponse(response, content_type="text/plain")

