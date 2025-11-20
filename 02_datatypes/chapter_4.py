is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling #upcastiing
print(f"Total actions (int + bool): {total_actions}")

milk_present = 0 # no milk : None, 0, False are considered as False
print(f"Is there milk ?{bool(milk_present)}")

water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print(f"Can we serve tea? {can_serve}")