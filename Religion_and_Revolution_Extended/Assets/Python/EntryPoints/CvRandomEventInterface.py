# Sid Meier's Civilization 4
# Copyright Firaxis Games 2005
#
# CvRandomEventInterface.py
#
# These functions are App Entry Points from C++
# WARNING: These function names should not be changed
# WARNING: These functions can not be placed into a class
#
# No other modules should import this
#
import CvUtil
import CvScreensInterface
from CvPythonExtensions import *

gc = CyGlobalContext()
localText = CyTranslator()

def doEventEndTutorial(argsList):
	eEvent = argsList[0]
	pTriggeredData = argsList[1]
	player = gc.getPlayer(pTriggeredData.ePlayer)
	CyMessageControl().sendPlayerOption(PlayerOptionTypes.PLAYEROPTION_TUTORIAL, false)

def isExpiredFoundColony(argsList):
	eEvent = argsList[0]
	pTriggeredData = argsList[1]
	player = gc.getPlayer(pTriggeredData.ePlayer)
	if player.getNumCities() > 0:
		return true
	return false

def doEventCivilopediaSettlement(argsList):
	eEvent = argsList[0]
	pTriggeredData = argsList[1]
	CvScreensInterface.pediaShowHistorical((CivilopediaPageTypes.CIVILOPEDIA_PAGE_CONCEPT, gc.getInfoTypeForString("CONCEPT_SETTLEMENTS")))

def canDoTriggerImmigrant(argsList):
	pTriggeredData = argsList[0]
	player = gc.getPlayer(pTriggeredData.ePlayer)
	if player.getNumEuropeUnits() == 0:
		return false
	return true

def canDoTriggerImmigrantDone(argsList):
	pTriggeredData = argsList[0]
	player = gc.getPlayer(pTriggeredData.ePlayer)
	if player.getNumEuropeUnits() > 0:
		return false
	return true

def doEventCivilopediaEurope(argsList):
	eEvent = argsList[0]
	pTriggeredData = argsList[1]
	CvScreensInterface.pediaShowHistorical((CivilopediaPageTypes.CIVILOPEDIA_PAGE_CONCEPT, gc.getInfoTypeForString("CONCEPT_EUROPE")))

def doEventCivilopediaImmigration(argsList):
	eEvent = argsList[0]
	pTriggeredData = argsList[1]
	CvScreensInterface.pediaShowHistorical((CivilopediaPageTypes.CIVILOPEDIA_PAGE_CONCEPT, gc.getInfoTypeForString("CONCEPT_IMMIGRATION")))


def canDoTriggerMotherland(argsList):
	pTriggeredData = argsList[0]
	player = gc.getPlayer(pTriggeredData.ePlayer)
	(unit, iter) = player.firstUnit()
	while (unit):
		if unit.getDomainType() == DomainTypes.DOMAIN_SEA and unit.getUnitTravelState() == UnitTravelStates.UNIT_TRAVEL_STATE_TO_EUROPE and unit.getUnitTravelTimer() == 1:
			return true
		(unit, iter) = player.nextUnit(iter)
	return false

def doEventCivilopediaProfessions(argsList):
	eEvent = argsList[0]
	pTriggeredData = argsList[1]
	CvScreensInterface.pediaShowHistorical((CivilopediaPageTypes.CIVILOPEDIA_PAGE_CONCEPT, gc.getInfoTypeForString("CONCEPT_PROFESSIONS")))

def canDoTriggerPioneer(argsList):
	pTriggeredData = argsList[0]
	player = gc.getPlayer(pTriggeredData.ePlayer)

	improvementList = [gc.getInfoTypeForString("IMPROVEMENT_FARM"), gc.getInfoTypeForString("IMPROVEMENT_MINE"), gc.getInfoTypeForString("IMPROVEMENT_LODGE")]
	for iImprovement in improvementList:
		if player.getImprovementCount(iImprovement) > 0:
			return false

	ePioneer = gc.getInfoTypeForString("PROFESSION_PIONEER")
	(unit, iter) = player.firstUnit()
	while (unit):
		if unit.getProfession() == ePioneer:
			return false
		(unit, iter) = player.nextUnit(iter)

	return true

def canDoTriggerImproveLand(argsList):
	pTriggeredData = argsList[0]
	player = gc.getPlayer(pTriggeredData.ePlayer)

	improvementList = [gc.getInfoTypeForString("IMPROVEMENT_FARM"), gc.getInfoTypeForString("IMPROVEMENT_MINE"), gc.getInfoTypeForString("IMPROVEMENT_LODGE")]
	for iImprovement in improvementList:
		if player.getImprovementCount(iImprovement) > 0:
			return false

	ePioneer = gc.getInfoTypeForString("PROFESSION_PIONEER")
	(unit, iter) = player.firstUnit()
	while (unit):
		if unit.getProfession() == ePioneer:
			return true
		(unit, iter) = player.nextUnit(iter)

	return false

def doEventCivilopediaImproveLand(argsList):
	eEvent = argsList[0]
	pTriggeredData = argsList[1]
	CvScreensInterface.pediaShowHistorical((CivilopediaPageTypes.CIVILOPEDIA_PAGE_CONCEPT, gc.getInfoTypeForString("CONCEPT_IMPROVEMENTS")))

def canDoTriggerFoundingFather(argsList):
	pTriggeredData = argsList[0]
	player = gc.getPlayer(pTriggeredData.ePlayer)
	team = gc.getTeam(player.getTeam())

	for iFather in range(gc.getNumFatherInfos()):
		if (team.canConvinceFather(iFather)):
			return true
	return false

def doEventCivilopediaFoundingFather(argsList):
	eEvent = argsList[0]
	pTriggeredData = argsList[1]
	CvScreensInterface.pediaShowHistorical((CivilopediaPageTypes.CIVILOPEDIA_PAGE_CONCEPT, gc.getInfoTypeForString("CONCEPT_FATHERS")))

def doEventCivilopediaNativeVillages(argsList):
	eEvent = argsList[0]
	pTriggeredData = argsList[1]
	CvScreensInterface.pediaShowHistorical((CivilopediaPageTypes.CIVILOPEDIA_PAGE_CONCEPT, gc.getInfoTypeForString("CONCEPT_NATIVES")))

def canDoTriggerRevolution( argsList ):
	pTriggeredData = argsList[ 0 ]
	player = gc.getPlayer( pTriggeredData.ePlayer )

	if gc.getTeam(player.getTeam()).canDoRevolution():
		return true

	return false

def doEventCivilopediaRevolution(argsList):
	eEvent = argsList[0]
	pTriggeredData = argsList[1]
	CvScreensInterface.pediaShowHistorical((CivilopediaPageTypes.CIVILOPEDIA_PAGE_CONCEPT, gc.getInfoTypeForString("CONCEPT_LIBERTY")))

def canDoCityTriggerTools(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iCityId = argsList[2]
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCityId)

	if (not city.isNone() and city.getYieldRate(gc.getInfoTypeForString("YIELD_TOOLS")) > 0):
		return true

	return false

def doEventCivilopediaTools(argsList):
	eEvent = argsList[0]
	pTriggeredData = argsList[1]
	CvScreensInterface.pediaShowHistorical((CivilopediaPageTypes.CIVILOPEDIA_PAGE_CONCEPT, gc.getInfoTypeForString("CONCEPT_PROFESSIONS")))

def canDoCityTriggerBuildingRequiresTools(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iCityId = argsList[2]
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCityId)
	building = city.getProductionBuilding()

	if building != BuildingTypes.NO_BUILDING:
		if (gc.getBuildingInfo(building).getYieldCost(gc.getInfoTypeForString("YIELD_TOOLS")) > 0):
			return true

	return false

def doEventCivilopediaAutomatedTools(argsList):
	eEvent = argsList[0]
	pTriggeredData = argsList[1]
	CvScreensInterface.pediaShowHistorical((CivilopediaPageTypes.CIVILOPEDIA_PAGE_CONCEPT, gc.getInfoTypeForString("CONCEPT_TRADE")))

def canDoSpeakToChief(argsList):
	pTriggeredData = argsList[0]
	player = gc.getPlayer(pTriggeredData.ePlayer)	

	bFoundNative = false
	for iPlayer in range(gc.getMAX_PLAYERS()):
		loopPlayer = gc.getPlayer(iPlayer)
		if loopPlayer.isAlive() and loopPlayer.isNative():
			bFoundNative = true
			(city, iter) = loopPlayer.firstCity(true)
			while(city):
				if city.isScoutVisited(player.getTeam()):
					return false
				(city, iter) = loopPlayer.nextCity(iter, true)
	
	return bFoundNative
	
def canDoSpeakToChiefCompleted(argsList):
	pTriggeredData = argsList[0]
	player = gc.getPlayer(pTriggeredData.ePlayer)	

	for iPlayer in range(gc.getMAX_PLAYERS()):
		loopPlayer = gc.getPlayer(iPlayer)
		if loopPlayer.isAlive() and loopPlayer.isNative():
			(city, iter) = loopPlayer.firstCity(true)
			while(city):
				if city.isScoutVisited(player.getTeam()):
					return true
				(city, iter) = loopPlayer.nextCity(iter, true)
	
	return false
	
def doEventCivilopediaWar(argsList):
	eEvent = argsList[0]
	pTriggeredData = argsList[1]
	CvScreensInterface.pediaShowHistorical((CivilopediaPageTypes.CIVILOPEDIA_PAGE_CONCEPT, gc.getInfoTypeForString("CONCEPT_WAR")))

def canCityTriggerDoOverstock(argsList):
	eTrigger = argsList[0]
	ePlayer = argsList[1]
	iCityId = argsList[2]
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCityId)

	for i in range(YieldTypes.NUM_YIELD_TYPES):
		if (not city.isNone() and city.getYieldStored(i) > city.getMaxYieldCapacity() and i != gc.getInfoTypeForString("YIELD_FOOD")):
			return true

	return false
	
def canDoTaxes(argsList):
	pTriggeredData = argsList[0]
	player = gc.getPlayer(pTriggeredData.ePlayer)	

	if player.getTaxRate() > 0:
		return true
		
	return false

####### TAC Events ########

######## SECOND CITY ###########

def canTriggerSecondCity(argsList):
	ePlayer = argsList[1]
	iCity = argsList[2]
	
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)

	if city.isNone():
		return false
	
	if not player.isPlayable():
		return false
	
	if player.getNumCities() >= 2:
		return true

	return false
	
def applySecondCity1(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	if not player.isHuman():
		city = player.firstCity(true)[0]
	Speed = gc.getGameSpeedInfo(CyGame().getGameSpeedType())
	iYield1 = gc.getInfoTypeForString("YIELD_SAILCLOTH")
	city.changeYieldStored(iYield1, event.getGenericParameter(1)*Speed.getTrainPercent()/100)
	iYield2 = gc.getInfoTypeForString("YIELD_TOOLS")
	city.changeYieldStored(iYield2, event.getGenericParameter(2)*Speed.getTrainPercent()/100)
	iYield3 = gc.getInfoTypeForString("YIELD_HORSES")
	city.changeYieldStored(iYield3, event.getGenericParameter(3)*Speed.getTrainPercent()/100)

def getHelpSecondCity1(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	city = player.getCity(kTriggeredData.iCityId)
	Speed = gc.getGameSpeedInfo(CyGame().getGameSpeedType())
	iYield1 = gc.getInfoTypeForString("YIELD_SAILCLOTH")
	iYield2 = gc.getInfoTypeForString("YIELD_TOOLS")
	iYield3 = gc.getInfoTypeForString("YIELD_HORSES")
	szHelp = localText.getText("TXT_KEY_EVENT_SECONDCOLONY_1_HELP", (king.getCivilizationAdjectiveKey(), ))
	if event.getGenericParameter(1) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_YIELD_GAIN", (event.getGenericParameter(1)*Speed.getTrainPercent()/100,  gc.getYieldInfo(iYield1).getChar(), city.getNameKey()))
	if event.getGenericParameter(2) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_YIELD_GAIN", (event.getGenericParameter(2)*Speed.getTrainPercent()/100,  gc.getYieldInfo(iYield2).getChar(), city.getNameKey()))
	if event.getGenericParameter(3) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_YIELD_GAIN", (event.getGenericParameter(3)*Speed.getTrainPercent()/100,  gc.getYieldInfo(iYield3).getChar(), city.getNameKey()))
	if event.getGenericParameter(1) <> 0 :
		overflow = event.getGenericParameter(1)*Speed.getTrainPercent()/100 + city.getYieldStored(iYield1) - city.getMaxYieldCapacity()
		if overflow > 0:
			szHelp += "\n" + localText.getText("TXT_KEY_EVENT_YIELD_OVERFLOW", (overflow,  gc.getYieldInfo(iYield1).getChar(), city.getNameKey()))
	if event.getGenericParameter(2) <> 0 :
		overflow = event.getGenericParameter(2)*Speed.getTrainPercent()/100 + city.getYieldStored(iYield2) - city.getMaxYieldCapacity()
		if overflow > 0:
			szHelp += "\n" + localText.getText("TXT_KEY_EVENT_YIELD_OVERFLOW", (overflow,  gc.getYieldInfo(iYield2).getChar(), city.getNameKey()))
	if event.getGenericParameter(3) <> 0 :
		overflow = event.getGenericParameter(3)*Speed.getTrainPercent()/100 + city.getYieldStored(iYield3) - city.getMaxYieldCapacity()
		if overflow > 0:
			szHelp += "\n" + localText.getText("TXT_KEY_EVENT_YIELD_OVERFLOW", (overflow,  gc.getYieldInfo(iYield3).getChar(), city.getNameKey()))

	return szHelp

def applySecondCity2(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	if not player.isHuman():
		city = player.firstCity(true)[0]
	Speed = gc.getGameSpeedInfo(CyGame().getGameSpeedType())
	iYield1 = gc.getInfoTypeForString("YIELD_MUSKETS")
	city.changeYieldStored(iYield1, event.getGenericParameter(1)*Speed.getTrainPercent()/100)


def getHelpSecondCity2(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	city = player.getCity(kTriggeredData.iCityId)
	Speed = gc.getGameSpeedInfo(CyGame().getGameSpeedType())
	iYield1 = gc.getInfoTypeForString("YIELD_MUSKETS")
	szHelp = localText.getText("TXT_KEY_EVENT_SECONDCOLONY_2_HELP", (king.getCivilizationAdjectiveKey(), ))
	if event.getGenericParameter(1) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_YIELD_GAIN", (event.getGenericParameter(1)*Speed.getTrainPercent()/100,  gc.getYieldInfo(iYield1).getChar(), city.getNameKey()))
		overflow = event.getGenericParameter(1)*Speed.getTrainPercent()/100 + city.getYieldStored(iYield1) - city.getMaxYieldCapacity()
		if overflow > 0:
			szHelp += "\n" + localText.getText("TXT_KEY_EVENT_YIELD_OVERFLOW", (overflow,  gc.getYieldInfo(iYield1).getChar(), city.getNameKey()))
	return szHelp

######## FESTIVITY ###########

def canTriggerFestivity(argsList):
	ePlayer = argsList[1]
	iCity = argsList[2]
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	
	if not player.isPlayable():
		return false
	if city.isNone():
		return false
		
	king = gc.getPlayer(player.getParent())
	if not king.isEurope():
		return false
	if player.isInRevolution():
		return false

	# Read Parameter 1 from the two events and check if enough yield is stored in city
	eEvent1 = gc.getInfoTypeForString("EVENT_FESTIVITY_2")
	event1 = gc.getEventInfo(eEvent1)
	eEvent2 = gc.getInfoTypeForString("EVENT_FESTIVITY_3")
	event2 = gc.getEventInfo(eEvent2)
	iYield1 = gc.getInfoTypeForString("YIELD_CIGARS")
	iYield2 = gc.getInfoTypeForString("YIELD_RUM")
	if city.getYieldStored(iYield1) < -event1.getGenericParameter(1) and city.getYieldStored(iYield2) < -event2.getGenericParameter(1):
		return false
	# If player has reached the maximum for max tax rate, do not start event
	if player.NBMOD_GetMaxTaxRate() == gc.getDefineINT("MAX_TAX_RATE"):
		return false
	return true

def applyFestivity1(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	player.AI_changeAttitudeExtra(eking, event.getGenericParameter(2))
	king.AI_changeAttitudeExtra(kTriggeredData.ePlayer, event.getGenericParameter(2))
	if player.getTaxRate() + event.getGenericParameter(1) <= player.NBMOD_GetMaxTaxRate():
		player.changeTaxRate(event.getGenericParameter(1))
	else:
		player.NBMOD_IncreaseMaxTaxRate()

def getHelpFestivity1(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	szHelp = localText.getText("TXT_KEY_EVENT_FESTIVITY_1_HELP", ())
	if (player.getTaxRate() + event.getGenericParameter(1) <= player.NBMOD_GetMaxTaxRate()) and event.getGenericParameter(1) <>0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_TAX_INCREASE", (event.getGenericParameter(1), player.getTaxRate() + event.getGenericParameter(1)))
	if (player.getTaxRate() + event.getGenericParameter(1) > player.NBMOD_GetMaxTaxRate()) and event.getGenericParameter(1) <>0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_MAXTAX_INCREASE", (gc.getDefineINT("INCREASE_MAX_TAX_RATE"), player.NBMOD_GetMaxTaxRate()+gc.getDefineINT("INCREASE_MAX_TAX_RATE")))
	if event.getGenericParameter(2) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_RELATION_KING_DECREASE", (event.getGenericParameter(2), king.getCivilizationAdjectiveKey()))
	return szHelp
	
def CanDoFestivity2(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	iYield = gc.getInfoTypeForString("YIELD_CIGARS")
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	if city.isNone():
		return false
	if city.getYieldStored(iYield) < -event.getGenericParameter(1) :
		return false
	return true

def applyFestivity2(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	city = player.getCity(kTriggeredData.iCityId)
	player.AI_changeAttitudeExtra(eking, event.getGenericParameter(3))
	king.AI_changeAttitudeExtra(kTriggeredData.ePlayer, event.getGenericParameter(3))
	iYield = gc.getInfoTypeForString("YIELD_CIGARS")
	iPrice = king.getYieldBuyPrice(iYield)
	king.setYieldBuyPrice(iYield, iPrice+event.getGenericParameter(2), 1)
	city.changeYieldStored(iYield, event.getGenericParameter(1))
	if event.getGenericParameter(4) == 1 :
		player.NBMOD_DecreaseMaxTaxRate()

def getHelpFestivity2(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	city = player.getCity(kTriggeredData.iCityId)
	iYield = gc.getInfoTypeForString("YIELD_CIGARS")
	szHelp = localText.getText("TXT_KEY_EVENT_FESTIVITY_2_HELP", ())
	if event.getGenericParameter(1) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_YIELD_LOOSE", (event.getGenericParameter(1),  gc.getYieldInfo(iYield).getChar(), city.getNameKey()))
	if event.getGenericParameter(2) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_PRICE_INCREASE", (event.getGenericParameter(2), gc.getYieldInfo(iYield).getChar(), king.getCivilizationShortDescriptionKey()))
	if event.getGenericParameter(4) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_MAXTAXDECREASE", (-gc.getDefineINT("DECREASE_MAX_TAX_RATE"), player.NBMOD_GetMaxTaxRate()-gc.getDefineINT("DECREASE_MAX_TAX_RATE")))
	if event.getGenericParameter(3) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_RELATION_KING_INCREASE", (event.getGenericParameter(3), king.getCivilizationAdjectiveKey()))
	return szHelp

def CanDoFestivity3(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	iYield = gc.getInfoTypeForString("YIELD_RUM")
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	if city.getYieldStored(iYield) < -event.getGenericParameter(1) :
		return false
	return true

def applyFestivity3(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	city = player.getCity(kTriggeredData.iCityId)
	player.AI_changeAttitudeExtra(eking, event.getGenericParameter(3))
	king.AI_changeAttitudeExtra(kTriggeredData.ePlayer, event.getGenericParameter(3))
	iYield = gc.getInfoTypeForString("YIELD_RUM")
	iPrice = king.getYieldBuyPrice(iYield)
	king.setYieldBuyPrice(iYield, iPrice+event.getGenericParameter(2), 1)
	city.changeYieldStored(iYield, event.getGenericParameter(1))
	if event.getGenericParameter(4) == 1 :
		player.NBMOD_DecreaseMaxTaxRate()

def getHelpFestivity3(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	city = player.getCity(kTriggeredData.iCityId)
	iYield = gc.getInfoTypeForString("YIELD_RUM")
	szHelp = localText.getText("TXT_KEY_EVENT_FESTIVITY_2_HELP", ())
	if event.getGenericParameter(1) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_YIELD_LOOSE", (event.getGenericParameter(1),  gc.getYieldInfo(iYield).getChar(), city.getNameKey()))
	if event.getGenericParameter(2) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_PRICE_INCREASE", (event.getGenericParameter(2), gc.getYieldInfo(iYield).getChar(), king.getCivilizationShortDescriptionKey()))
	if event.getGenericParameter(4) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_MAXTAXDECREASE", (-gc.getDefineINT("DECREASE_MAX_TAX_RATE"), player.NBMOD_GetMaxTaxRate()-gc.getDefineINT("DECREASE_MAX_TAX_RATE")))
	if event.getGenericParameter(3) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_RELATION_KING_INCREASE", (event.getGenericParameter(3), king.getCivilizationAdjectiveKey()))

	return szHelp

def CanDoFestivity4(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	iYield1 = gc.getInfoTypeForString("YIELD_CIGARS")
	iYield2 = gc.getInfoTypeForString("YIELD_RUM")
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	if (city.getYieldStored(iYield1) < -event.getGenericParameter(1)) or (city.getYieldStored(iYield2) < -event.getGenericParameter(1)) :
		return false
	return true

def applyFestivity4(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	city = player.getCity(kTriggeredData.iCityId)
	player.AI_changeAttitudeExtra(eking, event.getGenericParameter(3))
	king.AI_changeAttitudeExtra(kTriggeredData.ePlayer, event.getGenericParameter(3))
	iYield = gc.getInfoTypeForString("YIELD_CIGARS")
	iPrice = king.getYieldBuyPrice(iYield)
	king.setYieldBuyPrice(iYield, iPrice+event.getGenericParameter(2), 1)
	city.changeYieldStored(iYield, event.getGenericParameter(1))
	iYield = gc.getInfoTypeForString("YIELD_RUM")
	iPrice = king.getYieldBuyPrice(iYield)
	king.setYieldBuyPrice(iYield, iPrice+event.getGenericParameter(2), 1)
	city.changeYieldStored(iYield, event.getGenericParameter(1))
	if event.getGenericParameter(4) == 1 :
		player.NBMOD_DecreaseMaxTaxRate()

def getHelpFestivity4(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	city = player.getCity(kTriggeredData.iCityId)
	iYield1 = gc.getInfoTypeForString("YIELD_CIGARS")
	iYield2 = gc.getInfoTypeForString("YIELD_RUM")
	szHelp = localText.getText("TXT_KEY_EVENT_FESTIVITY_4_HELP", ())
	if event.getGenericParameter(1) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_YIELD_LOOSE", (event.getGenericParameter(1),  gc.getYieldInfo(iYield1).getChar(), city.getNameKey()))
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_YIELD_LOOSE", (event.getGenericParameter(1),  gc.getYieldInfo(iYield2).getChar(), city.getNameKey()))
	if event.getGenericParameter(2) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_PRICE_INCREASE", (event.getGenericParameter(2), gc.getYieldInfo(iYield1).getChar(), king.getCivilizationShortDescriptionKey()))
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_PRICE_INCREASE", (event.getGenericParameter(2), gc.getYieldInfo(iYield2).getChar(), king.getCivilizationShortDescriptionKey()))
	if event.getGenericParameter(4) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_MAXTAXDECREASE", (-gc.getDefineINT("DECREASE_MAX_TAX_RATE"), player.NBMOD_GetMaxTaxRate()-gc.getDefineINT("DECREASE_MAX_TAX_RATE")))
	if event.getGenericParameter(3) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_RELATION_KING_INCREASE", (event.getGenericParameter(3), king.getCivilizationAdjectiveKey()))
	return szHelp

######## WINTER ###########

def canTriggerWinter(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	if not player.isPlayable():
		return false
	king = gc.getPlayer(player.getParent())
	if not king.isEurope():
		return false
	iCurrentTurn = CyGame().getGameTurn()
	szDate = CyGameTextMgr().getTimeStr(iCurrentTurn+1, true)
	January = localText.getText("TXT_KEY_MONTH_JANUARY", ())
	February = localText.getText("TXT_KEY_MONTH_FEBRUARY", ())
	December = localText.getText("TXT_KEY_MONTH_DECEMBER", ())
	November = localText.getText("TXT_KEY_MONTH_NOVEMBER", ())
	October = localText.getText("TXT_KEY_MONTH_OCTOBER", ())
	if (gc.getGameSpeedInfo(gc.getGame().getGameSpeedType()).getGameTurnInfo(0).iMonthIncrement != 12):
		if (January in szDate or February in szDate or December in szDate or November in szDate or October in szDate):
			return true
	return false

def applyWinter(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	iYield1 = gc.getInfoTypeForString("YIELD_COATS")
	iYield2 = gc.getInfoTypeForString("YIELD_FUR")
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	iPrice1 = king.getYieldBuyPrice(iYield1)
	king.setYieldBuyPrice(iYield1, iPrice1+event.getGenericParameter(1), 1)
	iPrice2 = king.getYieldBuyPrice(iYield2)
	king.setYieldBuyPrice(iYield2, iPrice2+event.getGenericParameter(2), 1)

def getHelpWinter(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	iYield1 = gc.getInfoTypeForString("YIELD_COATS")
	iYield2 = gc.getInfoTypeForString("YIELD_FUR")
	szHelp = localText.getText("TXT_KEY_EVENT_WINTER_HELP", (king.getCivilizationShortDescriptionKey(),))
	if event.getGenericParameter(1) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_PRICE_INCREASE", (event.getGenericParameter(2), gc.getYieldInfo(iYield1).getChar(), king.getCivilizationShortDescriptionKey()))
	if event.getGenericParameter(2) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_PRICE_INCREASE", (event.getGenericParameter(2), gc.getYieldInfo(iYield2).getChar(), king.getCivilizationShortDescriptionKey()))

	return szHelp

def canEndWinter(argsList):
	iCurrentTurn = CyGame().getGameTurn()
	#kTriggeredData = argsList[1]
	#player = gc.getPlayer(kTriggeredData.ePlayer)
	#eEvent = gc.getInfoTypeForString("EVENT_WINTER_1")
	#kEventdata = player.getEventOccured(eEvent)
	#iWinterTurn = kEventdata.iTurn
	#CyInterface().addImmediateMessage(str(iWinterTurn)+" Winter Start", "")
	#CyInterface().addImmediateMessage(str(iCurrentTurn)+" Aktuell", "")
	#if iCurrentTurn <= (iWinterTurn + 3) :
	#	return false
	szDate = CyGameTextMgr().getTimeStr(iCurrentTurn+1, true)
	January = localText.getText("TXT_KEY_MONTH_JANUARY", ())
	February = localText.getText("TXT_KEY_MONTH_FEBRUARY", ())
	December = localText.getText("TXT_KEY_MONTH_DECEMBER", ())
	November = localText.getText("TXT_KEY_MONTH_NOVEMBER", ())
	October = localText.getText("TXT_KEY_MONTH_OCTOBER", ())
	if (gc.getGameSpeedInfo(gc.getGame().getGameSpeedType()).getGameTurnInfo(0).iMonthIncrement != 12):
		if not (January in szDate or February in szDate or December in szDate or November in szDate or October in szDate):
			return true
	return false

def applyEndWinter(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	iYield1 = gc.getInfoTypeForString("YIELD_COATS")
	iYield2 = gc.getInfoTypeForString("YIELD_FUR")
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	iPrice1 = king.getYieldBuyPrice(iYield1)
	king.setYieldBuyPrice(iYield1, iPrice1+event.getGenericParameter(1), 1)
	iPrice2 = king.getYieldBuyPrice(iYield2)
	king.setYieldBuyPrice(iYield2, iPrice2+event.getGenericParameter(2), 1)

def getHelpEndWinter(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	iYield1 = gc.getInfoTypeForString("YIELD_COATS")
	iYield2 = gc.getInfoTypeForString("YIELD_FUR")
	szHelp = localText.getText("TXT_KEY_EVENT_END_WINTER_HELP", (king.getCivilizationShortDescriptionKey(), ))
	if event.getGenericParameter(1) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_PRICE_DECREASE", (event.getGenericParameter(2), gc.getYieldInfo(iYield1).getChar(), king.getCivilizationShortDescriptionKey()))
	if event.getGenericParameter(2) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_PRICE_DECREASE", (event.getGenericParameter(2), gc.getYieldInfo(iYield2).getChar(), king.getCivilizationShortDescriptionKey()))
	return szHelp

######## Peasant War Preparations ###########

def canTriggerPeasantWarPrep(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	player2 = gc.getPlayer(kTriggeredData.eOtherPlayer)
	iStartYear = 1495
	if not player.isPlayable() or not player2.isPlayable() :
		return false
	if not player.isHuman():
		return false
	king = gc.getPlayer(player.getParent())
	if not king.isEurope():
		return false
	iCurrentYear = CyGame().getGameTurnYear()
	if iCurrentYear < iStartYear :
		return false
	iChance = gc.getGame().getSorenRandNum(100, "(c) TAC 2010 Events")
	iChance = iChance + 10 * (iCurrentYear-iStartYear)+5
	if iChance > 100 :
		return true
	return false

def applyPeasantWarPrep(argsList):
	kTriggeredData = argsList[1]
	iPriceChange = 2
	iYield1 = gc.getInfoTypeForString("YIELD_MUSKETS")
	iYield2 = gc.getInfoTypeForString("YIELD_FOOD")
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	iPrice1 = king.getYieldBuyPrice(iYield1)
	king.setYieldBuyPrice(iYield1, iPrice1+iPriceChange, 1)
	iPrice2 = king.getYieldBuyPrice(iYield2)
	king.setYieldBuyPrice(iYield2, iPrice2+iPriceChange, 1)

def getHelpPeasantWarPrep(argsList):
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	iYield1 = gc.getInfoTypeForString("YIELD_MUSKETS")
	iYield2 = gc.getInfoTypeForString("YIELD_FOOD")
	iPriceChange = 2
	szHelp = localText.getText("TXT_KEY_EVENT_PEASANT_WARPREP_HELP", (iPriceChange, gc.getYieldInfo(iYield1).getChar(), king.getCivilizationDescriptionKey(), iPriceChange, gc.getYieldInfo(iYield2).getChar(), king.getCivilizationDescriptionKey()))
	return szHelp

######## The Lost Tribe ###########

def canTriggerLostTribe(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	unit = player.getUnit(kTriggeredData.iUnitId)
	eScout = gc.getInfoTypeForString("PROFESSION_SCOUT")
	if unit.getProfession() != eScout:
		return false
	# Read parameter 3 from the event as random chance
	if TriggerChance(argsList):
		return true
	return false
 
def canDoLostTribe4(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	(unit, iter) = player.firstUnit()
	while (unit):
		if unit.getUnitClassType() == CvUtil.findInfoTypeNum('UNITCLASS_SCOUT'):
			return false
		(unit, iter) = player.nextUnit(iter)
	return true

def getHelpLostTribe4(argsList):
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	unit = player.getUnit(kTriggeredData.iUnitId)
	szHelp = getHelpChangeFatherPoints(argsList)
	UnitClass = gc.getUnitClassInfo(CvUtil.findInfoTypeNum('UNITCLASS_SCOUT'))
	UnitClass2 = gc.getUnitClassInfo(unit.getUnitClassType())
	UnitProf1 = gc.getProfessionInfo(unit.getProfession())
	szHelp += "\n" + localText.getText("TXT_KEY_EVENT_LOST_TRIBE_4_HELP", (UnitClass2.getTextKey(), UnitProf1.getTextKey(), UnitClass.getTextKey())) 
	if not canDoLostTribe4(argsList):
		szHelp += "\n\n" + localText.getText("TXT_KEY_EVENT_LOST_TRIBE_4B_HELP", (UnitClass.getTextKey(),))
	return szHelp

def applyLostTribe4(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	ChangeFatherPoints(argsList)
	iUnitClassType = CvUtil.findInfoTypeNum('UNITCLASS_SCOUT')
	iProfession = CvUtil.findInfoTypeNum("PROFESSION_SCOUT")
	iUnitType = gc.getCivilizationInfo(player.getCivilizationType()).getCivilizationUnits(iUnitClassType)
	if iUnitType != -1:
		player.initUnit(iUnitType, iProfession, kTriggeredData.iPlotX, kTriggeredData.iPlotY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH, 0)
	(unitnew, iter) = player.firstUnit()
	while (unitnew):
		if unitnew.getUnitClassType() == CvUtil.findInfoTypeNum('UNITCLASS_SCOUT'):
			break
		(unitnew, iter) = player.nextUnit(iter)
	unit = player.getUnit(kTriggeredData.iUnitId)
	unitnew.convert(unit)
 
######## Pacific Quest ###########

def canTriggerPacificDone(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	iAchieve = gc.getInfoTypeForString("ACHIEVE_PACIFIC")
	#CyInterface().addImmediateMessage("iAchieve "+str(iAchieve), "")
	if player.isAchieveGained(iAchieve):
		return true
	return false

def getHelpPacific(argsList):
	szHelp = localText.getText("TXT_KEY_EVENT_PACIFIC_HELP", ())
	return szHelp


######## VOLCANO ###########

def getHelpVolcano1(argsList):

	szHelp = localText.getText("TXT_KEY_EVENT_VOLCANO_1_HELP", ())

	return szHelp

def canApplyVolcano1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	iNumImprovements = 0
	for iDX in range(-1, 2):
		for iDY in range(-1, 2):
			loopPlot = plotXY(kTriggeredData.iPlotX, kTriggeredData.iPlotY, iDX, iDY)
			if not loopPlot.isNone():
				if (iDX != 0 or iDY != 0):
					if loopPlot.getImprovementType() != -1:
						iNumImprovements += 1

	return (iNumImprovements > 0)

def applyVolcano1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	plot.setPlotType(PlotTypes.PLOT_LAND, True, True)
	plot.setFeatureType(gc.getInfoTypeForString('FEATURE_VOLCANO'), 0)
	
	listPlots = []
	for iDX in range(-1, 2):
		for iDY in range(-1, 2):
			loopPlot = plotXY(kTriggeredData.iPlotX, kTriggeredData.iPlotY, iDX, iDY)
			if not loopPlot.isNone():
				if (iDX != 0 or iDY != 0):
					if loopPlot.getImprovementType() != -1:
						listPlots.append(loopPlot)
					
	listRuins = []
	listRuins.append(CvUtil.findInfoTypeNum('IMPROVEMENT_FARM'))
	listRuins.append(CvUtil.findInfoTypeNum('IMPROVEMENT_PLANTATION'))

	
	iRuins = CvUtil.findInfoTypeNum('IMPROVEMENT_CITY_RUINS')

	for i in range(3):
		if len(listPlots) > 0:
			plot = listPlots[gc.getGame().getSorenRandNum(len(listPlots), "Volcano event improvement destroyed")]
			iImprovement = plot.getImprovementType()
			szBuffer = localText.getText("TXT_KEY_EVENT_CITY_IMPROVEMENT_DESTROYED", (gc.getImprovementInfo(iImprovement).getTextKey(), ))
			CyInterface().addMessage(kTriggeredData.ePlayer, false, gc.getEVENT_MESSAGE_TIME(), szBuffer, "AS2D_BOMBARDED", InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getImprovementInfo(iImprovement).getButton(), gc.getInfoTypeForString("COLOR_RED"), plot.getX(), plot.getY(), true, true)
			if iImprovement in listRuins:
				plot.setImprovementType(iRuins)
			else:
				plot.setImprovementType(-1)
			listPlots.remove(plot)
			
			if i == 1 and gc.getGame().getSorenRandNum(100, "Volcano event num improvements destroyed") < 50:
				break


######## VOLCANO DORMANT ###########

def canTriggerVolcanoDormant1(argsList):
					
	if gc.getGame().getSorenRandNum(100, "Volcano event dormant") < 25:
		return true
	return false

def applyVolcanoDormant1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	plot.setPlotType(PlotTypes.PLOT_PEAK, True, True)

######## TORNADO ###########

def applyTornado1(argsList):
	iEvent = argsList[0]
	kTriggeredData = argsList[1]
	
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	plot.setFeatureType(gc.getInfoTypeForString('FEATURE_TORNADO'), 0)

######## BABY BOOM ###########

def canTriggerBabyBoom(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	team = gc.getTeam(player.getTeam())
	if team.getAtWarCount() > 0:
		return false
	if not TriggerChance(argsList):
		return false
	#for iLoopTeam in range(gc.getMAX_CIV_TEAMS()):
	#	if iLoopTeam != player.getTeam():
	#		if team.AI_getAtPeaceCounter(iLoopTeam) == 1:
	#			CyInterface().addImmediateMessage("True!", "")
	#			return true
	#CyInterface().addImmediateMessage("anderes", "")
	return true

def ApplyBabyBoom(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	count = 0
	# Alle St�dte auf Bev�lkerungswachstum pr�fen
	(loopCity, iter) = player.firstCity(false)
	while(loopCity):
		if gc.getGame().getSorenRandNum(100, "(c) TAC 2010 Events") < event.getGenericParameter(1):
			if not loopCity.isNone():
				loopCity.setFood(loopCity.growthThreshold())
				count += 1
				# Abbrechen, wenn maximale Zahl St�dte erreicht
		if count > event.getGenericParameter(2):
			break
		(loopCity, iter) = player.nextCity(iter, false)
	# Wenn keine Stadt Wachstum hat, eine festlegen
	if count < 1:
		city.setFood(city.growthThreshold())

def getHelpBabyBoom(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	if event.getGenericParameter(2) <> 0 :
		szHelp = localText.getText("TXT_KEY_EVENT_BABY_BOOM_HELP", (event.getGenericParameter(2),))
	return szHelp

######## Flaute ###########

def canApplyCalm(argsList):
	eEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	unit = player.getUnit(kTriggeredData.iUnitId)
	if unit.isNone():
		return false
	if (unit.getUnitTravelState() == UnitTravelStates.UNIT_TRAVEL_STATE_IN_EUROPE):
		return false
	return true

def applyCalm(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	unit = player.getUnit(kTriggeredData.iUnitId)
	if not unit.isNone():
		if (unit.getUnitTravelState() == UnitTravelStates.UNIT_TRAVEL_STATE_FROM_EUROPE) or (unit.getUnitTravelState() == UnitTravelStates.UNIT_TRAVEL_STATE_TO_EUROPE):
			unit.setUnitTravelTimer(unit.getUnitTravelTimer() + 1)

def getHelpCalm(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	unit = player.getUnit(kTriggeredData.iUnitId)
	szHelp = ""
	if not unit.isNone():
		if (unit.getUnitTravelState() == UnitTravelStates.UNIT_TRAVEL_STATE_FROM_EUROPE) or (unit.getUnitTravelState() == UnitTravelStates.UNIT_TRAVEL_STATE_TO_EUROPE):
				szHelp = localText.getText("TXT_KEY_EVENT_CALM_HELP", (1, unit.getName()))
	return szHelp

######## R�ckenwind ###########

def applyTailwind(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	unit = player.getUnit(kTriggeredData.iUnitId)
	if not unit.isNone():
		if event.getGenericParameter(1) > 0 :
			if (unit.getUnitTravelState() == UnitTravelStates.UNIT_TRAVEL_STATE_FROM_EUROPE) or (unit.getUnitTravelState() == UnitTravelStates.UNIT_TRAVEL_STATE_TO_EUROPE):
				if unit.getUnitTravelTimer() > 1 :
					unit.setUnitTravelTimer(unit.getUnitTravelTimer() - 1)
			else:
				unit.changeMoves(-60 * event.getGenericParameter(1))

def canApplyTailwind(argsList):
	eEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	unit = player.getUnit(kTriggeredData.iUnitId)
	if unit.isNone():
		return false
	if (unit.getUnitTravelState() == UnitTravelStates.UNIT_TRAVEL_STATE_IN_EUROPE):
		return false
	if (unit.getUnitTravelState() == UnitTravelStates.UNIT_TRAVEL_STATE_FROM_EUROPE) or (unit.getUnitTravelState() == UnitTravelStates.UNIT_TRAVEL_STATE_TO_EUROPE):
		if unit.getUnitTravelTimer() <= 1 :
			return false
	return true

def getHelpTailwind(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	unit = player.getUnit(kTriggeredData.iUnitId)
	szHelp = ""
	if not unit.isNone():
		if event.getGenericParameter(1) > 0 :
			if (unit.getUnitTravelState() == UnitTravelStates.UNIT_TRAVEL_STATE_FROM_EUROPE) or (unit.getUnitTravelState() == UnitTravelStates.UNIT_TRAVEL_STATE_TO_EUROPE):
				szHelp = localText.getText("TXT_KEY_EVENT_TAILWIND_HELP_2", (1, unit.getName()))
			else:
				szHelp = localText.getText("TXT_KEY_EVENT_TAILWIND_HELP_1", (event.getGenericParameter(1), unit.getName()))
	return szHelp

######## RUNAWAY - Entlaufene Pferde ###########

def canTriggerRunAway(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	player2 = gc.getPlayer(kTriggeredData.eOtherPlayer)
	if player.isNone() or player2.isNone() :
		return false
	if city.isNone():
		return false
	# Read Parameter 1 from the first event and check if enough yield is stored in city
	eEvent1 = gc.getInfoTypeForString("EVENT_RUNAWAY_1")
	event1 = gc.getEventInfo(eEvent1)
	iYield = gc.getInfoTypeForString("YIELD_HORSES")
	if city.getYieldStored(iYield) < -event1.getGenericParameter(1)*2 :
		return false
	return true

def applyRunAway1(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	player2 = gc.getPlayer(kTriggeredData.eOtherPlayer)
	nativecity = player2.getCity(kTriggeredData.iOtherPlayerCityId)
	iYield = gc.getInfoTypeForString("YIELD_HORSES")
	city.changeYieldStored(iYield, event.getGenericParameter(1))
	nativecity.changeYieldStored(iYield, -event.getGenericParameter(1))

def getHelpRunAway1(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	player2 = gc.getPlayer(kTriggeredData.eOtherPlayer)
	nativecity = player2.getCity(kTriggeredData.iOtherPlayerCityId)
	iYield = gc.getInfoTypeForString("YIELD_HORSES")
	szHelp = ""
	if event.getGenericParameter(1) <> 0 :
		szHelp = localText.getText("TXT_KEY_EVENT_YIELD_LOOSE", (event.getGenericParameter(1),  gc.getYieldInfo(iYield).getChar(), city.getNameKey()))
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_YIELD_GAIN", (-event.getGenericParameter(1),  gc.getYieldInfo(iYield).getChar(), nativecity.getNameKey()))
	return szHelp

######## Terra X Quest ###########

def canTriggerTerraX(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	if not player.isPlayable():
		return false
	(city, iter) = player.firstCity(true)
	while(city):
		if not city.isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
			return true
		(city, iter) = player.nextCity(iter, true)
	return false

def getHelpTerraX(argsList):
	worldsize = gc.getWorldInfo(CyMap().getWorldSize())
	szHelp = localText.getText("TXT_KEY_EVENT_TERRAX_HELP", (str(3+(3*worldsize.getBuildingClassPrereqModifier()/100)),))
	return szHelp

def canTriggerTerraXDone(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	if not player.isPlayable():
		return false
	inlandcity = 0
	(city, iter) = player.firstCity(true)
	while(city):
		if not city.isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
			inlandcity += 1
		(city, iter) = player.nextCity(iter, true)
	worldsize = gc.getWorldInfo(CyMap().getWorldSize())
	if inlandcity >= 3+(3*worldsize.getBuildingClassPrereqModifier()/100):
		return true
	return false

def isExpiredTerraX(argsList):
	eEvent = argsList[0]
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	worldsize = gc.getWorldInfo(CyMap().getWorldSize())
	for j in range(gc.getMAX_PLAYERS()):
		if j != kTriggeredData.ePlayer:
			otherplayer = gc.getPlayer(j)
			if (otherplayer.isAlive() and otherplayer.isPlayable()):
				inlandcity = 0
				(city, iter) = otherplayer.firstCity(true)
				while(city):
					if not city.isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
						inlandcity += 1
					(city, iter) = otherplayer.nextCity(iter, true)
				if inlandcity >= 3+(3*worldsize.getBuildingClassPrereqModifier()/100):
					return true
	return false

######## Waldbrand ###########

def applyForestFire(argsList):
	eEvent = argsList[0]
	kTriggeredData = argsList[1]
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	CyEngine().triggerEffect(gc.getInfoTypeForString("EFFECT_SETTLERSMOKE"), pPlot.getPoint())

######## Cargospace ###########

def canTriggerCargoSpace(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	unit = player.getUnit(kTriggeredData.iUnitId)
	if city.getX() == unit.getX() and city.getY() == unit.getY():
		return true
	return false

def applyCargoSpace(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	unit = player.getUnit(kTriggeredData.iUnitId)
	if gc.getGame().getSorenRandNum(100, "(c) TAC 2010 Events") < event.getGenericParameter(3):
		if event.getGenericParameter(1) > 0:
			unit.changeCargoSpace(event.getGenericParameter(1))
			CyInterface().addImmediateMessage(localText.getText("TXT_KEY_EVENT_CARGOSPACE_SUCCESS", (unit.getName(),)), "")
	else:
		CyInterface().addImmediateMessage(localText.getText("TXT_KEY_EVENT_CARGOSPACE_FAILED", ()), "")
	if event.getGenericParameter(2) > 0:
		unit.setImmobileTimer(event.getGenericParameter(2)) 

def helpCargoSpace(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	unit = player.getUnit(kTriggeredData.iUnitId)
	szHelp = ""
	if event.getGenericParameter(1) > 0:
		szHelp = localText.getText("TXT_KEY_EVENT_CARGOSPACE_HELP", (event.getGenericParameter(1), unit.getName(), event.getGenericParameter(3)))
	if event.getGenericParameter(2) > 0:
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_IMMOBILE_UNIT", (event.getGenericParameter(2), unit.getName()))
	return szHelp

######## Anti Pirate ###########

def canTriggerAntiPirate(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	iKilledTradeships = 0
	iWarships = 0
	i=0
	eEvent = gc.getEventTriggerInfo(kTriggeredData.eTrigger).getEvent(0)
	event = gc.getEventInfo(eEvent)
	if player.isInRevolution():
		return false
	for i in range(gc.getNumUnitInfos()):
		if gc.getUnitInfo(i).isMatchForLink("UNIT_CARAVEL",1) or gc.getUnitInfo(i).isMatchForLink("UNIT_FLUYT",1) or gc.getUnitInfo(i).isMatchForLink("UNIT_MERCHANTMAN",1) or gc.getUnitInfo(i).isMatchForLink("UNIT_WHALING_BOAT",1):
			iKilledTradeships += CyStatistics().getPlayerNumUnitsLost(kTriggeredData.ePlayer, i)
	if iKilledTradeships >= event.getGenericParameter(1):
		(loopUnit, iter) = player.firstUnit()
		while(loopUnit):
			if loopUnit.getUnitType() == gc.getInfoTypeForString("UNIT_FRIGATE") or loopUnit.getUnitType() == gc.getInfoTypeForString("UNIT_SHIP_OF_THE_LINE") or loopUnit.getUnitType() == gc.getInfoTypeForString("UNIT_MAN_O_WAR"):
				iWarships += 1
			(loopUnit, iter) = player.nextUnit(iter)
		if iWarships > 0:
			return false
		return true
	return false

######## RUM BLOSSOM - Schnapsnasen ###########

def canTriggerRumBlossom(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	player2 = gc.getPlayer(kTriggeredData.eOtherPlayer)
	if player.isNone() or player2.isNone() :
		return false
	if city.isNone():
		return false
	# Read Parameter 1 from the first event and check if enough yield is stored in city
	eEvent1 = gc.getInfoTypeForString("EVENT_RUM_BLOSSOM_1")
	event1 = gc.getEventInfo(eEvent1)
	iYield = gc.getInfoTypeForString("YIELD_RUM")
	if city.getYieldStored(iYield) < -event1.getGenericParameter(1) :
		return false
	return true

def applyRumBlossom1(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	player2 = gc.getPlayer(kTriggeredData.eOtherPlayer)
	nativecity = player2.getCity(kTriggeredData.iOtherPlayerCityId)
	iYield = gc.getInfoTypeForString("YIELD_RUM")
	city.changeYieldStored(iYield, event.getGenericParameter(1))
	nativecity.changeYieldStored(iYield, -event.getGenericParameter(1))

def getHelpRumBlossom1(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	player2 = gc.getPlayer(kTriggeredData.eOtherPlayer)
	nativecity = player2.getCity(kTriggeredData.iOtherPlayerCityId)
	iYield = gc.getInfoTypeForString("YIELD_RUM")
	szHelp = ""
	if event.getGenericParameter(1) <> 0 :
		szHelp = localText.getText("TXT_KEY_EVENT_YIELD_LOOSE", (event.getGenericParameter(1),  gc.getYieldInfo(iYield).getChar(), city.getNameKey()))
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_YIELD_GAIN", (-event.getGenericParameter(1),  gc.getYieldInfo(iYield).getChar(), nativecity.getNameKey()))
	return szHelp

def canApplyRumBlossom3(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	player2 = gc.getPlayer(kTriggeredData.eOtherPlayer)
	city = player.getCity(kTriggeredData.iCityId)
	if player.isNone() or player2.isNone() :
		return false
	if city.isNone():
		return false
	# Read Parameter 1 from event and check if enough yield is stored in city
	iYield = gc.getInfoTypeForString("YIELD_RUM")
	if city.getYieldStored(iYield) < -event.getGenericParameter(1) :
		return false
	return true

######## Ruins Quest ###########

def isExpiredRuins(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	improvementtype = gc.getInfoTypeForString("IMPROVEMENT_CITY_RUINS")
	if (plot.getOwner() != kTriggeredData.ePlayer):
		return true
	if plot.getImprovementType() != improvementtype:
		return true
	if gc.getGame().getGameTurn() >= kTriggeredData.iTurn + event.getGenericParameter(1):
		return true
	return false

def getHelpRuins(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	UnitClass = gc.getUnitClassInfo(CvUtil.findInfoTypeNum('UNITCLASS_SCOUT'))
	szHelp = localText.getText("TXT_KEY_EVENT_RUINS_HELP", (UnitClass.getTextKey(), city.getNameKey(), event.getGenericParameter(1)))
	return szHelp

def applyRuins5(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	iUnitClassType = CvUtil.findInfoTypeNum('UNITCLASS_CARRIER')
	iUnitType = gc.getCivilizationInfo(player.getCivilizationType()).getCivilizationUnits(iUnitClassType)
	if iUnitType != -1:
		player.initUnit(iUnitType, 0, kTriggeredData.iPlotX, kTriggeredData.iPlotY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH, 0)

def getHelpRuins5(argsList):
	UnitClass = gc.getUnitClassInfo(CvUtil.findInfoTypeNum('UNITCLASS_CARRIER'))
	szHelp = localText.getText("TXT_KEY_EVENT_BONUS_UNIT", (1, UnitClass.getTextKey(), ))
	return szHelp

	
####### The Royals Event ########	
	
def getHelpTheRoyals1(argsList):
	szHelp = localText.getText("TXT_KEY_EVENT_THE_ROYALS_1PYTHON", ())
	return szHelp
	
def getHelpTheRoyals2(argsList):
	szHelp = localText.getText("TXT_KEY_EVENT_THE_ROYALS_2PYTHON", ())
	return szHelp
	
def getHelpTheRoyals3(argsList):
	szHelp = localText.getText("TXT_KEY_EVENT_THE_ROYALS_3PYTHON", ())
	return szHelp
	
def getHelpTheRoyals4(argsList):
	szHelp = localText.getText("TXT_KEY_EVENT_THE_ROYALS_4PYTHON", ())
	return szHelp

def getHelpTheRoyals2a(argsList):
	szHelp = localText.getText("TXT_KEY_EVENT_THE_ROYALS_2aPYTHON", ())
	return szHelp
	
####### Pirates Event ########

def canTriggerPirates(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	unit = player.getUnit(kTriggeredData.iUnitId)
	if city.getX() == unit.getX() and city.getY() == unit.getY():
		return true
	return false

def CanDoPirates3(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	iYield = gc.getInfoTypeForString("YIELD_HORSES")
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	if city.getYieldStored(iYield) < -event.getGenericParameter(1) :
		return false
	return true

def CanDoPirates4(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	iYield = gc.getInfoTypeForString("YIELD_MUSKETS")
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	if city.getYieldStored(iYield) < -event.getGenericParameter(1) :
		return false
	return true
	
def applyPirates3(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)	
	city = player.getCity(kTriggeredData.iCityId)
	iYield = gc.getInfoTypeForString("YIELD_HORSES")		
	city.changeYieldStored(iYield, event.getGenericParameter(1))

def applyPirates4(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)	
	city = player.getCity(kTriggeredData.iCityId)
	iYield = gc.getInfoTypeForString("YIELD_MUSKETS")		
	city.changeYieldStored(iYield, event.getGenericParameter(1))	
	
def getHelpPirates3(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)		
	iYield = gc.getInfoTypeForString("YIELD_HORSES")
	szHelp = ""
	if event.getGenericParameter(1) <> 0 :
		szHelp = localText.getText("TXT_KEY_EVENT_YIELD_LOOSE", (event.getGenericParameter(1),  gc.getYieldInfo(iYield).getChar(), city.getNameKey()))		
	return szHelp

def getHelpPirates4(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)		
	iYield = gc.getInfoTypeForString("YIELD_MUSKETS")
	szHelp = ""
	if event.getGenericParameter(1) <> 0 :
		szHelp = localText.getText("TXT_KEY_EVENT_YIELD_LOOSE", (event.getGenericParameter(1),  gc.getYieldInfo(iYield).getChar(), city.getNameKey()))		
	return szHelp
	
####### TAC Events - General Functions########

######## Units Funktionen ###########

def CreateTreasure(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	iUnitClassType = CvUtil.findInfoTypeNum('UNITCLASS_TREASURE')
	iTreasure = event.getGenericParameter(1) + gc.getGame().getSorenRandNum(event.getGenericParameter(2), "Ronnar")
	iUnitType = gc.getCivilizationInfo(player.getCivilizationType()).getCivilizationUnits(iUnitClassType)
	if iUnitType != -1:
		player.initUnit(iUnitType, 0, kTriggeredData.iPlotX, kTriggeredData.iPlotY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH, iTreasure)

def getHelpCreateTreasure(argsList):
	UnitClass = gc.getUnitClassInfo(CvUtil.findInfoTypeNum('UNITCLASS_TREASURE'))
	szHelp = localText.getText("TXT_KEY_EVENT_BONUS_UNIT", (1, UnitClass.getTextKey(), ))
	return szHelp

	
def countUnits(argsList, iUnitType):
   kTriggeredData = argsList[0]
   player = gc.getPlayer(kTriggeredData.ePlayer)
   iUnitsCurrent = 0
   (loopUnit, iter) = player.firstUnit()
   while(loopUnit):
      if iUnitType == loopUnit.getUnitType():
         iUnitsCurrent += 1
      (loopUnit, iter) = player.nextUnit(iter)

   for i in range(player.getNumEuropeUnits()):
      loopUnit = player.getEuropeUnit(i)
      if iUnitType == loopUnit.getUnitType():
         iUnitsCurrent += 1
         
   (city, iter) = player.firstCity(true)
   while(city):
      for iCitizen in range(city.getPopulation()):
         Unit = city.getPopulationUnitByIndex(iCitizen)
         if iUnitType == Unit.getUnitType():
            iUnitsCurrent += 1
      (city, iter) = player.nextCity(iter, true)
   
   return iUnitsCurrent
   
def CheckCarpenter(argsList):
   iUnitType = CvUtil.findInfoTypeNum('UNIT_CARPENTER')
   iUnitsCurrent = countUnits(argsList, iUnitType)
   if iUnitsCurrent > 0:
      return true
   return false
	

######## Bonus Funktionen ###########

def CanApplyBonus(argsList):
	eEvent = argsList[0]
	kTriggeredData = argsList[1]
	event = gc.getEventInfo(eEvent)
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	bonustype = event.getGenericParameter(1)
	# CyInterface().addImmediateMessage(str(kTriggeredData.iPlotX) + ", " + str(kTriggeredData.iPlotY), "")
	if plot.isNone():
		return false
	if not plot.canHaveBonus(bonustype, false):
		return false
	if not plot.isBeingWorked():
		return false
	return true

def CanApplyBonusOcean(argsList):
	eEvent = argsList[0]
	kTriggeredData = argsList[1]
	event = gc.getEventInfo(eEvent)
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	bonustype = event.getGenericParameter(1)
	# CyInterface().addImmediateMessage(str(kTriggeredData.iPlotX) + ", " + str(kTriggeredData.iPlotY), "")
	if plot.isNone():
		return false
	if not plot.canHaveBonus(bonustype, false):
		return false
	return true

def SetBonus(argsList):
	eEvent = argsList[0]
	kTriggeredData = argsList[1]
	event = gc.getEventInfo(eEvent)
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	bonustype = event.getGenericParameter(1)
	if not plot.isNone() and plot.canHaveBonus(bonustype, false):
		plot.setBonusType(bonustype)

def getHelpBonus(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	bonustype = event.getGenericParameter(1)
	if bonustype != -1 :
		szHelp = localText.getText("TXT_KEY_EVENT_BONUS_HELP", (gc.getBonusInfo(bonustype).getTextKey(),))
	return szHelp

######## Landmark Funktionen ###########

def CheckLandmark(argsList):
	eEvent = argsList[0]
	kTriggeredData = argsList[1]
	event = gc.getEventInfo(eEvent)
	szLandmark = "TXT_KEY_"+event.getType()+"_LANDMARK"
	for i in range (CyEngine().getNumSigns()):
		Sign = CyEngine().getSignByIndex(i)
		if (Sign.getPlot().getX() == kTriggeredData.iPlotX and Sign.getPlot().getY() == kTriggeredData.iPlotY):
			return false
	return true

def SetLandmark(argsList):
	eEvent = argsList[0]
	kTriggeredData = argsList[1]
	event = gc.getEventInfo(eEvent)
	if gc.getDefineINT("SHOW_LANDMARKS") == 1:
		szLandmark = "TXT_KEY_"+event.getType()+"_LANDMARK"
		plot = gc.getMap().plot(kTriggeredData.iPlotX,  kTriggeredData.iPlotY)
		CyEngine().addSign(plot, -1, szLandmark)

######## Gr�ndungsv�ter Funktionen ###########

def ChangeFatherPoints(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	team = gc.getTeam(player.getTeam())
	FatherPointChange = 0
	if event.getGenericParameter(1)!=-1:
		Handicap = gc.getHandicapInfo(CyGame().getHandicapType())
		Speed = gc.getGameSpeedInfo(CyGame().getGameSpeedType())
		FatherPointChange = event.getGenericParameter(2)*Speed.getFatherPercent()/100*Handicap.getFatherPercent()/100
		team.changeFatherPoints(event.getGenericParameter(1), FatherPointChange)

def getHelpChangeFatherPoints(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	FatherPointChange = 0
	szHelp = ""
	if event.getGenericParameter(1)!=-1:
		Handicap = gc.getHandicapInfo(CyGame().getHandicapType())
		Speed = gc.getGameSpeedInfo(CyGame().getGameSpeedType())
		FatherPointChange = event.getGenericParameter(2)*Speed.getFatherPercent()/100*Handicap.getFatherPercent()/100
		szHelp = localText.getText("TXT_KEY_EVENT_FATHER_POINTS", (FatherPointChange, gc.getFatherPointInfo(event.getGenericParameter(1)).getChar(), gc.getFatherPointInfo(event.getGenericParameter(1)).getDescription()))
	return szHelp

######## Trigger Funktionen ###########

def hasAllBuildings(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	iNumTriggerBuildings = trigger.getNumBuildingsRequired()
	if city.isNone() or iNumTriggerBuildings<=0:
		return false
	bHasAllBuildings = true
	i = 0
	for i in range(iNumTriggerBuildings): 
		iBuilding = trigger.getBuildingRequired(i)
		eBuilding = gc.getCivilizationInfo(player.getCivilizationType()).getCivilizationBuildings(iBuilding)
		#CyInterface().addImmediateMessage("iBuilding "+str(iBuilding) + "eBuilding "+str(eBuilding)+str(city.isHasBuilding(eBuilding)) , "")
		if not city.isHasBuilding(eBuilding):
			bHasAllBuildings = false
	return bHasAllBuildings

def hasSilverBonus(argsList):
	pTriggeredData = argsList[0]
	plot = gc.getMap().plot(pTriggeredData.iPlotX, pTriggeredData.iPlotY)
	bonustype = gc.getInfoTypeForString("BONUS_SILVER")
	if not gc.getPlayer(pTriggeredData.ePlayer).isPlayable():
		return false
	if (plot.getOwner() != pTriggeredData.ePlayer):
		return false
	if (plot.getBonusType() == bonustype):
		return true
	return false

def hasFurBonus(argsList):
	pTriggeredData = argsList[0]
	plot = gc.getMap().plot(pTriggeredData.iPlotX, pTriggeredData.iPlotY)
	bonustype = gc.getInfoTypeForString("BONUS_FUR")
	if (plot.getOwner() != pTriggeredData.ePlayer):
		return false
	if (plot.getBonusType() == bonustype):
		return true
	return false

def hasCottonBonus(argsList):
	pTriggeredData = argsList[0]
	plot = gc.getMap().plot(pTriggeredData.iPlotX, pTriggeredData.iPlotY)
	bonustype = gc.getInfoTypeForString("BONUS_COTTON")
	if (plot.getOwner() != pTriggeredData.ePlayer):
		return false
	if (plot.getBonusType() == bonustype):
		return true
	return false

def hasSugarBonus(argsList):
	pTriggeredData = argsList[0]
	plot = gc.getMap().plot(pTriggeredData.iPlotX, pTriggeredData.iPlotY)
	bonustype = gc.getInfoTypeForString("BONUS_SUGAR")
	if (plot.getOwner() != pTriggeredData.ePlayer):
		return false
	if (plot.getBonusType() == bonustype):
		return true
	return false

def hasTobaccoBonus(argsList):
	pTriggeredData = argsList[0]
	plot = gc.getMap().plot(pTriggeredData.iPlotX, pTriggeredData.iPlotY)
	bonustype = gc.getInfoTypeForString("BONUS_TOBACCO")
	if (plot.getOwner() != pTriggeredData.ePlayer):
		return false
	if (plot.getBonusType() == bonustype):
		return true
	return false

def hasIronBonus(argsList):
	pTriggeredData = argsList[0]
	plot = gc.getMap().plot(pTriggeredData.iPlotX, pTriggeredData.iPlotY)
	bonustype = gc.getInfoTypeForString("BONUS_IRON")
	if (plot.getOwner() != pTriggeredData.ePlayer):
		return false
	if (plot.getBonusType() == bonustype):
		return true
	return false

def hasCocoaBonus(argsList):
	pTriggeredData = argsList[0]
	plot = gc.getMap().plot(pTriggeredData.iPlotX, pTriggeredData.iPlotY)
	bonustype = gc.getInfoTypeForString("BONUS_COCOA")
	if (plot.getOwner() != pTriggeredData.ePlayer):
		return false
	if (plot.getBonusType() == bonustype):
		return true
	return false

def hasMineralsBonus(argsList):
	pTriggeredData = argsList[0]
	plot = gc.getMap().plot(pTriggeredData.iPlotX, pTriggeredData.iPlotY)
	bonustype = gc.getInfoTypeForString("BONUS_MINERALS")
	if (plot.getOwner() != pTriggeredData.ePlayer):
		return false
	if (plot.getBonusType() == bonustype):
		return true
	return false

def hasTimberBonus(argsList):
	pTriggeredData = argsList[0]
	plot = gc.getMap().plot(pTriggeredData.iPlotX, pTriggeredData.iPlotY)
	bonustype = gc.getInfoTypeForString("BONUS_TIMBER")
	if (plot.getOwner() != pTriggeredData.ePlayer):
		return false
	if (plot.getBonusType() == bonustype):
		return true
	return false

def hasFoodBonus(argsList):
	pTriggeredData = argsList[0]
	plot = gc.getMap().plot(pTriggeredData.iPlotX, pTriggeredData.iPlotY)
	bonustype1 = gc.getInfoTypeForString("BONUS_POTATO")
	bonustype2 = gc.getInfoTypeForString("BONUS_BISON")
	bonustype3 = gc.getInfoTypeForString("BONUS_CORN")
	# bonustype4 = gc.getInfoTypeForString("BONUS_BANANA")
	if (plot.getOwner() != pTriggeredData.ePlayer):
		return false
	if plot.getBonusType() in (bonustype1, bonustype2, bonustype3):
		return true
	return false

def hasSeaFoodBonus(argsList):
	pTriggeredData = argsList[0]
	plot = gc.getMap().plot(pTriggeredData.iPlotX, pTriggeredData.iPlotY)
	bonustype1 = gc.getInfoTypeForString("BONUS_PEARLS")
	bonustype2 = gc.getInfoTypeForString("BONUS_CRAB")
	bonustype3 = gc.getInfoTypeForString("BONUS_FISH")
	if (plot.getOwner() != pTriggeredData.ePlayer):
		return false
	if plot.getBonusType() in (bonustype1, bonustype2, bonustype3):
		return true
	return false
	
def hasNoBonus(argsList):
	pTriggeredData = argsList[0]
	plot = gc.getMap().plot(pTriggeredData.iPlotX, pTriggeredData.iPlotY)
	#if (plot.getOwner() != pTriggeredData.ePlayer):
	#	return false
	if (plot.getBonusType() == -1):
		return true
	return false

def isPlayable(argsList):
	pTriggeredData = argsList[0]
	player = gc.getPlayer(pTriggeredData.ePlayer)
	if player.isPlayable():
		return true
	else:
		return false

def isHuman(argsList):
	pTriggeredData = argsList[0]
	player = gc.getPlayer(pTriggeredData.ePlayer)
	if player.isHuman():
		return true
	else:
		return false

def TriggerChance(argsList):
	kTriggeredData = argsList[0]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	# Read parameter 3 from the first event as random chance
	eventtrigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	eEvent = eventtrigger.getEvent(0)
	event = gc.getEventInfo(eEvent)
	if gc.getGame().getSorenRandNum(1000, "(c) TAC 2010 Events") < event.getGenericParameter(3):
		return true
	return false
	
######## ORLANTH EVENTS ########

def canTriggerKingFurious(argsList):
	return false
	ePlayer = argsList[1]
	player = gc.getPlayer(ePlayer)
	if not player.isPlayable():
		return false
	if player.isNative():
		return false
	king = gc.getPlayer(player.getParent())
	if not king.isEurope():
		return false
	if king.AI_getAttitude(ePlayer) > 0:
		return false
	if player.isInRevolution():
		return false
	return true
	
def canTriggerKingHappy(argsList):
	return false
	ePlayer = argsList[1]
	player = gc.getPlayer(ePlayer)
	if not player.isPlayable():
		return false
	if player.isNative():
		return false
	king = gc.getPlayer(player.getParent())
	if not king.isEurope():
		return false
	if king.AI_getAttitude(ePlayer) > 4:
		return false
	if player.isInRevolution():
		return false
	return true

def canDoNotInRevolution(argsList):
	ePlayer = argsList[1]
	player = gc.getPlayer(ePlayer)
	if not player.isPlayable():
		return false
	if player.isNative():
		return false
	king = gc.getPlayer(player.getParent())
	if not king.isEurope():
		return false
	if player.isInRevolution():
		return false
	return true

def canDoInRevolution(argsList):
	ePlayer = argsList[1]
	player = gc.getPlayer(ePlayer)
	if player.isNative():
		return false
	if player.isInRevolution():
		return true
	return false

def canTriggerDeliverLumber(argsList):
	pTriggeredData = argsList[0]
	ePlayer = argsList[1]
	iCity = argsList[2]
	player = gc.getPlayer(ePlayer)
	if not player.isPlayable():
		return false
	king = gc.getPlayer(player.getParent())
	if not king.isEurope():
		return false
	city = player.getCity(iCity)
	if city.isNone():
		return false
	# Read Parameters 1+2 from the two events and check if enough yield is stored in city
	eEvent = gc.getInfoTypeForString("EVENT_DELIVER_LUMBER")
	event = gc.getEventInfo(eEvent)
	iYield = gc.getInfoTypeForString("YIELD_LUMBER")
	if city.getYieldStored(iYield) < -event.getGenericParameter(1):
		return false
	return true
	
def canTriggerDeliverCoats(argsList):
	pTriggeredData = argsList[0]
	ePlayer = argsList[1]
	iCity = argsList[2]
	player = gc.getPlayer(ePlayer)
	if not player.isPlayable():
		return false
	king = gc.getPlayer(player.getParent())
	if not king.isEurope():
		return false
	city = player.getCity(iCity)
	if city.isNone():
		return false
	# Read Parameters 1+2 from the two events and check if enough yield is stored in city
	eEvent = gc.getInfoTypeForString("EVENT_DELIVER_COATS")
	event = gc.getEventInfo(eEvent)
	iYield = gc.getInfoTypeForString("YIELD_COATS")
	if city.getYieldStored(iYield) < -event.getGenericParameter(1):
		return false
	return true

def CanDoRequisitionDeliver(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	yields = {
		1 : "YIELD_LUMBER",
		2 : "YIELD_COATS",
		3 : "YIELD_CLOTH"
		}
	iChoose = yields[event.getGenericParameter(2)]
	iYield = gc.getInfoTypeForString(iChoose)
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	if city.isNone():
		return false
	if city.getYieldStored(iYield) < -event.getGenericParameter(1):
		return false
	return true

def applyRequisitionDeliver(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	city = player.getCity(kTriggeredData.iCityId)
	player.AI_changeAttitudeExtra(eking, event.getGenericParameter(3))
	king.AI_changeAttitudeExtra(kTriggeredData.ePlayer, event.getGenericParameter(3))
	yields = {
		1 : "YIELD_LUMBER",
		2 : "YIELD_COATS",
		3 : "YIELD_CLOTH"
		}
	iChoose = yields[event.getGenericParameter(2)]
	iYield = gc.getInfoTypeForString(iChoose)
	iPrice = king.getYieldBuyPrice(iYield)
	iChange = event.getGenericParameter(1)
	city.changeYieldStored(iYield, iChange)
	king.setYieldBuyPrice(iYield, iPrice+event.getGenericParameter(4), 1)
	
def getHelpRequisition(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	city = player.getCity(kTriggeredData.iCityId)
	yields = {
		1 : "YIELD_LUMBER",
		2 : "YIELD_COATS",
		3 : "YIELD_CLOTH"
		}
	iChoose = yields[event.getGenericParameter(2)]
	iYield = gc.getInfoTypeForString(iChoose)
	szHelp = localText.getText("TXT_KEY_EVENT_REQUISITION_HELP", ())
	if event.getGenericParameter(1) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_YIELD_LOOSE", (event.getGenericParameter(1),  gc.getYieldInfo(iYield).getChar(), city.getNameKey()))
	if event.getGenericParameter(2) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_PRICE_INCREASE", (event.getGenericParameter(4), gc.getYieldInfo(iYield).getChar(), king.getCivilizationShortDescriptionKey()))
	if event.getGenericParameter(3) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_RELATION_KING_INCREASE", (event.getGenericParameter(3), king.getCivilizationAdjectiveKey()))
	return szHelp

def applyKingPleased(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	player.AI_changeAttitudeExtra(eking, event.getGenericParameter(3))
	king.AI_changeAttitudeExtra(kTriggeredData.ePlayer, event.getGenericParameter(3))
	if event.getGenericParameter(4) == 1 :
		player.NBMOD_DecreaseMaxTaxRate()

def getHelpKingPleased(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	szHelp = localText.getText("TXT_KEY_EVENT_KING_PLEASED_HELP", ())
	if event.getGenericParameter(4) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_MAXTAXDECREASE", (-gc.getDefineINT("DECREASE_MAX_TAX_RATE"), player.NBMOD_GetMaxTaxRate()-gc.getDefineINT("DECREASE_MAX_TAX_RATE")))
	if event.getGenericParameter(3) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_RELATION_KING_INCREASE", (event.getGenericParameter(3), king.getCivilizationAdjectiveKey()))
	return szHelp

def applyKingAngry(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	player.AI_changeAttitudeExtra(eking, event.getGenericParameter(3))
	king.AI_changeAttitudeExtra(kTriggeredData.ePlayer, event.getGenericParameter(3))
	if event.getGenericParameter(4) == 1 :
		player.NBMOD_IncreaseMaxTaxRate()

def getHelpKingAngry(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	eking = player.getParent()
	king = gc.getPlayer(eking)
	szHelp = localText.getText("TXT_KEY_EVENT_KING_ANGRY_HELP", ())
	if event.getGenericParameter(4) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_MAXTAXINCREASE", (-gc.getDefineINT("INCREASE_MAX_TAX_RATE"), player.NBMOD_GetMaxTaxRate()-gc.getDefineINT("INCREASE_MAX_TAX_RATE")))
	if event.getGenericParameter(3) <> 0 :
		szHelp += "\n" + localText.getText("TXT_KEY_EVENT_RELATION_KING_DECREASE", (event.getGenericParameter(3), king.getCivilizationAdjectiveKey()))
	return szHelp

def canTriggerHorsethief(argsList):
	eEvent = gc.getInfoTypeForString("EVENT_HORSETHIEF_2")
	event = gc.getEventInfo(eEvent)
	ePlayer = argsList[1]
	iCity = argsList[2]
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	if not player.isPlayable():
		return false
	if city.isNone():
		return false
	iYield = gc.getInfoTypeForString("YIELD_HORSES")
	if (city.getYieldStored(iYield) + event.getGenericParameter(1)) < 1:
		return false
	return true
	
def canTriggerCattlethief(argsList):
	eEvent = gc.getInfoTypeForString("EVENT_CATTLETHIEF_1")
	event = gc.getEventInfo(eEvent)
	ePlayer = argsList[1]
	iCity = argsList[2]
	player = gc.getPlayer(ePlayer)
	city = player.getCity(iCity)
	if not player.isPlayable():
		return false
	if city.isNone():
		return false
	iYield = gc.getInfoTypeForString("YIELD_CATTLE")
	if (city.getYieldStored(iYield) + event.getGenericParameter(1)) < 1:
		return false
	return true

def applyHorsethief_2(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	iYield = gc.getInfoTypeForString("YIELD_HORSES")
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	city.changeYieldStored(iYield, event.getGenericParameter(1))
	return true
	
def applyCattlethief_1(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	iYield = gc.getInfoTypeForString("YIELD_CATTLE")
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	city.changeYieldStored(iYield, event.getGenericParameter(1))
	return true
	
def getHelpHorsethief_2(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	iYield = gc.getInfoTypeForString("YIELD_HORSES")
	szHelp = "Gain 1 Petty Criminal."
	szHelp += "\n" + localText.getText("TXT_KEY_EVENT_YIELD_LOOSE", (event.getGenericParameter(1),  gc.getYieldInfo(iYield).getChar(), city.getNameKey()))

def getHelpCattlethief_1(argsList):
	eEvent = argsList[0]
	event = gc.getEventInfo(eEvent)
	kTriggeredData = argsList[1]
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = player.getCity(kTriggeredData.iCityId)
	iYield = gc.getInfoTypeForString("YIELD_CATTLE")
	szHelp = localText.getText("TXT_KEY_EVENT_YIELD_LOOSE", (event.getGenericParameter(1),  gc.getYieldInfo(iYield).getChar(), city.getNameKey()))

def canTriggerArchbishopric(argsList):
	ePlayer = argsList[1]
	player = gc.getPlayer(ePlayer)
	iAchieve = gc.getInfoTypeForString("ACHIEVE_THREE_CHURCHES")
	if player.isAchieveGained(iAchieve):
		iAchieve = gc.getInfoTypeForString("TXT_KEY_ACHIEVE_TEN_CROSSES")
		if player.isAchieveGained(iAchieve):
			return true
	return false
	
def canTriggerNativeTrade(argsList):
	ePlayer = argsList[1]
	player = gc.getPlayer(ePlayer)
	iAchieve = gc.getInfoTypeForString("ACHIEVE_FIVE_NATIVE_CONTACT")
	if player.isAchieveGained(iAchieve):
		return true
	return false

def canTriggerEuroTrade(argsList):
	ePlayer = argsList[1]
	player = gc.getPlayer(ePlayer)
	iAchieve = gc.getInfoTypeForString("ACHIEVE_FOUR_EURO_CONTACT")
	if player.isAchieveGained(iAchieve):
		return true
	return false

def canTriggerPirateAttack1(argsList):
	ePlayer = argsList[1]
	player = gc.getPlayer(ePlayer)
	iAchieve = gc.getInfoTypeForString("ACHIEVE_TENTHOUSAND_TRADE")
	if not player.isPlayable():
		return false
	if player.isAchieveGained(iAchieve):
		return true
	return false

def canTriggerPirateAttack2(argsList):
	ePlayer = argsList[1]
	player = gc.getPlayer(ePlayer)
	iAchieve = gc.getInfoTypeForString("ACHIEVE_HUNDREDTHOUSAND_TRADE")
	if not player.isPlayable():
		return false
	if player.isAchieveGained(iAchieve):
		return true
	return false
	
#def doPirateAttack1(argsList):
#	iEvent = argsList[0]
#	kTriggeredData = argsList[1]
#	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
#	bPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
#	if pPlot.isNone() == False:
#		newUnit = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_PRIVATEER'), pPlot.getX(), pPlot.getY(), UnitAITypes.UNITAI_PIRATE_SEA, DirectionTypes.DIRECTION_SOUTH)
#		newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT2'), True)
#		iRnd = CyGame().getSorenRandNum(1000, "YarrrrMatey")
#		if iRnd > 80:
#			newUnit.setName("Blackbeard")
#		elif iRnd > 60:
#			newUnit.setName("Anne Bonny")
#		elif iRnd > 40:
#			newUnit.setName("Calico Jack Rackham")
#		elif iRnd > 20:
#			newUnit.setName("Black Bart")
#		else:
#			newUnit.setName("Dread Pirate Roberts")
#		newUnit2 = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_SLOOP'), pPlot.getX(), pPlot.getY(), UnitAITypes.UNITAI_PIRATE_SEA, DirectionTypes.DIRECTION_SOUTH)
#		newUnit3 = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_BRIGANTINE'), pPlot.getX(), pPlot.getY(), UnitAITypes.UNITAI_PIRATE_SEA, DirectionTypes.DIRECTION_SOUTH)
#
#def doPirateAttack2(argsList):
#	iEvent = argsList[0]
#	kTriggeredData = argsList[1]
#	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
#	bPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
#	if pPlot.isNone() == False:
#		newUnit = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_MAN_O_WAR'), pPlot.getX(), pPlot.getY(), UnitAITypes.UNITAI_PIRATE_SEA, DirectionTypes.DIRECTION_SOUTH)
#		newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT2'), True)
#		newUnit2 = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_FRIGATE'), pPlot.getX(), pPlot.getY(), UnitAITypes.UNITAI_PIRATE_SEA, DirectionTypes.DIRECTION_SOUTH)
#		newUnit3 = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_BRIGANTINE'), pPlot.getX(), pPlot.getY(), UnitAITypes.UNITAI_PIRATE_SEA, DirectionTypes.DIRECTION_SOUTH)
#		newUnit3 = bPlayer.initUnit(gc.getInfoTypeForString('UNIT_PRIVATEER'), pPlot.getX(), pPlot.getY(), UnitAITypes.UNITAI_PIRATE_SEA, DirectionTypes.DIRECTION_SOUTH)	