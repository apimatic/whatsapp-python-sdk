# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from whatsappcloudapi.api_helper import APIHelper


class Language(object):

    """Implementation of the 'Language' model.

    TODO: type model description here.

    Attributes:
        code (string): The code of the language or locale to use. Accepts both
            language and language_locale formats (e.g., en and en_US).
        policy (string): The language policy the message should follow.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'code',
        "policy": 'policy'
    }

    _optionals = [
        'policy',
    ]

    def __init__(self,
                 code=None,
                 policy='deterministic'):
        """Constructor for the Language class"""

        # Initialize members of the class
        self.code = code 
        self.policy = policy 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        code = dictionary.get("code") if dictionary.get("code") else None
        policy = dictionary.get("policy") if dictionary.get("policy") else 'deterministic'
        # Return an object of this model
        return cls(code,
                   policy)