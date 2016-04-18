"""
.. _tut_viz_epochs:

Visualize Epochs data
=====================

"""
import os.path as op

import mne

data_path = op.join(mne.datasets.sample.data_path(), 'MEG', 'sample')
raw = mne.io.read_raw_fif(op.join(data_path, 'sample_audvis_raw.fif'))
events = mne.read_events(op.join(data_path, 'sample_audvis_raw-eve.fif'))
epochs = mne.Epochs(raw, events, [1, 2])

###############################################################################
# This tutorial focuses on visualization of epoched data. All of the functions
# introduced here are basically high level matplotlib functions with built in
# intelligence to work with epoched data. All the methods return a handle to
# matplotlib figure instance.
#
# All plotting functions start with ``plot``. Let's start with the most
# obvious. :func:`mne.Epochs.plot` offers an interactive browser that allows
# rejection by hand when called in combination with a keyword ``block=True``.
# This blocks the execution of the script until the browser window is closed.
epochs.plot(block=True)

###############################################################################
# The numbers at the top refer to the event id of the epoch. We only have
# events with id numbers of 1 and 2 since we included only those when
# constructing the epochs.
#
# Since we did no artifact correction or rejection, there are epochs
# contaminated with blinks and saccades. For instance, epoch number 9 (see
# numbering at the bottom) seems to be contaminated by a blink. This epoch can
# be marked for rejection by clicking on top of the browser window. The epoch
# should turn red when you click it. This means that it will be dropped as the
# window is closed.