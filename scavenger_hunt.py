import matplotlib.pyplot as plt
import numpy as np

def read_waveforms(LA, RV, RA) :
    infile = open('waveforms.csv', 'r')

    line = infile.readline()
    wf = 0 # which waveform are we trying to read (0 = LA, 1 = RV, 2 = RA)

    while line :
        line = line.strip()
        data = line.split(',')

        for i in range(0, len(data)) : 
            data[i] = float(data[i])

        if(wf == 0) :
            LA.append(data)
        elif(wf == 1) :
            RV.append(data)
        elif(wf == 2) :
            RA.append(data)
        
        wf = (wf + 1) % 3
        line = infile.readline()

    infile.close()

def read_times(TL, TR) :
    infile = open('times.csv', 'r')
    line = infile.readline()
    data = line.strip().split(',')

    for i in range(0, len(data)):
        data[i] = float(data[i]) * 1000

    TL.append(data)

    line = infile.readline()
    data = line.strip().split(',')

    for i in range(0, len(data)) : 
        data[i] = float(data[i])

    TR.append(data)
    infile.close()

def plot_waveforms(LA, RV, RA, TL, TR) :
    print('create your individual waveform plots here')


# make empty data and time Lists
LA_list = []
RV_list = []
RA_list = []
TL_list = []
TR_list = []

read_waveforms(LA_list, RV_list, RA_list)
read_times(TL_list, TR_list)

# convert all data and time lists to numpy arrays for plotting
LA = np.array(LA_list)
RV = np.array(RV_list)
RA = np.array(RA_list)
TL = np.array(TL_list[0])
TR = np.array(TR_list[0])


MLA = []
ALA = []
PLA = []
MRV = []
ARV = []
PRV = []
MRA = []
ARA = []
PRA = []

for i in range(65):
#     a = []
#     a1 = []
#     a2 = []
#     a.append(np.min(RV[i]))
#     a1.append(np.mean(RV[i]))
#     a2.append(np.max(RV[i]))
#     MRV.append(a)
#     ARV.append(a1)
#     PRV.append(a2)
    a3 = []
    a4 = []
    a5 = []
    a3.append(np.min(RA[i]))
    a4.append(np.mean(RA[i]))
    a5.append(np.max(RA[i]))
    MRA.append(a3)
    ARA.append(a4)
    PRA.append(a5)
# print(np.min(MRV))
# print(np.max(MRV))
# print(np.mean(MRV))
# print(np.min(ARV))
# print(np.max(ARV))
# print(np.mean(ARV))
# print(np.min(PRV))
# print(np.max(PRV))
# print(np.mean(PRV))
print(np.min(MRA))
print(np.max(MRA))
print(np.mean(MRA))
print(np.min(ARA))
print(np.max(ARA))
print(np.mean(ARA))
print(np.min(PRA))
print(np.max(PRA))
print(np.mean(PRA))
# plt.plot(MRV)
# plt.title('Min Rot Velocity')
# plt.xlabel('Instance)')
# plt.ylabel('Rot Velocity')
# plt.xticks(np.arange(0, 70, step=5))
# plt.savefig('Instance4.png')
# plt.close()
# plt.plot(ARV)
# plt.title('Average Rot Velocity')
# plt.xlabel('Instance)')
# plt.ylabel('Rot Velocity')
# plt.xticks(np.arange(0, 70, step=5))
# plt.savefig('Instance5.png')
# plt.close()
# plt.plot(PRV)
# plt.title('Peak Rot Velocity')
# plt.xlabel('Instance)')
# plt.ylabel('Rot Velocity')
# plt.xticks(np.arange(0, 70, step=5))
# plt.savefig('Instance6.png')
# plt.close()
plt.plot(MRA)
plt.title('Min Rot Acceleration')
plt.xlabel('Instance)')
plt.ylabel('Rot Acceleration')
plt.xticks(np.arange(0, 70, step=5))
plt.savefig('Instance7.png')
plt.close()
plt.plot(ARA)
plt.title('Average Rot Acceleration')
plt.xlabel('Instance)')
plt.ylabel('Rot Acceleration')
plt.xticks(np.arange(0, 70, step=5))
plt.savefig('Instance8.png')
plt.close()
plt.plot(PRA)
plt.title('Peak Rot Acceleration')
plt.xlabel('Instance)')
plt.ylabel('Rot Acceleration')
plt.xticks(np.arange(0, 70, step=5))
plt.savefig('Instance9.png')
plt.close()

plt.scatter(ARV, PRV)
plt.ylabel('F1')
plt.xlabel('F2')
plt.title('Features')
plt.xlim(0,7)
plt.ylim(0,3)
plt.savefig('scatter.png')
plt.close()