"""
learnify Django application initialization.
"""

from django.apps import AppConfig


class LearnifyConfig(AppConfig):
    """
    Configuration for the learnify Django application.
    """

    name = 'learnify'
    verbose_name = 'Learnify'

    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'learnify',
                'regex': '^api/learnify/',
                'relative_path': 'api.urls',
            }
        },
        'settings_config': {
            'lms.djangoapp': {
                'production': { 'relative_path': 'settings.production' },
                'common': { 'relative_path': 'settings.common' },
            }
        }
    }
