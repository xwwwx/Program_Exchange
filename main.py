import Stock_list
import xlwt
st=[]
file = xlwt.Workbook()
table = file.add_sheet('stock',cell_overwrite_ok=True)
table.write(0,0,"股票名稱")
table.write(0,1,"獲利")
table.write(0,2,"累計ROI")
table.write(0,3,"ROI平均")
table.write(0,4,"ROI最大值")
table.write(0,5,"ROI最小值")
table.write(0,6,"ROI標準差")
table.write(0,7,"ROI勝率")
table.write(0,8,"交易次數")
k=1
for i in range(0,10000,1):
    a=i
    s=str(a)+'.tw'
    st.append(Stock_list.Stock_list())
    st[i].read(s)
    income=st[i].tactics()
    if income == 0 and st[i].getroisum() == 0 and st[i].getroimax() == 0 and st[i].getroimin() == 1 :
        continue
    table.write(k,0,s)
    table.write(k,1,income)
    table.write(k,2,st[i].getroisum())
    table.write(k,3,st[i].getroimean())
    table.write(k,4,st[i].getroimax())
    table.write(k,5,st[i].getroimin())
    table.write(k,6,st[i].getroistd())
    table.write(k,7,st[i].getroiwinp())
    table.write(k,8,st[i].getroilen())
    k += 1
    print(s,"done",k)
file.save('stock.xls') 