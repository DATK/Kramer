def det(A):
    if len(A) == 1:
        return A[0]
    elif len(A) == 4:
        return A[0]*A[3]-A[1]*A[2]
    elif len(A) == 9:
        return A[0]*A[4]*A[8]+A[3]*A[7]*A[2]+A[1]*A[5]*A[6]-A[2]*A[4]*A[6]-A[1]*A[3]*A[8]-A[0]*A[5]*A[7]
    else:
        return "No"


def krm(A, R, m="3x3"):
    detA = det(A)
    if detA != 0:
        A1 = [R[0], A[1], A[2], R[1], A[4], A[5], R[2], A[8], A[8]]
        A2 = [A[0], R[0], A[2], A[3], R[1], A[5], A[6], R[2], A[8]]
        A3 = [A[0], A[1], R[0], A[3], A[4], R[1], A[6], A[7], R[2]]
        x = [(det(A1)/detA), (det(A2)/detA), (det(A3)/detA)]
        return x
    else:
        return "Det(A)=0"


a = [4,-3,2,2,5,-3,5,6,-2]
b = [9,4,18]


x=krm(a, b)

print(f"""x = {x[0]}
y = {x[1]}
z = {x[2]}""")
