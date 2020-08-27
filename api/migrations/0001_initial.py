from django.db import migrations
from api.user.models import CustomUser



class Migration(migrations.Migration):
	def seed_data(apps, schema_editor):
		user = CustomUser(first_name="harish",
            last_name="more",
			email = "harishmore05@gmail.com",
			is_staff = True,
			is_superuser = True,
			)
		user.set_password("12345")
		user.save()

	dependencies = [

	]

	operations = [
		migrations.RunPython(seed_data),
	]