data = set()

for number in nums:
    if number in data:
        return True

    data.add(number)

return False 
