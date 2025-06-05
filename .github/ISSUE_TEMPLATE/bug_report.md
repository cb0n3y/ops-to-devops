name: Bug Report
description: Report an issue with the scripts, setup, or tools.
title: "[Bug]: "
labels: [bug]
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        Please provide detailed information so the issue can be reproduced and resolved.

  - type: textarea
    id: what-happened
    attributes:
      label: What happened?
      description: Describe the issue you encountered.
      placeholder: Describe the bug...
    validations:
      required: true

  - type: input
    id: environment
    attributes:
      label: Environment
      description: What OS, Vagrant version, or tool versions are you using?
      placeholder: "Ubuntu 22.04, Vagrant 2.4.0, VirtualBox 7.x"
