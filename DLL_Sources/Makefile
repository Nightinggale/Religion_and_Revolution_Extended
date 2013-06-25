#### Civilization 4 SDK Makefile 2.0 ####
####  Copyright 2013 Nightinggale    ####
#########################################
#### Civilization 4 SDK Makefile 1.0 ####
####  Copyright 2010 Danny Daemonic  ####
#########################################

#### Paths ####
TOOLKIT=C:\Program Files (x86)\Microsoft Visual C++ Toolkit 2003
PSDK=C:\Program Files (x86)\Microsoft SDKs\Windows\v7.0A
## Uncomment to have newly compiled dlls copied to your mod's Assets directory
YOURMOD=..

## Civ install path
## Path to the directory where boost and python is stored
## Overwritten by enviroment variable CIV4_LIB_INSTALL_PATH
#CIV4_PATH=C:\Program Files (x86)\2K Games\Firaxis Games\Sid Meier's Civilization IV Colonization\CvGameCoreDLL

#### Tools ####
CC="$(TOOLKIT)\bin\cl.exe"
CPP="$(TOOLKIT)\bin\cl.exe"
LD="$(TOOLKIT)\bin\link.exe"
RC="$(PSDK)\bin\rc.exe"
## Uncomment to build dependencies using fastdep
## Overwritten by enviroment variable FASTDEP_FULL_PATH
FD="$(MAKEDIR)\bin\fastdep.exe"

#### BLACKLIST ####
## Uncomment to block CvTextScreen (accidentally included by Firaxis)
BLACKLIST=CvTextScreens

#### DEFINES ####
## copy the following lines into "Additional options" in NMAKE properties
## This will make VC++ aware of what is defined and what isn't, which affects the help popup and red lines
## Use Release_DEFINES for all targets except debug
## Assert adds /DFASSERT_ENABLE, which should be added to additional options too, if you care.
## However you will only be able to tell a difference if you do something with asserts other than FAssert() or FAssertMsg()

Debug_DEFINES=/DWIN32 /D_WINDOWS /D_USRDLL /DCVGAMECOREDLL_EXPORTS /D_DEBUG
Release_DEFINES=/DWIN32 /D_WINDOWS /D_USRDLL /DCVGAMECOREDLL_EXPORTS /DNDEBUG /DFINAL_RELEASE

#### You shouldn't need to modify anything beyond this point ####
#################################################################

## Enrironmental path overwrite
!IFDEF CIV4_LIB_INSTALL_PATH
CIV4_PATH=$(CIV4_LIB_INSTALL_PATH)
!ENDIF

!IFDEF FASTDEP_FULL_PATH
FD=$(FASTDEP_FULL_PATH)
!ENDIF

#### Target Files ####
Target_BIN=$(TARGET)\CvGameCoreDLL.dll

!IF [IF NOT EXIST CvGameCoreDLL.rc EXIT 1] == 0
Target_RESOURCE=$(TARGET)\CvGameCoreDLL.res
!ENDIF

Target_STATICLIB=$(TARGET)\CvGameCoreDLL.lib

Target_LIBDEF=$(TARGET)\CvGameCoreDLL.def

Target_PCH=$(TARGET)\CvGameCoreDLL.pch

Target_PDB=$(TARGET)\CvGameCoreDLL.pdb

Target_OTHER=$(TARGET)\CvGameCoreDLL.exp

#### CFLAGS ####
GLOBAL_CFLAGS=/GR /Gy /W3 /EHsc /Gd /Gm- /Yu"CvGameCoreDLL.h" /Fp"$(Target_PCH)"
Debug_CFLAGS=/MD /Zi /Od /RTC1 $(Debug_DEFINES) $(GLOBAL_CFLAGS)
Release_CFLAGS= /MD /O2 /Oy /Oi /G7 $(Release_DEFINES) $(GLOBAL_CFLAGS)

#### LDFLAGS ####
GLOBAL_LDFLAGS=/DLL /NOLOGO /SUBSYSTEM:WINDOWS /LARGEADDRESSAWARE /TLBID:1 /PDB:"$(Target_PDB)"
Debug_LDFLAGS=/INCREMENTAL /DEBUG /IMPLIB:"$(Target_STATICLIB)" $(GLOBAL_LDFLAGS)
Release_LDFLAGS=/INCREMENTAL:NO /OPT:REF /OPT:ICF $(GLOBAL_LDFLAGS)

#### INCLUDES ####
GLOBAL_INCS=/I"$(TOOLKIT)/include" /I"$(PSDK)/Include" /I"$(PSDK)/Include/mfc"
!IFDEF CIV4_PATH
PROJECT_INCS=/I"$(CIV4_PATH)/Boost-1.32.0/include" /I"$(CIV4_PATH)/Python24/include"
PROJECT_LIBS=/LIBPATH:"$(CIV4_PATH)"/Python24/libs /LIBPATH:"$(CIV4_PATH)"/boost-1.32.0/libs/ boost_python-vc71-mt-1_32.lib
!ELSE
PROJECT_INCS=/IBoost-1.32.0/include /IPython24/include
PROJECT_LIBS=/LIBPATH:Python24/libs /LIBPATH:boost-1.32.0/libs/ boost_python-vc71-mt-1_32.lib
!ENDIF
INCS = $(PROJECT_INCS) $(GLOBAL_INCS)

#### LIBS ####
GLOBAL_LIBS=/LIBPATH:"$(TOOLKIT)/lib" /LIBPATH:"$(PSDK)/Lib" winmm.lib user32.lib
LIBS = $(PROJECT_LIBS) $(GLOBAL_LIBS)

#### Auto SOURCES/OBJS ####
!IF [ECHO SOURCES= \> sources.mk] == 0 && \
    [FOR %i IN (*.cpp) DO @ECHO. "%i" \>> sources.mk] == 0 && \
    [ECHO.>> sources.mk] == 0 && \
	[ECHO OBJS= \>> sources.mk] == 0 && \
    [FOR /F "delims=." %i IN ('dir /b *.cpp') DO @ECHO. $(TARGET)\%i.obj \>> sources.mk] == 0 && \
    [ECHO.>> sources.mk] == 0
!INCLUDE sources.mk
!IF [DEL sources.mk]
!ENDIF
!ENDIF

!IF "$(TARGET)" == "Debug"
!IFNDEF _NMAKE_VER
!ERROR Jom can't be used on Debug builds
!ENDIF
CFLAGS  = $(Debug_CFLAGS)
LDFLAGS = $(Debug_LDFLAGS)
LIBS    = $(LIBS) msvcprt.lib
!ENDIF
!IF "$(TARGET)" == "Release"
CFLAGS  = $(Release_CFLAGS)
LDFLAGS = $(Release_LDFLAGS)
!ENDIF
!IF "$(TARGET)" == "Assert"
CFLAGS  = $(Release_CFLAGS) /DFASSERT_ENABLE
LDFLAGS = $(Release_LDFLAGS)
!ENDIF
!IF "$(TARGET)" == "Profile"
!IFNDEF _NMAKE_VER
!ERROR Jom can't be used on profile builds
!ENDIF
CFLAGS  = $(Release_CFLAGS) /Zi
LDFLAGS = $(Debug_LDFLAGS)
!ENDIF

!IFNDEF CFLAGS
!ERROR Target "$(TARGET)" not supported. Supported targets: Debug Release Assert Profile
!ENDIF

#### Targets ####
#################

.PHONY: all clean build precompile Make_Dir

all: Precompile build

dll: all

clean:
	@FOR %i IN ($(Target_BIN) $(Target_STATICLIB) $(Target_LIBDEF) \
		$(TARGET)\*.obj $(TARGET)\*.@ $(Target_RESOURCE) \
		$(Target_PCH) $(Target_PDB) $(Target_OTHER)) DO @IF EXIST "%i" DEL "%i"

build: $(Target_BIN)
!IFDEF YOURMOD
	-COPY "$(Target_BIN)" "$(YOURMOD)\Assets\."
!ENDIF

precompile: Make_Dir Target_unfinished $(Target_PCH)

Make_Dir:
	-@IF NOT EXIST "$(TARGET)\." MKDIR "$(TARGET)"

Target_unfinished:
	@ECHO.>$(TARGET)\unfinished.@
	@FOR /F "delims=@" %i IN ('dir /b $(TARGET)\*.@') DO \
		@IF EXIST "$(TARGET)\%i" DEL "$(TARGET)\%i"
	@FOR /F %i IN ('dir /b $(TARGET)\*.@') DO \
		@IF EXIST "$(TARGET)\%i" DEL "$(TARGET)\%i"

$(Target_BIN): $(OBJS) $(Target_RESOURCE)
	$(LD) /out:$(Target_BIN) $(LDFLAGS) $(LIBS) $(OBJS) $(Target_RESOURCE)

.cpp{$(TARGET)}.obj:
	@ECHO.>"$*.obj.@"
    $(CPP) /nologo $(CFLAGS) $(INCS) /Fo$*.obj /c $<
	@DEL "$*.obj.@"

$(Target_PCH) $(TARGET)\_precompile.obj:
	@ECHO.>"$(Target_PCH).@"
	@ECHO.>"$(TARGET)\_precompile.obj.@"
    $(CPP) /nologo $(CFLAGS) $(INCS) /YcCvGameCoreDLL.h /Fo"$(TARGET)\_precompile.obj" /c _precompile.cpp
	@DEL "$(Target_PCH).@"
	@DEL "$(TARGET)\_precompile.obj.@"

.rc{$(TARGET)}.res:
	@ECHO.>"$*.res.@"
	$(RC) /Fo$@ $(INCS) $<
	@DEL "$*.res.@"

!IFDEF BLACKLIST
$(TARGET)\$(BLACKLIST).obj: $(BLACKLIST).cpp
	@ECHO.>"$*.obj.@"
	@ECHO.>"$*-dummy.cpp"
	$(CPP) /nologo /DFASSERT_ENABLE $(Release_CFLAGS) $(Release_INCS) /Y- /Fo$@ /c "$*-dummy.cpp"
	@DEL "$*-dummy.cpp"
	@DEL "$*.obj.@"

!ENDIF


!IFDEF FD

# jom can't handle FD
# make sure only NMAKE will try
# jom only executes right after nmake generated the needed file anyway
!IFDEF _NMAKE_VER

!IF [IF NOT EXIST $(FD) EXIT 1] == 0
!IF [$(FD) --objectextension=pch -q -O $(TARGET) CvGameCoreDLL.cpp > depends] != 0 || \
    [$(FD) --objectextension=obj -q -O $(TARGET) $(SOURCES) >> depends] != 0
!MESSAGE Error running fastdep.
!ENDIF
!ELSE
!IF [ECHO "fastdep.exe" NOT FOUND! && \
     ECHO Please edit Makefile to reflect the correct path of fastdep. && \
     ECHO. ]
!ENDIF
!ENDIF

!ENDIF

!ENDIF

!IF EXIST(depends)
!INCLUDE depends
!ENDIF
