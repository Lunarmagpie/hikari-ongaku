# ruff: noqa
import unittest

from ongaku.abc.lavalink import ExceptionError
from ongaku.abc.lavalink import Info
from ongaku.abc.lavalink import InfoGit
from ongaku.abc.lavalink import InfoPlugin
from ongaku.abc.lavalink import InfoVersion
from ongaku.abc.lavalink import RestError
from ongaku.enums import SeverityType


class InfoTest(unittest.TestCase):
    def test_info(self):
        test_info_version = InfoVersion(
            "semver_test", 1, 2, 3, "prerelease_test", "build_test"
        )
        test_info_git = InfoGit("branch_test", "commit_test", 30)
        test_info_plugin_1 = InfoPlugin("plugin_test_1", "1.2")
        test_info_plugin_2 = InfoPlugin("plugin_test_2", "3.4")
        test_info = Info(
            test_info_version,
            60,
            test_info_git,
            "jvm_test",
            "lavaplayer_test",
            ["youtube", "soundcloud"],
            ["equalizer", "karaoke", "timescale", "channelMix"],
            [test_info_plugin_1, test_info_plugin_2],
        )

        assert test_info.build_time == 60
        assert test_info.jvm == "jvm_test"
        assert test_info.lavaplayer == "lavaplayer_test"
        assert test_info.version.semver == "semver_test"
        assert test_info.version.major == 1
        assert test_info.version.minor == 2
        assert test_info.version.patch == 3
        assert test_info.version.pre_release == "prerelease_test"
        assert test_info.version.build == "build_test"
        assert test_info.git.branch == "branch_test"
        assert test_info.git.commit == "commit_test"
        assert test_info.git.commit_time == 30
        assert test_info.plugins[0].name == "plugin_test_1"
        assert test_info.plugins[0].version == "1.2"
        assert test_info.plugins[1].name == "plugin_test_2"
        assert test_info.plugins[1].version == "3.4"
        assert test_info.source_managers[0] == "youtube"
        assert test_info.source_managers[1] == "soundcloud"
        assert test_info.filters[0] == "equalizer"
        assert test_info.filters[1] == "karaoke"
        assert test_info.filters[2] == "timescale"
        assert test_info.filters[3] == "channelMix"

    def test_info_payload(self):
        payload = {
            "version": {
                "semver": "semver_test",
                "major": 3,
                "minor": 7,
                "patch": 0,
                "preRelease": "prerelease_test",
                "build": "build_test",
            },
            "buildTime": 60,
            "git": {"branch": "branch_test", "commit": "commit_test", "commitTime": 30},
            "jvm": "jvm_test",
            "lavaplayer": "lavaplayer_test",
            "sourceManagers": ["youtube", "soundcloud"],
            "filters": ["equalizer", "karaoke", "timescale", "channelMix"],
            "plugins": [
                {"name": "plugin_test_1", "version": "1.2"},
                {"name": "plugin_test_2", "version": "3.4"},
            ],
        }

        test_info = Info._from_payload(payload)

        assert test_info.build_time == 60
        assert test_info.jvm == "jvm_test"
        assert test_info.lavaplayer == "lavaplayer_test"
        assert test_info.version.semver == "semver_test"
        assert test_info.version.major == 3
        assert test_info.version.minor == 7
        assert test_info.version.patch == 0
        assert test_info.version.pre_release == "prerelease_test"
        assert test_info.version.build == "build_test"
        assert test_info.git.branch == "branch_test"
        assert test_info.git.commit == "commit_test"
        assert test_info.git.commit_time == 30
        assert test_info.plugins[0].name == "plugin_test_1"
        assert test_info.plugins[0].version == "1.2"
        assert test_info.plugins[1].name == "plugin_test_2"
        assert test_info.plugins[1].version == "3.4"
        assert test_info.source_managers[0] == "youtube"
        assert test_info.source_managers[1] == "soundcloud"
        assert test_info.filters[0] == "equalizer"
        assert test_info.filters[1] == "karaoke"
        assert test_info.filters[2] == "timescale"
        assert test_info.filters[3] == "channelMix"

        assert test_info.to_payload == payload

    def test_info_version(self):
        test_info_version = InfoVersion(
            "semver_test", 1, 2, 3, "prerelease_test", "build_test"
        )

        assert test_info_version.semver == "semver_test"
        assert test_info_version.major == 1
        assert test_info_version.minor == 2
        assert test_info_version.patch == 3
        assert test_info_version.pre_release == "prerelease_test"
        assert test_info_version.build == "build_test"

    def test_info_version_payload(self):
        payload = {
            "semver": "semver_test",
            "major": 3,
            "minor": 7,
            "patch": 0,
            "preRelease": "prerelease_test",
            "build": "build_test",
        }

        test_info_version = InfoVersion._from_payload(payload)

        assert test_info_version.semver == "semver_test"
        assert test_info_version.major == 3
        assert test_info_version.minor == 7
        assert test_info_version.patch == 0
        assert test_info_version.pre_release == "prerelease_test"
        assert test_info_version.build == "build_test"

        assert test_info_version.to_payload == payload

    def test_info_git(self):
        test_info_git = InfoGit("branch_test", "commit_test", 30)

        assert test_info_git.branch == "branch_test"
        assert test_info_git.commit == "commit_test"
        assert test_info_git.commit_time == 30

    def test_info_git_payload(self):
        payload = {"branch": "branch_test", "commit": "commit_test", "commitTime": 30}

        test_info_git = InfoGit._from_payload(payload)

        assert test_info_git.branch == "branch_test"
        assert test_info_git.commit == "commit_test"
        assert test_info_git.commit_time == 30

        assert test_info_git.to_payload == payload

    def test_info_plugin(self):
        test_info_plugin = InfoPlugin("plugin_test_1", "1.2")

        assert test_info_plugin.name == "plugin_test_1"
        assert test_info_plugin.version == "1.2"

    def test_info_plugin_payload(self):
        payload = {"name": "plugin_test_1", "version": "1.2"}

        test_info_plugin = InfoPlugin._from_payload(payload)

        assert test_info_plugin.name == "plugin_test_1"
        assert test_info_plugin.version == "1.2"

        assert test_info_plugin.to_payload == payload


class TestErrors(unittest.TestCase):
    def test_rest_error(self):
        test_rest_error = RestError(
            32, 12, "test_error", "test_trace", "test_message", "test_path"
        )

        assert test_rest_error.timestamp == 32
        assert test_rest_error.status == 12
        assert test_rest_error.error == "test_error"
        assert test_rest_error.trace == "test_trace"
        assert test_rest_error.message == "test_message"
        assert test_rest_error.path == "test_path"

    def test_rest_error_payload(self):
        payload = {
            "timestamp": 32,
            "status": 12,
            "error": "test_error",
            "trace": "test_trace",
            "message": "test_message",
            "path": "test_path",
        }

        test_rest_error = RestError._from_payload(payload)

        assert test_rest_error.timestamp == 32
        assert test_rest_error.status == 12
        assert test_rest_error.error == "test_error"
        assert test_rest_error.trace == "test_trace"
        assert test_rest_error.message == "test_message"
        assert test_rest_error.path == "test_path"

    def test_exception_error(self):
        test_exception_error = ExceptionError(
            "test_message", SeverityType.COMMON, "test_cause"
        )

        assert test_exception_error.message == "test_message"
        assert test_exception_error.severity == SeverityType.COMMON
        assert test_exception_error.cause == "test_cause"

    def test_exception_error_payload(self):
        payload = {
            "message": "test_message",
            "severity": "common",
            "cause": "test_cause",
        }

        test_exception_error = ExceptionError._from_payload(payload)

        assert test_exception_error.message == "test_message"
        assert test_exception_error.severity == SeverityType.COMMON
        assert test_exception_error.cause == "test_cause"
