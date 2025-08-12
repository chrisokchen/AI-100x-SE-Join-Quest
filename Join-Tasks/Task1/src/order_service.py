from src.promotion import DoubleElevenPromotion, BuyOneGetOnePromotion, ThresholdDiscountPromotion

class OrderService:
    def __init__(self):
        pass

    def process_order(self, order_items, promotions):
        # 計算原始總金額
        original_amount = 0
        result_items = []
        for item in order_items:
            original_amount += item['quantity'] * item['unitPrice']
            result_items.append({
                'productName': item['productName'],
                'quantity': item['quantity'],
                'category': item.get('category', None)
            })

        # promotion context
        context = {
            'originalAmount': original_amount,
            'discount': 0,
            'totalAmount': None,
            'promotion_applied': False
        }

        # 將 promotions dict 轉為 Promotion 物件
        promotion_objs = []
        for p in promotions:
            if p.get('type') == 'double_eleven':
                promotion_objs.append(DoubleElevenPromotion())
            elif p.get('type') == 'buy_one_get_one':
                promotion_objs.append(BuyOneGetOnePromotion(p['category']))
            elif p.get('type') == 'threshold_discount':
                promotion_objs.append(ThresholdDiscountPromotion(p['threshold'], p['discount']))

        # 依序套用促銷
        for promo in promotion_objs:
            promo.apply(order_items, result_items, context)

        # 如果 double eleven 有作用，直接回傳
        if context.get('promotion_applied') and context.get('totalAmount') is not None:
            return {
                'totalAmount': context['totalAmount'],
                'originalAmount': None,
                'discount': None,
                'items': result_items
            }

        # 處理 threshold_discount
        total_amount = original_amount - context.get('discount', 0)
        return {
            'totalAmount': total_amount,
            'originalAmount': original_amount,
            'discount': context.get('discount', 0),
            'items': result_items
        }
