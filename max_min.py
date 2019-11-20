def minmax(data):
    if len(data):
        small = large = data[0]
        for value in data:
            if value<small: small = value 
            elif value>large: large = value  #don't necessarily need to assign this if small passes
        return (small, large)
        
    else:
        print ('Your data source is empty')
        return
