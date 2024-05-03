from django.test import TestCase
from . import models
# Create your tests here.


class TestModels(TestCase):
    def test_expense(self):
        expense = models.Expense.objects.create(amount=249.99, merchant="amazon", description="anc headphones", category="Music")
        inserted_expense = models.Expense.objects.get(pk=expense.id)

        self.assertEqual(249.99, inserted_expense.amount)
        self.assertEqual("amazon", inserted_expense.merchant)
        self.assertEqual("anc headphones", inserted_expense.description)
        self.assertEqual("Music", inserted_expense.category)


