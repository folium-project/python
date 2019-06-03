"""
Copyright 2019 Dragos Cirjan <dragos.cirjan@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import abc


class Fetch:
    """
    Interface for implementing REST Fetch method.
    :see https://en.wikipedia.org/wiki/Representational_state_transfer
    """
    
    OPTION_COUNT = '__count'

    @abc.abstractmethod
    def fetch(self, criteria: list = [], fields: list = [], options: dict = {}):
        """
        If no field is passed, all resource fields should be presented to output.
        Read resource(s) from the database according to a set of criteria and based on a set of fields to be returned

        read([ [ 'id', '>', '10' ] ])

        or

        read(
          [ [ 'id', '>', '10' ] ],
          [ 'id', 'name', 'email' ]
        )

        or

        read([], [], [ '__count' => True ])

        :param criteria: list   (list of tuples) criteria to filter database data
        :param fields: list     list of fields to read, can be empty (will read al fields)
        :param options: dict    options used by method:
                                __count - if True, will return count of resources in stead of list
        :return: list|int       array (or count) of resources matching the criteria (and having only the fields required)
        """
        pass