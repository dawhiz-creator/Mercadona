from django import template

register = template.Library()

@register.filter
def truncate_chars(value, max_length):
    """
    Renvoie la chaîne de caractères `value` tronquée à `max_length` caractères.
    Si la chaîne de caractères est plus courte que `max_length`, elle est renvoyée telle quelle.
    Si la chaîne de caractères est plus longue que `max_length`, elle est tronquée à la 
    dernière occurrence d'un espace avant `max_length` et suivi de "...".
    """
    if len(value) <= max_length:
        return value
    else:
        return value[:max_length].rsplit(' ', 1)[0] + '...'
 