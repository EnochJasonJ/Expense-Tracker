from django.test import TestCase
from . import models
from django.urls import reverse
# Create your tests here.


class TestModels(TestCase):
    def test_expense(self):
        expense = models.Expense.objects.create(amount=249.99, merchant="amazon", description="anc headphones", category="Music")
        inserted_expense = models.Expense.objects.get(pk=expense.id)

        self.assertEqual(249.99, inserted_expense.amount)
        self.assertEqual("amazon", inserted_expense.merchant)
        self.assertEqual("anc headphones", inserted_expense.description)
        self.assertEqual("Music", inserted_expense.category)


class TestViews(TestCase):
    def test_expense_create(self):
        payload = {
            "amount": 50,
            "merchant": "AT & T",
            "description": "Cell Phone Subscription",
            "category": "Utilities"
        }

        res = self.client.post(reverse("restapi:expense-list-create"), payload, format="json")

        self.assertEqual(201 , res.status_code)

        json_res = res.json()

        self.assertEqual(str(payload["amount"]) , json_res["amount"])
        self.assertEqual(payload["merchant"] , json_res["merchant"])
        self.assertEqual(payload["description"] , json_res["description"])
        self.assertEqual(payload["category"] , json_res["category"])
        self.assertIsInstance(json_res["id"] , int)