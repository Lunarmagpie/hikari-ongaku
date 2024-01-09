import enum


class SeverityType(str, enum.Enum):
    """
    Track error severity type.

    The severity type of the lavalink track error.
    Find out more [here](https://lavalink.dev/api/websocket#severity).
    """

    COMMON = "common"
    """The cause is known and expected, indicates that there is nothing wrong with the library itself"""
    SUSPICIOUS = "suspicious"
    """The cause might not be exactly known, but is possibly caused by outside factors. For example when an outside service responds in a format that we do not expect"""
    FAULT = "fault"
    """The probable cause is an issue with the library or there is no way to tell what the cause might be. This is the default level and other levels are used in cases where the thrower has more in-depth knowledge about the error"""


class TrackEndReasonType(str, enum.Enum):
    """
    Track end reason type.

    The track end reason type for the track that was just playing.
    Find out more [here](https://lavalink.dev/api/websocket#track-end-reason).
    """

    FINISHED = "finished"
    """The track finished playing"""
    LOADFAILED = "loadFailed"
    """The track failed to load"""
    STOPPED = "stopped"
    """The track was stopped"""
    REPLACED = "replaced"
    """The track was replaced"""
    CLEANUP = "cleanup"
    """The track was cleaned up"""


class PlatformType(int, enum.Enum):
    YOUTUBE = 0
    """Youtube search"""
    YOUTUBE_MUSIC = 1
    """Youtube music search"""
    SPOTIFY = 2
    """
    Spotify search

    !!! WARNING
        Not currently supported, or working. Uses Youtube if selected.
    """
    SOUNDCLOUD = 3
    """Soundcloud search"""


class VersionType(enum.Enum):
    """
    The lavalink server version.
    """

    V3 = "v3"
    """V3 Servers"""
    V4 = "v4"
    """V4 Servers"""


class ConnectionType(enum.Enum):
    """
    The connection status for the bot.
    """

    FAILURE = 0
    """The bot has failed to connect to the lavalink server."""
    LOADING = 1
    """The bot has not yet attempted to connect to the server."""
    CONNECTED = 2
    """The bot has successfully connected to the lavalink server"""


# MIT License

# Copyright (c) 2023 MPlatypus

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
