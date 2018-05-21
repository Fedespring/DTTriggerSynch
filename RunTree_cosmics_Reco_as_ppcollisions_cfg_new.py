import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras

process = cms.Process("DTNT",eras.Run2_2018)

##process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration/StandardSequences/Services_cff')

###process.load('Configuration/StandardSequences/Geometry_cff')  ##  Deprecated in new versions > 53X
##process.load('Configuration.Geometry.GeometryIdeal_cff')  ## In versions 7X problems with few STA events crashing the runing # but it works in the first tests of 750pre5 
##process.load('Configuration/StandardSequences/GeometryDB_cff')  
process.load('Configuration/StandardSequences/GeometryRecoDB_cff')  ##  solve STA problem
process.load('Configuration/EventContent/EventContent_cff')
process.load("Geometry.DTGeometryBuilder.dtGeometryDB_cfi")
process.load("RecoMuon.DetLayers.muonDetLayerGeometry_cfi")

###process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cff")
##process.load("Geometry.DTGeometry.dtGeometry_cfi")
##process.load("Geometry.CSCGeometry.cscGeometry_cfi")
##process.load("Geometry.DTGeometryBuilder.idealForDigiDtGeometry_cff")
##process.load("Geometry.DTGeometryBuilder.idealForDigiDtGeometry_cff")

process.load('Configuration.StandardSequences.RawToDigi_Data_cff')

# for DTTF (Not used from 2016)
process.load("EventFilter.DTTFRawToDigi.dttfunpacker_cfi")
process.load("EventFilter.DTTFRawToDigi.dttfpacker_cfi")
process.dttfunpacker.DTTF_FED_Source = "rawDataCollector"

# for TWINMUX (Start to use in 2016)
process.load("EventFilter.L1TXRawToDigi.twinMuxStage2Digis_cfi")

#for RAW
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")

process.load("Configuration.StandardSequences.MagneticField_cff")
##process.load('Configuration/StandardSequences/MagneticField_AutoFromDBCurrent_cff')
##process.load('Configuration/StandardSequences/GeometryExtended_cff')  ## For Run1
###process.load('Configuration.Geometry.GeometryExtended2016_cff')  ## 
process.load("RecoMuon.TrackingTools.MuonServiceProxy_cff")

##process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
##process.GlobalTag.globaltag = "GR_E_V48::All"
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")  #DB v2, at least since GR_E_V42
##process.GlobalTag.globaltag = '80X_dataRun2_Express_v0' ##for CMSSW_8_0_X X>0
##process.GlobalTag.globaltag = '80X_dataRun2_Express_v1' ##for CMSSW_8_0_X X>0
##process.GlobalTag.globaltag = '80X_dataRun2_Express_v4' ##for CMSSW_8_0_X X>0
##process.GlobalTag.globaltag = '90X_dataRun2_Express_v1' ##for CMSSW_9_0_X 
process.GlobalTag.globaltag = '101X_dataRun2_Express_v7'

# for the emulator
process.load("L1TriggerConfig.DTTPGConfigProducers.L1DTTPGConfigFromDB_cff")
process.load("L1Trigger.DTTrigger.dtTriggerPrimitiveDigis_cfi")
process.dtTriggerPrimitiveDigis.debug = False
process.L1DTConfigFromDB.debug = False

process.load('EventFilter.ScalersRawToDigi.ScalersRawToDigi_cfi')
process.load('RecoLuminosity.LumiProducer.lumiProducer_cfi')

# process.load('EventFilter.L1TRawToDigi.l1tRawtoDigiBMTF_cfi')
process.load('EventFilter.L1TRawToDigi.bmtfDigis_cfi')



### Copied from DQM/DTMonitorModule/python/dt_standalonedatabases_cfi.py trying to fix the problem of crashing (perhaps due to a wrong geom)
###from CondCore.DBCommon.CondDBSetup_cfi import *
###geometryESSource = cms.ESSource("PoolDBESSource",
###      CondDBSetup,
###      toGet = cms.VPSet(cms.PSet(record = cms.string('GlobalPositionRcd'),
###                       tag = cms.string('IdealGeometry')
###                       ),
###              cms.PSet(record = cms.string('DTAlignmentRcd'),
###                       tag = cms.string('DTIdealGeometry200_mc')
###                       ),
###              cms.PSet(record = cms.string('DTAlignmentErrorRcd'),
###                       tag = cms.string('DTIdealGeometryErrors200_mc')
###                       ),
###              cms.PSet(record = cms.string('CSCAlignmentRcd'),
###                       tag = cms.string('CSCIdealGeometry200_mc')
###                       ),
###              cms.PSet(record = cms.string('CSCAlignmentErrorRcd'),
###                       tag = cms.string('CSCIdealGeometryErrors200_mc')
###                       ),
###              cms.PSet(record = cms.string('TrackerAlignmentRcd'),
###                       tag = cms.string('TrackerIdealGeometry210_mc')
###                       ),
###              cms.PSet(record = cms.string('TrackerAlignmentErrorRcd'),
###                       tag = cms.string('TrackerIdealGeometryErrors210_mc')
###                      )
###                      ),
###     connect = cms.string('frontier://cms_conditions_data/CMS_COND_21X_ALIGNMENT')
###)


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",

  fileNames = cms.untracked.vstring
  (
       # '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/094/00000/96B6BCEA-8154-E811-AFE1-FA163E998CFB.root'
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/085/00000/265D2E56-6E54-E811-A9D6-FA163E79B489.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/085/00000/4CC56CD9-6E54-E811-A2BC-FA163EA1368E.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/085/00000/683B9957-6E54-E811-8E88-FA163E6A5422.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/085/00000/7A2F189C-6D54-E811-A702-FA163ED05A75.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/085/00000/98D7C19A-6D54-E811-9359-FA163E1ECDC7.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/085/00000/CEC2976C-6D54-E811-9010-FA163E4F3A7C.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/085/00000/EC5B6A8D-6D54-E811-A978-FA163E426D1A.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/087/00000/1C97AD44-7654-E811-AEBC-FA163E48F925.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/087/00000/2894A890-7654-E811-AF2A-FA163EBE6EF1.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/087/00000/2C581D1D-7654-E811-BD95-FA163EC11662.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/087/00000/2C98FB1C-7654-E811-885C-02163E019EBE.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/087/00000/42F3CF5E-7654-E811-BFB1-FA163E6A5422.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/087/00000/6C7E1A37-7654-E811-9F19-FA163E832FBF.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/087/00000/A86DEE55-7654-E811-B804-FA163EB61A35.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/087/00000/B872D25C-7654-E811-9C94-FA163E76BCDA.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/087/00000/E26BAB47-7654-E811-8509-FA163E458FFF.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/087/00000/E8F66434-7654-E811-ABC3-02163E019F18.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/087/00000/F022CB35-7654-E811-9842-FA163EC8B7BD.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/090/00000/4AC2C12E-7954-E811-953B-FA163E18DCD1.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/090/00000/9E28A207-7954-E811-A981-FA163E450DDB.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/090/00000/C6D82B0A-7954-E811-8D13-FA163E7C2A73.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/090/00000/CCAAB8FF-7854-E811-A02F-FA163E687EE7.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/090/00000/E2005C04-7954-E811-B8D7-FA163E81B685.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/090/00000/E45D2707-7954-E811-BA69-FA163E8257B8.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/090/00000/EAF13F09-7954-E811-A80B-02163E019EC5.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/091/00000/0AA860CF-7A54-E811-910D-FA163E054896.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/091/00000/2222D47D-7B54-E811-BECA-FA163ED11D1B.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/091/00000/240E696C-7D54-E811-BC75-FA163EE92B1D.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/091/00000/24C3D11C-7D54-E811-B281-FA163ED0CAD6.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/091/00000/3239BFC6-7A54-E811-BFB5-FA163EDCB9C5.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/091/00000/4ED3A01F-7B54-E811-B2E1-FA163E9297D7.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/091/00000/58E095EF-7B54-E811-933C-FA163E4E6CF7.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/091/00000/70A0E2E4-7A54-E811-A90F-FA163E436522.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/091/00000/9824080C-7D54-E811-BE7C-FA163ED141EE.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/091/00000/A44D7AF2-7B54-E811-9F82-FA163E66C5CD.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/091/00000/A829A72A-7D54-E811-A1E2-FA163E595F01.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/091/00000/B4F35DFE-7B54-E811-845D-02163E017FE7.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/091/00000/B8CFB986-7B54-E811-BB54-FA163E2F2005.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/091/00000/C41FDFB5-7A54-E811-A3A5-FA163E3E2F39.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/091/00000/C49CD4D4-7A54-E811-A07F-FA163EF69597.root',
        '/store/express/Run2018A/ExpressCosmics/FEVT/Express-v1/000/316/091/00000/C6B13942-7D54-E811-B573-FA163EEA5B2C.root'

  ),
  secondaryFileNames = cms.untracked.vstring(
  )
)


############################################################################################### 
##  LOCAL RECO FOR COSMIC DATA RECONSTRUCTED AS PP COLLISIONS - FOR FEVT or RAW-RECO samples ##
############################################################################################### 
from RecoLocalMuon.Configuration.RecoLocalMuon_cff import *
process.Newdt1DRecHits=dt1DRecHits.clone();

process.Newdt2DSegments=dt2DSegments.clone();
process.Newdt2DSegments.recHits1DLabel='Newdt1DRecHits'

process.Newdt4DSegments=dt4DSegments.clone();
process.Newdt4DSegments.recHits1DLabel='Newdt1DRecHits'
process.Newdt4DSegments.recHits2DLabel='Newdt2DSegments'

process.Newdt4DSegmentsT0Seg=dt4DSegmentsT0Seg.clone()
process.Newdt4DSegmentsT0Seg.recHits4DLabel='Newdt4DSegments'

############################################################################################### 
#this is to select collisions
process.primaryVertexFilter = cms.EDFilter("VertexSelector",
   src = cms.InputTag("offlinePrimaryVertices"),
   #cut = cms.string("!isFake && ndof > 4 && abs(z) <= 15 && position.Rho <= 2"), # tracksSize() > 3 for the older cut
   cut = cms.string("!isFake && ndof > 4"), # && abs(z) <= 15 && position.Rho <= 2" # tracksSize() > 3 for the older cut
   filter = cms.bool(True),   # otherwise it won't filter the events, just produce an empty vertex collection.
)

process.noscraping = cms.EDFilter("FilterOutScraping",
                                  applyfilter = cms.untracked.bool(True),
                                  debugOn = cms.untracked.bool(False),
                                  numtrack = cms.untracked.uint32(10),
                                  thresh = cms.untracked.double(0.25)
)

process.DTMuonSelection = cms.EDFilter("DTMuonSelection",
                                 src = cms.InputTag('muons'),
                                 Muons = cms.InputTag('muons'),
                                 SAMuons = cms.InputTag('standAloneMuons'),
                                 dtSegmentLabel = cms.InputTag('dt4DSegments'),
                                 etaMin = cms.double(-1.25),
                                 etaMax = cms.double(1.25),
                                 ptMin = cms.double(3.),
                                 tightness = cms.int32(0) # 0 = loose (e.g. unstable collisions, minimum bias, requires a DT segment)
                                                          # 1 = medium (e.g. cosmics, requires a stand alone muon)
                                                          # 2 = tight (good collisions, requires a global muon)
)


process.load("UserCode/DTDPGAnalysis/DTTTreGenerator_cfi")
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(False)
)

process.myDTNtuple.localDTmuons = cms.untracked.bool(False)
process.myDTNtuple.outputFile = "DTNtuple.root"
process.myDTNtuple.dtTrigSimDCCLabel = cms.InputTag("dtTriggerPrimitiveDigis")
process.myDTNtuple.dtDigiLabel = cms.InputTag("muonDTDigis")
process.myDTNtuple.dtSegmentLabel = cms.InputTag("Newdt4DSegments")
##process.myDTNtuple.staMuLabel = cms.InputTag("standAloneMuons")
process.myDTNtuple.runLegacy_gmt = cms.untracked.bool(False)
process.myDTNtuple.bmtfOutputDigis = cms.InputTag("bmtfDigis:BMTF")

## RPC unpacking
process.load("EventFilter.RPCRawToDigi.rpcUnpackingModule_cfi")

## RPC recHit
process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")
process.load("Geometry.RPCGeometry.rpcGeometry_cfi")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")
process.load("RecoLocalMuon.RPCRecHit.rpcRecHits_cfi")
process.rpcRecHits.rpcDigiLabel = cms.InputTag('rpcUnpackingModule')

## pp collisions before 2016 (DTTF - DCC)
###process.p = cms.Path(process.DTMuonSelection *  process.muonDTDigis * process.dttfunpacker * process.scalersRawToDigi * process.muonDTDigis * process.dtTriggerPrimitiveDigis + process.myDTNtuple)

## pp collisions from 2016 (TM)
##process.p = cms.Path( process.DTMuonSelection * process.muonDTDigis * process.twinMuxStage2Digis  * process.scalersRawToDigi * process.lumiProducer * process.muonDTDigis * process.dtTriggerPrimitiveDigis + process.myDTNtuple)

### Cosmics before 2016 (DTTF - DCC) 
###process.p = cms.Path(process.muonDTDigis * process.dttfunpacker + process.myDTNtuple)

### Cosmics since 2016 (TM) 
### For cosmics MWGR2016 first is needed to put false the part of Global muons because the global cosmics muon tracks are not available
############ process.myDTNtuple.AnaTrackGlobalMu = cms.untracked.bool(False)    ## Comment this when the global cosmics muon tracks are available again
##process.p = cms.Path(process.muonDTDigis * process.twinMuxStage2Digis * process.lumiProducer + process.myDTNtuple)


### Cosmics after RPC variables included on CMSSW_9_0_0 (2017) 
####process.p = cms.Path(process.muonDTDigis * process.twinMuxStage2Digis * process.lumiProducer + process.BMTFStage2Digis + process.rpcUnpackingModule + process.rpcRecHits + process.myDTNtuple)
process.p = cms.Path(process.muonDTDigis + process.twinMuxStage2Digis + process.Newdt1DRecHits + process.Newdt2DSegments + process.Newdt4DSegments + process.lumiProducer  + process.bmtfDigis + process.rpcUnpackingModule + process.rpcRecHits + process.myDTNtuple)

### Collisions after RPC variables included on CMSSW_9_0_0 (2017) 
####process.p = cms.Path( process.DTMuonSelection * process.muonDTDigis * process.twinMuxStage2Digis  * process.scalersRawToDigi * process.lumiProducer * process.muonDTDigis * process.dtTriggerPrimitiveDigis + process.BMTFStage2Digis + process.rpcUnpackingModule + process.rpcRecHits + process.myDTNtuple)
##process.p = cms.Path( process.DTMuonSelection * process.muonDTDigis * process.twinMuxStage2Digis  * process.scalersRawToDigi * process.lumiProducer * process.muonDTDigis * process.dtTriggerPrimitiveDigis + process.bmtfDigis + process.rpcUnpackingModule + process.rpcRecHits + process.myDTNtuple)


## RE-RECO with CMSSW712: RECO only in the dataset!
#process.myDTNtuple.runOnRaw = cms.bool(False)
#process.p = cms.Path(process.myDTNtuple)

# Output
#process.out = cms.OutputModule("PoolOutputModule"
#                               , outputCommands = cms.untracked.vstring(
#                                                                                                "keep *",
#                                                                         "keep *_*_*_testRPCTwinMuxRawToDigi"
#                                                                       , "keep *_*_*_DTNTandRPC"
#                                                                                                            )
#                               , fileName = cms.untracked.string("file:cia.root")
#                               , SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("p"))
#)

#process.this_is_the_end = cms.EndPath(process.out)
