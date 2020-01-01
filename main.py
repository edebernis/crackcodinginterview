#!/usr/bin/env python3

import sys
import pytest

errcode = pytest.main(['-s'])
sys.exit(errcode)
