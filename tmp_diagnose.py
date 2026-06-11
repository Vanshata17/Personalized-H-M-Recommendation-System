import os
import sys
print('cwd=', os.getcwd())
print('python', sys.version)
print('sys.path[0]=', sys.path[0])
try:
    import recsys
    print('recsys imported', recsys.__file__)
    from recsys import hopsworks_integration
    from recsys.config import settings
    from recsys.features.customers import DatasetSampler
    print('DatasetSampler supported sizes:', DatasetSampler.get_supported_sizes())
except Exception as e:
    import traceback
    traceback.print_exc()
