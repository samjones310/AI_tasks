import prettytable
def display(data):
    #tab=tt.TextTable()
    tab=prettytable.PrettyTable(data[0])
    for i in range(1,len(data)):
        tab.add_row(data[i])
    print(tab)