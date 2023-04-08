'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stucked then read the hint                   ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net_product = 0.0
    net_payment = 0.0

    for item in order.items:
        if item.type == 'payment':
            net_payment += item.amount
        elif item.type == 'product':
            net_product -= item.amount * item.quantity
        else:
            return("Invalid item type: %s" % item.type)
    
    total = net_product + net_payment

    if not(total < 0.001 and total > -0.001):
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, total))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
