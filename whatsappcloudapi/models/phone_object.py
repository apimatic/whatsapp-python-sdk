# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from whatsappcloudapi.api_helper import APIHelper


class PhoneObject(object):

    """Implementation of the 'PhoneObject' model.

    TODO: type model description here.

    Attributes:
        phone (string): Automatically populated with the wa_id value as a
            formatted phone number.
        wa_id (string): WhatsApp ID.
        mtype (PhoneTypeEnum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "phone": 'phone',
        "wa_id": 'wa_id',
        "mtype": 'type'
    }

    _optionals = [
        'phone',
        'wa_id',
        'mtype',
    ]

    def __init__(self,
                 phone=APIHelper.SKIP,
                 wa_id=APIHelper.SKIP,
                 mtype=APIHelper.SKIP):
        """Constructor for the PhoneObject class"""

        # Initialize members of the class
        if phone is not APIHelper.SKIP:
            self.phone = phone 
        if wa_id is not APIHelper.SKIP:
            self.wa_id = wa_id 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 

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

        phone = dictionary.get("phone") if dictionary.get("phone") else APIHelper.SKIP
        wa_id = dictionary.get("wa_id") if dictionary.get("wa_id") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        # Return an object of this model
        return cls(phone,
                   wa_id,
                   mtype)
