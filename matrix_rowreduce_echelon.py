import logging

logger = logging.getLogger(__name__)


"""
    Row reduced echlon form
"""
def row_reduced_echlon(M, sd):   
    if not M: return
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    A = M[:] # Making a copy of matrix
    # logger.debug("Matrix {0}".format(A))
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while A[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        A[i],A[r] = A[r],A[i]
        lv = A[r][lead]

        A[r] = [ round((mrx / float(lv)), sd) for mrx in A[r]]
        # logger.debug("Alpha value with significant digit {0} : {1}".format(sd, A[r]))
        for i in range(rowCount):
            if i != r:
                lv = A[i][lead]
                A[i] = [ iv - lv*rv for rv,iv in zip(A[r],A[i])]
                # logger.debug("Computed value {0} ".format(A[i]))
        lead += 1
        
    return A # Return the rref matrix


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    # reduced = row_reduced_echlon(A)
    mtx_p = [[1.0000, 1.0000, 1.0000],[0.0003, 3.0000, 2.0001],]
    mtx_wp = [[0.0003, 3.0000, 2.0001],[1.0000, 1.0000, 1.0000],]

    print("---"*30 +"\n\t\t\t\t with Pivoting \t\t\twithout Pivoting\n"+ "---"*30 +"\nSignificant Digit\t|\t X1 \t|\t X2 \t|\t X1 \t|\t X2 \t|\n"+ "---"*30)
    for s in range(3, 8):
        rref_m = row_reduced_echlon(mtx_p, s)
        rref_mp = row_reduced_echlon(mtx_wp, s)

        print("\t{0} \t\t| {1} \t| {2} \t| {3} \t\t| {4} \t|".format(s, round(rref_m[0][2], s), round(rref_m[1][2], s), round(rref_mp[0][2], s), round(rref_mp[1][2],s)))
