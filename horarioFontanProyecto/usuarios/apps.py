from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'


# usuarios/apps.py

class UsuariosConfig(AppConfig):
    name = 'usuarios'

    def ready(self):
        import usuarios.signals  # Importa las señales cuando la app está lista
