#!/usr/bin/python3
#pylint: disable= duplicate-code
'''
Enumerations defined to standardize names.
'''
#######################        MANDATORY IMPORTS         #######################
import sys
import os
#######################         GENERIC IMPORTS          #######################
from datetime import datetime
#######################       THIRD PARTY IMPORTS        #######################
from sqlalchemy import select, insert
#######################    SYSTEM ABSTRACTION IMPORTS    #######################
from system_logger_tool import sys_log_logger_get_module_logger
if __name__ == '__main__':
    from system_logger_tool import SysLogLoggerC
    cycler_logger = SysLogLoggerC(file_log_levels="code/log_config.yaml")
log = sys_log_logger_get_module_logger(__name__)

#######################          PROJECT IMPORTS         #######################

#######################          MODULE IMPORTS          #######################
sys.path.append(os.getcwd()+'/code/')
from drv_db.src.wattrex_driver_db import DrvDbSqlEngineC, DrvDbTypeE, DrvDbCacheExperimentC, \
    DrvDbCacheGenericMeasureC, DrvDbCacheStatusC, DrvDbCacheExtendedMeasureC,\
    DrvDbAlarmC, DrvDbCyclingModeE

#######################              ENUMS               #######################

#######################             CLASSES              #######################

def test_read() -> None:
    """Runs the test read command from cache database.
    """
    drv = DrvDbSqlEngineC(db_type=DrvDbTypeE.CACHE_DB,
                          config_file='code/drv_db/tests/.cred_cache.yaml')
    stmt = select(DrvDbCacheExperimentC)
    result = drv.session.execute(stmt).all()
    row: DrvDbCacheExperimentC = result[0][0]
    print(row.__dict__)

    gen_meas = {'ExpID': 1,'Voltage': 4000, 'Current': 1000, 'Power': 4000, 'InstrID': 1,
                'PwrMode': DrvDbCyclingModeE.CC}
    stmt = insert(DrvDbCacheGenericMeasureC).values(Timestamp= datetime.now(), MeasID= 3,
                                                   **gen_meas)
    drv.session.execute(stmt)

    stmt = select(DrvDbCacheGenericMeasureC).where(DrvDbCacheGenericMeasureC.MeasID == 3)
    result = drv.session.execute(stmt).all()
    row : DrvDbCacheGenericMeasureC = result[0][0]
    print(row.__dict__)

    stmt = select(DrvDbCacheGenericMeasureC)
    result = drv.session.execute(stmt).all()
    row : DrvDbCacheGenericMeasureC = result[0][0]
    print(row.__dict__)

    stmt = select(DrvDbAlarmC)
    result = drv.session.execute(stmt).all()
    row : DrvDbAlarmC = result[0][0]
    print(row.__dict__)

    stmt = select(DrvDbCacheStatusC)
    result = drv.session.execute(stmt).all()
    row : DrvDbCacheStatusC = result[0][0]
    print(row.__dict__)


    stmt = select(DrvDbCacheExtendedMeasureC)
    result = drv.session.execute(stmt).all()
    row : DrvDbCacheExtendedMeasureC = result[0][0]
    print(row.__dict__)
    drv.session.commit()
    drv.session.close()

if __name__ == '__main__':
    test_read()
