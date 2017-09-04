from context import lagouSample
import time

start = time.time()

# company = input("Please enter the name of comany -> ")
jobList = lagouSample.lagou.lagouMethod("探探")

end = time.time()

print("The time usage to find job in {:s} is {:f} with timeout 20s".format(company,(end-start)))

start = time.time()

# company = input("Please enter the name of comany -> ")
jobList = lagouSample.lagou.lagouMethod("百度")

end = time.time()

print("The time usage to find job in {:s} is {:f} with timeout 20s".format(company,(end-start)))
