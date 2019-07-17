import display
import operations
import read
import store
if __name__=="__main__":
    data=read.read_csv()
    lis=operations.csvOperations(data)
    display.display(lis)
    store.store_results(lis)