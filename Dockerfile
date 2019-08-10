FROM plone:5.1.5

COPY docker.cfg /plone/instance/
COPY --chown=plone:plone  .   /plone/instance/src/hiremi.api
RUN gosu plone buildout -c docker.cfg