import csv

invert = []

with open('inventory.csv', 'r') as invertory_file : 
    read_file = csv.DictReader(invertory_file)

    for read in read_file : 
        item = {
            'name' : read['Item'],
            'quantity' : int(read['Current Quantity']),
            'threshold' : int(read['Threshold'])
        }
        invert.append(item)

restock = []

for i in invert : 
    if i['quantity'] < i['threshold'] : 
        if i['quantity'] <= i['threshold'] *0.25 : 
            current = 'Critical'
        else : 
            current = 'low'

        order_again = i['threshold'] - i['quantity']

        restock.append({
            'Item' : i['name'],
            'Current Quantity' : i['quantity'],
            'threshold' : i['threshold'],
            'Priority' : current,
            'reorder items' : order_again,
        })

print('-----------warehouse Restock data---------')

for j in restock : 
    print(f'{j['Item']} ,',f' current : {j['Current Quantity']} ,', f'threshold : {j['threshold']} ,',f'Perority : {j['Priority']} , ',f'Reorder items : {j['reorder items']}')


with open('report.csv','w',newline="") as report_file : 
    fields = ['Item','Current Quantity','threshold','Priority','reorder items']

    writer = csv.DictWriter(report_file,fieldnames=fields)
    writer.writeheader()
    writer.writerows(restock)
