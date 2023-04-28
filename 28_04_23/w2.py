days = {
    'วันจันทร์':'Monday',
    'วันอังคาร':'Tuesday',
    'วันพุธ':'Wednesday',
    'วันพฤหัส':'Thursday',
    'วันศุกร์':'Friday',
    'วันเสาร์':'Saturday',
    'วันอาทิตย์':'Sunday'
}
select = days.keys() if input("Eng or Thai :").lower() == 'thai' else days.values()
for day in select:
    print(day)

#OUTPUT
"""
Eng or Thai :thai
วันจันทร์
วันอังคาร
วันพุธ
วันพฤหัส
วันศุกร์
วันเสาร์
วันอาทิตย์
"""