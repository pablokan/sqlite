a = ['mesa', 10, 2.3]
aa = [f"'{e}'" if type(e)==str else str(e) for e in a]
field_values = ", ".join(aa)

print(field_values)