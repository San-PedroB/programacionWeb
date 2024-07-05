from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Validador para solo letras
class ValidadorSoloLetras:
    def __init__(self):
        self.validador = RegexValidator(
            regex='^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]*$',
            message='Este campo solo puede contener letras.',
            code='invalid_field'
        )

    def validate(self, valor):
        self.validador(valor)

    def get_help_text(self):
        return "Este campo solo puede contener letras."

# Validador para solo letras y números
class ValidadorSoloLetrasNumeros:
    def __init__(self):
        self.validador = RegexValidator(
            regex='^[a-zA-Z0-9]*$',
            message='Este campo solo puede contener letras y números.',
            code='invalid_username'
        )

    def validate(self, valor):
        self.validador(valor)

    def get_help_text(self):
        return "Este campo solo puede contener letras y números."

# Validador para al menos un carácter numérico
class ValidadorCaracterNumerico:
    def validate(self, valor, usuario=None):
        if not any(char.isdigit() for char in valor):
            raise ValidationError(
                "La contraseña debe contener al menos un carácter numérico."
            )

    def get_help_text(self):
        return "Tu contraseña debe contener al menos un carácter numérico."