from gateway_state_def import *
import threading
WAITING_FOR_DATA_TOUT =30
''' timer implementation '''
def tWaitingForDataHandler():
	pass
threading.Timer(WAITING_FOR_DATA_TOUT, tWaitingForDataHandler, args = None, kwargs = None)

''' Handler invoked after waiting for data timer expires.'''
def tWaitingForDataHandler():
	pass

def StartGatewayDiagnostic():
		
	pass

def stateChange():
	pass
	

''' Gateway state machine functions callback definitions.'''

''' Call back function to process inventory data and keep alive control events
    in Create Initial state and move state to Online
    
    Action towards device -> None
    Action towards Field User -> None
    Action on timers -> 
    • Timer tWaitingForData is started for waiting for data.
	• Initialize RecoveryInitiatedCount to 0. This counter is used to count how many times tWaitingForData timer expired
	• If tWaitingForData Expired then send event EV_GW_tWaitingForDataExpired
	Action towards Admin user -> State change to ONLINE
	Action on Sensors -> None
	'''
def processDataInCreateInitial():
	pass

''' processWaitingForDataTimerExpired
	Call back function to process when timer=twice the frequency of data arrival, expires.
    
    Action towards device -> 
		• If  RecoveryInitiatedCount < 3
		   o  Increment RecoveryInitiatedCount
		   o Start GatewayDiagnostics
		• Else 
		   o Send EV_GW-ConnectionLost
 
    Action towards Field User -> 
		Start tGWDiagnostic timer to monitor if diagnostic is completed within that time.
		If Timer expires then raise  EV_GW-SensorDiagExpired
    
    Action on timers -> 
		Start timer tGWDiagnostic
	Action towards Admin user -> None
	Action on Sensors -> None
	'''
def processWaitingForDataTimerExpired():
	''' Action towards device '''
	if ( RecoveryInitiatedCount > MAX_RECOVERY_TRIES ):
		''' Send event EV_GW_ConnectionLost'''
		SendEvent(EV_GW_ConnectionLost)
	else:
		RecoveryInitiatedCount +=1
		StartGatewayDiagnostic()


''' processDiagnosticPassed()
	Call back function when diagnostic returns pass
    Action towards device -> None
	Action towards Field User -> None
	Action on timers -> 
		Reeset tGWDignostic and Reset RecoveryInitiatedCount
	Action towards Admin user -> None
	Action on Sensors -> None
	'''
def processDiagnosticPassed():
	pass
	
''' processDiagnosticTimerExpired()
	Call back function when diagnostic timer expired
    Action towards device -> 
    • If  RecoveryInitiatedCount < 3
       o  Increment RecoveryInitiatedCount
       o Start GatewayDiagnostics
	• Else 
       o Send EV_GW-ConnectionLost
 
	Action towards Field User -> None
	Action on timers -> 
		Start tGWDiagnostic timer to monitor if diagnostic is completed within that time. 
		If Timer expires then raise  EV_GW-SensorDiagExpired
		
	Action towards Admin user -> None
	Action on Sensors -> None
	'''
def processDiagnosticTimerExpired():
	pass

''' processCPUUtalisationHigh()
	Call back function when CPU utalisation is high
    Action towards device -> 
    • If  RecoveryInitiatedCount < 3
       o  Increment RecoveryInitiatedCount
       o Start GatewayDiagnostics
	• Else 
       o Send EV_GW-ConnectionLost
 
	Action towards Field User -> None
	Action on timers -> 
		Start tGWDiagnostic timer to monitor if diagnostic is completed within that time. 
		If Timer expires then raise  EV_GW-SensorDiagExpired
		
	Action towards Admin user ->
		Issue alert CPU utalisation High
	Action on Sensors -> None
	'''

def processCPUUtalisationHigh():
	pass

''' processMemUtalisationHigh()
	Call back function when Memory utalisation is high at Gateway
    Action towards device -> 
    • If  RecoveryInitiatedCount < 3
       o  Increment RecoveryInitiatedCount
       o Start GatewayDiagnostics
	• Else 
       o Send EV_GW-ConnectionLost
 
	Action towards Field User -> None
	Action on timers -> 
		Start tGWDiagnostic timer to monitor if diagnostic is completed within that time. 
		If Timer expires then raise  EV_GW-SensorDiagExpired
		
	Action towards Admin user ->
		Issue alert CPU utalisation High
	Action on Sensors -> None
	'''
def processMemUtalisationHigh():
	pass

''' processGWConnectionLost()
	Call back function when Connection lost is declared after all the diagnostic efforts.
    Action towards device -> None
    
 
	Action towards Field User -> 
	Raise Work Order with code = Gateway_Connection_Lost 
	and sub code= high Memory utalisation or high CPU utalization, 
					or Diagnostic failed or diagtimer expired
	Action on timers -> 
		Start tWaitingForWOAck timer, if timer expires 
		then raise EV_GW-tWorkOrderAckExpired
		
	Action towards Admin user ->
		State change to Offline
	Action on Sensors -> All child sensors shall go offline
	'''
def processGWConnectionLost():
	pass


''' processGWAdminOffline()
	Call back function when Admin user puts gateway offline. This event comes if GW runs on battery
    Action towards device -> None
    
 
	Action towards Field User -> 
	Raise Work Order with code = Gateway_Connection_Lost 
	and sub code= high Memory utalisation or high CPU utalization, 
					or Diagnostic failed or diagtimer expired
	Action on timers -> 
		Start tWaitingForWOAck timer, if timer expires 
		then raise EV_GW-tWorkOrderAckExpired
		
	Action towards Admin user ->
		State change to Offline
	Action on Sensors -> All child sensors shall go offline
	'''
def processGWBatteryLow():
	pass


''' processGWAdminOffline()
	Call back function when Admin user puts gateway offline.
	Action towards device ->  
    
		Stop sending data from Edge i.e. ECC, Green Grass or Gateway device 
		to avoid unnecessary messages going to IoT Core. This will save cost at AWS.
	Action towards Field User -> None
		
	Action on timers -> 
		Stop all the Timers and counters.
		
	Action towards Admin user ->
		State change to Offline
	Action on Sensors -> All child sensors shall go offline
	'''
def processGWAdminOffline():
	pass
def tWaitingForDataHandler():
	pass

''' processGWWOAckReceived()
	Call back function when work order ack is received.
	Action towards device -> None
   	Action towards Field User -> None
	Action on timers -> 
		stop ack timer		
	Action towards Admin user -> None
	Action on Sensors -> None
	'''
def processGWWOAckReceived():
	pass
