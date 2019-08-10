# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from quito.core import _
from plone.supermodel import model
from zope import schema

class ISkillWorker(model.Schema):
    """Schema for Conference Presenter content type.
    """
    model.load('models/skillworker.xml')

class IJobs(model.Schema):

    """Schema for Conference Presenter content type."""

    model.load('models/jobs.xml')

class ICarousel(model.Schema):

    """Schema for Conference Presenter content type.
    """

    model.load('models/carousel.xml')

