# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from whatsappcloudapi.api_helper import APIHelper


class Text(object):

    """Implementation of the 'Text' model.

    TODO: type model description here.

    Attributes:
        body (string): Required for text messages. The text of the text
            message which can contain URLs which begin with http:// or
            https:// and formatting. See available formatting options here. If
            you include URLs in your text and want to include a preview box in
            text messages (preview_url: true), make sure the URL starts with
            http:// or https:// —https:// URLs are preferred. You must include
            a hostname, since IP addresses will not be matched.
        preview_url (bool): By default, WhatsApp recognizes URLs and makes
            them clickable, but you can also include a preview box with more
            information about the link. Set this field to true if you want to
            include a URL preview box. The majority of the time, the receiver
            will see a URL they can click on when you send an URL, set
            preview_url to true, and provide a body object with a http or
            https link. URL previews are only rendered after one of the
            following has happened: The business has sent a message template
            to the user. The user initiates a conversation with a "click to
            chat" link. The user adds the business phone number to their
            address book and initiates a conversation.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "body": 'body',
        "preview_url": 'preview_url'
    }

    _optionals = [
        'preview_url',
    ]

    def __init__(self,
                 body=None,
                 preview_url=False):
        """Constructor for the Text class"""

        # Initialize members of the class
        self.body = body 
        self.preview_url = preview_url 

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

        body = dictionary.get("body") if dictionary.get("body") else None
        preview_url = dictionary.get("preview_url") if dictionary.get("preview_url") else False
        # Return an object of this model
        return cls(body,
                   preview_url)