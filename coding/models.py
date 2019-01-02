from django.db import models

class zira(models.Model):
	ticket_num = models.IntegerField()
	issue_description = models.CharField(max_length=10000)
	uploaded_by = models.CharField(max_length=100)
	date = models.DateField(auto_now=True,auto_now_add=False)

	def __str__(self):
		return str(self.ticket_num)