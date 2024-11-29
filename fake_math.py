def dev(first,second):
    if second == 0 :
        return "ОШИБКА"
    else :
        return float(first/second)

# Test block

if __name__ == "__main__" :
      print(dev(1,0))

