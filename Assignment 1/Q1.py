print("Yahya Shamim")
print("24k-0020")
print("Q1")
print()

transactionLog = [
    {'orderId': 1001, 'customerId': 'cust_Ahmed', 'productId': 'prod_10'},
    {'orderId': 1001, 'customerId': 'cust_Ahmed', 'productId': 'prod_12'},
    {'orderId': 1002, 'customerId': 'cust_Bisma', 'productId': 'prod_10'},
    {'orderId': 1002, 'customerId': 'cust_Bisma', 'productId': 'prod_15'},
    {'orderId': 1003, 'customerId': 'cust_Ahmed', 'productId': 'prod_15'},
    {'orderId': 1004, 'customerId': 'cust_Faisal', 'productId': 'prod_12'},
    {'orderId': 1004, 'customerId': 'cust_Faisal', 'productId': 'prod_10'}
]

productcatalog = {
    'prod_10': 'Wireless Mouse',
    'prod_12': 'Keyboard',
    'prod_15': 'USB-C Hub',
}

def processTransactions(transactionlist):
    customer_products = {}
    for entry in transactionlist:
        cust_id = entry['customerId']
        item_id = entry['productId']
        
        customer_exists = False
        for existing_cust in customer_products.keys():
            if existing_cust == cust_id:
                customer_exists = True
                break
                
        if not customer_exists:
            customer_products[cust_id] = []
            
        customer_products[cust_id].append(item_id)

    return customer_products

def findFrequentPairs(customerData):
    pair_frequency = {}
    for customer in customerData.keys():      
        items = customerData[customer]
        item_count = len(items)
        
        for i in range(item_count):
            for j in range(i+1, item_count):
                if i == j:
                    continue
                product_pair = tuple(sorted([items[i], items[j]]))
                if product_pair in pair_frequency:
                    pair_frequency[product_pair] += 1
                else:
                    pair_frequency[product_pair] = 1

    return pair_frequency

def getRecommendations(targetProductId, frequentPairs):
    recommendation_items = []
    for productA, productB in frequentPairs:
        if targetProductId == productA:
            recommendation_items.append((productB, frequentPairs[(productA, productB)]))
        elif targetProductId == productB:
            recommendation_items.append((productA, frequentPairs[(productA, productB)]))
    
    def sort_key(item):
        return item[1]

    recommendation_items.sort(key=sort_key, reverse=True)

    return recommendation_items

def generateReport(targetProductId, recommendations, Catalog):
    print("Analysis for:", Catalog[targetProductId])
    print("Top companion products:")
    
    for position, item in enumerate(recommendations, start=1):
        product_code = item[0]
        count = item[1]
        print(f"{position}. {Catalog[product_code]} (co-purchased {count} times)")

customer_results = processTransactions(transactionLog)
print("Customer purchase summary:", customer_results)
print()

pair_results = findFrequentPairs(customer_results)
print("Product pairing analysis:", pair_results)
print()

suggestions = getRecommendations('prod_12', pair_results)
generateReport('prod_12', suggestions, productcatalog)