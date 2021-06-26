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
EV_GW_GatewyBatteryLow ='014'
EV_GW_AdminOnline ='015'
EV_GW_AdminOffline ='016'
EV_GW_AdminMaintenance ='017'
EV_GW_MaintenanceWindowExpired ='018'

''' Gateway states '''
gateway_states = [ST_GW_CREATE_INITIAL, ST_GW_ONLINE, ST_GW_OFFLINE, ST_GW_MAINTENANCE]

'''Current state (src)
Next state (dst)
rule for transition (Event)
callback for the transition (callback)
'''
#{'Current state':, 'next state':, 'condition':, 'callback': },
GW_FSM_MAP = (
	{'current_state': ST_GW_CREATE_INITIAL,'next_state': ST_GW_ONLINE,'event': EV_GW_TelemetryDataReceived, 'callback': processDataInCreateInitial},
	{'current_state': ST_GW_CREATE_INITIAL,'next_state': ST_GW_ONLINE,'event': EV_GW_KeepAliveReceived, 'callback' : processDataInCreateInitial},
	{'current_state': ST_GW_ONLINE,'next_state': ST_GW_OFFLINE,'event': EV_GW_ConnectionLost, 'callback' : processGWConnectionLost},
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
	{'current_state': ST_GW_CREATE_INITIAL,'next_state': ST_GW_ONLINE,'event': EV_GW_KeepAliveReceived, 'callback' : processDataInCreateInitial},
	
	)


