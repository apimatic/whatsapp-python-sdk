# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from whatsappcloudapi.api_helper import APIHelper
from whatsappcloudapi.models.document import Document
from whatsappcloudapi.models.image import Image
from whatsappcloudapi.models.video import Video


class Header(object):

    """Implementation of the 'Header' model.

    TODO: type model description here.

    Attributes:
        mtype (HeaderTypeEnum): The header type you would like to use.
        text (string): Required if type is set to text. Text for the header.
            Formatting allows emojis, but not markdown.
        video (Video): Required if type is set to video. Contains the media
            object for this video.
        image (Image): Required if type is set to image. Contains the media
            object for this image.
        document (Document): Required if type is set to document. Contains the
            media object for this document.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "text": 'text',
        "video": 'video',
        "image": 'image',
        "document": 'document'
    }

    _optionals = [
        'text',
        'video',
        'image',
        'document',
    ]

    def __init__(self,
                 mtype=None,
                 text=APIHelper.SKIP,
                 video=APIHelper.SKIP,
                 image=APIHelper.SKIP,
                 document=APIHelper.SKIP):
        """Constructor for the Header class"""

        # Initialize members of the class
        self.mtype = mtype 
        if text is not APIHelper.SKIP:
            self.text = text 
        if video is not APIHelper.SKIP:
            self.video = video 
        if image is not APIHelper.SKIP:
            self.image = image 
        if document is not APIHelper.SKIP:
            self.document = document 

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

        mtype = dictionary.get("type") if dictionary.get("type") else None
        text = dictionary.get("text") if dictionary.get("text") else APIHelper.SKIP
        video = Video.from_dictionary(dictionary.get('video')) if 'video' in dictionary.keys() else APIHelper.SKIP 
        image = Image.from_dictionary(dictionary.get('image')) if 'image' in dictionary.keys() else APIHelper.SKIP 
        document = Document.from_dictionary(dictionary.get('document')) if 'document' in dictionary.keys() else APIHelper.SKIP 
        # Return an object of this model
        return cls(mtype,
                   text,
                   video,
                   image,
                   document)
