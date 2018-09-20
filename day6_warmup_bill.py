def calc_bill(bill, tax_pct, tip_pct):
    print(bill, tax_pct/100, tip_pct/100)
    bill_before_tip=bill + bill*(tax_pct/100)
    bill_with_tip=bill_before_tip + bill_before_tip*(tip_pct/100)
    return(bill_before_tip, bill_with_tip)

if __name__ == '__main__':
    bill=int(input("Input amount of bill: "))
    tax_pct=int(input("Input tax rate,: "))
    tip_pct=int(input("Input tip rate: "))
    bill_before_tip,bill_with_tip=calc_bill(bill, tax_pct, tip_pct)
    print(bill_before_tip, bill_with_tip)


   