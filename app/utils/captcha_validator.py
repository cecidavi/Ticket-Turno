# app/utils/captcha_validator.py

import requests
from flask import current_app

def validar_captcha(token):
    """Valida el token de reCAPTCHA enviado por el usuario."""
    secret_key = current_app.config['RECAPTCHA_SECRET_KEY']
    url = 'https://www.google.com/recaptcha/api/siteverify'
    payload = {
        'secret': secret_key,
        'response': token
    }

    response = requests.post(url, data=payload)
    result = response.json()
    return result.get('success', False)
