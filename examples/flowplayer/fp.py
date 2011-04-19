
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from FlowPlayer import Player, Configuration, ControlsPlugin, ContentPlugin, Clip
from pyjamas import log


class FlowPlayerExample:
    
    def onModuleLoad(self):
        self.panel = VerticalPanel()
        self.player = self.getPlayer()
        
        # Add the Player to the Panel
        self.panel.add(self.player)
        RootPanel().add(self.panel)
        
        
    def getPlayer(self):
        """
        Create a player
        """
        # Url to the flowplayer flashmovie
        url = 'swf/flowplayer.swf'
        
        # Create the initial configuration
        config = Configuration()
        
        # Add a Content
        plugin = self.getContentTop()
        config.addPlugin(plugin)
        
        # Customize Controls, if controls not added,
        # default controls will be used
        plugin = self.getControls()
        config.addPlugin(plugin)
        
        # Add the Common-Clip to configuration
        common_clip = Clip()
        common_clip.setAttr('autoBuffering', True)
        common_clip.setAttr('autoPlay', False)
        config.setCommonClip(common_clip)
        
        # Set a playlist
        playlist = self.getPlaylist()
        config.setPlaylist(playlist)
        
        # Create the Player Object with the initial configuration
        #log.writebr('Loading Player')
        player = Player(url, config)
        
        # Add Listener to the player
        player.addListener(self)
        
        return player
    
    
    def getPlaylist(self):
        """
        Create a playlist
        """
        playlist = []
        playlist.append(Clip('movies/movie1.flv'))
        playlist.append(Clip('movies/movie2.flv'))
        playlist.append(Clip('movies/movie3.flv'))
        #playlist.append(Clip('movies/movie4.flv'))
        # Add Listener to the Clips
        for clip in playlist:
            clip.addListener(self)
        return playlist
        
        
    def getControls(self):
        """
        Create and configure the Controls Plugin
        """
        controls = ControlsPlugin()
        controls.setAttr('height', 20)
        controls.setAttr('timeColor', '#5b80b2')
        controls.setAttr('durationColor', '#000000')
        controls.setAttr('timeBgColor', '#DBDBDB')
        controls.setAttr('volumeSliderColor', '#DBDBDB')
        controls.setAttr('sliderColor', '#000000')
        controls.setAttr('bufferColor', '#DBDBDB')
        controls.setAttr('progressColor', '#bbbbbb')
        controls.setAttr('backgroundColor', '#FFFFFF')
        controls.setAttr('playlist', True)
        
        return controls
    
    
    def getContentTop(self):
        """
        Create and configure a content plugin
        """
        content = ContentPlugin(url='swf/flowplayer.content.swf', name='contentTop')
        content.setAttr('top', 0)
        content.setAttr('left', 0)
        content.setAttr('borderRadius', 15)
        content.setAttr('borderColor', '#222222')
        content.setAttr('width', '100%')
        content.setAttr('height', 60)
        content.setAttr('backgroundColor', '#112233')
        content.setAttr('backgroundGradient', 'low')
        content.setAttr('opacity', 0.9)
        content.addListener(self)
        
        return content
    
    
    def getContentBottom(self):
        """
        Create and configure another content plugin
        """
        content = ContentPlugin(url='swf/flowplayer.content.swf', name='contentBottom')
        content.setAttr('bottom', 20)
        content.setAttr('left', 0)
        content.setAttr('borderRadius', 15)
        content.setAttr('borderColor', '#222222')
        content.setAttr('width', 1)
        content.setAttr('height', 1)
        content.setAttr('backgroundColor', '#112233')
        content.setAttr('backgroundGradient', 'low')
        content.setAttr('opacity', 0.9)
        content.addListener(self)
        
        return content
        
        
    # Player events
    
    def onLoadPlayer(self):
        """
        This is a Player Event
        Fired if the Player is loaded
        """
        #log.writebr('Player loaded')
        # Load a Content-Plugin at runtime into the player
        content = self.getContentBottom()
        self.player.loadPlugin(content)
        
    def onLoadPlugin(self, name):
        """
        This is a Player Event
        Fired if a plugin is loaded
        """
        #log.writebr('Plugin %s loaded' % name)
        if name == 'contentBottom':
            # Animate the content on bottom, if it is loaded
            content = self.player.getPlugin('contentBottom')
            props = {'width': 80, 'bottom': 40, 'left': 40, 'height': 30}
            content.animate(props)
            content.setHtml('Click me')
    
    def onClipAdd(self, clip, index):
        """
        This is a Player Event
        Fired if a clip is added to playlist
        """
        #log.writebr('Clip %s on index %s added' % (clip.url, index))
        pass
    
    def onPlaylistReplace(self, clips):
        """
        This is a Player Event
        Fired if the playlist is replaced
        """
        #log.writebr('Playlist is replaced')
        pass
        
    def onError(self, args):
        """
        This is a Player Event
        Fired on an error
        """
        log.writebr('Error: %s' % str(args))
    
    
    # Plugin events
    
    def onClickPlugin(self, plugin):
        """
        This is a Plugin Event
        Fired if a plugin is clicked
        """
        #log.writebr('Plugin %s clicked' % plugin.name)
        plugin = self.player.getPlugin(plugin.name)
        if plugin.name == 'contentTop':
            # Fade out the top content and start playing
            plugin.fadeOut()
            self.player.play()
        if plugin.name == 'contentBottom':
            # Fade out the bottom content
            plugin.fadeOut()
            # Add one more clip at runtime to the playlist
            #clip = Clip('movies/movie5.flv')
            #clip.addListener(self)
            #log.writebr('Add Clip')
            #self.player.addClip(clip, 3)
    
    def onAnimatePlugin(self, plugin):
        """
        This is a Plugin Event
        Fired if a plugin is animated
        """
        #log.writebr('Plugin %s animated' % plugin.name)
        pass
    
    # Clip events
    
    def onResume(self, clip):
        """
        This is a Clip Event
        Fired if the player is resumed
        """
        #log.writebr('Clip %s resumed' % clip.url)
        # Get the contentTop plugin, and fade it out
        plugin = self.player.getPlugin('contentTop')
        plugin.fadeOut()
        
    def onPause(self, clip):
        """
        This is a Clip Event
        Fired if the player is paused
        """
        #log.writebr('Clip %s paused' % clip.url)
        # Get the contentTop plugin, set some Text
        # and fade it in
        plugin = self.player.getPlugin('contentTop')
        plugin.setHtml('<b>%s</b>' % clip.url)
        plugin.append('<br>More Text')
        plugin.fadeIn()
    

if __name__ == '__main__':
    app = FlowPlayerExample()
    app.onModuleLoad()
