#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2018 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, match = netedit.setupAndStart(neteditTestRoot)

# go to select mode
netedit.selectMode()

# select all using invert
netedit.selectionInvert()

# go to inspect mode
netedit.inspectMode()

# inspect POILanes
netedit.leftClick(match, 155, 170)

# Change parameter 0 with a non valid value (dummy)
netedit.modifyAttribute(0, "dummyLatPosition")

# Change parameter 0 with a valid value (negative)
netedit.modifyAttribute(0, "-20")

# Change parameter 0 with a valid value
netedit.modifyAttribute(0, "15")

# Change parameter 1 with a non valid value (dummy)
netedit.modifyAttribute(2, "dummyColor")

# Change parameter 14 with a non valid value (invalid format)
netedit.modifyAttribute(2, "255,255,500")

# Change parameter 1 with a valid value (valid format)
netedit.modifyAttribute(2, "blue")

# Change parameter 1 with a valid value (valid format)
netedit.modifyAttribute(2, "125,60,200")

# Change parameter 2 with a valid value
netedit.modifyAttribute(3, "myOwnType")

# Change parameter 3 with a non valid value
netedit.modifyAttribute(4, "dummyLayer")

# Change parameter 3 with a valid value (negative)
netedit.modifyAttribute(4, "-2")

# Change parameter 3 with a valid value (negative)
netedit.modifyAttribute(4, "2")

# Change parameter 4 with a non valid value (dummy)
netedit.modifyAttribute(5, "dummyWidth")

# Change parameter 4 with a non valid value (negative)
netedit.modifyAttribute(5, "-2")

# Change parameter 4 with a valid value
netedit.modifyAttribute(5, "5")

# Change parameter 5 with a non valid value (dummy)
netedit.modifyAttribute(6, "dummyHeight")

# Change parameter 5 with a non valid value (negative)
netedit.modifyAttribute(6, "-3")

# Change parameter 5 with a valid value
netedit.modifyAttribute(6, "5")

# Change parameter 6 with a non valid value (invalid)
netedit.modifyAttribute(7, "%$$%%%%%")

# Change parameter 6 with a non valid value (no exist)
netedit.modifyAttribute(7, "paris.ico")

# Change parameter 6 with a valid value (valid)
netedit.modifyAttribute(7, "berlin_icon.ico")

# Change boolean parameter 7
netedit.modifyShapeDefaultBoolValue(8)

# Change parameter 8 with a non valid value (dummy)
netedit.modifyAttribute(9, "dummyAngle")

# Change parameter 8 with a valid value (negative)
netedit.modifyAttribute(9, "-12")

# Change parameter 8 with a valid value (> 360)
netedit.modifyAttribute(9, "500")

# Change parameter 8 with a valid value
netedit.modifyAttribute(9, "30")

# Change boolean parameter block
netedit.modifyShapeDefaultBoolValue(12)

# go to select mode
netedit.selectMode()

# clear selection
netedit.selectionClear()

# Check undos and redos
netedit.undo(match, 14)
netedit.redo(match, 14)

# save shapes
netedit.saveShapes()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
