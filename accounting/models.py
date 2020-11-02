from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import Q

class Account(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=512)
	balance = models.DecimalField(decimal_places=5, max_digits=20, default=0)
	clearance_period = models.IntegerField()
	TYPE = [
	    ('DA', 'Asset'),
	    ('DE', 'Expense'),
	    ('CL', 'Liability'),
	    ('CE', 'Equity'),
	]
	account_type = models.CharField(choices=TYPE, default='DA', max_length=2)

	def real_balance(self):
		# sum all transactions where the transaction clearance period
		# is greater than this account's clearance period, or is uncleared,
		# plus the balance on the Account.
		total = self.balance
		total += sum(t.amount for t in Transaction.objects.filter(debit=self))
		total -= sum(t.amount for t in Transaction.objects.filter(credit=self))
		if self.account_type[0]=='C':
			total = -total
		return total

	def __str__(self):
		return str({"name":self.name, "owner":self.owner})

class Transaction(models.Model):
	debit = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="debit")
	credit = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="credit")
	cleared = models.BooleanField()
	clearance_period = models.IntegerField()
	amount = models.DecimalField(decimal_places=5, max_digits=20, default=0)

	def __str__(self):
		return "amount={}  debit {} credit {} ".format(self.amount, self.debit, self.credit) 

class Clearance(models.Model):	
	clearance_period = models.AutoField(primary_key = True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "clearance_period {} date {}".format(self.clearance_period, self.date)
