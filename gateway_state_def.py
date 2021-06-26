from gatewaycallbacks import *
# Mongodb definitions
MONGODB_CLIENT_PORT = 27017
WAITING_FOR_DATA_TOUT = 1800  # Waitintg for data is set to 30 minutes,double the data interval
KAFKA_SERVER ='192.168.43.231:9092'
KAFKA_DATA_TOPIC ='data_queue'
KAFKA_CONTROL_TOPIC = 'control_queue'

''' Defining Gateway states '''

ST_GW_CREATE_INITIAL ="01"
ST_GW_ONLINE =  "02"
ST_GW_OFFLINE = " 03"
ST_GW_MAINTENANCE = "04"

''' GW Event definitions '''

EV_GW_Config_Trigger ='001'
EV_GW_TelemetryDataReceived = '002'
EV_GW_SensorDataReceived ='003'
EV_GW_KeepAliveReceived = '004'
EV_GW_WaitingforDataTimerExpired ='005'
EV_GW_WaitingForDiagFailed = '006'
EV_GW_DiagnosticsPassed ='007'
EV_GW_CPUUtalisationHigh ='008'
EV_GW_MemUtalisationHigh ='009'
EV_GW_WorkOrderAckReceived ='010'
EV_GW_ConnectionLost ='011'
EV_GW_WaitingForWorkOrderAckExpired ='012'
EV_GW_WaitingForDiagTimerExpired ='013'
EV_GW_BatteryLow ='014'
EV_GW_AdminOnline ='015'
EV_GW_AdminOffline ='016'
EV_GW_AdminMaintenance ='017'
EV_GW_MaintenanceWindowExpired ='018'
EV_GW_CFG_Available = '019'

NULL = None
''' Gateway states '''
gateway_states = [ST_GW_CREATE_INITIAL, ST_GW_ONLINE, ST_GW_OFFLINE, ST_GW_MAINTENANCE]

'''Current state (src)
Next state (dst)
rule for transition (Event)
callback for the transition (callback)
'''
'''{'Current state':,'Prev state':,'Prev Event':,'Current event':, 'next state':, 'Action towards GW':'Action towards Field':,'Timer action':,'Action towards Admin': },'''
GW_FSM_MAP = (
	{'current_state': ST_GW_CREATE_INITIAL,'prev_state':NULL,'prev_event':EV_GW_CFG_Available,'curr_event':EV_GW_TelemetryDataReceived,'next_state': ST_GW_ONLINE,'ActionTowardsDevice': NULL,'ActionTowardsField':NULL,'TimerAction':tWaitingForDataHandler,'ActionTowardsAdmin':stateChange},
	{'current_state': ST_GW_CREATE_INITIAL,'next_state': ST_GW_ONLINE,'event': EV_GW_KeepAliveReceived, 'callback' : processDataInCreateInitial},
	{'current_state': ST_GW_ONLINE,'next_state': ST_GW_ONLINE,'event':  EV_GW_WaitingforDataTimerExpired  , 'callback' : processWaitingForDataTimerExpired},
	{'current_state': ST_GW_ONLINE,'next_state': ST_GW_ONLINE,'event':  EV_GW_DiagnosticsPassed  , 'callback' : processDiagnosticPassed},
	{'current_state': ST_GW_ONLINE,'next_state': ST_GW_ONLINE,'event':  EV_GW_WaitingForDiagTimerExpired  , 'callback' : processDiagnosticTimerExpired},
	{'current_state': ST_GW_ONLINE,'next_state': ST_GW_ONLINE,'event':  EV_GW_CPUUtalisationHigh  , 'callback' : processCPUUtalisationHigh},
	{'current_state': ST_GW_ONLINE,'next_state': ST_GW_ONLINE,'event':  EV_GW_MemUtalisationHigh  , 'callback' : processMemUtalisationHigh},
	{'current_state': ST_GW_ONLINE,'next_state': ST_GW_OFFLINE,'event': EV_GW_ConnectionLost  , 'callback' : processGWConnectionLost},
	{'current_state': ST_GW_ONLINE,'next_state': ST_GW_ONLINE,'event': EV_GW_BatteryLow , 'callback' : processGWBatteryLow},
	{'current_state': ST_GW_ONLINE,'next_state': ST_GW_OFFLINE,'event': EV_GW_AdminOffline , 'callback' : processGWAdminOffline},
	{'current_state': ST_GW_ONLINE,'next_state': ST_GW_ONLINE,'event': EV_GW_WorkOrderAckReceived , 'callback' : processGWWOAckReceived},
	
	{'current_state': ST_GW_CREATE_INITIAL,'next_state': ST_GW_ONLINE,'event': EV_GW_KeepAliveReceived, 'callback' : processDataInCreateInitial},
	{'current_state': ST_GW_CREATE_INITIAL,'next_state': ST_GW_ONLINE,'event': EV_GW_KeepAliveReceived, 'callback' : processDataInCreateInitial},
	{'current_state': ST_GW_CREATE_INITIAL,'next_state': ST_GW_ONLINE,'event': EV_GW_KeepAliveReceived, 'callback' : processDataInCreateInitial},
	{'current_state': ST_GW_CREATE_INITIAL,'next_state': ST_GW_ONLINE,'event': EV_GW_KeepAliveReceived, 'callback' : processDataInCreateInitial},
	{'current_state': ST_GW_CREATE_INITIAL,'next_state': ST_GW_ONLINE,'event': EV_GW_KeepAliveReceived, 'callback' : processDataInCreateInitial},
	{'current_state': ST_GW_CREATE_INITIAL,'next_state': ST_GW_ONLINE,'event': EV_GW_KeepAliveReceived, 'callback' : processDataInCreateInitial},
	{'current_state': ST_GW_CREATE_INITIAL,'next_state': ST_GW_ONLINE,'event': EV_GW_KeepAliveReceived, 'callback' : processDataInCreateInitial},
	{'current_state': ST_GW_CREATE_INITIAL,'next_state': ST_GW_ONLINE,'event': EV_GW_KeepAliveReceived, 'callback' : processDataInCreateInitial},
	{'current_state': ST_GW_CREATE_INITIAL,'next_state': ST_GW_ONLINE,'event': EV_GW_KeepAliveReceived, 'callback' : processDataInCreateInitial},
	{'current_state': ST_GW_CREATE_INITIAL,'next_state': ST_GW_ONLINE,'event': EV_GW_KeepAliveReceived, 'callback' : processDataInCreateInitial},
	{'current_state': ST_GW_CREATE_INITIAL,'next_state': ST_GW_ONLINE,'event': EV_GW_KeepAliveReceived, 'callback' : processDataInCreateInitial},
	{'current_state': ST_GW_CREATE_INITIAL,'next_state': ST_GW_ONLINE,'event': EV_GW_KeepAliveReceived, 'callback' : processDataInCreateInitial},
	{'current_state': ST_GW_CREATE_INITIAL,'next_state': ST_GW_ONLINE,'event': EV_GW_KeepAliveReceived, 'callback' : processDataInCreateInitial},
	{'current_state': ST_GW_CREATE_INITIAL,'next_state': ST_GW_ONLINE,'event': EV_GW_KeepAliveReceived, 'callback' : processDataInCreateInitial},
	
	)

''' Gateway class definition '''

