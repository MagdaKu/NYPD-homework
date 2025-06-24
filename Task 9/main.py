import numpy as np

if __name__ == "__main__":
    file = np.load("sample_treated.npz")
    outputs = file["outputs"] # size (1000,200)

    #option 1 - we identify the objects whose size at some point is at least double their initial size
    indices = []
    for i in range(len(outputs)):
        if np.max(outputs[i]) >= 2*outputs[i][0]:
            indices.append(i)
    print("Indices of objects that at some point doubled their initial size: ")
    print(np.array(indices))
    print("----------------------------------")

    #option 2 - we check if the last observation is around twice the initial size 
    mask = np.isclose(outputs[:, -1], 2 * outputs[:, 0], rtol=0.1)
    indices = np.where(mask)[0]
    print("Indices of objects whose final size is twice the initial size: ")
    print(indices)