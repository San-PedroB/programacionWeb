from django import template

register = template.Library()

#revisar
@register.filter(name='add_class')
def add_class(value, css_class):
    return value.as_widget(attrs={'class': css_class})

# filtro para multiplicar
@register.filter(name='multiplicar')
def multiplicar(valor, cantidad):
    return valor * cantidad
