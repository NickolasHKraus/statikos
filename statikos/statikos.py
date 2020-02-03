# -*- coding: utf-8 -*-
"""Main module."""

import os

from . import utils
from .api import CloudFormation
from .exceptions import ConfigNotFound
from .template import create_template


class Statikos():
    """
    Primary class for the statikos Python package.

    The Statikos class is responsible for managing local state and exposes a
    high-level API for creating, deploying, and removing a Statikos service.
    """
    STATIKOS_DIR = '.statikos'
    STATIKOS_YML = 'statikos.yml'
    CLOUDFORMATION_JSON = os.path.join(STATIKOS_DIR, 'cloudformation.json')

    def __init__(self, *args: list, **kwargs: dict) -> None:
        """
        Create a new `Statikos` object.

        :rtype: None
        :return: None
        """
        self.__dict__.update(**kwargs)
        self.cfn = CloudFormation()
        self.config = self._get_config()

    def _get_config(self) -> dict:
        """
        Retrieve contents of `statikos.yml`.

        :rtype: dict
        :return: contents of `statikos.yml`
        """
        try:
            return utils.read_yaml_file(self.STATIKOS_YML)
        except FileNotFoundError:
            raise ConfigNotFound

    def _setup(self) -> None:
        """
        Setup the current directory.

        The following artifacts are created:
          - .statikos/
          - .statikos/cloudformation.json
          - statikos.yml

        :rtype: None
        :return: None
        """
        utils.mkdir(self.STATIKOS_DIR)
        utils.touch(self.CLOUDFORMATION_JSON)
        utils.touch(self.STATIKOS_YML)

    def _teardown(self) -> None:
        """
        Teardown the current directory.

        The following artifacts are removed:
          - .statikos/
          - .statikos/cloudformation.json
          - statikos.yml

        :rtype: None
        :return: None
        """
        utils.rm(self.STATIKOS_DIR)
        utils.rm(self.STATIKOS_YML)

    def create(self) -> None:
        """
        Create the CloudFormation template and parameters file.

        :rtype: None
        :return: None
        """
        self._setup()
        template = create_template(parameters=self.config)
        utils.write_json_file(template.to_dict(), self.CLOUDFORMATION_JSON)

    def deploy(self, dry_run: bool) -> None:
        """
        Deploy the CloudFormation stack.

        :rtype: None
        :return: None
        """
        self.create()

        if dry_run:
            return

        stack_name = self.config['stack_name']
        self.cfn.deploy(
            stack_name=stack_name, template_file=self.CLOUDFORMATION_JSON
        )
        self.publish()

    def generate(self, command: str) -> None:
        """
        Generate static content.
        """

    def publish(self) -> None:
        """
        Upload content to S3.
        """
        self.cfn.sync()

    def remove(self, stack_only: str) -> None:
        """
        Remove the CloudFormation stack and all Statikos artifacts.

        :type stack_only: bool
        :param stack_only: whether to only remove the CloudFormation stack

        :rtype: None
        :return: None
        """
        if not stack_only:
            self._teardown()
        stack_name = self.config['stack_name']
        self.cfn.delete(stack_name=stack_name)
