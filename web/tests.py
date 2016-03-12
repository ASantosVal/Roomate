# coding: latin1
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.test import TestCase
from unittest import skip

#-------------------------------------------------------------------------------

class DefaultTestCase(TestCase):
    # Inicializar la base de datos que se va a utilizar en las pruebas
    def setUp(self):
        self.username = "user1"
        self.password = "pass1"
        self.email = "false@email.com"
        User.objects.create_user(self.username, self.email, self.password)

#-------------------------------------------------------------------------------

class LoginTest(DefaultTestCase):
    def test_login_success(self):
        # Iniciar sesión con datos correctos
        response = self.client.post('/accounts/login/', {'username': self.username, 'password': self.password})
        self.assertIn('_auth_user_id', self.client.session)

        # El usuario es redirigido a la página principal
        self.assertRedirects(response, '/')

    def test_login_failure(self):
        #Iniciar sesión con datos incorrectos
        response = self.client.post('/accounts/login/', {'username': self.username, 'password': 'incorrect_pass'})
        self.assertNotIn('_auth_user_id', self.client.session)

    @skip("Ignorado por el momento")
    def test_login_logged_user(self):
        self.client.login(username = self.username, password = self.password)
        response = self.client.get('/accounts/login/')
        self.assertRedirects(response, '/')

#-------------------------------------------------------------------------------

class LogoutTest(DefaultTestCase):
    def test_logout_logged_user(self):
        # Iniciar sesion
        self.client.login(username = self.username, password = self.password)
        self.assertIn('_auth_user_id', self.client.session)

        # Cerrar sesión
        response = self.client.get('/accounts/logout/')
        self.assertNotIn('_auth_user_id', self.client.session)

        # El usuario es redirigido a la página principal
        self.assertRedirects(response, '/')

    def test_logout_not_logged_user(self):
        # Cerrar sesión sin haber iniciado sesión previamente
        response = self.client.get('/accounts/logout/')
        self.assertNotIn('_auth_user_id', self.client.session)

        # El usuario es redirigido a la página principal
        self.assertRedirects(response, '/')

#-------------------------------------------------------------------------------

class PasswordChangeTest(DefaultTestCase):
    def test_password_change_not_logged_user(self):
        # El usuario es redigido a la página de login
        response = self.client.get('/accounts/password/change/')
        self.assertRedirects(response, '/accounts/login/?next=/accounts/password/change/', target_status_code=302)

    def test_password_change_success(self):
        self.new_password = "new_password123"

        # Iniciar sesión
        self.client.login(username = self.username, password = self.password)
        self.assertIn('_auth_user_id', self.client.session)

        # Cambiar la contraseña
        response = self.client.post('/accounts/password/change/',
        {'old_password' : self.password,
         'new_password1' : self.new_password,
         'new_password2' : self.new_password})

        # Comprobar que el cambio se ha guardado en la base de datos
        user = User.objects.get(username = self.username)
        self.assertTrue(user.check_password(self.new_password))

        self.assertRedirects(response, '/accounts/password/change/done/')

    def test_password_change_failure(self):
        # Iniciar sesión
        self.client.login(username = self.username, password = self.password)
        self.assertIn('_auth_user_id', self.client.session)

        # Cambiar la contraseña con datos incorrectos
        response = self.client.post('/accounts/password/change/',
        {'old_password' : 'incorrect_old_pass',
         'new_password1' : 'incorrect_new_pass1',
         'new_password2' : 'incorrect_new_pass2'})

        # Comprobar que no se ha realizado ningún cambio
        user = User.objects.get(username = self.username)
        self.assertTrue(user.check_password(self.password))

#-------------------------------------------------------------------------------

class DeleteUserTest(DefaultTestCase):
    def test_delete_user_not_logged_user(self):
        # El usuario es redigido a la página de login
        response = self.client.get('/accounts/user/delete/')
        self.assertRedirects(response, '/accounts/login/?next=/accounts/user/delete/', target_status_code=302)

    def test_delete_user_success(self):
        # Iniciar sesión
        self.client.login(username = self.username, password = self.password)
        self.assertIn('_auth_user_id', self.client.session)

        # Enviar petición de borrado con confirmación correcta
        response = self.client.post('/accounts/user/delete/', {'username' : self.username})

        # Comprobar que el usuario ha sido eliminado de la base de datos
        query = User.objects.filter(username = self.username)
        self.assertFalse(query.exists())

        # Comprobar que se ha cerrado la sesión del usuario
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_delete_user_failure(self):
        # Iniciar sesión
        self.client.login(username = self.username, password = self.password)
        self.assertIn('_auth_user_id', self.client.session)

        # Enviar petición de borrado con confirmación incorrecta
        response = self.client.post('/accounts/user/delete/', {'username' : 'incorrect_username'})

        # Comprobar que el usuario NO ha sido eliminado de la base de datos
        query = User.objects.filter(username = self.username)
        self.assertTrue(query.exists())

        # Comprobar que se muestra el mensaje de error correspondiente
        self.assertContains(response, 'El nombre de usuario introducido no coincide con tu nombre de usuario.')
