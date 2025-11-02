def energy_charge(units, rates):
    slabs = [100, 100, 300, float("inf")]  # slab sizes
    charge = 0.0
    remaining = units
    for slab, rate in zip(slabs, rates):
        take = min(remaining, slab)
        charge += take * rate
        remaining -= take
        if remaining <= 0:
            break
    return charge

def compute_bill(pu, cu, cust_type):
    if cu < pu:
        raise ValueError("Present month reading (CU) must be >= Previous month reading (PU).")
    units = cu - pu

    # Rates (per unit) by customer type and slabs
    rates = {
        "domestic": [3.00, 4.50, 6.00, 7.50],
        "commercial": [5.00, 6.50, 8.00, 9.50],
    }
    fixed_charges = {"domestic": 50.0, "commercial": 150.0}
    customer_charges = {"domestic": 25.0, "commercial": 75.0}
    ed_percent = {"domestic": 0.05, "commercial": 0.10}  # Electricity duty fraction

    key = cust_type.strip().lower()
    # accept common synonyms
    if key in ("household", "house", "home"):
        key = "domestic"
    if key not in rates:
        raise ValueError("Unknown customer type. Use 'commercial' or 'household' (or 'domestic').")

    ec = energy_charge(units, rates[key])
    fc = fixed_charges[key]
    cc = customer_charges[key]
    ed = ec * ed_percent[key]
    bill = ec + fc + cc + ed

    return {
        "Units": units,
        "EC": round(ec, 2),
        "FC": round(fc, 2),
        "CC": round(cc, 2),
        "ED": round(ed, 2),
        "Bill": round(bill, 2),
    }

def main():
    try:
        pu = float(input("Enter Previous Month Reading (PU): ").strip())
        cu = float(input("Enter Present Month Reading (CU): ").strip())
        cust_type = input("Enter Purpose (commercial/household): ").strip()

        result = compute_bill(pu, cu, cust_type)
        print("\n--- TSNPDCL ---")
        print(f"Units consumed           : {result['Units']}")
        print(f"EC (Energy Charges)      : {result['EC']:.2f}")
        print(f"FC (Fixed Charges)       : {result['FC']:.2f}")
        print(f"CC (Customer Charges)    : {result['CC']:.2f}")
        print(f"ED (Electricity Duty)    : {result['ED']:.2f}")
        print(f"Total Bill               : {result['Bill']:.2f}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()