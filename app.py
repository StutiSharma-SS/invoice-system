from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-invoice', methods=['POST'])
def generate_invoice():
    item_names = request.form.getlist('item_name[]')
    quantities = request.form.getlist('quantity[]')
    prices = request.form.getlist('price[]')
    items = []
    subtotal = 0
    

    for i in range(len(item_names)):
        if item_names[i].strip() == '':
            continue
            
        qty = float(quantities[i])
        price = float(prices[i])
        item_total = qty * price
        subtotal += item_total
        item_data = {
            'name': item_names[i],
            'quantity': qty,
            'price': price,
            'total': item_total
        }
        items.append(item_data)
    
    # Calculate GST (18% of subtotal)CUSTOM FEATURE
    gst_rate = 0.18
    gst_amount = subtotal * gst_rate
    
    # Calculate grand total (subtotal + GST)CUSTOM FETURE
    grand_total = subtotal + gst_amount
    return render_template('invoice.html', 
                         items=items,
                         subtotal=subtotal,
                         gst_amount=gst_amount,
                         grand_total=grand_total,
                         gst_rate=gst_rate)

if __name__ == '__main__':
    app.run(debug=True)
