# lernpfad/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib import admin
from module import models as module_models
from django.utils.html import format_html

class AccountManager(BaseUserManager):
    #https://dev.to/joshwizzy/customizing-django-authentication-using-abstractbaseuser-llg
    use_in_migrations = True

    def _create_user(self, email, name, phone, password, **extra_fields):
        values = [email, name, phone]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, phone, password, **extra_fields)

    def create_superuser(self, email, name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, name, phone, password, **extra_fields)

class QuizAnswer(models.Model):
    #https://stackoverflow.com/questions/50501420/how-do-i-save-user-specific-quiz-answers-in-django-models
    answer_option = models.ForeignKey(module_models.Antwort, on_delete=models.CASCADE)
    user = models.ForeignKey('Account', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.answer_option.frage) + ' - ' + str(self.answer_option.antwort_text)
        
        
class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nachname = models.CharField(max_length=150)
    vorname = models.CharField(max_length=150)
    phone = models.CharField(max_length=50, blank= True, default=0)
    date_of_birth = models.DateField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)
    
    @admin.display
    def get_quiz_answers(self):
        my_answers = QuizAnswer.objects.filter(user=self)
        answers = ''
        for answer in my_answers:
            answers += str(answer) + '\n'
        return answers
    #get_quiz_answers.boolean = True
    get_quiz_answers.short_description = 'quizanswers'
    #quiz_answer = models.ForeignKey('QuizAnswer', on_delete=models.CASCADE, blank=True, null=True)
    

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'nachname', 'vorname']

    def get_full_name(self):
        return self.name

    #def get_short_name(self):
    #    return self.name.split()[0]
        

