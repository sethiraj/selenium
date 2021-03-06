# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import pytest

from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver_kwargs(request, driver_kwargs):
    options = Options()
    options.set_preference('browser.startup.homepage_override.mstone', '')
    options.set_preference('startup.homepage_welcome_url', 'about:')
    driver_kwargs['firefox_options'] = options
    return driver_kwargs


def test_preferences_are_used(driver):
    assert 'about:' == driver.current_url
