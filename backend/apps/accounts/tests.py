from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UsuarioSMIATest(TestCase):

    def test_creacion_usuario(self):
        usuario = User.objects.create_user(
            email='test@gamlp.bo',
            password='123456'
        )

        self.assertEqual(usuario.email, 'test@gamlp.bo')
        self.assertTrue(usuario.check_password('123456'))

    def test_estado_usuario_activo(self):
        usuario = User.objects.create_user(
            email='activo@gamlp.bo',
            password='123456'
        )

        self.assertTrue(usuario.is_active)