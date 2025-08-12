from abc import ABC, abstractmethod

class Promotion(ABC):
    @abstractmethod
    def apply(self, order_items, result_items, context):
        pass

class DoubleElevenPromotion(Promotion):
    def apply(self, order_items, result_items, context):
        total_amount = 0
        for item in order_items:
            qty = item['quantity']
            price = item['unitPrice']
            tens = qty // 10
            remain = qty % 10
            total_amount += tens * 10 * price * 0.8 + remain * price
        total_amount = int(total_amount)
        context['totalAmount'] = total_amount
        context['promotion_applied'] = True

class BuyOneGetOnePromotion(Promotion):
    def __init__(self, category):
        self.category = category
    def apply(self, order_items, result_items, context):
        for item in result_items:
            if item.get('category') == self.category:
                item['quantity'] = item['quantity'] + 1

class ThresholdDiscountPromotion(Promotion):
    def __init__(self, threshold, discount):
        self.threshold = threshold
        self.discount = discount
    def apply(self, order_items, result_items, context):
        original_amount = context.get('originalAmount', 0)
        if original_amount >= self.threshold:
            context['discount'] = context.get('discount', 0) + self.discount
