
import random

def get_profile_settings():

    return {
        "general.useragent.override": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "dom.webdriver.enabled": False,
        "useAutomationExtension": False,
        "media.navigator.permission.disabled": True,
        "geo.enabled": False,
        "geo.provider.use_corelocation": False,
        "geo.prompt.testing": False,
        "geo.prompt.testing.allow": False,
        "privacy.trackingprotection.enabled": True,
    }
