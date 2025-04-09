def calculate_paracetamol_volume(weight_kg, strength):  
    if weight_kg < 10 or weight_kg > 100:
        raise ValueError("The weight must between 10 and 100kg")
    # check if the weight is within a reasonable range
    if strength not in ["120mg/5ml", "250mg/5ml"]:
        raise ValueError("The strength of paracetamol must be '120mg/5ml'or'250mg/5ml'")
    # check whether the strength meets the expected requirements    
    dose_mg = 15 * weight_kg
    # calculate the required dosage (mg)
    if strength == "120mg/5ml":  # calculate volume (ml) based on the strength
        concentration = 120 / 5  
    else:  # 250mg/5ml
        concentration = 250 / 5 
    volume_ml = dose_mg / concentration
    return volume_ml

try:
    # normal condition 
    print(calculate_paracetamol_volume(20, "120mg/5ml"))  # output: 12.5
    print(calculate_paracetamol_volume(30, "250mg/5ml"))  # output: 9.0
    
    # abnormal condition
    print(calculate_paracetamol_volume(5, "120mg/5ml"))  # underweight
    print(calculate_paracetamol_volume(20, "500mg/5ml"))  # the strength is incorrrect
except ValueError as e:
    print(f"错误: {e}")