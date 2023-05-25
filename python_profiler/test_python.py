# define
start=2
end=1000000

#calculate mean in the range
total = sum(range(start,end+1))
mean = total/(end - start +1)

#print
print(f"The mean of the numbers in the range {start} to {end} is: {mean}")