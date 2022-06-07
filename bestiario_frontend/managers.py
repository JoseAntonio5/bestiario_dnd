from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, nome, senha, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not nome:
            raise ValueError(('nome obrigatorio'))
        user = self.model(nome=nome, **extra_fields)
        user.set_password(senha)
        user.save()
        return user

    def create_superuser(self, nome, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(nome, password, **extra_fields)