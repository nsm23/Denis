from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migration = True

    def _create_user(self, username=None,
                     email=None, phone=None,
                     password=None, **user_fields):
        if not username:
            if not email and not phone:
                raise ValueError('Enter email/phone to continue')
        if email:
            email = self.normalize_email(email)
            if not username:
                username = email
            user = self.model(email=email,
                              username=username,
                              **user_fields)
        if phone:
            if not username:
                username = phone
            user = self.model(username=username,
                              phone=phone,
                              **user_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_user(self, username, email,
                    password, **user_fields):
        user_fields.setdefault('is superuser', False)
        return self._create_user(self, username=username,
                                 email=email, password=password, **user_fields)

    def create_superuser(self, username, password, **user_fields):
        user_fields.setdefault('is_superuser', True)
        user_fields.setdefault('is_staff', True)
        user_fields.setdefault('is_active', True)
        return self._create_user(username=username,
                                 password=password,
                                 **user_fields)




