import wikipedia 
import itertools
import threading
import time
import sys

#print(wikipedia.search('Egypt', results=15))

#print(wikipedia.geosearch(40.775114, -73.968802,title=None, results=10, radius=1000))

TitlesList = []
Results = []
print("")
topic = input('Please Enter The Topic  :  ')
n = int(input('Please Enter Number Of Result You Want [The Larger Number > The More Searching Time]   :  '))
for title in wikipedia.search(topic,n) :
    TitlesList.append(title)
print("") 
if n == 0:
    print(' You Entered [0] So There Is No Result For You Today :D ')
    exit()
print('[Please Wait] We Are Working Hard On The Following Topics')
print(TitlesList)
print("")
for x in range(100):
    sys.stdout.write('\rConnecting To Servers ....  ' +str(x))
    sys.stdout.flush()
    time.sleep(0.1)
time.sleep(5)

done = False
#here is the animation

#(['|', '/', '-', '\\'])
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rGrabing Data ....  ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")


t = threading.Thread(target=animate)
t.start()



for onetitle in TitlesList:
    titlePage = wikipedia.page(onetitle)
    Results.append(titlePage.content)
    time.sleep(10)

print('==============================================================================')
num = 0

done=True
for title in TitlesList:
    with open(title+'.txt', 'w', encoding="utf-8") as output:
        output.writelines(' ------ '+title+' ------ '+'\n')
        output.writelines('==================================================\n')
        output.writelines(Results[num])
        num = num+1
        output.writelines('\n')
        output.writelines('==================================================\n')
        print('  '+title+'  <-> Done')
        time.sleep(5)



