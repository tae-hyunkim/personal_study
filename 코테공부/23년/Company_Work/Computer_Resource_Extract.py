# 윈도우 노트북에서 CPU/RAM/GPU Memory Check 

# H/W Spec 
## CPU : i5-8250-U
## RAM : 16GB (8GB * 2EA)
## GPU : Geforce GTX 1050

# GPU 사용량을 알기위해 Nvidia Drive, CUDA, Cudnn 작업을 진행하였으나 GPU 인식이 안됨
## 추가 작업 진행하기로 함 (23.07.01)
### visual studio 설치부터 하자.(Python Version과 매칭이 안됨)
### 추후 포맷한번 진행하면 작업하자. 


import psutil # CPU, Memory Resource Extract 
from tensorflow.python.client import device_lib

print('Using CPU Percent : {}'.format(psutil.cpu_percent()))
print('Using RAM Percent : {}'.format(psutil.virtual_memory().percent))
print(device_lib.list_local_devices())
