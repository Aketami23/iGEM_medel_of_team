# テキストデータ（実際にはファイルから読み込むことになります）
text_data = """
ABOATurku: Gold 0, Silver 1, Bronze 0
ABSIKenya: Gold 0, Silver 0, Bronze 1
AFCMEgypt: Gold 3, Silver 0, Bronze 2
AFMUChina: Gold 0, Silver 1, Bronze 0
AHUTChina: Gold 0, Silver 1, Bronze 1
AHUTZJUChina: Gold 1, Silver 0, Bronze 0
AISChina: Gold 1, Silver 0, Bronze 0
AISSUUnion: Gold 0, Silver 1, Bronze 0
ANUAustralia: Gold 0, Silver 1, Bronze 0
ASIJTokyo: Gold 3, Silver 0, Bronze 0
ASTWSChina: Gold 3, Silver 0, Bronze 0
ASU: Gold 1, Silver 0, Bronze 2
AUCEGYPT: Gold 0, Silver 1, Bronze 0
Aachen: Gold 4, Silver 1, Bronze 0
AaltoHelsinki: Gold 3, Silver 1, Bronze 1
Aboa: Gold 0, Silver 3, Bronze 0
AixMarseille: Gold 0, Silver 3, Bronze 2
Alma: Gold 2, Silver 3, Bronze 0
AmazonasBrazil: Gold 0, Silver 0, Bronze 1
Amsterdam: Gold 0, Silver 1, Bronze 0
AnatoliaCollegeHS: Gold 0, Silver 0, Bronze 1
AshesiGhana: Gold 1, Silver 2, Bronze 0
Athens: Gold 4, Silver 1, Bronze 0
AuburnAlabama: Gold 0, Silver 0, Bronze 1
AustinUTexas: Gold 4, Silver 1, Bronze 0
BAIDChina: Gold 1, Silver 0, Bronze 0
BASISChina: Gold 1, Silver 0, Bronze 0
BEASChina: Gold 1, Silver 0, Bronze 0
BFSUICUnited: Gold 0, Silver 2, Bronze 0
BGIMammothEduChina: Gold 1, Silver 0, Bronze 0
BGUIsrael: Gold 1, Silver 1, Bronze 1
BHSF: Gold 1, Silver 0, Bronze 0
BHSFND: Gold 1, Silver 0, Bronze 0
BIBSbeijingchina: Gold 0, Silver 0, Bronze 1
BIT: Gold 2, Silver 1, Bronze 2
BITChina: Gold 3, Silver 2, Bronze 0
BITSPilaniGoaIndia: Gold 1, Silver 1, Bronze 0
BJ101HS: Gold 0, Silver 0, Bronze 1
BJ101ID: Gold 0, Silver 1, Bronze 0
BJEAChina: Gold 2, Silver 1, Bronze 0
BJHS: Gold 0, Silver 1, Bronze 0
BJUChina: Gold 0, Silver 1, Bronze 0
BJWZChina: Gold 0, Silver 1, Bronze 1
BJYUANCHINA: Gold 0, Silver 1, Bronze 0
BMAMU: Gold 1, Silver 0, Bronze 0
BNDSChina: Gold 3, Silver 1, Bronze 1
BNSCChina: Gold 0, Silver 0, Bronze 1
BNUChina: Gold 4, Silver 1, Bronze 0
BNUZChina: Gold 1, Silver 0, Bronze 0
BNUZHChina: Gold 2, Silver 0, Bronze 0
BOKUVienna: Gold 3, Silver 2, Bronze 0
BPIChina: Gold 0, Silver 0, Bronze 1
BSCUnited: Gold 0, Silver 1, Bronze 0
BSUnitedChina: Gold 2, Silver 1, Bronze 0
BUAPMexico: Gold 0, Silver 0, Bronze 1
BUCT: Gold 1, Silver 3, Bronze 0
BUCTChina: Gold 2, Silver 2, Bronze 1
BZK: Gold 0, Silver 1, Bronze 0
BZKSH: Gold 1, Silver 0, Bronze 0
BaltimoreBioCrew: Gold 2, Silver 1, Bronze 0
BarcelonaUB: Gold 2, Silver 0, Bronze 0
Beijing4ELEVEN: Gold 1, Silver 0, Bronze 0
BeijingUnited: Gold 0, Silver 0, Bronze 1
BielefeldCeBiTec: Gold 4, Silver 0, Bronze 0
BilkentUNAMBG: Gold 1, Silver 0, Bronze 0
BioBrussels: Gold 1, Silver 0, Bronze 0
BioWithoutBorders: Gold 0, Silver 0, Bronze 1
BioplusChina: Gold 1, Silver 1, Bronze 0
BioplusShanghai: Gold 1, Silver 0, Bronze 0
Bolivia: Gold 1, Silver 0, Bronze 0
BonnRheinbach: Gold 0, Silver 2, Bronze 1
BostonUHW: Gold 1, Silver 1, Bronze 0
BotchanLabTokyo: Gold 0, Silver 1, Bronze 1
BritishColumbia: Gold 2, Silver 0, Bronze 0
BrnoCzechRepublic: Gold 2, Silver 0, Bronze 0
BrownStanfordPrinctn: Gold 1, Silver 0, Bronze 0
Bulgaria: Gold 0, Silver 3, Bronze 0
CAFAChina: Gold 0, Silver 1, Bronze 0
CAUChina: Gold 5, Silver 0, Bronze 0
CCASanDiego: Gold 1, Silver 2, Bronze 2
CCUTaiwan: Gold 3, Silver 2, Bronze 0
CHINAFAFU: Gold 1, Silver 1, Bronze 0
CHSMissouriUS: Gold 0, Silver 0, Bronze 1
CJUHJLUChina: Gold 1, Silver 0, Bronze 0
CKWAChina: Gold 0, Silver 1, Bronze 0
CLSCLSGUK: Gold 0, Silver 1, Bronze 0
CMUQ: Gold 0, Silver 0, Bronze 1
CNASRomania: Gold 0, Silver 0, Bronze 1
CPUCHINA: Gold 5, Silver 0, Bronze 0
CPUNanjing: Gold 0, Silver 1, Bronze 0
CSMUTaiwan: Gold 4, Silver 1, Bronze 0
CSUCHINA: Gold 3, Silver 2, Bronze 0
CTRAlbertaCanada: Gold 0, Silver 1, Bronze 0
CU: Gold 0, Silver 0, Bronze 1
CUBoulder: Gold 0, Silver 0, Bronze 2
CUEgypt: Gold 0, Silver 1, Bronze 0
CUGChina: Gold 1, Silver 1, Bronze 0
CUHKHongKongSBS: Gold 0, Silver 1, Bronze 0
CUHKSZ: Gold 0, Silver 1, Bronze 1
Calgary: Gold 4, Silver 0, Bronze 0
Cambridge: Gold 2, Silver 0, Bronze 0
CantonHS: Gold 0, Silver 1, Bronze 1
ChalmersGothenburg: Gold 1, Silver 1, Bronze 3
CityUHK: Gold 0, Silver 1, Bronze 0
CityUHongKong: Gold 0, Silver 0, Bronze 1
CityofLondonUK: Gold 1, Silver 2, Bronze 0
ConcordiaMontreal: Gold 3, Silver 1, Bronze 1
Cornell: Gold 4, Silver 1, Bronze 0
CostaRica: Gold 1, Silver 1, Bronze 0
Crete: Gold 0, Silver 2, Bronze 0
DKU: Gold 0, Silver 3, Bronze 0
DKUChina: Gold 0, Silver 1, Bronze 0
DNHSSanDiego: Gold 0, Silver 1, Bronze 0
DNHSSanDiegoCA: Gold 2, Silver 0, Bronze 1
DTUDenmark: Gold 4, Silver 1, Bronze 0
DUTChina: Gold 4, Silver 0, Bronze 0
DUTChinaA: Gold 1, Silver 0, Bronze 0
DUTChinaB: Gold 1, Silver 0, Bronze 0
DeNovoCastrians: Gold 0, Silver 0, Bronze 1
DeNovocastrians: Gold 0, Silver 1, Bronze 0
Duesseldorf: Gold 3, Silver 2, Bronze 0
Duke: Gold 0, Silver 2, Bronze 0
ECNUAS: Gold 0, Silver 2, Bronze 1
ECUSTChina: Gold 1, Silver 1, Bronze 1
ELTE: Gold 1, Silver 0, Bronze 0
EPFL: Gold 5, Silver 0, Bronze 0
ETHZurich: Gold 1, Silver 0, Bronze 0
EastChapelHillHS: Gold 0, Silver 1, Bronze 0
EastCoastBioCrew: Gold 1, Silver 1, Bronze 0
Ecuador: Gold 1, Silver 0, Bronze 0
Edinburgh: Gold 2, Silver 1, Bronze 0
EdinburghOG: Gold 0, Silver 1, Bronze 0
EdinburghUG: Gold 1, Silver 0, Bronze 0
EdinburghUHASGhana: Gold 1, Silver 0, Bronze 0
EstoniaTUIT: Gold 3, Silver 1, Bronze 0
EvryParisSaclay: Gold 5, Silver 0, Bronze 0
Exeter: Gold 4, Silver 0, Bronze 0
FAFU: Gold 0, Silver 1, Bronze 0
FAFUCHINA: Gold 0, Silver 1, Bronze 1
FAFUChina: Gold 0, Silver 1, Bronze 0
FAUErlangen: Gold 0, Silver 1, Bronze 0
FCBUANL: Gold 2, Silver 0, Bronze 0
FDRHBPeru: Gold 0, Silver 2, Bronze 3
FSHSGD: Gold 0, Silver 1, Bronze 0
FSU: Gold 1, Silver 4, Bronze 0
FZPtCHINA: Gold 1, Silver 0, Bronze 0
FZUChina: Gold 0, Silver 0, Bronze 1
Florida: Gold 0, Silver 1, Bronze 0
Freiburg: Gold 3, Silver 0, Bronze 0
Fudan: Gold 5, Silver 0, Bronze 0
FudanTSI: Gold 1, Silver 0, Bronze 0
FujianUnited: Gold 2, Silver 1, Bronze 0
GAStateSWJiaotong: Gold 0, Silver 1, Bronze 2
GCGSChina: Gold 1, Silver 0, Bronze 0
GDSYZX: Gold 1, Silver 2, Bronze 1
GECCHINA: Gold 0, Silver 1, Bronze 0
GECGuangzhou: Gold 0, Silver 1, Bronze 0
GEMSTaiwan: Gold 2, Silver 0, Bronze 0
GENASChina: Gold 1, Silver 0, Bronze 0
GIFUTOKAI: Gold 0, Silver 0, Bronze 1
GOParisSaclay: Gold 3, Silver 1, Bronze 0
GUFrankfurt: Gold 1, Silver 0, Bronze 0
GXUChina: Gold 0, Silver 2, Bronze 1
GYHS: Gold 1, Silver 0, Bronze 0
GZHFI: Gold 1, Silver 0, Bronze 0
GZHSUnited: Gold 0, Silver 0, Bronze 1
GastonDaySchool: Gold 0, Silver 1, Bronze 2
GastonDayShangde: Gold 0, Silver 0, Bronze 1
GeorgiaState: Gold 0, Silver 0, Bronze 1
GeorgiaStateSWJTU: Gold 0, Silver 1, Bronze 0
Gifu: Gold 1, Silver 1, Bronze 0
GoetheFrankfurt: Gold 0, Silver 1, Bronze 0
Goettingen: Gold 0, Silver 1, Bronze 0
GreatBaySCIE: Gold 4, Silver 0, Bronze 0
GreatBaySZ: Gold 3, Silver 0, Bronze 0
GreatBayUnited: Gold 1, Silver 0, Bronze 0
GreatbaySCIE: Gold 1, Silver 0, Bronze 0
GreeceUnited: Gold 1, Silver 0, Bronze 0
GrenobleAlpes: Gold 2, Silver 0, Bronze 0
Groningen: Gold 4, Silver 1, Bronze 0
GuangxiUChina: Gold 0, Silver 0, Bronze 1
GuangzhouMedX: Gold 0, Silver 1, Bronze 0
Guelph: Gold 1, Silver 2, Bronze 0
Gunma: Gold 0, Silver 1, Bronze 1
GunnVistaPingryUS: Gold 1, Silver 0, Bronze 0
H14ZAP: Gold 0, Silver 1, Bronze 0
HBUTChina: Gold 2, Silver 0, Bronze 1
HKCPUWFNWYY: Gold 0, Silver 0, Bronze 2
HKCPUWYY: Gold 0, Silver 0, Bronze 1
HKGTC: Gold 3, Silver 0, Bronze 0
HKHCY: Gold 0, Silver 0, Bronze 1
HKIS: Gold 0, Silver 1, Bronze 0
HKJointSchool: Gold 1, Silver 0, Bronze 0
HKPOLYU: Gold 0, Silver 1, Bronze 0
HKSKHLPSS: Gold 0, Silver 1, Bronze 1
HKSSC: Gold 2, Silver 2, Bronze 0
HKUHongKong: Gold 2, Silver 0, Bronze 0
HKUST: Gold 3, Silver 0, Bronze 0
HNUChina: Gold 0, Silver 1, Bronze 1
HSASNU: Gold 1, Silver 0, Bronze 0
HSChina: Gold 2, Silver 0, Bronze 0
HSShanghai: Gold 0, Silver 1, Bronze 0
HUBUChina: Gold 1, Silver 0, Bronze 0
HUBUSKYChina: Gold 1, Silver 0, Bronze 0
HUBUWUHAN: Gold 0, Silver 1, Bronze 0
HUBUWUHANCHINA: Gold 0, Silver 1, Bronze 0
HUST2China: Gold 1, Silver 0, Bronze 0
HUSTChina: Gold 4, Silver 0, Bronze 0
HUSTUEVEUPSaclay: Gold 0, Silver 1, Bronze 0
HUSUnited: Gold 0, Silver 1, Bronze 0
HZAUChina: Gold 3, Silver 1, Bronze 0
HZNFHSHangzhou: Gold 0, Silver 1, Bronze 0
HainanChina: Gold 0, Silver 0, Bronze 1
HainanUChina: Gold 2, Silver 0, Bronze 0
Hamburg: Gold 2, Silver 1, Bronze 1
HangzhouBioX: Gold 1, Silver 0, Bronze 0
HangzhouSDG: Gold 1, Silver 0, Bronze 0
Hannover: Gold 1, Silver 0, Bronze 0
Harvard: Gold 1, Silver 1, Bronze 1
Heidelberg: Gold 4, Silver 0, Bronze 0
HiZJUChina: Gold 2, Silver 1, Bronze 0
HongKongCUHK: Gold 1, Silver 0, Bronze 0
HongKongCityU: Gold 0, Silver 0, Bronze 1
HongKongHKU: Gold 0, Silver 2, Bronze 1
HongKongHKUST: Gold 0, Silver 1, Bronze 0
HongKongJSS: Gold 2, Silver 0, Bronze 1
HongKongLFCPC: Gold 1, Silver 0, Bronze 0
HongKongPuiChing: Gold 0, Silver 1, Bronze 0
HongKongUCCKE: Gold 0, Silver 1, Bronze 1
Hopkins: Gold 2, Silver 0, Bronze 1
HumboldtBerlin: Gold 1, Silver 1, Bronze 0
ICJFLS: Gold 1, Silver 1, Bronze 0
ICSBKK: Gold 0, Silver 0, Bronze 1
ICTMumbai: Gold 0, Silver 1, Bronze 0
IFBGdansk: Gold 1, Silver 0, Bronze 0
IISERBerhampur: Gold 2, Silver 1, Bronze 0
IISERBhopal: Gold 3, Silver 1, Bronze 1
IISERKolkata: Gold 3, Silver 0, Bronze 0
IISERMohali: Gold 1, Silver 0, Bronze 0
IISERPune2India: Gold 1, Silver 0, Bronze 0
IISERPuneIndia: Gold 4, Silver 1, Bronze 0
IISERTVM: Gold 2, Silver 1, Bronze 0
IISERTirupati: Gold 1, Silver 0, Bronze 0
IISERTirupatiIndia: Gold 4, Silver 0, Bronze 0
IIScBangalore: Gold 2, Silver 0, Bronze 0
IIScBengaluru: Gold 2, Silver 0, Bronze 0
IITChicago: Gold 0, Silver 1, Bronze 0
IITDelhi: Gold 1, Silver 1, Bronze 0
IITMadras: Gold 1, Silver 1, Bronze 0
IITRoorkee: Gold 3, Silver 0, Bronze 0
INSAENSLyon1: Gold 1, Silver 0, Bronze 0
INSALyon1: Gold 1, Silver 0, Bronze 0
IOANNINA: Gold 0, Silver 1, Bronze 1
ITESOGuadalajara: Gold 0, Silver 1, Bronze 0
ImperialCollege: Gold 1, Silver 0, Bronze 0
ImperialCollegeLondon: Gold 1, Silver 0, Bronze 0
IonisParis: Gold 4, Silver 1, Bronze 0
IvyMakerChina: Gold 1, Silver 1, Bronze 0
JACOXHChina: Gold 1, Silver 0, Bronze 0
JCVIUCSD: Gold 0, Silver 1, Bronze 0
JLUChina: Gold 1, Silver 1, Bronze 0
JNFLS: Gold 2, Silver 0, Bronze 0
JNUChina: Gold 1, Silver 0, Bronze 0
JapanUnited: Gold 1, Silver 0, Bronze 0
JiangnanChina: Gold 3, Silver 1, Bronze 1
JiangnanUChina: Gold 1, Silver 0, Bronze 0
JiangsuHighSchool: Gold 0, Silver 1, Bronze 0
JiangsuUnited: Gold 0, Silver 1, Bronze 0
Jianhua: Gold 0, Silver 1, Bronze 0
JilinChina: Gold 4, Silver 1, Bronze 0
KAITJapan: Gold 0, Silver 0, Bronze 1
KCISNewTaipei: Gold 1, Silver 0, Bronze 0
KCISXiugangTaipei: Gold 1, Silver 1, Bronze 0
KCLUK: Gold 2, Silver 3, Bronze 0
KEYSTONE: Gold 2, Silver 1, Bronze 0
KEYSTONEA: Gold 1, Silver 0, Bronze 0
KOREA: Gold 0, Silver 0, Bronze 1
KSAKOREA: Gold 1, Silver 0, Bronze 0
KUASKorea: Gold 0, Silver 0, Bronze 2
KUASSEOUL: Gold 1, Silver 0, Bronze 0
KUISTANBUL: Gold 1, Silver 0, Bronze 0
KULEUVEN: Gold 0, Silver 1, Bronze 0
KULeuven: Gold 0, Silver 3, Bronze 0
Keystone: Gold 0, Silver 1, Bronze 0
KoreaHS: Gold 4, Silver 1, Bronze 0
KoreaSIS: Gold 1, Silver 0, Bronze 0
Kyoto: Gold 3, Silver 0, Bronze 0
LINKSChina: Gold 4, Silver 0, Bronze 0
LMSU: Gold 1, Silver 0, Bronze 0
LZUCHINA: Gold 2, Silver 1, Bronze 0
LZUHSCHINA: Gold 1, Silver 0, Bronze 0
LZUHSChinaC: Gold 1, Silver 0, Bronze 0
LZUHSChinaE: Gold 0, Silver 0, Bronze 1
LZUHSProA: Gold 0, Silver 1, Bronze 0
LZUHSProB: Gold 0, Silver 1, Bronze 0
LambertGA: Gold 5, Silver 0, Bronze 0
LatviaRiga: Gold 1, Silver 0, Bronze 1
Leiden: Gold 4, Silver 1, Bronze 0
Lethbridge: Gold 2, Silver 0, Bronze 3
LethbridgeHS: Gold 2, Silver 3, Bronze 0
Linkoping: Gold 1, Silver 0, Bronze 0
LinkopingSweden: Gold 2, Silver 1, Bronze 0
LubbockTTU: Gold 0, Silver 1, Bronze 0
Lund: Gold 5, Silver 0, Bronze 0
MADRIDUCM: Gold 1, Silver 1, Bronze 0
MADRIDUCMHS: Gold 0, Silver 1, Bronze 0
MEPhI: Gold 0, Silver 0, Bronze 1
MIPTMSU: Gold 1, Silver 0, Bronze 0
MIT: Gold 1, Silver 4, Bronze 0
MITADTBIOPune: Gold 0, Silver 0, Bronze 1
MITMAHE: Gold 3, Silver 0, Bronze 1
MRIIRSFARIDABAD: Gold 0, Silver 0, Bronze 1
MSPMaastricht: Gold 1, Silver 3, Bronze 0
MTUCORK: Gold 0, Silver 1, Bronze 0
MacquarieAustralia: Gold 1, Silver 0, Bronze 0
MakerereUganda: Gold 0, Silver 1, Bronze 0
Manchester: Gold 4, Silver 0, Bronze 0
ManualKY: Gold 0, Silver 1, Bronze 0
Marburg: Gold 2, Silver 1, Bronze 0
McGill: Gold 2, Silver 0, Bronze 0
McMaster: Gold 0, Silver 1, Bronze 0
McMasterA: Gold 0, Silver 1, Bronze 0
McMasterCanada: Gold 0, Silver 1, Bronze 1
McMasterU: Gold 0, Silver 0, Bronze 1
MiamiU: Gold 0, Silver 1, Bronze 0
MiamiUOH: Gold 1, Silver 0, Bronze 0
Michigan: Gold 2, Silver 1, Bronze 1
MichiganState: Gold 0, Silver 2, Bronze 2
Mines: Gold 0, Silver 0, Bronze 1
Mingdao: Gold 5, Silver 0, Bronze 0
MissouriMiners: Gold 0, Silver 0, Bronze 2
Montpellier: Gold 2, Silver 1, Bronze 0
Moscow: Gold 2, Silver 0, Bronze 0
MoscowCity: Gold 0, Silver 1, Bronze 0
Munich: Gold 3, Silver 0, Bronze 0
MunichBioinformatics: Gold 1, Silver 0, Bronze 0
NANJINGNFLSFC: Gold 0, Silver 1, Bronze 0
NAUCHINA: Gold 4, Silver 1, Bronze 0
NAWIGraz: Gold 1, Silver 0, Bronze 1
NCHUTaichung: Gold 1, Silver 1, Bronze 0
NCKUTainan: Gold 4, Silver 0, Bronze 0
NCSU: Gold 0, Silver 1, Bronze 0
NCTUFormosa: Gold 3, Silver 0, Bronze 0
NDNFChina: Gold 1, Silver 0, Bronze 0
NDSU: Gold 1, Silver 1, Bronze 1
NEFUChina: Gold 5, Silver 0, Bronze 0
NEUCHINA: Gold 2, Silver 1, Bronze 1
NFLS: Gold 1, Silver 0, Bronze 0
NISKazakhstan: Gold 1, Silver 0, Bronze 0
NITWarangal: Gold 0, Silver 1, Bronze 0
NJMUChina: Gold 3, Silver 0, Bronze 0
NJTechChina: Gold 1, Silver 1, Bronze 2
NJTechChinaA: Gold 1, Silver 0, Bronze 0
NJTechChinaB: Gold 1, Silver 0, Bronze 0
NJUChina: Gold 1, Silver 3, Bronze 0
NMUChina: Gold 3, Silver 0, Bronze 0
NNUCHINA: Gold 1, Silver 0, Bronze 0
NNUChina: Gold 2, Silver 0, Bronze 0
NOFLSYZ: Gold 1, Silver 0, Bronze 1
NOVALxPortugal: Gold 0, Silver 2, Bronze 0
NPUCHINA: Gold 0, Silver 2, Bronze 1
NTHUTaiwan: Gold 3, Silver 1, Bronze 1
NTNUTrondheim: Gold 0, Silver 1, Bronze 0
NTUSingapore: Gold 2, Silver 1, Bronze 0
NUDTCHINA: Gold 5, Silver 0, Bronze 0
NUKazakhstan: Gold 2, Silver 1, Bronze 1
NUSSingapore: Gold 3, Silver 0, Bronze 0
NWUCHINAA: Gold 1, Silver 3, Bronze 0
NWUCHINAB: Gold 0, Silver 1, Bronze 0
NWUChina: Gold 1, Silver 0, Bronze 0
NYCB1O: Gold 0, Silver 1, Bronze 0
NYCEmpireState: Gold 1, Silver 1, Bronze 0
NYCUFormosa: Gold 2, Silver 0, Bronze 0
NYCUTaipei: Gold 2, Silver 1, Bronze 0
NYMUTaipei: Gold 1, Silver 0, Bronze 1
NYUAbuDhabi: Gold 2, Silver 2, Bronze 1
NYUNewYork: Gold 0, Silver 2, Bronze 1
NYUShanghai: Gold 0, Silver 1, Bronze 0
NanjingBioX: Gold 1, Silver 0, Bronze 0
NanjingBioXstem: Gold 0, Silver 1, Bronze 0
NanjingChina: Gold 4, Silver 1, Bronze 0
NanjingHS: Gold 0, Silver 0, Bronze 1
NanjingHighSchool: Gold 0, Silver 0, Bronze 1
NanjingNFLS: Gold 5, Silver 0, Bronze 0
NanjingSDG: Gold 0, Silver 1, Bronze 0
Nanjinghighschool: Gold 0, Silver 2, Bronze 0
Nantes: Gold 0, Silver 2, Bronze 1
NavarraBG: Gold 0, Silver 4, Bronze 0
Newcastle: Gold 1, Silver 0, Bronze 0
NorthernBC: Gold 0, Silver 1, Bronze 0
Northwestern: Gold 0, Silver 0, Bronze 1
Nottingham: Gold 2, Silver 0, Bronze 0
OKstate: Gold 0, Silver 0, Bronze 1
OSA: Gold 1, Silver 0, Bronze 0
OTIAHangzhou: Gold 1, Silver 0, Bronze 0
OUCChina: Gold 3, Silver 0, Bronze 1
OUCHaide: Gold 1, Silver 0, Bronze 0
OUCR: Gold 1, Silver 0, Bronze 0
OhioState: Gold 3, Silver 0, Bronze 1
OhioStateFABE: Gold 0, Silver 0, Bronze 1
OpenScienceGlobal: Gold 1, Silver 0, Bronze 0
Oxford: Gold 1, Silver 1, Bronze 0
PIHSBeijing: Gold 0, Silver 0, Bronze 1
PINGHE: Gold 1, Silver 1, Bronze 0
PLKLFC1: Gold 0, Silver 1, Bronze 0
PUMCCHINA: Gold 0, Silver 0, Bronze 1
PYMSGZChina: Gold 1, Silver 0, Bronze 0
ParisBettencourt: Gold 2, Silver 0, Bronze 1
PasteurParis: Gold 0, Silver 1, Bronze 0
Patras: Gold 0, Silver 1, Bronze 2
PatrasMed: Gold 1, Silver 0, Bronze 0
PatrasMedicine: Gold 1, Silver 0, Bronze 0
Peking: Gold 4, Silver 0, Bronze 0
PekingHSC: Gold 1, Silver 0, Bronze 0
Penn: Gold 0, Silver 0, Bronze 1
PennState: Gold 0, Silver 1, Bronze 0
Pittsburgh: Gold 2, Silver 0, Bronze 0
Poitiers: Gold 1, Silver 0, Bronze 0
Potsdam: Gold 0, Silver 1, Bronze 0
Princeton: Gold 0, Silver 1, Bronze 0
PuiChingMacau: Gold 5, Silver 0, Bronze 0
Purdue: Gold 1, Silver 1, Bronze 1
QHFZChina: Gold 2, Silver 0, Bronze 0
Qdai: Gold 0, Silver 3, Bronze 1
QueensCanada: Gold 4, Silver 1, Bronze 0
RBHSSanDiegoCA: Gold 0, Silver 1, Bronze 1
RDFZCHINA: Gold 2, Silver 0, Bronze 1
RDFZChina: Gold 1, Silver 0, Bronze 0
RECCHENNAI: Gold 1, Silver 1, Bronze 0
RHIT: Gold 0, Silver 0, Bronze 1
RHSCalgary: Gold 0, Silver 0, Bronze 1
RPTUKaiserslautern: Gold 1, Silver 0, Bronze 0
RSUnitedChina: Gold 0, Silver 0, Bronze 1
RUBochum: Gold 1, Silver 0, Bronze 1
RUMUPRM: Gold 2, Silver 0, Bronze 1
RainsACAChina: Gold 0, Silver 1, Bronze 0
Rice: Gold 1, Silver 0, Bronze 0
RioUFRJBrazil: Gold 0, Silver 1, Bronze 0
Rochester: Gold 4, Silver 0, Bronze 0
RotterdamHR: Gold 0, Silver 0, Bronze 1
SASTRAThanjavur: Gold 0, Silver 1, Bronze 0
SCAUChina: Gold 2, Silver 0, Bronze 0
SCIEPearlDelta: Gold 1, Silver 0, Bronze 0
SCUBSEChina: Gold 1, Silver 0, Bronze 0
SCUChina: Gold 4, Silver 0, Bronze 1
SCUTChina: Gold 2, Silver 3, Bronze 0
SCUWestChina: Gold 1, Silver 0, Bronze 0
SDSZChina: Gold 0, Silver 1, Bronze 1
SDUCHINA: Gold 2, Silver 0, Bronze 0
SDUDenmark: Gold 4, Silver 0, Bronze 0
SEFLSShanghai: Gold 0, Silver 0, Bronze 1
SEHSChina: Gold 1, Silver 0, Bronze 0
SEU: Gold 0, Silver 1, Bronze 0
SEUNanjingChina: Gold 1, Silver 0, Bronze 0
SHBSBANZ: Gold 0, Silver 0, Bronze 1
SHSBNUChina: Gold 5, Silver 0, Bronze 0
SHSID: Gold 1, Silver 2, Bronze 0
SHSIDChina: Gold 1, Silver 0, Bronze 0
SISKorea: Gold 1, Silver 0, Bronze 0
SJTUBioXShanghai: Gold 3, Silver 2, Bronze 0
SJTUSoftware: Gold 1, Silver 0, Bronze 0
SJTUsoftware: Gold 3, Silver 1, Bronze 0
SJTang: Gold 0, Silver 1, Bronze 0
SMBU: Gold 0, Silver 0, Bronze 1
SMMUChina: Gold 0, Silver 1, Bronze 0
SMSShenzhen: Gold 3, Silver 0, Bronze 0
SNUIndia: Gold 0, Silver 1, Bronze 0
SUISShanghai: Gold 0, Silver 1, Bronze 0
SUNYOneonta: Gold 0, Silver 3, Bronze 0
SUSTechCHINA: Gold 0, Silver 1, Bronze 0
SUSTechEMB: Gold 0, Silver 1, Bronze 0
SUSTechMED: Gold 1, Silver 0, Bronze 0
SUSTechOCE: Gold 0, Silver 1, Bronze 0
SUSTechShenzhen: Gold 3, Silver 1, Bronze 1
SVCECHENNAI: Gold 0, Silver 0, Bronze 1
SWUerChina: Gold 0, Silver 0, Bronze 1
SYPHUChina: Gold 0, Silver 1, Bronze 0
SYSUCHINA: Gold 2, Silver 2, Bronze 0
SYSUSLSCHINA: Gold 1, Silver 0, Bronze 0
SYSUSoftware: Gold 3, Silver 1, Bronze 0
SZPTCHINA: Gold 4, Silver 0, Bronze 0
SZSHD: Gold 4, Silver 0, Bronze 0
SZTARMGSzeged: Gold 1, Silver 0, Bronze 0
SZTASzegedHU: Gold 0, Silver 0, Bronze 1
SZUChina: Gold 5, Silver 0, Bronze 0
SaintJoseph: Gold 0, Silver 2, Bronze 0
SaoCarlosBrazil: Gold 0, Silver 1, Bronze 0
SeoulKorea: Gold 1, Silver 0, Bronze 0
SesameShenzhen: Gold 1, Silver 0, Bronze 0
ShanghaiBioX: Gold 0, Silver 1, Bronze 0
ShanghaiCity: Gold 0, Silver 0, Bronze 1
ShanghaiCityUnited: Gold 0, Silver 0, Bronze 1
ShanghaiFLSChina: Gold 0, Silver 0, Bronze 1
ShanghaiHS: Gold 0, Silver 4, Bronze 1
ShanghaiHSID: Gold 0, Silver 0, Bronze 1
ShanghaiHSUnited: Gold 0, Silver 3, Bronze 0
ShanghaiHighSchool: Gold 1, Silver 0, Bronze 0
ShanghaiMedX: Gold 0, Silver 1, Bronze 0
ShanghaiMetro: Gold 0, Silver 1, Bronze 0
ShanghaiMetroHS: Gold 0, Silver 1, Bronze 0
ShanghaiMetroUtd: Gold 0, Silver 0, Bronze 1
ShanghaiMetropolis: Gold 1, Silver 1, Bronze 0
ShanghaiSDG: Gold 1, Silver 0, Bronze 0
ShanghaiSFLSSPBS: Gold 1, Silver 0, Bronze 0
ShanghaiTechChina: Gold 4, Silver 1, Bronze 0
ShanghaiUnited: Gold 1, Silver 3, Bronze 0
ShanghaiUnitedHS: Gold 0, Silver 1, Bronze 0
Shanghaicity: Gold 1, Silver 3, Bronze 0
Shanghaihighschool: Gold 0, Silver 1, Bronze 1
Sheffield: Gold 2, Silver 1, Bronze 0
ShymBILNIS: Gold 0, Silver 0, Bronze 1
Siberia: Gold 0, Silver 1, Bronze 0
SogangKorea: Gold 1, Silver 0, Bronze 0
SorbonneUParis: Gold 4, Silver 1, Bronze 0
SoundBio: Gold 0, Silver 0, Bronze 1
SquirrelBeijingI: Gold 1, Silver 0, Bronze 0
SquirrelCHN: Gold 1, Silver 0, Bronze 0
SquirrelCHNII: Gold 1, Silver 0, Bronze 0
SquirrelGuangzhou: Gold 1, Silver 0, Bronze 0
SquirrelShanghai: Gold 1, Silver 0, Bronze 0
Sriwijaya: Gold 0, Silver 0, Bronze 1
StAndrews: Gold 2, Silver 1, Bronze 0
Stanford: Gold 1, Silver 3, Bronze 1
Stockholm: Gold 3, Silver 2, Bronze 0
StonyBrook: Gold 1, Silver 2, Bronze 2
Strasbourg: Gold 1, Silver 0, Bronze 0
Stuttgart: Gold 1, Silver 2, Bronze 1
SuZhouUnion: Gold 0, Silver 0, Bronze 1
SubCatChina: Gold 2, Silver 0, Bronze 0
SubCatGD: Gold 0, Silver 1, Bronze 0
SubCatHongKong: Gold 0, Silver 0, Bronze 1
SubCatPeking: Gold 1, Silver 0, Bronze 0
SubCatShanghai: Gold 0, Silver 2, Bronze 0
SydneyAustralia: Gold 3, Silver 0, Bronze 0
TAMU: Gold 0, Silver 0, Bronze 1
TASTaipei: Gold 3, Silver 0, Bronze 0
TAUIsrael: Gold 4, Silver 1, Bronze 0
TECCOSTARICA: Gold 0, Silver 1, Bronze 0
THINKERCHINA: Gold 1, Silver 1, Bronze 0
THISChina: Gold 0, Silver 0, Bronze 1
TJUSLSChina: Gold 4, Silver 1, Bronze 0
TPHSSanDiego: Gold 0, Silver 1, Bronze 0
TPRChina: Gold 1, Silver 0, Bronze 0
TSBCSZ: Gold 0, Silver 1, Bronze 0
TUBraunschweig: Gold 1, Silver 1, Bronze 0
TUDarmstadt: Gold 3, Silver 0, Bronze 0
TUDelft: Gold 4, Silver 0, Bronze 0
TUDresden: Gold 3, Silver 0, Bronze 0
TUEindhoven: Gold 4, Silver 0, Bronze 0
TUKaiserslautern: Gold 3, Silver 0, Bronze 0
TacomaRAINmakers: Gold 0, Silver 0, Bronze 1
TaipeiKCISLKV1: Gold 1, Silver 0, Bronze 0
TartuTUIT: Gold 1, Silver 0, Bronze 0
TecCCM: Gold 1, Silver 0, Bronze 0
TecCEM: Gold 2, Silver 0, Bronze 0
TecChihuahua: Gold 3, Silver 0, Bronze 0
TecMonterrey: Gold 3, Silver 0, Bronze 0
TecMonterreyGDL: Gold 1, Silver 1, Bronze 1
TechnionIsrael: Gold 4, Silver 0, Bronze 0
TelHaiMigalIsrael: Gold 0, Silver 1, Bronze 0
ThailandRIS: Gold 0, Silver 2, Bronze 0
TheKingsSchoolAU: Gold 1, Silver 0, Bronze 0
TheKingsSchoolAUHS: Gold 1, Silver 0, Bronze 0
TheWebbSchools: Gold 0, Silver 1, Bronze 0
Thessaloniki: Gold 2, Silver 1, Bronze 0
ThessalonikiMeta: Gold 1, Silver 0, Bronze 0
Thessaly: Gold 5, Silver 0, Bronze 0
ThinkEduChina: Gold 1, Silver 0, Bronze 0
ThinkerGuangdong: Gold 0, Silver 1, Bronze 0
ThinkerSC: Gold 1, Silver 0, Bronze 0
ThinkerShanghai: Gold 0, Silver 1, Bronze 0
ThinkerShenzhen: Gold 0, Silver 1, Bronze 1
Thrace: Gold 1, Silver 1, Bronze 0
Tianjin: Gold 3, Silver 0, Bronze 1
TokyoTech: Gold 0, Silver 4, Bronze 0
TongjiChina: Gold 5, Silver 0, Bronze 0
TongjiSoftware: Gold 4, Silver 0, Bronze 1
Toronto: Gold 3, Silver 0, Bronze 0
ToulouseINSAUPS: Gold 4, Silver 0, Bronze 0
Tsinghua: Gold 3, Silver 1, Bronze 0
TsinghuaA: Gold 1, Silver 0, Bronze 1
TsinghuaTFL: Gold 1, Silver 0, Bronze 0
Tsukuba: Gold 0, Silver 1, Bronze 0
Tuebingen: Gold 2, Silver 2, Bronze 1
TunghaiTAPG: Gold 0, Silver 1, Bronze 0
UAHuntsville: Gold 0, Silver 0, Bronze 1
UAM: Gold 1, Silver 0, Bronze 0
UANL: Gold 0, Silver 0, Bronze 1
UAlberta: Gold 0, Silver 1, Bronze 1
UBCOkanagan: Gold 1, Silver 1, Bronze 0
UBCVancouver: Gold 1, Silver 1, Bronze 0
UBrawijaya: Gold 0, Silver 1, Bronze 0
UCASChina: Gold 3, Silver 1, Bronze 1
UCDavis: Gold 1, Silver 1, Bronze 0
UCL: Gold 3, Silver 0, Bronze 0
UCSC: Gold 4, Silver 1, Bronze 0
UCSanDiego: Gold 0, Silver 0, Bronze 1
UChicago: Gold 1, Silver 2, Bronze 1
UConn: Gold 0, Silver 0, Bronze 1
UCopenhagen: Gold 3, Silver 0, Bronze 0
UESTCBioTech: Gold 1, Silver 0, Bronze 0
UESTCChina: Gold 3, Silver 0, Bronze 0
UESTCSoftware: Gold 2, Silver 0, Bronze 0
UFMGUFVBrazil: Gold 1, Silver 0, Bronze 0
UFRGSBrazil: Gold 0, Silver 0, Bronze 1
UFlorida: Gold 0, Silver 2, Bronze 1
UGA: Gold 0, Silver 1, Bronze 0
UGMIndonesia: Gold 1, Silver 1, Bronze 0
UGent2Belgium: Gold 0, Silver 0, Bronze 1
UGentBelgium: Gold 0, Silver 1, Bronze 0
UIIndonesia: Gold 2, Silver 1, Bronze 0
UIUCIllinois: Gold 0, Silver 2, Bronze 2
ULC: Gold 1, Silver 0, Bronze 0
ULaVerneCollab: Gold 0, Silver 1, Bronze 0
ULaval: Gold 5, Silver 0, Bronze 0
UMAMALAGA: Gold 0, Silver 1, Bronze 1
UMMacau: Gold 3, Silver 2, Bronze 0
UManitoba: Gold 0, Silver 2, Bronze 0
UMaryland: Gold 1, Silver 0, Bronze 2
UNCChapelHill: Gold 0, Silver 0, Bronze 1
UNESPBrazil: Gold 0, Silver 0, Bronze 1
UNILALatAm: Gold 1, Silver 0, Bronze 1
UNILausanne: Gold 4, Silver 0, Bronze 0
UNIZAR: Gold 1, Silver 0, Bronze 0
UNSWAustralia: Gold 3, Silver 2, Bronze 0
UNT: Gold 0, Silver 0, Bronze 1
UNebraskaLincoln: Gold 0, Silver 1, Bronze 0
UOregon: Gold 0, Silver 1, Bronze 1
UPCHPeru: Gold 1, Silver 0, Bronze 0
UPFBarcelona: Gold 2, Silver 0, Bronze 0
UPNAvarraSpain: Gold 1, Silver 1, Bronze 1
UPRM: Gold 0, Silver 1, Bronze 0
UParisBME: Gold 0, Silver 1, Bronze 0
UPenn: Gold 2, Silver 0, Bronze 0
USAFA: Gold 2, Silver 2, Bronze 1
USAFRLCarrollHS: Gold 0, Silver 1, Bronze 0
USPBrazil: Gold 2, Silver 0, Bronze 1
USPEELBrazil: Gold 0, Silver 1, Bronze 1
USPSaoCarlosBrazil: Gold 0, Silver 1, Bronze 0
USTC: Gold 1, Silver 3, Bronze 0
USTCSoftware: Gold 1, Silver 3, Bronze 0
UTArlingtonTexasUSA: Gold 0, Silver 0, Bronze 1
UTokyo: Gold 3, Silver 0, Bronze 0
UUlm: Gold 0, Silver 0, Bronze 1
UVUUtah: Gold 0, Silver 1, Bronze 0
UZurich: Gold 4, Silver 1, Bronze 0
UiOsloNorway: Gold 1, Silver 4, Bronze 0
UniGEGeneva: Gold 0, Silver 1, Bronze 0
UniHamburg: Gold 0, Silver 1, Bronze 0
UniMuenster: Gold 0, Silver 1, Bronze 0
UniPaduaIT: Gold 1, Silver 0, Bronze 0
UnicampBrazil: Gold 1, Silver 0, Bronze 0
UniofBath: Gold 1, Silver 0, Bronze 0
UnitedShanghaiHS: Gold 0, Silver 1, Bronze 0
UofUppsala: Gold 1, Silver 0, Bronze 0
Uppsala: Gold 2, Silver 0, Bronze 0
UppsalaUniversitet: Gold 1, Silver 0, Bronze 0
VITVellore: Gold 1, Silver 2, Bronze 0
VictoriaWellington: Gold 0, Silver 0, Bronze 1
VilniusLithuania: Gold 5, Silver 0, Bronze 0
Virginia: Gold 4, Silver 1, Bronze 0
WFLAYKPAO: Gold 0, Silver 1, Bronze 0
WHSFremont: Gold 0, Silver 0, Bronze 1
WHUChina: Gold 4, Silver 0, Bronze 0
WLCMilwaukee: Gold 0, Silver 1, Bronze 3
WUSTChina: Gold 1, Silver 0, Bronze 0
WVHSSanDiego: Gold 0, Silver 2, Bronze 0
WVHSSanDiegoCA: Gold 0, Silver 0, Bronze 1
WWUMuenster: Gold 1, Silver 0, Bronze 0
WageningenUR: Gold 4, Silver 0, Bronze 0
Warwick: Gold 3, Silver 2, Bronze 0
Waseda: Gold 1, Silver 0, Bronze 0
WasedaTokyo: Gold 1, Silver 0, Bronze 0
Washington: Gold 0, Silver 3, Bronze 1
Waterloo: Gold 2, Silver 2, Bronze 1
WegoTaipei: Gold 1, Silver 1, Bronze 0
WestCentralHS: Gold 0, Silver 1, Bronze 0
WesternCanada: Gold 0, Silver 0, Bronze 1
WestlakeChina: Gold 1, Silver 0, Bronze 0
Whittle: Gold 0, Silver 0, Bronze 1
WilliamandMary: Gold 4, Silver 1, Bronze 0
WorldshaperHZ: Gold 0, Silver 0, Bronze 1
WorldshaperHZBIOX: Gold 0, Silver 1, Bronze 0
WorldshaperNJBIOX: Gold 1, Silver 0, Bronze 0
WorldshaperNanjing: Gold 3, Silver 0, Bronze 0
WorldshaperShanghai: Gold 3, Silver 1, Bronze 0
WorldshaperWuhan: Gold 1, Silver 1, Bronze 0
WorldshaperXSHS: Gold 1, Silver 0, Bronze 0
WrightState: Gold 0, Silver 1, Bronze 1
WrightStateOH: Gold 1, Silver 0, Bronze 0
Wroclaw: Gold 0, Silver 0, Bronze 1
WuhanHubeiChina: Gold 0, Silver 1, Bronze 0
XHDShanDongChina: Gold 1, Silver 0, Bronze 0
XHDWSWuhanA: Gold 0, Silver 1, Bronze 0
XHDWSWuhanB: Gold 0, Silver 0, Bronze 1
XHDWuHanChina: Gold 1, Silver 0, Bronze 0
XHDWuHanProChina: Gold 1, Silver 0, Bronze 0
XHDWuhanAChina: Gold 0, Silver 0, Bronze 1
XHDWuhanBChina: Gold 1, Silver 0, Bronze 0
XHDWuhanChina: Gold 1, Silver 0, Bronze 1
XHDWuhanProChina: Gold 0, Silver 1, Bronze 1
XJTLUCHINA: Gold 4, Silver 0, Bronze 0
XJTUCHINA: Gold 1, Silver 0, Bronze 0
XJTUChina: Gold 2, Silver 1, Bronze 0
XJUChina: Gold 0, Silver 1, Bronze 0
XMUChina: Gold 5, Silver 0, Bronze 0
XiamenCity: Gold 1, Silver 1, Bronze 0
Xiamencity: Gold 1, Silver 0, Bronze 0
YAUChina: Gold 0, Silver 1, Bronze 0
Yale: Gold 0, Silver 2, Bronze 0
YangzhouNOFLS: Gold 1, Silver 0, Bronze 0
YiYeChina: Gold 3, Silver 0, Bronze 0
YkPaO: Gold 1, Silver 0, Bronze 0
YonseiKorea: Gold 0, Silver 1, Bronze 0
YucaiSZ: Gold 0, Silver 1, Bronze 0
ZJFHNanjing: Gold 1, Silver 0, Bronze 0
ZJUChina: Gold 5, Silver 0, Bronze 0
ZJUTChina: Gold 3, Silver 1, Bronze 0
ZJUTChinaB: Gold 1, Silver 0, Bronze 0
ZJUintlChina: Gold 0, Silver 1, Bronze 1
ZhejiangUnited: Gold 1, Silver 0, Bronze 1
iBowuChina: Gold 3, Silver 2, Bronze 0
thessaloniki: Gold 0, Silver 1, Bronze 0
uOttawa: Gold 1, Silver 0, Bronze 0
uniCRETE: Gold 0, Silver 1, Bronze 0

"""

# スコアを格納するリストを初期化
scores = []

# テキストを行ごとに処理する
for line in text_data.strip().split('\n'):
    parts = line.split(':')  # チーム名とメダル情報を分ける
    team = parts[0].strip()  # チーム名
    medals = parts[1].strip().split(',')  # メダル情報

    # メダル情報から数値を抽出して合計する
    gold = int(medals[0].split()[1])
    silver = int(medals[1].split()[1])
    bronze = int(medals[2].split()[1])
    total = gold + silver + bronze

    # totalを出場回数として平均スコアを計算する
    average_score = (gold * 3 + silver * 2 + bronze * 1) / total if total > 0 else 0

    # スコアとチーム名をリストに追加
    scores.append((team, total, average_score))

# スコアに基づいてリストを降順にソート
scores.sort(key=lambda x: x[2], reverse=True)

# 結果を保存するファイル名を定義
output_file = 'sorted_average_scores.txt'

# 結果を保存するファイルを開く
with open(output_file, 'w') as file:
    for team, total, average_score in scores:
        # 結果をファイルに書き込む
        file.write(f"{team}: Total {total}, Average Score {average_score:.2f}\n")

print(f"Sorted average scores have been saved to {output_file}")
# 既存のデータやコードからの続きです。

# 各チームのスコアとメダル合計を格納するリストを初期化
scores = []

# テキストを行ごとに処理する
for line in text_data.strip().split('\n'):
    parts = line.split(':')
    team = parts[0].strip()
    medals = parts[1].strip().split(',')

    # メダル情報から数値を抽出
    gold = int(medals[0].split()[1])
    silver = int(medals[1].split()[1])
    bronze = int(medals[2].split()[1])

    # メダルの合計枚数を計算
    total_medals = gold + silver + bronze

    # スコアを計算（ゴールド3点、シルバー2点、ブロンズ1点）
    score = gold * 3 + silver * 2 + bronze * 1

    # 平均スコアをメダル合計枚数で割る
    average_score = score / total_medals if total_medals > 0 else 0

    # スコアとチーム名をリストに追加
    scores.append((team, gold, silver, bronze, total_medals, score, average_score))

# 平均スコアでソートし、その後メダル合計枚数でソートする
scores.sort(key=lambda x: (-x[6], -x[4]))

# 結果を保存するファイル名を定義
output_file = 'sorted_scores_with_medals.txt'

# 結果を保存するファイルを開く
with open(output_file, 'w') as file:
    for team, gold, silver, bronze, total_medals, total_score, average_score in scores:
        # 結果をファイルに書き込む
        file.write(f"{team}: Gold {gold}, Silver {silver}, Bronze {bronze}, Total Medals {total_medals}, Total Score {total_score}, Average Score {average_score:.2f}\n")

print(f"Sorted scores with medal counts have been saved to {output_file}")
