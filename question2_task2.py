def highestSpentCustomer(query_result):
    max_spent = 0
    customerHighest= None
    
    for rsult in query_result:
        customer_name = result["CustomeName"]
        total_spent = result["TotalSpent"]
        
        if total_spent  >max_spent:
            max_spent = total_spent
            customerHighest = {
                "customerName" : customer_name,
                "TotalSpent": max_spent
            }
    return customerHighest
