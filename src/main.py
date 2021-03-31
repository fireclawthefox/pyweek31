#!/usr/bin/python
__author__ = "Fireclaw the Fox"
__license__ = """
Simplified BSD (BSD 2-Clause) License.
See License.txt or http://opensource.org/licenses/BSD-2-Clause for more info
"""

# Python imports
import os

# Panda3D imoprts
from direct.showbase.ShowBase import ShowBase
from direct.fsm.FSM import FSM
from direct.gui.DirectGui import DGG
from panda3d.core import (
    AntialiasAttrib,
    ConfigPageManager,
    ConfigVariableInt,
    ConfigVariableBool,
    ConfigVariableString,
    OFileStream,
    WindowProperties,
    loadPrcFileData,
    loadPrcFile,
    Filename)

# Game imports
from menu import GUI as Menu
from optionsHandler import OptionsHandler

from gameScreenHandler import GameScreenHandler

#
# PATHS AND CONFIGS
#
# set company and application details
companyName = "Grimfang Studio"
appName = "Station31"
versionstring = "21.04"

# build the path from the details we have
home = os.path.expanduser("~")
basedir = os.path.join(
    home,
    companyName,
    appName)
if not os.path.exists(basedir):
    os.makedirs(basedir)

# look for a config file
prcFile = os.path.join(basedir, "{}.prc".format(appName))
if os.path.exists(prcFile):
    mainConfig = loadPrcFile(Filename.fromOsSpecific(prcFile))

# set configurations that should not be changed from a config file
loadPrcFileData("",
"""
    #
    # Model loading
    #
    model-path $MAIN_DIR/assets/

    #
    # Window and graphics
    #
    window-title {}
    #show-frame-rate-meter 1

    #
    # Logging
    #
    #notify-level info
    notify-timestamp 1

    #
    # Audio
    #
    # Make sure to use OpenAL
    audio-library-name p3openal_audio
""".format(appName))

#
# MAIN GAME CLASS
#
class Main(ShowBase, FSM):
    """Main function of the application
    initialise the engine (ShowBase)"""

    def __init__(self):
        """initialise the engine"""
        ShowBase.__init__(self)
        base.notify.info("Version {}".format(versionstring))
        FSM.__init__(self, "FSM-Game")

        #
        # BASIC APPLICATION CONFIGURATIONS
        #
        # disable pandas default camera driver
        self.disableMouse()
        # set antialias for the complete sceen to automatic
        self.render.setAntialias(AntialiasAttrib.MAuto)
        # shader generator
        render.setShaderAuto()
        # Enhance font readability
        DGG.getDefaultFont().setPixelsPerUnit(100)
        # get the displays width and height for later usage
        self.dispWidth = self.pipe.getDisplayWidth()
        self.dispHeight = self.pipe.getDisplayHeight()

        self.win.setClearColor((0, 0, 0, 1))

        #
        # CONFIGURATION LOADING
        #
        # load given variables or set defaults
        # check if particles should be enabled
        # NOTE: If you use the internal physics engine, this always has
        #       to be enabled!
        #particles = ConfigVariableBool("particles-enabled", True).getValue()
        #if particles:
        #    self.enableParticles()

        def setFullscreen():
            """Helper function to set the window fullscreen
            with width and height set to the screens size"""
            # set window properties
            # clear all properties not previously set
            base.win.clearRejectedProperties()
            # setup new window properties
            props = WindowProperties()
            # Fullscreen
            props.setFullscreen(True)
            # set the window size to the screen resolution
            props.setSize(self.dispWidth, self.dispHeight)
            # request the new properties
            base.win.requestProperties(props)
            # Set the config variables so we correctly store the
            # new size and fullscreen setting later
            winSize = ConfigVariableString("win-size")
            winSize.setValue("{} {}".format(self.dispWidth, self.dispHeight))
            fullscreen = ConfigVariableBool("fullscreen")
            fullscreen.setValue(True)
            # Render a frame to make sure the fullscreen is applied
            # before we do anything else
            self.taskMgr.step()
            # make sure to propagate the new aspect ratio properly so
            # the GUI and other things will be scaled appropriately
            aspectRatio = self.dispWidth / self.dispHeight
            self.adjustWindowAspectRatio(aspectRatio)


        # check if the config file hasn't been created
        if not os.path.exists(prcFile):
            setFullscreen()
        # automatically safe configuration at application exit
        base.exitFunc = self.__writeConfig

        #
        # INITIALIZE GAME CONTENT
        #
        self.titleMusic = loader.loadMusic("audio/Golden_Antelope_-_Detective_Story.ogg")
        self.titleMusic.setLoop(True)
        self.titleMusic.play()

        #
        # EVENT HANDLING
        #
        # By default we accept the escape key
        self.accept("escape", self.__escape)

        #
        # ENTER GAMES INITIAL FSM STATE
        #
        self.request("Menu")

    #
    # FSM PART
    #

    def enterMenu(self):
        self.menu = Menu()
        self.accept("exit", self.userExit)
        self.accept("options", self.request, ["Options"])
        self.accept("startGame", self.request, ["Game"])

    def exitMenu(self):
        self.ignore("exit")
        self.ignore("options")
        self.ignore("startGame")
        self.menu.destroy()

    def enterOptions(self):
        self.accept("exit", self.request, ["Menu"])
        self.options = OptionsHandler()

    def exitOptions(self):
        self.ignore("exit")
        self.options.destroy()

    def enterGame(self):
        # main game logic should be started here
        self.gameScreenHandler = GameScreenHandler()
        self.accept("exit", self.request, ["Menu"])

    def exitGame(self):
        # cleanup for game code
        self.ignore("exit")
        self.gameScreenHandler.destroy()

    #
    # FSM PART END
    #

    #
    # BASIC FUNCTIONS
    #

    def __escape(self):
        """Handle user escape key klicks"""
        if self.state == "Menu":
            # In this state, we will stop the application
            self.userExit()
        if self.state == "Game":
            # user wants to quit, ask the game screen to handle this
            self.gameScreenHandler.askQuit()
        else:
            # In every other state, we switch back to the Game state
            self.request("Menu")

    def __writeConfig(self):
        """Save current config in the prc file or if no prc file exists
        create one. The prc file is set in the prcFile variable"""
        page = None

        #
        #TODO: add any configuration variable names that you have added
        #      to the dictionaries in the next lines. Set the current
        #      configurations value as value in this dictionary and it's
        #      name as key.
        configVariables = {
            # set the window size in the config file
            "win-size": ConfigVariableString("win-size", "{} {}".format(self.dispWidth, self.dispHeight)).getValue(),
            # set the default to fullscreen in the config file
            "fullscreen": "#t" if base.win.isFullscreen() else "#f",
            # particles
            "particles-enabled": "#t" if self.particleMgrEnabled else "#f",
            # audio
            "audio-volume": str(round(self.musicManager.getVolume(), 2)),
            "audio-music-active": "#t" if base.AppHasAudioFocus else "#f",
            "audio-sfx-active": "#t" if base.AppHasAudioFocus else "#f",
            # logging
            "notify-output": os.path.join(basedir, "game.log"),
            # window
            "framebuffer-multisample": "#t" if ConfigVariableBool("framebuffer-multisample").getValue() else "#f",
            "multisamples": str(ConfigVariableInt("multisamples", 8).getValue()),
            "texture-anisotropic-degree": str(ConfigVariableInt("texture-anisotropic-degree").getValue()),
            "textures-auto-power-2": "#t" if ConfigVariableBool("textures-auto-power-2", True).getValue() else "#f",
            }

        page = None
        # Check if we have an existing configuration file
        if os.path.exists(prcFile):
            # open the config file and change values according to current
            # application settings
            page = loadPrcFile(Filename.fromOsSpecific(prcFile))
            removeDecls = []
            for dec in range(page.getNumDeclarations()):
                # Check if our variables are given.
                # NOTE: This check has to be done to not loose our base
                #       or other manual config changes by the user
                if page.getVariableName(dec) in configVariables.keys():
                    removeDecls.append(page.modifyDeclaration(dec))
            for dec in removeDecls:
                page.deleteDeclaration(dec)
        else:
            # Create a config file and set default values
            cpMgr = ConfigPageManager.getGlobalPtr()
            page = cpMgr.makeExplicitPage("Application Config")

        # always write custom configurations
        for key, value in configVariables.items():
            page.makeDeclaration(key, value)
        # create a stream to the specified config file
        configfile = OFileStream(prcFile)
        # and now write it out
        page.write(configfile)
        # close the stream
        configfile.close()

    #
    # BASIC END
    #
# CLASS Main END

#
# START GAME
#
Game = Main()
Game.run()
