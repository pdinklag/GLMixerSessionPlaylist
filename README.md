# GLMixerSessionPlaylist
A Python script to control [GLMixer](https://sourceforge.net/projects/glmixer/) with a shuffled playlist of sessions.

## Usage
This is currently in early development, a usage documentation follows.

### GLMixer Setup
This tool uses Open Sound Control to control GLMixer, so the application must be [set up to listen to OSC messages](https://sourceforge.net/p/glmixer/wiki/GLMixer_OSC_Specs/).

GLMixer only supports *Next* and *Previous* messages to switch sessions, which makes it a bit tedious to work with. The following setup steps are required in GLMixer **before** starting this tool:

1. Select the folder containing your sessions in the *Session Swticher* view in GLMixer.
1. Make sure the sessions in the list are sorted by filename in ascending order.
1. Start playing the topmost session.
1. Start this tool with the same session folder.

## Requirements
Python 3 is required along with [python-osc](https://pypi.org/project/python-osc/).
