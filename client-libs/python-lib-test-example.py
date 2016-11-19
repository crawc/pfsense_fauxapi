#!/usr/bin/python3
# 
# Copyright 2016 Nicholas de Jong  <contact[at]nicholasdejong.com>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 

import pprint, sys
from python.fauxapi_lib import FauxapiLib

# check args exist
if(len(sys.argv) < 4):
    print('usage: ' + sys.argv[0] + ' <host> <apikey> <apisecret>')
    sys.exit(1)

# config
fauxapi_host=sys.argv[1]
fauxapi_apikey=sys.argv[2]
fauxapi_apisecret=sys.argv[3]

FauxapiLib = FauxapiLib(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)


# config get
config = FauxapiLib.config_get()

# config set
pprint.pprint(FauxapiLib.config_set(config))

# config backuo
pprint.pprint(FauxapiLib.config_backup())

# config reload
pprint.pprint(FauxapiLib.config_reload())

# system reboot
# pprint.pprint(FauxapiLib.system_reboot())

# config get just a section
config_filter = FauxapiLib.config_get('filter')
pprint.pprint(config_filter)

# config set just a section
config_aliases = FauxapiLib.config_get('aliases')
pprint.pprint(FauxapiLib.config_set(config_aliases, 'aliases'))
