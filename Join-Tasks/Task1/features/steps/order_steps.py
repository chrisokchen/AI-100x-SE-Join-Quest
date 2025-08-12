import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from behave import given, when, then
from src.order_service import OrderService


@given('no promotions are applied')
def step_no_promotions(context):
    context.order_service = OrderService()
    context.promotions = []

@given('the double 11 promotion is active')
def step_double11_promotion_active(context):
    if not hasattr(context, 'order_service'):
        context.order_service = OrderService()
        context.promotions = []
    context.promotions.append({
        'type': 'double_eleven'
    })

@when('a customer places an order with')
def step_place_order(context):
    context.order_items = []
    for row in context.table:
        item = {
            'productName': row['productName'],
            'quantity': int(row['quantity']),
            'unitPrice': int(row['unitPrice'])
        }
        # 如果有 category 欄位，加入 category 資訊
        if 'category' in row.headings:
            item['category'] = row['category']
        
        context.order_items.append(item)
    
    context.order_result = context.order_service.process_order(context.order_items, context.promotions)


@then('the order summary should be')
def step_verify_order_summary(context):
    for row in context.table:
        if 'totalAmount' in row.headings:
            expected_total = int(row['totalAmount'])
            assert context.order_result['totalAmount'] == expected_total, \
                f"Expected totalAmount {expected_total}, got {context.order_result['totalAmount']}"
        
        if 'originalAmount' in row.headings:
            expected_original = int(row['originalAmount'])
            assert context.order_result['originalAmount'] == expected_original, \
                f"Expected originalAmount {expected_original}, got {context.order_result['originalAmount']}"
        
        if 'discount' in row.headings:
            expected_discount = int(row['discount'])
            assert context.order_result['discount'] == expected_discount, \
                f"Expected discount {expected_discount}, got {context.order_result['discount']}"


@then('the customer should receive')
def step_verify_received_items(context):
    for row in context.table:
        product_name = row['productName']
        expected_quantity = int(row['quantity'])
        
        found = False
        for item in context.order_result['items']:
            if item['productName'] == product_name:
                assert item['quantity'] == expected_quantity, \
                    f"Expected {product_name} quantity {expected_quantity}, got {item['quantity']}"
                found = True
                break
        
        assert found, f"Product {product_name} not found in order result"


@given('the threshold discount promotion is configured')
def step_threshold_discount_config(context):
    context.order_service = OrderService()
    context.promotions = []
    for row in context.table:
        context.promotions.append({
            'type': 'threshold_discount',
            'threshold': int(row['threshold']),
            'discount': int(row['discount'])
        })


@given('the buy one get one promotion for cosmetics is active')
def step_bogo_cosmetics_config(context):
    if not hasattr(context, 'order_service'):
        context.order_service = OrderService()
        context.promotions = []
    
    context.promotions.append({
        'type': 'buy_one_get_one',
        'category': 'cosmetics'
    })
