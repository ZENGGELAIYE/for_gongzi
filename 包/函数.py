import test1.mode1
import test1.mode2
test1.mode1.mode1_func()
test1.mode2.mode2_func()

from test1 import mode1
from test1 import mode2
mode1.mode1_func()
mode2.mode2_func()

from test1.mode1 import mode1_func
from test1.mode2 import mode2_func
mode1_func()
mode2_func()

from test1 import *
mode1.mode1_func()
mode2.mode2_func()
