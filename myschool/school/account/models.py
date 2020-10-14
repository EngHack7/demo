from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser
from django.contrib.auth.hashers import make_password


class MyAccountManager(BaseUserManager):
	def create_user(self, the_id_number, username, password=None):
		

		if not the_id_number:
			raise ValueError('Users must have an the_id_number ')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			the_id_number = the_id_number,
			username=username,
			
		)
		
		user.password = make_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, the_id_number, username, password):
		

		user = self.create_user(
			the_id_number=the_id_number,
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Grades(models.Model):
	grade = models.IntegerField(unique=True)
	

	def __str__(self):
		return (str(self.grade))
	# def __unicode__(self):
	#     return u'%s' % (self.id)

class Account(AbstractBaseUser):
	the_id_number = models.IntegerField( unique=True ,  verbose_name="the_id_number" , null=True )
	grades = models.ForeignKey(Grades , on_delete=models.CASCADE ,blank=True , null=True , default=None)
	email = models.EmailField( max_length=60 , unique=True , verbose_name= "email" , null=True , blank=True )
	username = models.CharField(max_length=50 , unique= True)
	date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin =  models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'the_id_number' 
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	def __str__(self):
		return self.username

	# For checking permissions. to keep it simple all admin have ALL permissions
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True






class Subject(models.Model):
	subject = models.CharField(max_length=20 , unique=True)
	grade = models.ForeignKey(Grades , on_delete=models.CASCADE)

	def __str__(self):
		return self.subject

class Videos(models.Model):
	videos_URL = models.URLField(max_length=200)
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	subject = models.ForeignKey(Subject , on_delete=models.CASCADE)
	date_add = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	
	def __str__(self):
		return self.title

class TeacherNotes (models.Model):
	teacher_id = models.IntegerField()
	note = models.TextField()
	date = models.CharField(max_length=10)
	student_id = models.IntegerField() 
	is_read = models.BooleanField(default=False)

