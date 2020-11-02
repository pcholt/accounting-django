from django.shortcuts import render
from django.http import JsonResponse
from . import models
from django.db.models import Q

# Create your views here.
def home(self):
	return JsonResponse({
		"accounts": accounts(),
		})

def accounts():
	return [
		{
			"name": account.name,
			"balance": account.balance,
			"real_balance": account.real_balance(),
			"transactions": transactions(account)
		}
		for account in models.Account.objects.all()
	]

def transactions(account):
	return [
		{
			"type": 
				("credit" if transaction.credit==account else "debit" if transaction.debit==account else ""),
			"amount": transaction.amount,
		}
		for transaction in models.Transaction.objects.filter(Q(credit=account)|Q(debit=account))
	]