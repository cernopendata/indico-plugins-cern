# This file is part of the CERN Indico plugins.
# Copyright (C) 2014 - 2022 CERN
#
# The CERN Indico plugins are free software; you can redistribute
# them and/or modify them under the terms of the MIT License; see
# the LICENSE file for more details.

from indico.core.plugins import IndicoPluginBlueprint

from indico_conversion.conversion import RHConversionCheck, RHConversionFinished


blueprint = IndicoPluginBlueprint('conversion', __name__)
blueprint.add_url_rule('/conversion/finished', 'callback', RHConversionFinished, methods=('POST',))
blueprint.add_url_rule('/conversion/check', 'check', RHConversionCheck)
