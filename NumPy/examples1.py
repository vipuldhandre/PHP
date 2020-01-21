##import numpy as np
##
##a = np.array([1,2,3])
##print(a)
##print(type(a))

##import numpy as np
##
##a = np.array([[1,2,3],[4,5,1]])
##print(a)
##print(type(a))    

##import numpy as np
##
##a = np.array([[1,2,3],[1,2]])
##print(a)
##print(type(a))

##import numpy as np
##
##a = np.array([1,2,3],ndmin=2)
##print(a)
##a = np.array([1,2,3],ndmin=3)
##print(a)

##import numpy as np
##
##a = np.array([[1,2,3],[1,2,3]],dtype=complex)
##print(a)

import numpy as np

student  = np.dtype([('name','S20'),('age','i4'),('marks','f8')])

a = np.array([('vipul',22,99.99),('vikas',25,90)],dtype=student)

print(a)
















