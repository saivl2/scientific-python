#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


for arr in picture:
    for num in range(len(arr)):
        if arr[num] == 0:
            arr[num] = ' '
        else:
            arr[num] = '*'
    pic = ''.join(arr)
    print(pic)

