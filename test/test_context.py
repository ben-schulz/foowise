import os
import sys

sys.path.insert(0,
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__), '../channels')))

sys.path.insert(0,
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__), '../math')))

sys.path.insert(0,
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__), '../heuristic')))


import foowise.channels.Cla
import foowise.channels.Infomorphism
import foowise.channels.Invariant
import foowise.channels.Channel
import foowise.channels.DistSys

import foowise.channels.Index
import foowise.channels.Value

import foowise.channels.InfomorphismError
import foowise.channels.InfoPair
import foowise.channels.Theory
import foowise.channels.JudgeSet
import foowise.channels.Sequent

import foowise.math.LinAlg
import foowise.math.Set
import foowise.math.Relation
import foowise.math.Dual

import foowise.heuristic.GenQuotient
