def det(A):
    if len(A) == 1:
        return A[0]
    elif len(A) == 4:
        return A[0]*A[3]-A[1]*A[2]
    elif len(A) == 9:
        return A[0]*A[4]*A[8]+A[3]*A[7]*A[2]+A[1]*A[5]*A[6]-A[2]*A[4]*A[6]-A[1]*A[3]*A[8]-A[0]*A[5]*A[7]
    elif len(A) == 16:
        M1 = [A[5], A[6], A[7],
              A[9], A[10], A[11],
              A[13], A[14], A[15]]
        M2 = [A[4], A[6], A[7],
              A[8], A[10], A[11],
              A[12], A[14], A[15]]
        M3 = [A[4], A[5], A[7],
              A[8], A[9], A[11],
              A[12], A[13], A[15]]
        M4 = [A[4], A[5], A[6],
              A[8], A[9], A[10],
              A[12], A[13], A[14]]
        return A[0]*det(M1)-A[1]*det(M2)+A[2]*det(M3)-A[3]*det(M4)
    else:
        return "No"


def krm(A, R):
    detA = det(A)
    if detA != 0:
        lenM = len(A)
        if lenM == 9:
            A1 = [R[0], A[1], A[2],
                  R[1], A[4], A[5],
                  R[2], A[7], A[8]]
            A2 = [A[0], R[0], A[2],
                  A[3], R[1], A[5],
                  A[6], R[2], A[8]]
            A3 = [A[0], A[1], R[0],
                  A[3], A[4], R[1],
                  A[6], A[7], R[2]]
            x = [(det(A1)/detA), (det(A2)/detA), (det(A3)/detA)]
        elif lenM == 1:
            x = [R[0]/A[0]]
        elif lenM == 16:
            A1 = [R[0], A[1], A[2], A[3],
                  R[1], A[5], A[6], A[7],
                  R[2], A[9], A[10], A[11],
                  R[3], A[13], A[14], A[15]]
            A2 = [A[0], R[0], A[2], A[3],
                  A[4], R[1], A[6], A[7],
                  A[8], R[2], A[10], A[11],
                  A[12], R[3], A[14], A[15]]
            A3 = [A[0], A[1], R[0], A[3],
                  A[4], A[5], R[1], A[7],
                  A[8], A[9], R[2], A[11],
                  A[12], A[13], R[3], A[15]]
            A4 = [A[0], A[1], A[2], R[0],
                  A[4], A[5], A[6], R[1],
                  A[8], A[9], A[10], R[2],
                  A[12], A[13], A[14], R[3]]
            x = [(det(A1)/detA), (det(A2)/detA),
                 (det(A3)/detA), (det(A4)/detA)]
        elif lenM == 4:
            A1 = [R[0], A[1],
                  R[1], A[3]]
            A2 = [A[0], R[0],
                  A[2], R[1]]
            x = [det(A1)/detA, det(A2)/detA]
        else:
            return "Error"
        return x
    else:
        return "Det(A)=0"


def res(a,b):
    x = krm(a, b)
    
    if len(x) == 3:
        print(f"""x = {x[0]}
y = {x[1]}
z = {x[2]}""")
    elif len(x) == 2:
        print(f"""x = {x[0]}
y = {x[1]}""")
    elif len(x) == 1:
        print(f"x = {x[0]}")
    elif x == "Error":
        print("Error")
    elif x == "Det(A)=0":
        print("Det(A)=0")
    else:
        print(f"""x = {x[0]}
y = {x[1]}
z = {x[2]}
t = {x[3]}""")
    
    
    
    
a = [1,2,3,4,5,6,7,8,8,7,6,5,4,3,2,1]
b = [1,1,1,1]



res(a,b)

