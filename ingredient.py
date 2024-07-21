# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:51:54 2024

@author: Amitr
"""

from datetime import datetime
import re

class Ingredient:
    def __init__(self, name, quantity, unit, expiry_date=None):
        if not re.match(r'^[\w\s]+$', name):
            raise ValueError("Ingredient name should be alphanumeric and can include spaces")
        if not isinstance(quantity, (int, float)):
            raise ValueError("Ingredient quantity should be numeric")
        if unit not in ['g', 'kg', 'ml', 'l', 'units']:
            raise ValueError("Invalid unit for ingredient")

        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.expiry_date = expiry_date

    def is_expired(self):
        if self.expiry_date:
            return datetime.now() > self.expiry_date
        return False

    def __repr__(self):
        expiry_status = "Expired" if self.is_expired() else "Not expired"
        return f"{self.name} ({self.quantity} {self.unit}) - {expiry_status}"

# Example usage
# ingredient = Ingredient('tomato', 200, 'g', datetime(2024, 7, 21))
